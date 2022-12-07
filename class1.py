import random
def check(str1,choosen_word):
    #Checking for the match
    print()
    print(str1)
    if choosen_word == str1:
        print("*****")
        return True
    #converting string to list
    l1 = list(str1)
    counter = 0
    out=''
    #Checking with the string
    for letter in l1:
        if counter == 5:
            break
        if letter == choosen_word[counter]:
            out = out+'*'
        elif letter in choosen_word:
            out = out+'?'
        else:
            out = out+'x'
        counter += 1
    print(out)
    print()
    return False


#Defining words
#words = ['thanu','lekhs','rachu','vinni','bharr','kallu']
file1 = open('words.txt', 'r')
words = file1.readlines()
choosen_word=random.choice(words)[:-1]
#input from user
print("Hello!")
flag = False
i = 0#loop counter
while True:
    test_str = input("Guess the string: ")
    if len(test_str) != 5:
        print("Please enter a 5 letter word")
        continue
    if test_str.lower()+'\n' not in words:
        print("Invalid Word")
        continue
    flag = check(test_str.lower(),choosen_word)
    if i==5:
        break
    i+=1
    if flag == True:
        break

    
#Checking the no of tries
if i == 0 and flag==True:
    print("Awesome! You guessed it in your first try")
elif i == 1 and flag==True:
    print("Very Good\nYour guess is correct")
elif i == 2 and flag==True:
    print("Good\nYou are correct")
elif i == 3 and flag==True:
    print("Nice\nYou are correct")
elif i == 4 and flag==True:
    print("Not Bad\nYou are correct")
elif i == 5 and flag==True:
    print("Finally it is correct! \nYou need practice")
else:
    print(choosen_word)
    print("Better luck next time")
    
