import random
import colorama
from colorama import Fore

print(Fore.RED + "WELCOME TO THE GUESSING GAME!!")
print(Fore.MAGENTA + "You get 3 chances to guess the number.")

num1 = random.randint(0,20)
print(num1)
print(Fore.RESET + "")

usernum = int(input("Enter your guess: "))
count = 3

while usernum != num1:
	count -= 1
	if count <= 0:
		break
	if usernum > num1:
		print("Your guess is too high\nTRY AGAIN!!")
		print("You have " + str(count) + " chances remaining")
		usernum = int(input("Enter a number: "))
	if usernum < num1:
		print("Your guess is too low\nTRY AGAIN!!")
		print("You have " + str(count) + " chances remaining")
		usernum = int(input("Enter a number: "))
if usernum == num1:
	print(Fore.MAGENTA + "You win!!! :D".upper())
	quit()

print(Fore.MAGENTA + "Out of chances\nYou lose!!".upper())

		








