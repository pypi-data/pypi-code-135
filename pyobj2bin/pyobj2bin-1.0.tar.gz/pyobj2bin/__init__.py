import io
import os

class FileObjectError(Exception):
	def __init__(self):
		global ErrorMessage
		self.ErrorMessage = ErrorMessage
		super().__init__(self.ErrorMessage)

types = [io.BufferedRWPair,io.BufferedRandom,io.BufferedReader,io.BufferedWriter,io.BytesIO,io.FileIO,io.StringIO,io.TextIOWrapper]

STRING = b'\xa0'
LIST = b'\xb0'
TUPLE = b'\xc0'
OTHERS = b'\xd0'
INT = b'\xe0'
FLOAT = b'\xf0'
DICT = b'\xdd'
BOOLEAN = b'\xaa'
COMPLEX = b'\xff'

DATATYPE_MARKS = {'STRING':b'\xa0','LIST':b'\xb0','TUPLE':b'\xc0','OTHERS':b'\xd0','INT':b'\xe0','FLOAT':b'\xf0','DICT':b'\xdd','BOOLEAN':b'\xaa','COMPLEX':b'\xff'}

def dump(o,f):
	try:
		preserved_obj = o
		if type(f) not in types:
			global ErrorMessage
			ErrorMessage = f"{f} is not a file handler object."
			raise FileObjectError
		else:
			o = bytes(str(o),"utf-8")
			l = list(o)
			for i in l:
				to_write = bytes(i)
				f.write(to_write)
				f.write(b'\x01')
		if str(type(preserved_obj)) == "<class 'str'>":
			f.write(STRING)
		elif str(type(preserved_obj)) == "<class 'list'>":
			f.write(LIST)
		elif str(type(preserved_obj)) == "<class 'tuple'>":
			f.write(TUPLE)
		elif str(type(preserved_obj)) == "<class 'int'>":
			f.write(INT)
		elif str(type(preserved_obj)) == "<class 'float'>":
			f.write(FLOAT)
		elif str(type(preserved_obj)) == "<class 'dict'>":
			f.write(DICT)
		elif str(type(preserved_obj)) == "<class 'bool'>":
			f.write(BOOLEAN)
		elif str(type(preserved_obj)) == "<class 'complex'>":
			f.write(COMPLEX)
		else:
			f.write(OTHERS)

		f.write(b'\x02')
		f.flush()
		os.fsync(f)
	except io.UnsupportedOperation:
		print("Cannot use read mode to write to file. Please use wb,ab or rb+ mode")
	except TypeError:
		print("Please use only rb+,wb,wb+,ab or ab+ for writing to binary files")

def load(f):
	try:
		all_objs = []
		if type(f) not in types:
			global ErrorMessage
			ErrorMessage = f"{f} is not a file handler object."
			raise FileObjectError
		else:
			f.seek(0)
			data = f.read()
			diff_objs = data.split(b"\x02")
			del diff_objs[-1]
			for objs in diff_objs:
				bl=[]
				segments = objs.split(b'\x01')
				mark = segments.pop(-1)
				for element in segments:
					bl.append(len(element))
				decoded_obj = bytes(bl).decode('utf-8')
				if mark == STRING:
					all_objs.append(decoded_obj)
				elif mark == OTHERS:
					try:
						all_objs.append(eval(decoded_obj))
					except:
						all_objs.append(decoded_obj)
				else:
					all_objs.append(eval(decoded_obj))

		return all_objs

	except io.UnsupportedOperation:
		print("Cannot use write or append mode to read data. Please use rb,wb+ or ab+ mode")
	except TypeError:
		print("Please use only rb,rb+,wb+ or ab+ for reading data from binary files")

def showtype(f):
	try:
		if type(f) not in types:
			global ErrorMessage
			ErrorMessage = f"{f} is not a file handler object."
			raise FileObjectError
		else:
			f.seek(0)
			data = f.read()
			diff_objs = data.split(b'\x02')
			MARKS = []
			for objs in diff_objs:
				mark = objs.split(b'\x01')[-1]
				MARKS.append(mark)
		TYPES = []
		keys = list(DATATYPE_MARKS.keys())
		vals = list(DATATYPE_MARKS.values())
		for mark in MARKS:
			if mark in vals:
				TYPES.append(keys[vals.index(mark)])
		return TYPES
	except io.UnsupportedOperation:
		print("Cannot use write or append mode to read data. Please use rb,wb+ or ab+ mode")
	except TypeError:
		print("Please use only rb,rb+,wb+ or ab+ for reading data from binary files")

def update(f):
	objects = load(f)
	n=1
	print("Which object do you want to update:")
	for object in objects:
		print(f"{n}. {object}")
		n+=1
	c = int(input("Enter your choice: "))
	if c > 0 and c <= n:
		newval = input("Enter new value: ")

		if newval.isdigit():
			print("You have entered an integer value")
			yn = input("Do you want to store it as a string? (y or n): ")
			if yn == "y":
				objects[c-1] = newval
			else:
				objects[c-1] = int(newval)

		elif newval.replace('.','',1).isdigit():
			print("You have entered a float value")
			yn = input("Do you want to store it as a string? (y or n): ")
			if yn == "y":
				objects[c-1] = newval
			else:
				objects[c-1] = float(newval)
		elif newval in ['True','False']:
			objects[c-1] = eval(newval)
		else:
			try:
				complex_no = complex(newval)
				print("You have entered a complex number")
				yn = input("Do you want to store it as a string? (y or n): ")
				if yn == "y":
					objects[c-1] = newval
				else:
					objects[c-1] = complex_no
			except:
				try:
					if type(eval(newval)) in [int,float,bool,complex]:
						objects[c-1] = newval
					else:
						objects[c-1] = eval(newval)
				except:
					objects[c-1] = newval

	else:
		print(f"Invalid choice {c}")
	f.truncate(0)
	os.fsync(f)
	f.seek(0)
	for object in objects:
		dump(object,f)

def load_module(mod):
	globals()[mod] = __import__(mod)
