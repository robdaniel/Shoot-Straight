import paramiko

host = "****.****.****"                    					# Host address for the SFTP (stared for discretion)
port = 2200													# Port number for SFTP connection

transport = paramiko.Transport((host, port))				# Initiate connection with server

password = "*******"                						# Password for SFTP login (stared for discretion)
username = "*******"                						# Username for SFTP login (stared for discretion)

transport.connect(username = username, password = password)	# Login with above information

sftp = paramiko.SFTPClient.from_transport(transport)

import sys
path = './PATH TO FOLDER/' + "SSDItemExport.csv"    		# Where to put the file and what to name it
localpath = "SSD.csv"										# Local location of the file to be sent

sftp.put(localpath, path)									# Send file to server via SFTP

sftp.close()
transport.close()
print 'Upload done.'
