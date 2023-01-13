import json

with open("questions.json") as file:
    content = file.read()

score = 0

data = json.loads(content)
for question in data:
    print(question["question"])
    for index, option in enumerate(question["options"]):
        print(f"{index + 1} - {option}")
    user_option = int(input("Enter your answer: "))
    question["user_option"] = user_option

for index, question in enumerate(data):
    if question["user_option"] == question["correct_option"]:
        score = score + 1
        result = "Correct answer!"
    else:
        result = "Wrong answer!"
    print(f"{index+1} - {result} Your answer : {question['user_option']}, Correct answer : {question['correct_option']}")

print(f"score: {score}/{len(data)}")

