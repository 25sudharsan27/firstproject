print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
s=0
if playing.lower() != "yes":
    quit()
print("Okay! Let's play:)")
answer=input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    s=s+1
else:
    print("Incorrect!")

answer=input("What does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    s=s+1
else:
    print("Incorrect!")
answer=input("What does RAM stand for?")
if answer == "random access memory":
    print('Correct!')
    s=s+1
else:
    print("Incorrect!")
answer=input("What does PSU stand for?")
if answer.lower()=="power supply":
    print("Correct!")
    s=s+1
else:
    print("Incorrect!")
print("You got " + str(s) + "question correctly")
p=(s/4)*100
print("You got " + str(p) + "%.")