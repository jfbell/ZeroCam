import socket
import subprocess
import os

try:
    # Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
    # all interfaces)
    path = "/tmp/buf.fifo"
    if os._exists(path):
        os.rmdir(path)
    os.mkfifo(path)
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 5777))
    server_socket.listen(0)
    print('server up')

    # Accept a single connection and make a file-like object out of it
    connection = server_socket.accept()[0].makefile('rb')
    print('connection made')
    # Run a viewer with an appropriate command line. Uncomment the mplayer
    # version if you would prefer to use mplayer instead of VLC
    # cmdline = ['vlc', '--demux', 'h264', '-']
    # print('vlc called')


    #cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
    # player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
    # print('subprocess called \n entering while')
    fifo = open(path, "wb")
    print('fifo open')

    while True:
        # Repeatedly read 1k of data from the connection and write it to
        # the media player's stdin
        data = connection.read(1024)
        if not data:
            break
        fifo.write(data)
        # player.stdin.write(data)
finally:
    connection.close()
    server_socket.close()
    # player.terminate()
    fifo.close()
    os.rmdir(path)
    print('all closed')