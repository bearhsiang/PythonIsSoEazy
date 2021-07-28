import select
import socket

if __name__ == '__main__':

   s = socket.socket()
   ip, port = '', 12345
   s.bind((ip, port))
   s.listen()

   timeout = 1
   counter = 0

   while True:

       print(' '*20, end='\r')
       print('waiting', '.'*(counter%3), end='\r')

       connect_list, _, _ = select.select([s], [], [], timeout)

       if len(connect_list) != 0:
           print()
           break

       counter += 1

   conn, addr = s.accept()

   conn.sendall("get\n".encode())
   conn.close()
   s.close()
