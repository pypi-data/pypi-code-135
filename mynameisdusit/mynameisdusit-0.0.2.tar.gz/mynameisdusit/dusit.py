import random  

class UncleEngineer:
	"""
	This is about uncle engineer
	have website and youtube

	Example
	# ----------------------
	uncle = UncleEngineer()
	uncle.show_name() 
	uncle.show_youtube()
	uncle.show_page()
	uncle.about()
	uncle.show_art()
	# ---------------------
	"""

	def __init__(self):
		self.name = 'Dusit Lim'
		self.page = 'https://www.youtube.com/watch?v=5bN1wFTi89U'

	def show_name(self):
		print('Hello my name is {}'.format(self.name))

	def show_youtube(self):
		print('https://www.youtube.com/watch?v=BxcUnjuyonU&t=1s')

	def show_page(self):
		print('Youtube: {}'.format(self.page))

	def about(self):
		text = """
		-----------------------------------------
		Hello, it is me who is studying programming.
		I am following uncle webpage.
		-----------------------------------------
		"""

		print(text)

	def show_art(self):
		text = """
		    .-----.
		   .' -   - '.
		  /  .-. .-.  \
		  |  | | | |  |
		   \\ \\o/ \\o/ /
		  _/    ^    \\_
		 | \\  '---'  / |
		 / /`--. .--`\\ \
		/ /'---` `---'\\ \
		'.__.       .__.'
		    `|     |`
		     |     \
		     \\      '--.
		      '.        `\
		        `'---.   |
		   jgs     ,__) /
		            `..'		Credit: Joan Stark

		"""

		print(text)

	def dice(self):
		dice_list = ['⚀','⚁','⚂','⚃','⚄','⚅']	
		first = random.choice(dice_list)
		second = random.choice(dice_list)
		print('Your dice result is {} {}'.format(first,second))


if __name__ == '__main__':
	uncle = UncleEngineer()
	uncle.show_name() 
	uncle.show_youtube()
	uncle.show_page()
	uncle.about()
	uncle.show_art()
	uncle.dice()