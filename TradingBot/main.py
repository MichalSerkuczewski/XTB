import socket
import ssl
import json

global response,end,PROLOG_RESP


def login(s,login,pswd):
    parameters = {
        "command": "login",
        "arguments": {
            "userId":f"{login}",
            "password":pswd
        }
    }
    packet = json.dumps(parameters)
    s.send(packet.encode("UTF-8"))
    response = s.recv(8192)
    return json.loads(response)["streamSessionId"]

def send(s,command,arguments=None):
    args = dict()
    if arguments is None:
        parameters = {
            "command":command
        }
    else:
        for i in range(0, len(arguments)):
            args[f'arg{i + 1}Name'] = arguments[i]
        parameters = {
            "command":command,
            "arguments":args,
            "prettyPrint":True
        }
    packet = json.dumps(parameters)
    s.send(packet.encode('UTF-8'))
def receive(s):
    response = s.recv(8192)
    end = b'\n\n'
    if end in response:
        response = json.loads(response[:response.find(end)])
        print(response)
    else:
        print(response)

    return (response['status'],response['returnData'])

def main():
    PROLOG_RESP = "Resp: "
    host = 'xapi.xtb.com'
    port = 5124
    host = socket.getaddrinfo(host,port)[0][4][0]
    s = socket.socket()
    s.connect((host,port))
    s = ssl.wrap_socket(s)

    userId = 14497537
    password = "tMxhKzD3_di:d5-"

    streamSessionId = login(s,userId,password)
    print(streamSessionId)
    send(s,"getAllSymbols")
    print(receive(s))


if __name__ == '__main__':
    main()

