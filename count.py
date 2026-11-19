print("Welcome to Python")
text=input("Enter text: ")

letters=0
numbers=0
special=0

for ch in text:
    if ch.isalpha():
        letters+=1
    elif ch.isdigit():
        numbers+=1
    else:
        special+=1

print("Letters:", letters)
print("Numbers:", numbers)
print("Special characters:", special)

print("Counting completed, Thank You")