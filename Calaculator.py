import time
def calc(N1,N2,op):
        if op==1:
            ans=N1+N2
            print("Answer is", ans)
        elif op==2:
            ans=N1-N2
            print("The Answer Is",ans)
        elif op==3:
            ans=N1*N2
            print("The Answer Is",ans)
        elif op==4:
            ans=N1/N2
            print("The Answer Is",ans)
        else:
            print("""error &*52**^%68757 error
                PL3AS3 R3START APPL1CAT1ON""")
            exit()
def tutor():
    print("In this application, the first number will be the number that is operated on.")
    time.sleep(0.5)
    print("The second number will be the the number operating on the first number.")
    time.sleep(0.5)
    print("Do you want to start?(Yes or No)")
    start=str(input("-->"))
    strt(start)
def strt(start):
    if start=="Yes" or start=="yes" or start=="1":
        flag1=0
        flag2=0
        flagop=0
        while(flag1==0):
            N1=input("Number 1-->")
            if N1.isdigit():
                n1 = int(N1)
                flag1=1
            else:
                print("Wrong datatype. Please enter an integer.")
        time.sleep(0.5)
        while(flag2==0):
            N2=input("Number 2-->")
            if N2.isdigit():
                n2 = int(N2)
                flag2=1
            else:
                print("Wrong datatype. Please enter an integer.")
        time.sleep(0.5)
        print("(Choose your operation (1 for +, 2 for -, 3 for *, 4 for /)")
        while(flagop==0):
            op=input("-->")
            if op.isdigit():
                op1 = int(op)
                flagop=1
            else:
                print("Wrong datatype. Please enter an integer.")
        time.sleep(0.5)
        calc(n1,n2,op1)
        print("Do you want to continue?(Yes or No)")
        start=str(input("-->"))
        strt(start)
    elif start=="No" or start=="no" or start=="0":
        print("Thanks For Playing, Bye..")
    else:
        print("""error &*52**^%68757 error
            PL3AS3 R3START APPL1CAT1ON""")   
print("Welcome to the Calculator!")
time.sleep(0.5)
print("Do you want to see the tutorial?(Yes or No)")
tut=str(input("-->"))
if tut=="Yes"or tut=="yes" or tut=="1":
    tutor()
elif tut=="No"or tut=="no" or tut=="0":
    print("Do you want to start?(Yes or No)")
    start=str(input("-->"))
    strt(start)
else:
    print("""error &*52**^%68757 error
        PL3AS3 R3START APPL1CAT1ON""")