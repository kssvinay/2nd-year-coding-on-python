def swap_case(s):
    ans = ""
    for c in s:
        if c.isupper():
            ans += c.lower()
        elif c.islower():
            ans += c.upper()
        else:
            ans += c
    return ans

if _name_ == '_main_':
  s= input()
  print(swap_case(s))
