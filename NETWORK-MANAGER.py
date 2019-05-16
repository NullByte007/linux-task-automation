#!/usr/bin/python3 
# Copyright 2019, Aniket.N.Bhagwate, All rights reserved.
# Date Created : 12 february 2019
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# libraries 
import os
import keyboard

os.system("pip install colorama==0.3.3")
from colorama import Fore, Back, Style
print("[*] Downloading Required Library...")
os.system("clear")
print(Fore.GREEN + Style.BRIGHT + "") 

a = """
-------------------------------------------------------------
 __  __             _   _      _                      _    
|  \/  |_   _      | \ | | ___| |___      _____  _ __| | __
| |\/| | | | |_____|  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /
| |  | | |_| |_____| |\  |  __/ |_ \ V  V / (_) | |  |   < 
|_|  |_|\__, |     |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\ 
        |___/                
-------------------------------------------------------------                         
"""

print(a)
print(Fore.RED + Style.BRIGHT + "")
print("		# Code by : ~NULLBYTE007 ")
print(Fore.GREEN + Style.BRIGHT + "")
print("-------------------------------------------------------------")

menu = """
|-------------------------------|
| [*] CHOOSE FROM THE OPTIONS   |
|-------------------------------|
| 1 |	SETUP NEW NETWORK	|
|-------------------------------|
| 2 |	START EXISTING NETWORK	|
|-------------------------------|
| 3 |	DELETE EXISTING NETWORK	|
|-------------------------------|
| 4 |	LIST EXISTING NETWORKS	|
|-------------------------------|
| 5 |   EXIT			|
|-------------------------------|


"""
print(menu)

choice = input("==> ")

if choice =='1':
	print("|------------------------|")
	print("| [1] SETUP NEW NETWORK  |")
	print("|------------------------|")
		
	auto="yes"
	print("[*] PLEASE ENTER THE DETAILS FOR THE NEW NETWORK")
	os.system('nmcli device status | cut -d" " -f1 > networks.txt')
	f = open("networks.txt","r")
	f = f.read();
	f = f.split("\n")
	f.pop()	
	del f[0]
	rr=0
	auto = 'yes'
	name = input("[*] NAME FOR NETWORK ==> "+Fore.CYAN + Style.BRIGHT)	
	ip = input(Fore.GREEN + Style.BRIGHT+"[*] IP ADDRESS ==> "+Fore.CYAN + Style.BRIGHT)
	dns = input(Fore.GREEN + Style.BRIGHT+"[*] DNS ADDRESS ==> "+Fore.CYAN + Style.BRIGHT)	
	gateway = input(Fore.GREEN + Style.BRIGHT+"[*] GATEWAY ADDRESS ==> "+Fore.CYAN + Style.BRIGHT)
	auto = input (Fore.GREEN + Style.BRIGHT+"[*] DO YOU WANT THE NETWORK TO AUTOCONNECT ? yes/no ==> "+Fore.CYAN + Style.BRIGHT)
	print(Fore.GREEN + Style.BRIGHT+"\n")
	for x in f:
		rr = rr+1
		print("|------------------------|")
		print("|"+Fore.CYAN + Style.BRIGHT + " [*] {} : {}".format(rr,x))
		print(Fore.GREEN + Style.BRIGHT + "|------------------------|")
	print("\n[*] TOTAL INTERFACES AVAILABLE : {}".format(rr))
	choice = int(input("[*] SELECT THE INTERFACE ==> "))
	ifname = f[choice-1]
	print("[*] THIS INTERFACE IS SELECTED ==> "+Fore.CYAN + Style.BRIGHT+"{}".format(f[choice-1]))
	print(Fore.GREEN + Style.BRIGHT+"")
	os.system("nmcli con add con-name {} ifname {} connection.autoconnect {} ipv4.addresses {} ipv4.gateway {} ipv4.method manual ipv4.dns {} type ethernet".format(name,ifname,auto,ip,gateway,dns))

	print("[*] NETWORK "+Fore.CYAN + Style.BRIGHT + "{}".format(name) +Fore.GREEN + Style.BRIGHT+" SUCCESSFULLY CREATED !!")
	os.system("rm -rf networks.txt")

