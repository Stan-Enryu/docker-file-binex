#!/usr/bin/env python3

from argparse import ArgumentParser
import mako_main

parser = ArgumentParser(prog='make-docker')

parser.add_argument('type',help="For type", choices=["xinetd", "ynetd", "socat","pwnred"])
parser.add_argument('-n','--name',default="ctf",help="Default : ctf")
parser.add_argument('-p','--port',default=11100,type=int,help="Default : 11100")
parser.add_argument('-f','--file',default="chall",help="Default : chall")
parser.add_argument('-o','--os',default="ubuntu:latest",help="Default : ubuntu:latest")
parser.add_argument('-fl','--flag',default="FLAG{test}",help="Default : FLAG{test}")

args = parser.parse_args()

print ("Name :",args.name)
print ("Port :",args.port)
print ("File :",args.file)
print ("OS   :",args.os)
print ("Flag :",args.flag)

mako_main.create_file(args)
