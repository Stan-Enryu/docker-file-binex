#!/usr/bin/env python3
from pwn import *
from mako.template import Template
from shutil import copy
import os 

def create_file(args):
	path, filename = os.path.split(__file__)
	name_create_file=["./docker-compose.yml", "./Dockerfile"]

	src_file=["/template/docker-compose", "/template/Dockerfile", "/template/startchall", "/template/xinetd","/template/run", "/template/ynetd"]
	src_file = [ path+file for file in src_file] 

	out=[]
	
	dict_data = {
		"os" : args.os,
		"name" : args.name,
		"port" : args.port,
		"file" : args.file,
		"type" : args.type,
	}
	docker_compose = Template(filename=src_file[0])
	out.append(docker_compose.render(**dict_data))

	docker_file = Template(filename=src_file[1])
	out.append(docker_file.render(**dict_data))

	
	if args.type == "xinetd":
		name_create_file.append("./startchall.sh")
		name_create_file.append("./xinetd")
		name_create_file.append("./run.sh")

		start_chall = Template(filename=src_file[2])
		out.append(start_chall.render())

		xinetd = Template(filename=src_file[3])
		out.append(xinetd.render(name=args.name,port=args.port,file=args.file))

		run = Template(filename=src_file[4])
		out.append(run.render(name=args.name,file=args.file))

	elif args.type == "ynetd":

		with open(src_file[5],"rb") as f:
			data_ynetd = f.read()

		with open("./ynetd","wb") as f:
			f.write(data_ynetd)

	elif args.type == "socat":
		pass

	name_create_file.append("./flag.txt")
	out.append(args.flag)

	for i in range(len(name_create_file)):
		with open(name_create_file[i],"w") as f:
			f.write(out[i])