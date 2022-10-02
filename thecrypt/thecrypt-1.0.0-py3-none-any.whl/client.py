# Imports
import socket, threading
from cryptography.fernet import Fernet

# Program settings
bufferSize = 1024

# Initialisation
host = input('Input host IP to connect to:\n> ')
print()
port = int(input('Input host port to connect to:\n> '))
print()
cipher_raw = input('Input server password:\n> ')

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
client.connect((host, port))
client.send(cipher_raw.encode('ascii'))

publicKey = client.recv(bufferSize)
print(publicKey)
fernet = Fernet(publicKey)

verified = client.recv(bufferSize).decode('ascii')
verified = fernet.decrypt(verified).decode()

if verified == "VERIFIED":
    print("Connected to the server successfully.")
else:
    print("The password is incorrect.")
    exit()

alias = input('Input your alias:\n> ')
print()
print('Your alias is set to {}.\n'.format(alias))
print("To exit to program, enter \'exit\' at any point.")

# FUNCTIONS
def receive():
    while True:                                                 
        try:
            message = client.recv(bufferSize)
            message = fernet.decrypt(message).decode('ascii')
            if message == 'NICKNAME':
                client.send(fernet.encrypt(alias.encode('ascii'))) 
            else:
                print(message)

        except:                                                 
            print("An error occured.\nExiting the program.")
            client.close()
            break

def write():
    while True:  
        message = '{}: {}'.format(alias, input(''))
        name, content = message.split(':')
        content = content.lstrip()
        if content == 'exit':
            print("Thank you for using Crypt.\nGoodbye.")
            exit()
        else:
            client.send(message.encode('ascii'))

# Multithread to monitor send and receive simultaneously
receive_thread = threading.Thread(target=receive)               
receive_thread.start()
write_thread = threading.Thread(target=write)                   
write_thread.start()