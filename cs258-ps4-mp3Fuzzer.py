#!/usr/bin/python
# if files fail, try /home/jackey/Udacity
file_list = [
	"/home/jackey/Udacity/cs258-ps4-Fuzzer/mp3s/a.mp3",
	"/home/jackey/Udacity/cs258-ps4-Fuzzer/mp3s/b.mp3",
	"/home/jackey/Udacity/cs258-ps4-Fuzzer/mp3s/c.mp3",
	"/home/jackey/Udacity/cs258-ps4-Fuzzer/mp3s/d.mp3",
	"/home/jackey/Udacity/cs258-ps4-Fuzzer/mp3s/e.mp3",
	"/home/jackey/Udacity/cs258-ps4-Fuzzer/mp3s/f.mp3"
	]
# List of apps to test
apps = [
	"rhythmbox"
	]
fuzz_file = "/home/jackey/Udacity/cs258-ps4-Fuzzer/output_files/mp3output_file"
FuzzFactor = 250
num_tests = 20 # 10000
import math
import random
import string
import subprocess
import time
mp3resultfile = open(fuzz_file + "_results.txt","w")
for i in range(num_tests):
	file_choice = random.choice(file_list)
	mp3resultfile.write("--------------------------------------------\n")
	mp3resultfile.write("Test #" + str(i) + "\n")
	mp3resultfile.write("file_choice: " + file_choice + "\n")
	app = random.choice(apps)
	mp3resultfile.write("app:" + app + "\n")
	buf = bytearray(open(file_choice, 'rb').read())

	# start Charlie Miller code
	numwrites=random.randrange(math.ceil((float(len(buf)) / FuzzFactor)))+1
	mp3resultfile.write("numwrites: " + str(numwrites) + "\n")
	for j in range(numwrites):
		rbyte = random.randrange(256)
		rn = random.randrange(len(buf))
		buf[rn] = "%c"%(rbyte)
	# end Charlie Miller code
	
	fuzz_output = fuzz_file + str(i) + ".mp3"
	mp3resultfile.write("fuzz_output: " + fuzz_output + "\n")
	open(fuzz_output, 'wb').write(buf)
	process = subprocess.Popen([str(app),fuzz_output])
	time.sleep(25)
	if not process.poll():
		mp3resultfile.write("NO CRASH!!!!!\n")
		process.terminate()
	else:
		mp3resultfile.write("CRASH!!!!!!!!!!!!!!!!!!!\n")
	time.sleep(15)
mp3resultfile.close()
