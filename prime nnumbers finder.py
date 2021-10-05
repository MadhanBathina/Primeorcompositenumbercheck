n=int(input('Enter a Number'))
notprime = False
if n>1:
    for i in range (2, n):
        if (n%i) == 0 :
            notprime = True
            break
if notprime:
    print(n,'is a Composite number')
else :
    print(n,'is a Prime number')
