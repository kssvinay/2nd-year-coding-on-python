'''write a program to print student is pass or fail
sno,sname,group,s1`,s2,s3
c1:s1>=35 c2:s2>=35  c3:s3>=35--all conditions satisfy  true print pass
otherwise print fail'''

sno = input()
sname = input()
group = input()
s1 = int(input())
s2 = int(input())
s3 = int(input())
if s1>=35 and s2 >=35 and s3>=35:
  print("pass")
else:
  print("fail")
