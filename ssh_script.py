import paramiko

def createSSHConnection():
	connection = paramiko.SSHClient()
	connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	return connection

def commmandInjection(ssh_connection):
	ssh_connection

	print('')	


def main():
	hello

if __name__ == '__main__':
	main()
