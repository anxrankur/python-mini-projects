score = 0

print("=== Python Quiz ===")

answer = input("1. What is the capital of India? ")
if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. Which language are we learning? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. 5 + 5 = ")
if answer == "10":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nYour Score:", score, "/3")
