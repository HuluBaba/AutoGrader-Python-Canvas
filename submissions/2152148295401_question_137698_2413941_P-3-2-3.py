s=input("输入表达式: ")
count=0
for c in s:
    if c=="(":
        count=count+1
    elif c==")":
        count=count-1
if count==0:
    print("左右括号配对")
elif count>0:
    print("左括号比右括号多",count,"个")
else:
    print("右括号比左括号多",-count,"个")  