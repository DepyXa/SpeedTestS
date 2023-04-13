import os
import time

def clears():
	if os.name == "posix":
		os.system("clear")
	else:
		os.system("cls")

try:
	from colorama import init, Fore, Back, Style
except ModuleNotFoundError:
	os.system("pip install colorama --progress-bar off")
	from colorama import init, Fore, Back, Style
try:
	import speedtest
except ModuleNotFoundError:
	os.system("pip install speedtest-cli --progress-bar off")
	import speedtest
clears()
init(autoreset=True)

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

def starttest(n):
	sd = []
	su = []
	sp = []
	for x in range(n):
		x = x+1
		print(Fore.YELLOW + f"Testing {x}...")
		try:
			st = speedtest.Speedtest()
			download = st.download()
			down = round(download/(1024*1024), 3)
			dow = download/(1024*1024)
			sd.append(down)
		except speedtest.ConfigRetrievalError:
			print(Fore.RED + "Error: No Internet connection!")
			return
		clears()
		if down < 10:
			print(Fore.RED + f"	Download: {down} mb/s")
		elif down < 25:
			print(Fore.YELLOW + f"	Download: {down} mb/s")
		elif down < 45:
			print(Fore.GREEN + f"	Download: {down} mb/s")
		else:
			print(Fore.GREEN + Style. BRIGHT + f"	Download: {down} mb/s")
		try:
			upload = st.upload()
			upl = round(upload/(1024*1024), 3)
			up = upload/(1024*1024)
			su.append(up)
		except speedtest.ConfigRetrievalError:
			print(Fore.RED + "Error: No Internet connection!")
			return
		if upl < 8:
			print(Fore.RED + f"	Upload: {upl} mb/s")
		elif upl < 20:
			print(Fore.YELLOW + f"	Upload: {upl} mb/s")
		elif upl < 40:
			print(Fore.GREEN + f"	Upload: {upl} mb/s")
		else:
			print(Fore.GREEN + Style. BRIGHT + f"	Upload: {upl} mb/s")
		try:
			servernames = ""
			st.get_servers(servernames)
			ping = st.results.ping
			sp.append(ping)
		except speedtest.ConfigRetrievalError:
			print(Fore.RED + "Error: No Internet connection!")
			return
		print(Fore.GREEN + f"	Ping: {ping} ms")
		if ping > 0:
			print(Fore.GREEN + "	Commentar: Good ping!")
		elif ping > 110:
			print(Fore.YELLOW + "	Comentar: min. ping!")
		else:
			print(Fore.RED + Back.GREEN + "	Commentar: ping > 300 ms!")
		if x == n:
			time.sleep(5)
			clears()
			nsd = round((listsum(sd))/n, 3)
			if nsd < 10:
				print(Fore.RED + f"	Average download speed: {nsd} mb/s")
			elif nsd < 25:
				print(Fore.YELLOW + f"	Average download speed: {nsd} mb/s")
			elif nsd < 45:
				print(Fore.GREEN + f"	Average download speed: {nsd} mb/s")
			else:
				print(Fore.GREEN + Style. BRIGHT + f"	Average download speed: {nsd} mb/s")
			nsu = round((listsum(su))/n, 3)
			if nsu < 8:
				print(Fore.RED + f"	Average upload speed: {nsu} mb/s")
			elif nsu < 20:
				print(Fore.YELLOW + f"	Average upload speed: {nsu} mb/s")
			elif nsu < 40:
				print(Fore.GREEN + f"	Average upload speed: {nsu} mb/s")
			else:
				print(Fore.GREEN + Style. BRIGHT + f"	Average upload speed: {nsu} mb/s")
			nsp = round((listsum(sp))/n, 3)
			if nsp < 50:
				print(Fore.GREEN + Style. BRIGHT + f"	Average ping: {nsp} ms")
			elif nsp < 100:
				print(Fore.GREEN + f"	Average ping: {nsp} ms")
			elif nsp < 130:
				print(Fore.YELLOW + f"	Average ping: {nsp} ms")
			else:
				print(Fore.RED + f"	Average ping: {nsp} ms")

def main():
	while True:
		US = input(Fore.YELLOW + "Start/Restart? (Y/N/About): ")
		try:
			if US.lower() == "y":
				ne = input(Fore.BLUE + "Enter the number of tests: ")
				n = int(ne)
				if n < 1:
					print(Fore.RED + "You cannot test less than once!")
				if n > 10:
					print(Fore.RED + "You cannot test more than ten times!")
				else:
					starttest(n)
			elif US.lower() == "n":
				break
				print(Fore.GREEN + "Completing the test... (7s)")
				time.sleep(7)
				os.system("exit")
			elif US.lower() == "about":
				print(Fore.RED + Back.GREEN + "Telegram code creator: @DepyXa.\nDonatello website: http://donatello.to/DepyXa")
		except ValueError:
			print(Fore.GREEN + "A letter is entered in place of numbers, enter the number...")
			pass

main()
