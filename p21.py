x1,y1=map(int,raw_input().split())
x2,y2=map(int,raw_input().split())
x3,y3=map(int,raw_input().split())
if x1==0 and x2==0 and x3==0:
    print "yes"
elif y1==0 and y2==0 and y3==0:
    print "yes"
else:
    n=(y2-y1)/(x2-x1)
    d=(y3-y1)/(x3-x1)
    if n==d:
        print "yes"
    else:
        print "no"
  
