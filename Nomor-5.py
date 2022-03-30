import socket
import ssl

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('classroom.its.ac.id', 443)
client_socket.connect(server_address)
client_socket = ssl.wrap_socket(client_socket, ssl_version=ssl.PROTOCOL_SSLv23)

request_header = b'GET https://classroom.its.ac.id/ HTTP/1.0\r\nHost: classroom.its.ac.id\r\n\r\n'
client_socket.send(request_header)

response = ''
while True:
    received = client_socket.recv(1024)
    if not received:
        break
    response += received.decode('utf-8')


a = response.split('<ul class="list-unstyled pt-3">')[1].split('li')[1].strip("/").strip("><")
b = response.split('target="_blank" title=" Unduh PDF">')[1].split('</a>')[0].strip(" ")
c = response.split('[Video] Panduan Membuat Video Asinkronus dengan Power Point"> ')[1].split('</a>')[0]
d = response.split('Video Asinkronus dengan Power Point</a></li>')[1].split('</li>')[1].split('<li>')[1]

# print(d)

nomer5 = a+"\n" + "     " + b + "\n" + "     " + c + "\n" + d+"\n" + "     " + b

print(nomer5)

# # NOMOR 1
# charset = response_header.split('\r\n')[3]
# charset = charset.split()[2].split('=')[1]
# print(charset)


# print(response)
client_socket.close()