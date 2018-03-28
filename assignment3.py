import socket

ports=[21,22,25,80,110,9090]
socket.setdefaulttimeout(5)
host_file=open('host_names','r')
host_names=host_file.read()
host_names=host_names.split('\n')

s = socket.socket()

for host in host_names:
    for port in ports:
        try:
            Respons_name = "%s-%s.txt" % (host, port)
            Response_file = open(Respons_name, 'wb')

            s = socket.socket()
            s.connect((host, port))

            rec = s.recv(1024)
            Response_file.write(rec)

            Response_file.close()
            s.close

        except Exception as e:
            print(e)
