import json
import random

with open("questions.json", "r") as f:
    questions = json.load(f)

questions = random.sample(questions, 10)

score = 0
total = len(questions)

print("Welcome to the Quiz Game!\n")

for i, q in enumerate(questions, start=1):
    print(f"Q{i}: {q['question']}")
    options = q["options"]
    random.shuffle(options)
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")
    try:
        choice = int(input("Your choice (1-4): "))
        if options[choice - 1].lower() == q["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}\n")
    except (ValueError, IndexError):
        print(f"Invalid input! Correct answer: {q['answer']}\n")

print("Quiz Finished!")
print(f"Your score: {score}/{total}")
