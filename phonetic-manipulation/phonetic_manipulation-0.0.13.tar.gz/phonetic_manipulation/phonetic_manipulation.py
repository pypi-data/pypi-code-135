import pandas as pd
import re, os, pkg_resources

class Phonetic_Manipulation():
	"""
	Package designed for phonological analysis and IPA conversion phones to and from X-SAMPA

	Attributes
	__________
	ps : the full phoneset chart with features specified
	dm : a mapping chart for IPA diacritics
	ipa_p : a list of all the IPA phones for conversion
	dm_p : a list of all the IPA diacritics for conversion
	ipa_x : a list of all the X-SAMPA phones for conversion
	dm_x : a list of all the X-SAMPA diacritics for conversion

	vowels : a string of vowels ready for regex searching
		front_unrounded : a list of vowels of a certain place
		front_rounded : a list of vowels of a certain place
		mid_unrounded : a list of vowels of a certain place
		mid_rounded : a list of vowels of a certain place
		back_unrounded : a list of vowels of a certain place
		back_rounded : a list of vowels of a certain place
		high_front_unrounded_tense : a list of vowels of a certain place
		high_front_rounded_tense : a list of vowels of a certain place
		high_front_unrounded_lax : a list of vowels of a certain place
		high_front_rounded_lax : a list of vowels of a certain place
		high_front_unrounded : a list of vowels of a certain place
		high_front_rounded : a list of vowels of a certain place
		high_central_unrounded_tense : a list of vowels of a certain place
		high_central_rounded_tense : a list of vowels of a certain place
		high_central_unrounded_lax : a list of vowels of a certain place
		high_central_rounded_lax : a list of vowels of a certain place
		high_central_unrounded : a list of vowels of a certain place
		high_central_rounded : a list of vowels of a certain place
		high_back_unrounded_tense : a list of vowels of a certain place
		high_back_rounded_tense : a list of vowels of a certain place
		high_back_unrounded_lax : a list of vowels of a certain place
		high_back_rounded_lax : a list of vowels of a certain place
		high_back_unrounded : a list of vowels of a certain place
		high_back_rounded : a list of vowels of a certain place
		mid_front_unrounded_tense : a list of vowels of a certain place
		mid_front_rounded_tense : a list of vowels of a certain place
		mid_front_unrounded_lax : a list of vowels of a certain place
		mid_front_rounded_lax : a list of vowels of a certain place
		mid_front_unrounded : a list of vowels of a certain place
		mid_front_rounded : a list of vowels of a certain place
		mid_central_unrounded_tense : a list of vowels of a certain place
		mid_central_rounded_tense : a list of vowels of a certain place
		mid_central_unrounded_lax : a list of vowels of a certain place
		mid_central_rounded_lax : a list of vowels of a certain place
		mid_central_unrounded : a list of vowels of a certain place
		mid_central_rounded : a list of vowels of a certain place
		mid_back_unrounded_tense : a list of vowels of a certain place
		mid_back_rounded_tense : a list of vowels of a certain place
		mid_back_unrounded_lax : a list of vowels of a certain place
		mid_back_rounded_lax : a list of vowels of a certain place
		mid_back_unrounded : a list of vowels of a certain place
		mid_back_rounded : a list of vowels of a certain place
		low_front_unrounded : a list of vowels of a certain place
		low_front_rounded : a list of vowels of a certain place
		low_front : a list of vowels of a certain place
		low_central_unrounded : a list of vowels of a certain place
		low_central_rounded : a list of vowels of a certain place
		low_central : a list of vowels of a certain place
		low_back_unrounded : a list of vowels of a certain place
		low_back_rounded : a list of vowels of a certain place
		low_back : a list of vowels of a certain place
		dipthongs : a string of diphthongs ready for regex searching

	consonants : a string of consonants ready for regex searching
		glides : a list of consonants of a certain class
		liquids : a list of consonants of a certain class
		nasals : a list of consonants of a certain class
		obstruents : a list of consonants of a certain class
		stops : a list of consonants of a certain class
		affricates : a list of consonants of a certain class
		fricatives : a list of consonants of a certain class
	
	Methods
	_______
	from_IPA(word)
		Converts a word from IPA to X-SAMPA

	to_IPA(word)
		Converts a word to IPA from X-SAMPA

	__clarify_phones__(pd.DataFrame, phones, list of lists)
		Condenses the phoneset DataFrame based on specified list of phones

	__get_phones__(phonelist)
		Reduces processing by condencing DataFrame to only phones present in the data

	__phone_sets__(phones)
		Gets the phone attributes needed for analysis
	"""
	def __init__(self, phones: str, pl=None) -> None:
		"""
		Parameters:
		___________
		phones : str
			the phoneset you will be primarily using; accepts:
				- IPA
				- X-SAMPA
				- SAMPA
		pl : list
			an optional list of phones already found in the data
		"""

		phoneset = pkg_resources.resource_stream(__name__, 'data/phoneset_mapping.csv')
		diacritics = pkg_resources.resource_stream(__name__, 'data/diacritic_mappings.csv')

		self.ps = pd.read_csv(phoneset)
		self.dm = pd.read_csv(diacritics)
		if pl:
			self.__get_phones__(pl)
		self.__phone_sets__('IPA')
		self.ipa_p = self.ps['IPA'].tolist()
		self.dm_p = self.dm['IPA'].tolist()
		self.ipa_x = self.ps[phones].tolist()
		self.dm_x = self.dm['X-SAMPA'].tolist()

	def __clarify_phones__(self, df: pd.DataFrame, phones: str, *args) -> list:
		"""
		Condenses the data to a list of phones that match characteristics specified
		Parameters:
		___________
		df : pd.DataFrame
			a dataframe to condense
		phones : str
			the phoneset you will be primarily using; accepts:
				- IPA
				- X-SAMPA
				- SAMPA
		*args : list
			a list of lists that contain the phones to cross examine

		Returns:
		________
		df : list
			the condensed list of phones
		"""
		for l in args:
			df = df.loc[df[phones].isin(l)]
		return df[phones].tolist()

	def __phone_sets__(self, phones: str) -> None:
		"""
		Creates the instances of all the phone objects available for analysis

		Parameters:
		___________
		phones : str
			the phoneset you will be primarily using; accepts:
				- IPA
				- X-SAMPA
				- SAMPA
		"""
		vowelspace = self.ps['Syllabic']==1
		cons = self.ps['Consonantal']==1
		approx = self.ps['Approximant']==1
		son = self.ps['Sonorant']==1
		dr = self.ps['Delayed Release']==1
		cont = self.ps['Continuant']==1

		high = self.ps['High']==1
		low = self.ps['Low']==1
		tense = self.ps['Tense']==1
		front = self.ps['Front']==1
		back = self.ps['Back']==1
		r = self.ps['Round']==1

		vowels = self.ps.loc[vowelspace]
		self.vowels = '[' + ''.join(vowels[phones].tolist()) + ']'
		self.vowels = re.sub(r'\\', r'\\\\', self.vowels)

		self.high_tense = vowels.loc[(high) & (tense)][phones].tolist()
		self.high_lax = vowels.loc[(high) & (~tense)][phones].tolist()
		self.mid_tense = vowels.loc[(~high) & (tense)][phones].tolist()
		self.mid_lax = vowels.loc[(~high) & (tense)][phones].tolist()
		self.low = vowels.loc[low][phones].tolist()

		self.front_unrounded = vowels.loc[(front) & (~r)][phones].tolist()
		self.front_rounded = vowels.loc[(front) & (r)][phones].tolist()
		self.mid_unrounded = vowels.loc[(~front) & (~back) & (~r)][phones].tolist()
		self.mid_rounded = vowels.loc[(~front) & (~back) & (r)][phones].tolist()
		self.back_unrounded = vowels.loc[(back) & (~r)][phones].tolist()
		self.back_rounded = vowels.loc[(back) & (r)][phones].tolist()

		# High Front Vowels:
		self.high_front_unrounded_tense = self.__clarify_phones__(vowels, phones, self.high_tense, self.front_unrounded)
		self.high_front_rounded_tense = self.__clarify_phones__(vowels, phones, self.high_tense, self.front_rounded)
		self.high_front_unrounded_lax = self.__clarify_phones__(vowels, phones, self.high_lax, self.front_unrounded)
		self.high_front_rounded_lax = self.__clarify_phones__(vowels, phones, self.high_lax, self.front_rounded)
		self.high_front_unrounded = self.high_front_unrounded_tense + self.high_front_unrounded_lax
		self.high_front_rounded = self.high_front_rounded_tense + self.high_front_rounded_lax

		# High Central Vowels:
		self.high_central_unrounded_tense = self.__clarify_phones__(vowels, phones, self.high_tense, self.mid_unrounded)
		self.high_central_rounded_tense = self.__clarify_phones__(vowels, phones, self.high_tense, self.mid_rounded)
		self.high_central_unrounded_lax = self.__clarify_phones__(vowels, phones, self.high_lax, self.mid_unrounded)
		self.high_central_rounded_lax = self.__clarify_phones__(vowels, phones, self.high_lax, self.mid_rounded)
		self.high_central_unrounded = self.high_central_unrounded_tense + self.high_central_unrounded_lax
		self.high_central_rounded = self.high_central_rounded_tense + self.high_central_rounded_lax

		# High Back Vowels:
		self.high_back_unrounded_tense = self.__clarify_phones__(vowels, phones, self.high_tense, self.back_unrounded)
		self.high_back_rounded_tense = self.__clarify_phones__(vowels, phones, self.high_tense, self.back_rounded)
		self.high_back_unrounded_lax = self.__clarify_phones__(vowels, phones, self.high_lax, self.back_unrounded)
		self.high_back_rounded_lax = self.__clarify_phones__(vowels, phones, self.high_lax, self.back_rounded)
		self.high_back_unrounded = self.high_back_unrounded_tense + self.high_back_unrounded_lax
		self.high_back_rounded = self.high_back_rounded_tense + self.high_back_rounded_lax

		# Mid (Open-near to open-far) Front Vowels:
		self.mid_front_unrounded_tense = self.__clarify_phones__(vowels, phones, self.mid_tense, self.front_unrounded)
		self.mid_front_rounded_tense = self.__clarify_phones__(vowels, phones, self.mid_tense, self.front_rounded)
		self.mid_front_unrounded_lax = self.__clarify_phones__(vowels, phones, self.mid_lax, self.front_unrounded)
		self.mid_front_rounded_lax = self.__clarify_phones__(vowels, phones, self.mid_lax, self.front_rounded)
		self.mid_front_unrounded = self.mid_front_rounded_tense + self.mid_front_unrounded_lax
		self.mid_front_rounded = self.mid_front_rounded_tense + self.mid_front_rounded_lax

		# Mid (Open-near to open-far) Central Vowels:
		self.mid_central_unrounded_tense = self.__clarify_phones__(vowels, phones, self.mid_tense, self.mid_unrounded)
		self.mid_central_rounded_tense = self.__clarify_phones__(vowels, phones, self.mid_tense, self.mid_rounded)
		self.mid_central_unrounded_lax = self.__clarify_phones__(vowels, phones, self.mid_lax, self.mid_unrounded)
		self.mid_central_rounded_lax = self.__clarify_phones__(vowels, phones, self.mid_lax, self.mid_rounded)
		self.mid_central_unrounded = self.mid_central_rounded_tense + self.mid_central_unrounded_lax
		self.mid_central_rounded = self.mid_central_rounded_tense + self.mid_central_rounded_lax

		# Mid (Open-near to open-far) Back Vowels:
		self.mid_back_unrounded_tense = self.__clarify_phones__(vowels, phones, self.mid_tense, self.back_unrounded)
		self.mid_back_rounded_tense = self.__clarify_phones__(vowels, phones, self.mid_tense, self.back_rounded)
		self.mid_back_unrounded_lax = self.__clarify_phones__(vowels, phones, self.mid_lax, self.back_unrounded)
		self.mid_back_rounded_lax = self.__clarify_phones__(vowels, phones, self.mid_lax, self.back_rounded)
		self.mid_back_unrounded = self.mid_back_rounded_tense + self.mid_back_unrounded_lax
		self.mid_back_rounded = self.mid_back_rounded_tense + self.mid_back_rounded_lax

		# Low Front Vowels
		self.low_front_unrounded = self.__clarify_phones__(vowels, phones, self.low, self.front_unrounded)
		self.low_front_rounded = self.__clarify_phones__(vowels, phones, self.low, self.front_rounded)
		self.low_front = self.low_front_unrounded + self.low_front_rounded

		# Low Central Vowels
		self.low_central_unrounded = self.__clarify_phones__(vowels, phones, self.low, self.mid_unrounded)
		self.low_central_rounded = self.__clarify_phones__(vowels, phones, self.low, self.mid_rounded)
		self.low_central = self.low_central_rounded + self.low_central_unrounded

		# Low Back Vowels
		self.low_back_unrounded = self.__clarify_phones__(vowels, phones, self.low, self.back_unrounded)
		self.low_back_rounded = self.__clarify_phones__(vowels, phones, self.low, self.back_rounded)
		self.low_back = self.low_back_rounded + self.low_back_unrounded

		if phones == 'IPA':
			self.diphthongs = self.vowels + u'\u0361' + self.vowels
		else:
			self.diphthongs = self.vowels + '&' + self.vowels

		consonants = self.ps.loc[(~vowelspace)][phones].tolist()
		self.consonants = '[' + ''.join(consonants) + ']'
		self.consonants = re.sub(r'\\', r'\\\\', self.consonants)

		self.glides = self.ps.loc[(~vowelspace) & (~cons)][phones].tolist()
		#self.glides = '[' + ''.join(glides) + ']'

		self.liquids = self.ps.loc[(cons) & (approx)][phones].tolist()
		#self.liquids = '[' + ''.join(liquids) + ']'

		self.nasals = self.ps.loc[(~approx) & (son)][phones].tolist()
		#self.nasals = '[' + ''.join(nasal) + ']'

		self.obstruents = self.ps.loc[(~son)][phones].tolist()
		#self.obstruents = '[' + ''.join(obstruents) + ']'

		self.stops = self.ps.loc[(~son) & (~dr)][phones].tolist()
		#self.stops = '[' + ''.join(stops) + ']'

		self.affricates = self.ps.loc[(~son) & (~cont) & (dr)][phones].tolist()
		#self.affricates = '(' + '|'.join(affricates) + ')'

		self.fricatives = self.ps.loc[(~son) & (cont)][phones].tolist()
		#self.fricatives = '[' + ''.join(fricatives) + ']'

	def __get_phones__(self, pl: list) -> None:
		"""
		Condenses DataFrame with a predetermined list of phones.

		Parameters:
		___________
		pl : list
			a list of phones already found known to be included in the data
		"""
		self.ps = self.ps.loc[self.ps['IPA'].isin(pl)]

	def from_IPA(self, word: str) -> str:
		"""
		Converts a word from IPA to designated phoneset (X-SAMPA or SAMPA)

		Parameters:
		___________
		word : str
			a word to convert

		Returns:
		________
		word: str
			the converted word
		"""
		word = re.sub(u'\u0361', '&', word)

		new_word = []
		for letter in word:
			if '&' in letter:
				if re.search(self.vowels, letter):
					letter = letter.split('&')
					diphthong = []
					for l in letter:
						if l in ipa_p:
							i = self.ipa_p.index(l)
							diphthong.append(self.ipa_x[i])
						else:
							print(letter, l)
					new_word.append('&'.join(diphthong))
				else:
					letter = letter.split('&')
					affricate = []
					for l in letter:
						i = self.ipa_p.index(l)
						affricate.append(self.ipa_x[i])
					new_word.append(''.join(affricate))
			if letter in self.dm_p:
				i = self.dm_p.index(letter)
				new_word.append(self.dm_x[i])
				continue
			if letter in self.ipa_p:
				i = self.ipa_p.index(letter)
				new_word.append(self.ipa_x[i])
			else:
				new_word.append(letter)
	
		word = re.sub(' _', '_', ' '.join(new_word))

		return word

	def to_IPA(self, word: str) -> str:
		"""
		Converts a word back to IPA

		Parameters:
		___________
		word : str
			the word to convert

		Returns:
		________
		word: str
			the converted word
		"""
		new_word = []

		for letter in word.split():
			letter = self.to_IPA_l(letter)
			new_word.append(letter)
		word = ''.join(new_word)

		return word

	def to_IPA_l(self, letter):
		"""
		Converts a letter back to IPA

		Parameters:
		___________
		letter : str
			the letter to convert

		Returns:
		________
		letter: str
			the converted letter
		"""
		if '_' in letter:
			new_letter = []
			ds = letter.split('_')
			i = self.ipa_x.index(ds[0])
			new_letter.append(self.ipa_p[i])
			for i in range(len(ds[1:])):
				d = '_' + ds[i+1]
				n = self.dm_x.index(d)
				new_letter.append(self.dm_p[n])
			letter = ''.join(new_letter)
		elif '&' in letter:
			new_letter = []
			letter = letter.split('&')
			for l in letter:
				i = self.ipa_x.index(l)
				new_letter.append(self.ipa_p[i])
			letter = u'\u0361'.join(new_letter)
		else:
			new_letter = []
			for l in letter:
				if l in self.ipa_x:
					i = self.ipa_x.index(l)
					l = self.ipa_p[i]
					new_letter.append(l)
			if len(new_letter) > 1:
				letter = u'\u0361'.join(new_letter)
			elif new_letter:
				letter = new_letter[0]

		return letter