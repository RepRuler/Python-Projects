import random
import time
print("Welcome to RNG!")
time.sleep(1)
print("You Have To Guess A Number From 1-10 In 3 Tries")
ans=random.randrange(1,10)
x=int(input("Try One-->"))
time.sleep(1)
if(x==ans):
    print("Your Answer Is Correct!!")
else:
    print("The answer is wrong")
    y=int(input("Try Two-->"))
    time.sleep(1)
    if(y==ans):
        print("Your Answer Is Correct!!")
    else:
        print("The answer is wrong")
        z=int(input("Try Three-->"))
        time.sleep(1)
        if(z==ans):
            print("Your Answer Is Correct!!")
        else:
            print("The answer is wrong")
            time.sleep(1)
            print("You Failed")
            time.sleep(1)
            print("You Noob")
            time.sleep(1)
            print("The Answer Was",ans)