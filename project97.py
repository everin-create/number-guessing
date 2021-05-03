print('number guessing game')
print('choose a number between 1 to 9')
num= 8
for i in range(5):
    guess=int(input("enter your guess"))
    if(guess==num):
        print('you got the number!!')
        break
    elif(guess>num):
        print("the number is lesser than this number")
    else:
        print('the number is more than this number')
