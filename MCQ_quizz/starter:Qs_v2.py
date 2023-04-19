from question_class_v2 import *

playStatus = input("would you like to take the MCQ quizz ? (y/n) : ")
if playStatus.lower().strip() == "n":
    print("Next time then, have a nice day :)")
    quit()
elif playStatus.lower().strip() != "y":
    print("invalid input, try again")
    quit()
else:
    print("lets begin !")

name = input("enter your name here : ")

question_prompts = [
    "(Q1) How many stars make up the big dipper \n(a) 7 \n(b) 19 \n(c) 4 \nEnter your answer here : ",
    "(Q2) How many stars are there in the flag of Australia \n(a) 3 (b) 8 (c) 6 \nEnter your answer here : ",
    "(Q3) What country has the longest coastline \n(a) Japan (b) Canada (c) Jamaica \nEnter your answer here : ",
    "(Q4) What is a score of zero called in tennis \n(a) Nil (b) Turkey (c) Love \nEnter your answer here : ",
    "(Q5) What is the SI unit of magnetism \n(a) Ampere (b) Tesla (C) Watts \nEnter your answer here : ",
    "(Q6) What year did World War 1 end in \n(a) 1918 (b) 1920 (C) 1917 \nEnter your answer here : "
]

questions = [
    Questions(question_prompts[0], ("a", "7")),
    Questions(question_prompts[1], ("c", "6")),
    Questions(question_prompts[2], ("b", "canada")),
    Questions(question_prompts[3], ("c", "love")),
    Questions(question_prompts[4], ("b", "tesla")),
    Questions(question_prompts[5], ("a", "1918"))
]


def start_game(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower().strip() in question.answer:
            score += 1
        print("\n")
    print("\n")
    print(f"you got {score}/{len(question_prompts)} questions correct {name}")
    print(f"you scored {round((score / len(question_prompts)) * 100)}%")


start_game(questions)
