class Player():
	def __init__(self, name, score = 0):
		self.name  = name
		self.score = score
	def __str__(self):
		rep = self.name + ':\t' + str(self.score)
		return rep

def ask_number(question, low, high):
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return int(response)

def ask_yes_no(question):
	response = None
	while response not in ('yes', 'no'):
		response = input(question).lower()
	return response

if __name__ == "__main__":
	print('Модуль для игр')
	input('\nEnter, чтобы выйти')