if choice =='2':
	print("|----------------------------|")
	print("| [2] START EXISTING NETWORK |")
	print("|----------------------------|")
	print("\n[*] PLEASE SELECT THE NETWORK\n")
	os.system("nmcli con show > networks.txt")
	f=open("networks.txt","r")
	f = f.read()
	f = str(f)
	f = f.replace(" ","__")

	f = f.split("___")
	f = list(filter(None, f))
	list1=['']
	myNewList=[]
	for x in f:
		z = x.split("\n")
		del z[0]
		list1.append(z)
		if len(z)!=0:
			myNewList.append(z)
	rr=0
	myNewList.pop()
	list1=[]
	for x in myNewList:
		x[0] = x[0].replace("__"," ")
		list1.append(x[0])

	for x in list1:
		rr = rr+1
		print("|----------------------------------|")
		print("|"+Fore.CYAN + Style.BRIGHT + " [*] {} : {}".format(rr,x))
		print(Fore.GREEN + Style.BRIGHT + "|----------------------------------|")
	choice = int(input("==> "))
	
	print("[*] STARTING NETWORK ==> "+Fore.CYAN + Style.BRIGHT +" {}".format(list1[choice-1]) + Fore.GREEN + Style.BRIGHT+"")
	os.system("nmcli con up {}".format(list1[choice-1]))
	os.system("rm -rf networks.txt")

if choice =='3':
	print("|------------------------------|")
	print("| [3] DELETE EXISTING NETWORK  |")
	print("|------------------------------|")

	print("\n[*] PLEASE SELECT THE NETWORK\n")
	os.system("nmcli con show > networks.txt")
	f=open("networks.txt","r")
	f = f.read()
	f = str(f)
	f = f.replace(" ","__")

	f = f.split("___")
	f = list(filter(None, f))
	list1=['']
	myNewList=[]
	for x in f:
		z = x.split("\n")
		del z[0]
		list1.append(z)
		if len(z)!=0:
			myNewList.append(z)
	rr=0
	myNewList.pop()
	list1=[]
	for x in myNewList:
		x[0] = x[0].replace("__"," ")
		list1.append(x[0])

	for x in list1:
		rr = rr+1
		print("|----------------------------------|")
		print("|"+Fore.CYAN + Style.BRIGHT + " [*] {} : {}".format(rr,x))
		print(Fore.GREEN + Style.BRIGHT + "|----------------------------------|")
	choice = int(input("==> "))
	
	print("[*] DELETING NETWORK ==> "+Fore.CYAN + Style.BRIGHT +" {}".format(list1[choice-1]) + Fore.GREEN + Style.BRIGHT+"")
	os.system("nmcli con delete {}".format(list1[choice-1]))
	os.system("rm -rf networks.txt")



if choice =='4':
	print("|-----------------------------|")
	print("| [4] LIST EXISTING NETWORKS  |")
	print("|-----------------------------|")

	os.system("nmcli con show > networks.txt")
	f=open("networks.txt","r")
	f = f.read()
	f = str(f)
	f = f.replace(" ","__")

	f = f.split("___")
	f = list(filter(None, f))
	list1=['']
	myNewList=[]
	for x in f:
		z = x.split("\n")
		del z[0]
		list1.append(z)
		if len(z)!=0:
			myNewList.append(z)
	rr=0
	myNewList.pop()
	list1=[]
	for x in myNewList:
		x[0] = x[0].replace("__"," ")
		list1.append(x[0])

	for x in list1:
		rr = rr+1
		print("|----------------------------------|")
		print("|"+Fore.CYAN + Style.BRIGHT + " [*] {} : {}".format(rr,x))
		print(Fore.GREEN + Style.BRIGHT + "|----------------------------------|")
	os.system("rm -rf networks.txt")


if choice ==5:
	exit(0)



