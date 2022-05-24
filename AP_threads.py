#!/usr/bin/env python
import os
import datetime
import time
import subprocess

ProcessName_list=[
	'com.android.camera',
	'android.hardware.camera.provider@2.4-service_64',
]
ProcessPid={}
ProcessThreads={}

s_file = "LSaveFile"

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

def save_excel(name,data):
	write = pd.ExcelWriter(name+'.xlsx')

	procs={}
	for proc,threads in data.items():
		procs[proc]=len(threads)
		
		df=pd.DataFrame(threads)
		df.to_excel(write,sheet_name=proc,index=False,header=False)

	df=pd.DataFrame.from_dict(procs,orient='index')
	df.to_excel(write,sheet_name='CameraProcessTotal',header=['Threads Num'])

	write.save()
	write.close()
	print('Save File: '+name+'.xlsx')


def exec_cmd(c):
	sub = subprocess.Popen(c,stdout=subprocess.PIPE,shell=True)
	ret_b = sub.stdout.read()
	if ret_b is not None:
		ret = ret_b.decode()
	return ret

def loop():
	for proc in ProcessName_list:
		data = exec_cmd('adb shell pidof '+proc)
		
		if data:
			ProcessPid[proc]=data
			print(proc+' pid: '+data)

	for proc,pid in ProcessPid.items():
		data = exec_cmd('adb shell ps -T -p '+pid)
		if data:
			data = data.split('\r\n')[1:-1]	
			#print(data)
			ProcessThreads[proc]=data

	d = datetime.datetime.now()
	save_excel(d.strftime(time_format),ProcessThreads)		


if __name__ == '__main__':
	print(time.ctime())

	mkdir(s_file)

	loop()
