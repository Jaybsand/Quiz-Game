print("Welcome to my workout quiz!")

playing = input("would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Awesome Let's get started!")
score = 0

answer = input("Should you warm up before your workout? ")

if answer.lower() == "yes":
    print("That's Correct! You should always warm up before working out to avoid injuries.")
    score += 1
else:
    print("That's incorrect! You Should always warm up before working out to avoid injuries.")


answer = input("When should you use pre-workout? ")

if answer.lower() == "before working out":
    print("That's Correct! pre-workout is used before working out to prepare your body.")
    score += 1
else:
    print("That's incorrect! pre workout is used before working out to prepare your body.")


answer = input("Is stretching good before or after your workout? ")

if answer.lower() == "both":
    print("That's Correct! You can stretch before or after your workout both are good for you.")
    score += 1
else:
    print("That's incorrect! You can stretch before or after your workout both are good for you.")


answer = input("What is the cleanest source of protein? ")

if answer.lower() == "chicken":
    print("That's Correct! Chicken is the best source of protein.")
    score += 1
else:
    print("That's incorrect! Chicken is the best source if protein.")

print("You got " + str(score) + " questions correct!")
print("You got" + str((score / 4) * 100) + "%.")
