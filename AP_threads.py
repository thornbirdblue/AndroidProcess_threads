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

sleep_interval = 1
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
	while 1:
		data = exec_cmd(cmd)
		
		d = datetime.datetime.now()
		save_file(d.strftime(time_format),data)		

		time.sleep(sleep_interval)

if __name__ == '__main__':
	print(time.ctime())

	mkdir(s_file)

	loop()
