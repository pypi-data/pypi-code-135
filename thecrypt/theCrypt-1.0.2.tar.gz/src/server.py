# Imports
import socket, threading, base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import urllib.request

# Initialisation
def main():
    # Program globals
    bufferSize = 1024
    title = "\n   ______                 __ \n  / ____/______  ______  / /_\n / /   / ___/ / / / __ \/ __/\n/ /___/ /  / /_/ / /_/ / /_  \n\____/_/   \__, / .___/\__/  \n          /____/_/           \n\n"
    verification = 'VERIFIED'
    nickname = 'NICKNAME'

    # Initialisation
    print(title)
    confirmation = input("Please note that operating this server exposes and utilises your current public IP address, apply caution when using this and ensure due diligence when allowing access.\nDo you wish to proceed? (Y/N)\n> ")
    if(confirmation != "Y"):
        print("Thank you for using Crypt. Program exiting.\n")
        exit()
    host = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print()
    print("Your server will be started on address {}\n".format(host))
    port = int(input('Input host port to set, note the port must forward to your IP in your router configuration or the chatroom will only be accessible from the same network:\n> '))
    print()

    # Key setup
    cipher_raw = input('Input server access password to set:\n> ')
    cipher = cipher_raw.encode()
    salt = b"\xb9\x1f|}'S\xa1\x96\xeb\x154\x04\x88\xf3\xdf\x05"
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000)
    publicKey = base64.urlsafe_b64encode(kdf.derive(cipher))
    fernet = Fernet(publicKey)

    # Socket and server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print("Bound server instance on {} at port {}". format(host, port))
    server.listen(50)
    print("Server started successfully.")
    print("Input \'end\' to shutdown the server at any point.")

    # User params
    clients = []
    aliases = []

    # FUNCTIONS
    def uIn():
        userIn = input('')
        if userIn == "end":
            print()
            print("Shutting down server.")
            print("Thank you for using Crypt.\nGoodbye.")
            exit()

    def broadcast(message):
        for client in clients:
            message = fernet.encrypt(message)
            client.send(message)

    def handle(client):                                         
        while True:
            try:
                message = client.recv(bufferSize)
                broadcast(message)
            except:       
                index = clients.index(client)
                clients.remove(client)
                client.close()
                alias = aliases[index]
                broadcast('{} left.'.format(alias).encode('ascii'))
                aliases.remove(alias)
                break

    def receive():                                 
        while True:
            client, address = server.accept()

            if client not in clients:
                authReceived = client.recv(bufferSize).decode('ascii')
                if authReceived == cipher_raw: 
                    client.send(publicKey)
                    client.send(fernet.encrypt(verification.encode('ascii')))
                    print("User connected with {}".format(str(address))) 
                    client.send(fernet.encrypt(nickname.encode('ascii')))
                    alias = client.recv(bufferSize).decode('ascii')
                    alias = fernet.decrypt(alias).decode()
                    aliases.append(alias)
                    clients.append(client)
                    print("Alias is {}".format(alias))
                    broadcast("{} joined.".format(alias).encode('ascii'))
                    client.send(fernet.encrypt('Connected to server.'.encode('ascii')))
                    thread = threading.Thread(target=handle, args=(client,))
                    thread.start()
                else:
                    print("User attempted to connect to the server with the wrong password.")

    receive_thread = threading.Thread(target=receive)               
    receive_thread.start()
    input_thread = threading.Thread(target=uIn)                   
    input_thread.start()