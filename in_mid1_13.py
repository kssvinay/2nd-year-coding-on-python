#Assignment -13:
#Write a program to print given list is Unique or Duplicate?
def dup():
    l = list(map(int,input().split()))
    for i in l:
        if l.count(i) > 1:
            print("duplicate")
            return
    print("unique")
dup();
