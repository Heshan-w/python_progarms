from questions_v1 import *
correct = 0
question_tot = 5

playStatus = input("would you like to take the MCQ quizz ? (y/n) : ")
if playStatus.lower() == "n":
    print("Next time then, have a nice day :)")
    quit()
elif playStatus.lower() != "y":
    print("invalid input try again")
    quit()
else:
    print("lets begin !")

name = input("enter your name : ")
print("\n")
player = quiz(name)

player.question_1()
answer = input("Enter your answer here : ")
if answer.lower().strip() in player.q1_ans():
    correct += 1
print("\n")

player.question_2()
answer = input("Enter your answer here : ")
if answer.lower().strip() in player.q2_ans():
    correct += 1
print("\n")

player.question_3()
answer = input("Enter your answer here : ")
if answer.lower().strip() in player.q3_ans():
    correct += 1
print("\n")

player.question_4()
answer = input("Enter your answer here : ")
if answer.lower().strip() in player.q4_ans():
    correct += 1
print("\n")

player.question_5()
answer = input("Enter your answer here : ")
if answer.lower().strip() in player.q5_ans():
    correct += 1
print("\n")


print(f"you correctly answered {correct}/{question_tot} questions {player.get_name()}")
print(f"you scored {correct/question_tot * 100}%")
