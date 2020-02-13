import socket

print("Votre nom :")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 1111))
name = input(">> ")
s.send(name.encode())
print("Bonjour,", name, ":)")


#TODO import game and wait
