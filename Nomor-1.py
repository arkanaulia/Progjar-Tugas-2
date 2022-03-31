import socket
import ssl

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('its.ac.id', 443)
client_socket.connect(server_address)
client_socket = ssl.wrap_socket(client_socket, ssl_version=ssl.PROTOCOL_SSLv23)

request_header = b'GET https://www.its.ac.id/ HTTP/1.0\r\nHost: its.ac.id\r\n\r\n'
client_socket.send(request_header)

response = ''
while True:
    received = client_socket.recv(1024)
    if not received:
        break
    response += received.decode('utf-8')


response_header = response.split('\r\n\r\n')[0]
# print(response_header)

status_code = response_header.split('\r\n')[0]
status_code = status_code.split()[1:]
status_code= ' '.join(status_code)
print(status_code)


# print(response)
client_socket.close()