#!/usr/bin/env python

import os
import re
import sys 
import time
import urllib2


def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass

def banner():
	print("""\033[92m เชื่อมต่อ เทสระบบ""")
def command():
	os.system('clear')
	os.system('rm -f th-internet-*')
	os.system('rm -f th-internet.zip*')

def download():
	link = 'wget https://github.com/PiTOn-0/Alone/raw/main/th-internet.zip'
	print ' \033[94m\n[+]\033[94mโหลดไฟล์ \n\n' 
	os.system(link)

def unzip():
	download()
	crack = 'unzip th-internet.zip'
	print '\n \033[94m\n[+]\033[94m ---> ไฟล์\n\n'
	out = os.path.isfile('th-internet.zip')
	if out:
		os.system(crack)
	else:
		print 'Error: \033[93m\n[+]\033[93m ---> ไม่มีไฟล์ zip'

def getpass():
	print '\n \033[94m\n[+]\033[94m ---> Getting New Password\n\n'
	global user, passwd
	user = 'abcd'
	try:
		openUrl = urllib2.urlopen('https://github.com/PiTOn-0/Alone/tree/main')
	except urllib2.URLError:
		exit('ตรวจสอบว่าคุณเชื่อมต่อกับอินเทอร์เน็ต')
	kader = openUrl.read()
	joker = '''<li>Password: <strong>(.+?)</strong></li>'''
	dz = re.findall(joker, kader)
	if dz:
		passwd = dz[0]
	print '''
		\t\033[94m\n[+]\033[91m---> Username: {0}
		\t\033[94m\n[+]\033[93m---> Password: {1}
	\n'''.format(user, passwd)

def connect():
	os.system('openvpn --config th-internet.ovpn')

def main():
	banner()
	unzip()
	getpass()
	connect()
	exit()
def exit():
	os.system('exit')
	print "\nCtrl + C -> Exiting!!"
if __name__ == '__main__':
	main()
