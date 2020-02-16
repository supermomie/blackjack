import socket, select
from termcolor import colored


hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 9991

#function to send message to all connected clients
def send_to_all (sock, message):
    #message not forwarded to server and sender itself
    for socket in connected_list:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message.encode("Utf8"))
            except :
                # if connection not available
                socket.close()
                connected_list.remove(socket)

if __name__ == "__main__":
    name=""
    #dictionary to store address corresponding to username
    record={}
    #list to keep track of socket descriptors
    connected_list = []
    buffer = 4096
    port = PORT

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(("localhost", port))
    server_socket.listen(10) #listen atmost 10 connection at one time

    #add server socket to the list of readable connections
    connected_list.append(server_socket)
    print(colored('\t\t\t\tSERVER STARTED', 'green', attrs=['bold', 'reverse']))

    while 1:
    #get the list sockets which are ready to be read through select
        rList,wList,error_sockets = select.select(connected_list,[],[])

        for sock in rList:
            #new connection
            if sock == server_socket:
                #handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                name=sockfd.recv(buffer)
                connected_list.append(sockfd)
                record[addr]=""
                #print "record and conn list ",record,connected_list

                #if repeated username
                if name in record.values():
                    msg = colored("Le nom est deja pris !", "red", attrs=['bold'])
                    sockfd.send(msg.encode("Utf8"))
                    del record[addr]
                    connected_list.remove(sockfd)
                    sockfd.close()
                    continue
                else:
                    
                    #add name and address
                    record[addr]=name
                    print("name :",name)
                    print("Client (%s, %s) connected" % addr," [",record[addr],"]")
                    msg="\33[32m\r\33[1m Bienvenue. 'bye' pour quitter\n\33[0m"
                    sockfd.send(msg.encode("Utf8"))
                    send_to_all(sockfd, "\33[32m\33[1m\r "+name.decode("Utf8")+" a rrejoint la conversation \n\33[0m")

            #some incoming message from a client
            else:
                print("else")
                #data from client
                try:
                    data1 = sock.recv(buffer)
                    print("buffer :",data1)
                    #print("sock is: ",sock)
                    #print(" :",data1[:].decode("Utf8"))
                    #data=data1[:data1.index("\n")]
                    data=data1[:].decode("Utf8")
                    print("\ndata received: ",data)

                    #get addr of client sending the message
                    i,p=sock.getpeername()
                    if data == "bye":
                        #print(data)
                        print("bye ? :", data)
                        msg="\r\33[1m"+"\33[31m "+record[(i,p)].decode("Utf8")+" left the conversation \33[0m\n"
                        send_to_all(sock,msg.decode("Utf8"))
                        print("Client (%s, %s) is offline" % (i,p)," [",record[(i,p)],"]")
                        del record[(i,p)]
                        connected_list.remove(sock)
                        sock.close()
                        continue
                    else:
                        #print("record[(i,p)] :", record[(i,p)])
                        #print("record[(i,p)] :", record[(i,p)].decode("Utf8"))
                        #print("data :", data)
                        msg="\r"+colored(record[(i,p)].decode("Utf8"), 'magenta', attrs=['bold']) + data +"\n"
                        #msg="\r\33[1m"+"\33[35m "+record[(i,p)].decode("Utf8")+": "+"\33[0m"+data+"\n"
                        #print("msg :",msg)
                        print(record)
                        send_to_all(sock,msg)

                #abrupt/force user exit
                except:
                    #print("except")
                    (i,p)=sock.getpeername()
                    #print("sock.gethostname() :",sock.gethostname())
                    #print("i :", i)
                    #print("p :", p)
                    send_to_all(sock, "\r\33[31m \33[1m"+record[(i,p)].decode("Utf8")+" left the conversation unexpectedly\33[0m\n")
                    print("Client (%s, %s) is offline (error)" % (i,p)," [",record[(i,p)],"]\n")
                    del record[(i,p)]
                    connected_list.remove(sock)
                    sock.close()
                    continue

    server_socket.close()
