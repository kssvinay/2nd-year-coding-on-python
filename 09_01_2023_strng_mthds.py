s=input()
atoz=digits=uc=lc=0
for i in s:
    if i.isalpha():
        atoz=atoz+1  
    if i.isdigit():
        digits=digits+1  
    if i.isupper():
        uc=uc+1  
    if i.islower():
        lc=lc+1    
if atoz>0 or digits>0:
    print(True)
else:
    print(False)
if atoz>0:
    print(True)
else:
    print(False)
if digits>0:
    print(True)
else:
    print(False)
if lc>0:
    print(True)
else:
    print(False)
if uc>0:
    print(True)
else:
    print(False)
