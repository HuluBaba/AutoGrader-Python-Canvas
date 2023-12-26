import timeout_decorator
import sys
import os
import re
import pandas as pd
import io
from utils import bcolors
import pickle
import yaml
import argparse
import tqdm
from collections import OrderedDict
import matplotlib.pyplot as plt

# parse args and import config
def parse_args():
    parser = argparse.ArgumentParser(description='captor')
    parser.add_argument('--config', default='config_ex2.yaml', type=str)
    args = parser.parse_args()
    return args

args = parse_args()
with open(os.path.join('config',args.config), 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

NUM_QUESTIONS = config['NUM_QUESTIONS']
totalscorelist = config['totalscorelist']
issue_number_list = config['issue_number_list']
skip_questions = config['skip_questions']
load_execute_history = config['load_execute_history']
load_manual_history = config['load_manual_history']
load_auto_history = config['load_auto_history']
MANUAL_EXAMINATION_0 = config['MANUAL_EXAMINATION_0']

execute_history_file = config['ALL_PATH']['execute_history_file']
manual_history_file = config['ALL_PATH']['manual_history_file']
auto_history_file = config['ALL_PATH']['auto_history_file']
name_sid_file = config['ALL_PATH']['name_sid_file']
grade_function_file = config['ALL_PATH']['grade_function_file']
submission_dir = config['ALL_PATH']['submission_dir']
history_dir = config['ALL_PATH']['history_dir']
input_dir = config['ALL_PATH']['input_dir']
result_dir = config['ALL_PATH']['result_dir']



sys.path.append(submission_dir)



# Find history file

def get_history_data(load_history,history_file,target_filename,default_file_exist_flag):
    if load_history:
        if history_file:
            history_path=history_file
        else:
            if target_filename in names:
                history_path=os.path.join(history_dir,target_filename)
            else:
                history_path=None
    else:
        history_path=None
    if history_path:
        with open(history_path,'rb') as fp:
            history_data=pickle.load(fp)
    else:
        history_data={}
    return history_data

for target_dir in [submission_dir,history_dir,input_dir,result_dir]:
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

names=os.listdir(history_dir)

execute_history_data=get_history_data(load_execute_history,execute_history_file,'Execute.pkl','Execute.pkl' in names)
auto_history_data=get_history_data(load_auto_history,auto_history_file,'Auto.pkl','Auto.pkl' in names)
max_digit=0
for name in names:
    if name[:12]=='Manual_Score':
        digit=eval(name[-7:-4].lstrip('0'))
        max_digit=max(digit,max_digit)
target_digit=max_digit+1
target_path=os.path.join(history_dir,f"Manual_Score_{target_digit:03}.pkl")
manual_history_data=get_history_data(load_manual_history,manual_history_file,target_path,max_digit!=0)



# input redirection
class redirect(io.StringIO):
    def __init__(self):
        self.oddtime=True
        self.data={}
    def new_student(self,sid):
        self.data[sid]=self.data.get(sid,['' for i in range(2*NUM_QUESTIONS)]+['unscored' for i in range(NUM_QUESTIONS+1)])
        self.cur_sid=sid
    def new_question(self,serial):
        self.cur_serial=serial
    def write(self,s):
            self.data[self.cur_sid][self.cur_serial-1+NUM_QUESTIONS]+=s
    def flush(self):
        pass

initial_stdin=sys.stdin
initial_stdout=sys.stdout
sys.stdout=redirect()

# submission file list generation
def is_legal(file_names):
    if file_names[-3:]!=".py" and file_names[-3:]!=".PY":
        return False
    return True

answer_file_names=os.listdir(submission_dir)
for i in range(len(answer_file_names)-1,-1,-1):
    if os.path.isdir(os.path.join(submission_dir,answer_file_names[i])):
        answer_file_names.remove(answer_file_names[i])
        continue
    prefix_name, ext_name = os.path.splitext(answer_file_names[i])
    if "." in prefix_name:
        standard_prefix_name=prefix_name.replace(".","_")
        os.rename(os.path.join(submission_dir,f'{answer_file_names[i]}'),os.path.join(submission_dir,f'{standard_prefix_name}{ext_name}'))
        answer_file_names[i]=standard_prefix_name+ext_name



# submission file execution and storage; record sid-question status 

def time_limited_exec(module,time_limit=5):
    @timeout_decorator.timeout(time_limit)
    def _time_limited_exec(module):
        __import__(module)
    _time_limited_exec(module)
    



to_filename_table={}
pbar = tqdm.tqdm(total=len(answer_file_names),leave=False,file=initial_stdout)
for file_index,file_name in enumerate(answer_file_names):
    ext_name = os.path.splitext(file_name)[1]
    sid=eval(file_name[:7])
    issue_number=eval(file_name[23:29])
    serial=issue_number_list.index(issue_number)+1
    to_filename_table[sid]=to_filename_table.get(sid,{})
    to_filename_table[sid][serial]=file_name
    if sid in execute_history_data.keys() and execute_history_data[sid][serial-1]!='':
        sys.stdout.new_student(sid)
        sys.stdout.data[sid][serial-1]=execute_history_data[sid][serial-1]
        sys.stdout.data[sid][serial-1+NUM_QUESTIONS]=execute_history_data[sid][serial-1+NUM_QUESTIONS]
    else:
        sys.stdout.new_student(sid)
        sys.stdout.new_question(serial)
        if serial in skip_questions:
            sys.stdout.data[sid][serial-1]='Skip'
            continue
        elif ext_name in [".jpg",".png",".jpeg"]:
            sys.stdout.data[sid][serial-1]='Image'
            continue
        elif ext_name not in [".py",".PY"]:
            sys.stdout.data[sid][serial-1]='NotPFile'
            continue
        try:
            sys.stdin=open(os.path.join(input_dir,f'input_{serial}.in'),'r')
            time_limited_exec(file_name[:-3])
        except TimeoutError as e:
            sys.stdout.data[sid][serial-1]='TimeOut'
        except EOFError as e:
            sys.stdout.data[sid][serial-1]='InputNotEnough'
        except SyntaxError as e:
            if e.msg[1:8]=='unicode':
                sys.stdout.data[sid][serial-1]='UnicodeError'
                sys.stdout.data[sid][serial-1+NUM_QUESTIONS]+='\n'+e.msg
            else:
                sys.stdout.data[sid][serial-1]='ExeFail'
                sys.stdout.data[sid][serial-1+NUM_QUESTIONS]+='\n'+e.msg
        except Exception as e:
            sys.stdout.data[sid][serial-1]='ExeFail'
            sys.stdout.data[sid][serial-1+NUM_QUESTIONS]+='\n'+str(e)
        else:
            if sys.stdout.data[sid][serial+NUM_QUESTIONS-1]=='':
                sys.stdout.data[sid][serial-1]='OutputBlank'
            else:
                sys.stdout.data[sid][serial-1]='Common'
    
    pbar.set_postfix_str(f'{file_index/len(answer_file_names):7.3f}')
    pbar.update(1)
pbar.close()
pickle.dump(sys.stdout.data,open(os.path.join(history_dir,'Execute.pkl'),"wb"))


with open(name_sid_file,'r',encoding='gbk') as f1:
    name_sid=pd.read_csv(f1)
for sid in name_sid.sid:
    if sid not in to_filename_table.keys():
        sys.stdout.new_student(sid)
        for serial in range(1,1+NUM_QUESTIONS):
            sys.stdout.data[sid][serial-1]='StudentNotFound'
    else:
        for serial in range(1,1+NUM_QUESTIONS):
            if serial not in to_filename_table[sid]:
                sys.stdout.data[sid][serial-1]='QuesitionNotFound'




# stdout->istdout stdin->istdin students_result->sys.stdout.data
students_result=sys.stdout.data
sys.stdout=initial_stdout
sys.stdin=initial_stdin

# import grade_functions from grade_functions_file, which is a python file in another directory
grade_function_dir = grade_function_file[:grade_function_file.rfind('/')]
sys.path.append(grade_function_dir)
grade_functions=__import__(grade_function_file[grade_function_file.rfind('/')+1:-3]).grade_functions


# # grade storaged data
# from grade_functions import grade_functions

def grade(serial,answer):
    score=grade_functions[serial-1](answer)
    return score


# Auto score
manual_count=0
pbar = tqdm.tqdm(total=len(students_result),leave=False)
students_counter=0
for key,value in students_result.items():
    for serial in range(1,1+NUM_QUESTIONS):
        if key in auto_history_data.keys() and auto_history_data[key][serial-1]!='unscored':
            score=auto_history_data[key][serial-1]
            value[serial-1+2*NUM_QUESTIONS]=score
            if value[serial-1] in ['Common'] and score==0:
                value[serial-1]='False'
        else:
            if value[serial-1] in ['StudentNotFound','QuesitionNotFound']:
                score=0
                value[serial-1+2*NUM_QUESTIONS]=score
            elif value[serial-1] in ['Skip']:
                score=totalscorelist[serial-1]
                value[serial-1+2*NUM_QUESTIONS]=score
            elif value[serial-1] in ['Image','NotPFile']:
                score=0
                value[serial-1+2*NUM_QUESTIONS]=score
            elif value[serial-1] in ['InputNotEnough','UnicodeError','ExeFail','OutputBlank','TimeOut']:
                score=grade(serial,value[serial-1+NUM_QUESTIONS])
                value[serial-1+2*NUM_QUESTIONS]=score
            elif value[serial-1] in ['Common']:
                score=grade(serial,value[serial-1+NUM_QUESTIONS])
                value[serial-1+2*NUM_QUESTIONS]=score
                if score==0:
                    value[serial-1]='False'
    students_result[key][3*NUM_QUESTIONS]=sum(value[2*NUM_QUESTIONS:3*NUM_QUESTIONS])
    pbar.set_postfix_str(f'{students_counter+1/len(students_result):7.3f}')
    pbar.update(1)
    students_counter+=1
pbar.close()
pickle.dump({key:value[2*NUM_QUESTIONS:3*NUM_QUESTIONS] for key,value in students_result.items()},open(os.path.join(history_dir,'Auto.pkl'),"wb"))


# Show Auto grade data: proportion of the 3 most status of each question
for serial in range(1,1+NUM_QUESTIONS):
    status_counter={}
    for key,value in students_result.items():
        status_counter[value[serial-1]]=status_counter.get(value[serial-1],0)+1
    # show the biggest 3 status and their proportion
    print(f'Question {serial}')
    for status in sorted(status_counter,key=lambda x:status_counter[x],reverse=True)[:3]:
        print(f'{status}:{status_counter[status]/len(students_result):7.3f}')
    print('\n-----------------------------------------------------\n')

    
    
def ntimes_input(total_score,ntimes=3):
    for try_time in range(ntimes):
        try:
            manual_score=eval(input(f'Manual score (total {total_score} ) :'))
            assert 0<=manual_score<=total_score
        except:
            print(bcolors.OKBLUE+'Illegal Input'+bcolors.ENDC)
        else:
            break
    else:
        plt.close()
        assert False,f'Illegal Input for {ntimes} times, exit.'
    return manual_score


# Manual Score
if MANUAL_EXAMINATION_0:
    plt.ion()
    plt.figure(2, figsize=(10,15))
    ordered_students_result=OrderedDict(sorted(students_result.items(),key=lambda x:x[0]))
    for key in ordered_students_result.keys():
        value=students_result[key]
        for serial in range(1,1+NUM_QUESTIONS):
            status=value[serial-1]
            if status in ['Image','NotPFile','InputNotEnough','UnicodeError','ExeFail','OutputBlank','TimeOut','False']:
                print(f'   sid:{key}   serial:{serial}   {bcolors.OKRED}{status}{bcolors.ENDC}  ')
                if key in manual_history_data.keys() and serial in manual_history_data[key].keys():
                    manual_score=manual_history_data[key][serial]
                    print(f'History score (total {totalscorelist[serial-1]} ) :{manual_score}')
                else:
                    if status in ['Image']:
                        try:
                            plt.imshow(plt.imread(os.path.join(submission_dir,to_filename_table[key][serial])))
                        except:
                            print(bcolors.OKBLUE+'Read Image File Failed'+bcolors.ENDC)
                        else:
                            plt.pause(0.7)
                            print(bcolors.OKBLUE+"Evaluate image in subwindow"+bcolors.ENDC)
                        manual_score=ntimes_input(totalscorelist[serial-1])
                        plt.clf()
                    elif status in ['NotPFile']:
                        print(bcolors.OKBLUE+'Not Python File, Manual Check Please'+bcolors.ENDC)
                        manual_score=ntimes_input(totalscorelist[serial-1])
                    else:
                        try:
                            fp=open(os.path.join(submission_dir,to_filename_table[key][serial]),'r',encoding='utf-8')
                            content=fp.read()
                        except:
                            print(bcolors.OKBLUE+'Read Python File Failed'+bcolors.ENDC)
                        else:
                            print(bcolors.OKLBLUE+content+bcolors.ENDC)
                        finally:
                            fp.close()
                        print(bcolors.OKLYELLOW+value[serial-1+NUM_QUESTIONS]+bcolors.ENDC)
                        manual_score=ntimes_input(totalscorelist[serial-1])
                    manual_history_data[key]=manual_history_data.get(key,{})
                    manual_history_data[key][serial]=manual_score
                    manual_count+=1
                    if manual_count%5==0:
                        with open(target_path,"wb") as fp:
                            pickle.dump(manual_history_data,fp)
                print('\n-----------------------------------------------------\n')
                students_result[key][serial-1+2*NUM_QUESTIONS]=manual_score
        students_result[key][3*NUM_QUESTIONS]=sum(value[2*NUM_QUESTIONS:3*NUM_QUESTIONS])
    plt.close()
    plt.ioff()
    plt.show()


# result output to csv file

with open(os.path.join(result_dir,'originate_result.csv'),'w',encoding='utf-8') as f:
    f.write('sid,'+"".join([f'status{i},' for i in range(1,NUM_QUESTIONS+1)])+"".join([str(i)+',' for i in range(1,NUM_QUESTIONS+1)])+'Total\n')
    for key,value in students_result.items():
        f.write(f'{key}')
        for i in range(NUM_QUESTIONS):
            f.write(f',{students_result[key][i]}')
        for i in range(NUM_QUESTIONS+1):
            f.write(f',{students_result[key][i+2*NUM_QUESTIONS]}')
        f.write('\n')

# result output to file(find the corresbonding sid)
with open(os.path.join(name_sid_file),'r',encoding='gbk') as f1:
    name_sid=pd.read_csv(f1)
with open(os.path.join(result_dir,'originate_result.csv'),'r',encoding='utf-8') as f2:
    sid_score=pd.read_csv(f2)
sid_name_score=pd.merge(name_sid,sid_score,on='sid',how='left')
for serie_name in [str(i) for i in range(1,NUM_QUESTIONS+1)]:
    sid_name_score[serie_name]=sid_name_score[serie_name].astype(pd.Int64Dtype())
with open(os.path.join(result_dir,'graded01.csv'),'w',encoding='utf-8',newline='') as f3:
    sid_name_score.to_csv(f3,encoding='utf-8')