print("🔐 Password Strength Checker")

password = input("Enter your password: ")

length = len(password)

has_number = False
has_uppercase = False
has_lowercase = False
has_special = False

for char in password:
    if char.isdigit():
        has_number = True
    elif char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    else:
        has_special = True

score = 0

if length >= 8:
    score += 1

if has_number:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

if has_special:
    score += 1


if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")