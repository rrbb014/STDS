import random

if __name__ == "__main__":
	with open('stds-problems.txt', 'r', encoding='utf8') as f:
		problems = [p for p in f.read().split('\n') if p != '']
	
	for _ in range(3):
		p = random.choice(problems)
		problems.remove(p)
		print(p)