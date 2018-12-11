x,b,c=map(int,raw_input().split())
if(x>b and x>c):
  num1=x
  num2=b
  num3=c
elif(b>c and b>a):
  num1=b
  num2=x
  num3=c
else:
  num1=c
  num2=x
  num3=b
num1=num1**2
num2=num2**2
num3=num3**2
num4=num2+num3
if(num1==num4):
    print("yes")
else:
    print("no")
