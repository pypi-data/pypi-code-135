import sys
import os
import time
from colored import fg
import time
import socket


blue = fg("blue")
cyan = fg("cyan")


def main():
  arg1 = sys.argv[1]
#================================ORGANISE======================================
  if arg1 == "init":
    name = input(cyan + "Project name: ")
    desc = input(cyan + "Project description: ")
    version = input(cyan + "Version: ")
    author = input(cyan + "Author name: ")
    email = input(cyan + "Email: ")    
    path = f"{os.getcwd()}/{name}/config"
    if not os.path.exists(path):
        os.makedirs(path)
    with open(f"{os.getcwd()}/{name}/config/init.wize", "w") as project:
      project.write(f"""[
  [name]: {name}
  [description]: {desc}
  [version]: {version}
  [author]: {author}
  [email]: {email}
]
        """
      )
    print(cyan + "Success - Project File Created")

  else:
    print(blue + "Invalid Argument")

main()