import socket, select, sys
from termcolor import colored

PORT = 9991

#helper function (formatting)
def display() :
    you=colored("You", 'yellow', attrs=['bold'])+" : "
    sys.stdout.write(you)
    sys.stdout.flush()


def main():
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    print(host)

    port = PORT
    
    #asks for user name
    name=input(colored("NEW ID...\nTon surnom : ", "blue", attrs=['bold']))
    #print("socket.AF_INET :",socket.AF_INET)
    #print("socket.SOCK_STREAM :",socket.SOCK_STREAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    #print(s)
    print("host", host)
    print("port", port)
    #connecting host
    #s.connect(("localhost", port))
    try :
        s.connect(("localhost", port))
    except :
        print(colored("ERROR cnx server", "red", attrs=['bold','reverse','blink']))
        sys.exit()

    #if connected
    print("name", name)
    s.send(name.encode("utf-8"))
    display()
    while 1:
        socket_list = [sys.stdin, s]
        
        #get the list of sockets which are readable
        rList, wList, error_list = select.select(socket_list , [], [])
        #print("r :", rList)
        #print("w :", wList)
        #print("err :", error_list)
        for sock in rList:
            #incoming message from server
            #print("sock :", sock)
            if sock == s:
                data = sock.recv(4096).decode("Utf8")
                if not data :
                    print(colored("Deconnection", "red", attrs=["bold"]))
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    display()
        
            #user entered a message
            else :
                msg=sys.stdin.readline().encode("Utf8")
                s.send(msg)
                display()

if __name__ == "__main__":
    main()
