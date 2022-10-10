from rich import print

from __init__ import Loaf

loaf = Loaf(file="creds.ini")
q = loaf.query("SELECT * FROM User")
print(q)