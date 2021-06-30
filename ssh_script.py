import paramiko
import optparse
import sys

def createSSHConnection(target, port, username, password):
	print('[+] Attempting to connect to target')
	try:
		connection = paramiko.SSHClient()
		connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		connection.connect(target, port=port,username=username, password=password)
		print('[+] Successfully connected to target')
		return connection
	except:
		print('[-] Failed to connect to host!')
		sys.exit()

def commmandInjection(ssh_connection, cmd):
	try:
		stdin, stdout, stderr = ssh_connection.exec_command(cmd)
		output = stdout.readlines()
		error = stderr.readlines()
		for item in output:
			print(item.strip('\n'))
		if len(error) != 0:
			for item in error:
				print(item.strip('\n'))
			raise Exception()
	except:
		print('[-] Failed to execute Command')

def spawnShell(ssh_connection):
	command = ' '
	print('[+] Spawning Shell')
	while True:
		command = input('>>: ')
		if command != '':
			commmandInjection(ssh_connection, command)
		else:
			break
	print('[+] Closing Shell')

def main():
	command = optparse.OptionParser()
	command.add_option('-t', action='store', dest='target',type='string', help='specify the target that you would like to make an ssh connection with')
	command.add_option('-p', action='store', dest='port',type='int',help='specify the target port that you would like to connect to')
	command.add_option('-u', action='store', dest='username', type='string', help='specify the username to login via ssh')
	command.add_option('-w', action='store', dest='password', type='string', help='specify the password to login via ssh')
	options, args = command.parse_args()
	target = options.target
	port = options.port
	username = options.username
	password = options.password 
	ssh_connection = createSSHConnection(target, port, username, password)
	spawnShell(ssh_connection)
	ssh_connection.close()
	print('[+] Exiting Program!')

if __name__ == '__main__':
	main()
