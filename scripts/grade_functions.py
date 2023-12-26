import re

def grade_1(answer):
    lines=answer.splitlines()
    i=0
    while i<len(lines) and lines[i].strip()!='a' :
        i+=1
    if i==len(lines):
        return 0
    start_line=i
    chr_len=1
    chr_ord=ord('a')
    is_legal=True
    while i<len(lines) and lines[i].strip()==chr(chr_ord)*chr_len :
        chr_len+=1
        chr_ord+=1
        i+=1
    if 5<=i-start_line<=10:
        return 3
    else:
        return 2
    
def grade_2(answer):
    lines=answer.splitlines()
    i=0
    while i<len(lines) and lines[i].strip()!='A' :
        i+=1
    if i==len(lines):
        return 0
    chr_list_A=['A','B','C','D','E','F','G','H','I','J']
    pt_chrs=[]
    pt_lens=[]
    while i<len(lines) and lines[i].strip() and lines[i].strip()[0] in chr_list_A:
        pt_line=lines[i].strip()
        pt_chr=pt_line[0]
        pt_len=len(pt_line)
        for j in range(pt_len):
            if pt_line[j]!=pt_chr:
                return 0
        pt_chrs.append(pt_chr)
        pt_lens.append(pt_len)
        i+=1
    mode_A=True
    mode_B=False
    for i in range(len(pt_chrs)):
        if mode_A:
            if pt_chrs[i]!=chr_list_A[i]:
                mode_A=False
                mode_B=True
                repetition_line=i
                if repetition_line!=len(pt_chrs)//2+2:
                    return 0
            else:
                continue
        elif mode_B:
            if pt_chrs[i]!=chr_list_A[i-1]:
                mode_A=False
                mode_B=False
                break
            else:
                continue
    num_line=len(pt_chrs)
    if not mode_A and not mode_B:
        return 0
    elif num_line%2==0:
        turning_line=num_line//2
        for i in range(num_line):
            if i<turning_line:
                if pt_lens[i]!=2*i+1:
                    return 0
            else:
                if pt_lens[i]!=4*turning_line-2*i-1:
                    return 0
    else:
        turning_line=num_line//2
        for i in range(num_line):
            if i<turning_line:
                if pt_lens[i]!=2*i+1:
                    return 0
            else:
                if pt_lens[i]!=4*turning_line-2*i+1:
                    return 0
    return 3
    


def grade_3(answer):
    tokens=re.findall(r'左|右|多|少',answer)
    if len(tokens)==3:
        if tokens in [['右','多','左'],
                      ['左','少','右']
                      ]:
            return 3
        else:
            return 0
    else:
        return 0

def grade_4(answer):
    word="international"
    length='13'
    word_exist=re.findall(word,answer)
    length_exist=re.findall(length,answer)
    count=0
    if len(word_exist)>=1:
        count+=2
    if len(length_exist)>=1:
        count+=1
    return count

def grade_5(answer):
    pattern="488962"
    pattern_exist=re.findall(pattern,answer)
    if len(pattern_exist)>=1:
        return 3
    else:
        return 0

def grade_6(answer):
    numbers=re.findall(r'(?:[-+]?\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', answer)
    count=0
    for number in numbers:
        number=eval(number)
        if 2.3594<=number<=2.3596:
            count+=1
    if count>=1:
        return 3
    else:
        return 0

def grade_7(answer):
    numbers=re.findall(r'(?:[-+]?\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', answer)
    count=0
    for number in numbers:
        number=eval(number)
        if 3.1407<=number<=3.1409 or -0.0093<number<0.00090:
            count+=1
    if count>=1:
        return 3
    else:
        return 0

def grade_8(answer):
    numbers=re.findall(r'(?:[-+]?\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', answer)
    count=0
    for number in numbers:
        value=eval(number)
        if value in [153,370,371,407]:
            count+=1
    if count==4:
        return 3
    elif count==3:
        return 2
    elif count!=0:
        return 1
    else:
        return 0

def grade_9(answer):
    process_1=re.findall(r'2222',answer)
    process_2=re.findall(r'22222222',answer)
    n_process_3=re.findall(r'222222222',answer)
    result=re.findall(r'24691356',answer)
    count=0
    if len(result)>=1:
        count+=2
    if len(n_process_3)>=1:
        count+=0
    elif len(process_2)>=1 and len(process_1)>=1:
        count+=1
    else:
        count+=0
    return count

def grade_10(answer):
    chinese_to_numbers={'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'日':7}
    chinese_numbers=['一','二','三','四','五','六','七','日']
    lines=answer.splitlines()
    right_combinations=[(1,2,5),
                        (1,2,6),
                        (1,3,5),
                        (1,3,6),
                        (1,4,5),
                        (1,4,6),
                        (1,5,6),
                        (2,3,5),
                        (2,3,6),
                        (2,4,5),
                        (2,4,6),
                        (2,5,6),
                        (3,4,5),
                        (3,4,6),
                        (3,5,6),
                        (4,5,6)
                        ]
    count=0
    out_of_RC=False
    detected=[False for item in right_combinations]
    for line in lines:
        numbers=re.findall(r'1|2|3|4|5|6|7|一|二|三|四|五|六|七|日',line)
        numbers=((chinese_to_numbers[number] if number in chinese_to_numbers.keys() else eval(number) for number in numbers))
        if numbers in right_combinations:
            detected[right_combinations.index(numbers)]=True
        else:
            out_of_RC=True
    count+=sum(detected)
    if count==16 and not out_of_RC:
        return 3
    elif count==16 and out_of_RC:
        return 2
    elif 0<count<16 and not out_of_RC:
        return 2
    elif 0<count<16 and out_of_RC:
        return 1
    else:
        return 0

def grade_11(answer):
    return 3



grade_functions=[grade_1,grade_2,grade_3,grade_4,grade_5,grade_6,grade_7,grade_8,grade_9,grade_10,grade_11]
