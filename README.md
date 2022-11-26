# Palidrome
To check a Palindrome Number
def pal(p):
    if len(p)<1:
      return True
    else:
        if p[0]==p[-1]:
            return pal(p[1:-1])
        else:
            return False
a=str(input("Enter a number:"))
if (pal(a)==True):
    print("is palidrome")
else:
    print("not palidrome")
