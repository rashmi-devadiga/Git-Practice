print("Welcomeback to practice branch")
print("Keep Learning")
text=input("Enter text: ")

letters=0
numbers=0
special=0
spaces = 0

for ch in text:
    if ch.isalpha():
        letters+=1
    elif ch.isdigit():
        numbers+=1
    elif ch.isspace():
        spaces += 1
    else:
        special+=1

total = letters + numbers + spaces + special

print("Letters:", letters)
print("Numbers:", numbers)
print("Special characters:", special)
print("Spaces:", spaces)
print("Total characters:", total)

print("Counting completed, Thank You")
