#!/usr/bin/env python
import os
import datetime
import time
import subprocess

ProcessName_list=[com.android.camera,]
ProcessPid={}
ProcessThreads={}

s_file = "LSaveFile"

cmd = "adb shell pidof"

time_format = "%y%m%d%H%M%S"

def mkdir(d):
	if not os.path.isdir(d):
		os.mkdir(d)
	os.chdir(d)

def save_file(name,data):
	f_name = name+".txt"

	f = open(f_name,"w")
	f.write(str(data));
	f.close()

	print("Save file: "+f_name)

def exec_cmd(c):
	sub = subprocess.Popen(c,stdout=subprocess.PIPE,shell=True)
	ret_b = sub.stdout.read()
	if ret_b is not None:
		ret = ret_b.decode()
	return ret

def loop():
	for proc in ProcessName_list:
		data = exec_cmd(cmd)
		
		if data:
			ProcessPid[proc]=data
			print(proc+' pid: '+data)

	for proc,pid in ProcessPid.items():
		data = exec_cmd('adb shell ps -e|findstr pid')
		print(data)	

	#d = datetime.datetime.now()
	#save_file(d.strftime(time_format),data)		


if __name__ == '__main__':
	print(time.ctime())

	mkdir(s_file)

	loop()
