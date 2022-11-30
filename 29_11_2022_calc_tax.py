''' write a program to generate employee tax?

inputs:
empo,empname,empdesig,basicsalary,da(daily allowance),ta(Travelling allowance),hra(House Rental allowance),netsalary,tax
Process:
netsalary=basicsalary+da+ta+hra
Calculate tax:
    if netsalary>1lac
            tax=netsalary*10/100   netsalry>50thousand
           tax=7%
           >40000
              tax=4% 
              >20000
              tax=2 %
              <20000
              tax=0
print tax'''
empo = int(input())
empname = input()
empdesig = input()
salary = int(input())
da = int(input())
ta = int(input())
hra = int(input())
ns = salary + da+ta +hra
print("net salary is ",ns)
if ns > 100000:
  tax = ns*0.1
elif ns>50000:
  tax = ns*0.07
elif ns>40000:
  tax = ns*0.04
elif ns>20000:
  tax = ns*0.02
else:
  tax = 0
print("tax for",empname,"is",tax)
