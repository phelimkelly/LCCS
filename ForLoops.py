#For Loop Tasks from Textbook page 37
"""
#Task 1
for i in range(1,11):
    print(i)
    
i=1
while i<11:
    print(i)
    i+=1
    
#Task 2
num = int(input("Enter your number: "))
for i in range(1,num+1,2):
    print(i)
"""
#Task 3
sent = input("Enter your sentence: ")
vCounter=0
for char in sent:
    if char =="a" or char == "e"or char == "i"or char == "o"or char == "u":
        vCounter+=1
    elif char == "e":
        vCounter+=1
print ("There are",vCounter,"vowels in your sentence")

"""
#Task 4
sent = input("Enter your sentence: ")
sentLen = len(sent)
for i in range(sentLen-1,-1,-1):
    print(sent[i])


#Task 5
sent = input("Enter your sentence: ")
char = input("Enter your character: ")
sentLen = len(sent)
counter=0
for i in range (0,sentLen):
    if sent[i]==char:
        counter+=1
print("The letter",char,"appears",counter,"times in your sentence")

"""