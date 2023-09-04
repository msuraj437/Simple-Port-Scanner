import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input('Enter the IP address: ')
port = int(input('Enter the port you want to know: '))

if s.connect_ex((ip, port)):
    print('The prot is closed')
else:
    print('The port is open')

