text=input("Enter text: ")

letters=0
numbers=0

for ch in text:
    if ch.isalpha():
        letters+=1
    elif ch.isdigit():
        numbers+=1

print("Letters:", letters)
print("Numbers:", numbers)