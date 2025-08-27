import random

#easy to intermediate password
print("Welcome to Jeevan PyPassword Generator !")
nr_char = int(input("How many characters do you have? : "))
nr_symbols = int(input("How many symbols do you have? : "))
nr_numbers = int(input("How many numbers do you have? : "))
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','&','*','(',')']
numbers = ['1','2','3','4','5','6','7','8','9']
password = ""
for i in range(1,nr_char+1):
    password += random.choice(characters)
for i in range(1, nr_symbols+1):
    password+=random.choice(symbols)
for i in range(1, nr_numbers+1):
    password += random.choice(numbers)
print(f"Your Password is : {password}")

#hard to guess password
temp = []
for i in range(1,nr_char+1):
    temp.append(random.choice(characters))
for i in range(1, nr_symbols+1):
    temp.append(random.choice(symbols))
for i in range(1, nr_numbers+1):
    temp.append(random.choice(numbers))
random.shuffle(temp)
strong_pass = ""
for char in temp:
    strong_pass += char
print(temp)

print(f"Your strong password is : {strong_pass}")