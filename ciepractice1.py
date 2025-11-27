import sys
if len(sys.argv)==5 :
script_name=sys.argv[0]
sub1=sys.argv[1]
sub2=sys.argv[2]
sub3=sys.argv[3]
sub4=sys.argv[4]
else :
 script_name=sys.argv[0]
 sub1=20
 sub2=30
 sub3=20
 sub4=10
print("sub 1 =",sub1)
print("sub 2 =",sub2)
print("sub 3 =",sub3)
print("sub 4 =",sub4)
avg=(sub1+sub2+sub3+sub4)/4
print("average=",avg)
if(avg>35) :
  print("a")
elif(avg>30) :
  print("b")
elif(avg>20) :
  print("c") :
else :
  print("d") 
