#Deep python. Homework 1.
#Task 3.
#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать «больше» или «меньше» после каждой попытки.
#Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
def enter_number():
	while True:
		try:
			number = int(input("Enter number:\n>>>"))
			if number < -1:
				raise Exception
			break
		except Exception:
			print("It's not allowed number, try again")
	
	return number	


def player_mode():
	number = randint(0, 1001)
	print('For exit enter -1\nGuess number from 0 to 1000 ')
	for i in range(10):
		print(f'You have {10 - i} tries')
		ans = enter_number()
		if ans == -1:
			answer = 'Exiting...'
			print(answer)
			break
		if ans > number:
			answer = 'Lower'
		elif ans < number:
			answer = 'Higher'
		elif ans == number:
			answer = "Congratulations, you're right!"
		print(answer)
		if ans == number:
			break
	print(f'Game over. It was {number}. Good luck next time!')
	
	
def ai_mode():
	win = 0
	min_ans = -1
	max_ans = 1001
	for i in range(10):
		if win == 1:
			break
		guess = (min_ans + max_ans) // 2
		print(f"I guess it's number {guess}")
		try:
			ans = input("Enter 'h' or 'l' if answer is higher or lower than AI's guess\nEnter '+' if AI's right\n")
			if ans == 'h':
				min_ans = guess
			elif ans == 'l':
				max_ans = guess
			elif ans == '+':
				win = 1
			else:
				raise Exception
		except Exception:
			print(f'Command unknown, try again')

while True:
	mode = input("Choose who's guessing:\n1 for you, 2 for AI\nEnter exit for exit\n")
	if mode.lower() == 'exit':
		print('Exiting...')
		break
	elif mode == '1':
		player_mode()
	elif mode == '2':
		ai_mode()
	else:
		print("Command unknown, try again")
	