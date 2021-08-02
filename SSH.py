import paramiko

host = "host"
port = 22
username = "user"
password = "password123!"
command = "command like grep "


#connect
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
except:
    print("Could not connect")

#send command
try:
    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    for line in lines:
        print(line)
except:
    print("Could not sent command")

