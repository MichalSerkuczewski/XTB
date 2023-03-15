import socket
import ssl
import json

def main():
    PROLOG_RESP = "Resp: "

    host = 'xapi.xtb.com'
    port = 5124
    host = socket.getaddrinfo(host,port)[0][4][0]
    s = socket.socket()
    s.connect((host,port))
    s = ssl.wrap_socket(s)
    end = b'\n\n'

    login = 1000
    pswd = 'PASSWORD'
    parameters = {
        "command": "login",
        "arguments": {
            "userId": f'{login}',
            "password": f'{pswd}'
        }
    }
    packet = json.dumps(parameters)
    print(packet)
    s.send(packet.encode("UTF-8"))

    response = s.recv(8192)
    if end in response:
        print(PROLOG_RESP, response[:response.find(end)])
    else:
        print('login:', response)


if __name__ == '__main__':
    main()

