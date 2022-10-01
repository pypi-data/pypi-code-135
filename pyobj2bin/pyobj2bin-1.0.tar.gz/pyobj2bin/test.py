import __init__
with open("t.dat","ab+") as f:
	__init__.load_module("datetime")
	__init__.dump([1,2,3],f)
	r = __init__.load(f)
	print(r)
	__init__.update(f)
	r = __init__.load(f)
	print(r)
