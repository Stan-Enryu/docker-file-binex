#!/usr/bin/env python3
from pwn import *
from mako.template import Template
from shutil import copy
import os

def create_file(args):
    # Get the directory path of the current file
    path = os.path.dirname(__file__)
    
    # Define template source files
    src_file_names = ["docker-compose", "Dockerfile", "ynetd"]
    if args.type == "pwnred":
    	src_file_names[0] = "docker-compose.pwnred"
    	src_file_names[1] = "Dockerfile.pwnred"

    src_files = [os.path.join(path, "template", file) for file in src_file_names]
    
    # Output file names
    output_files = ["./docker-compose.yml", "./Dockerfile"]

    # Dictionary to be passed to the template renderer
    dict_data = {
        "os": args.os,
        "name": args.name,
        "port": args.port,
        "file": args.file,
        "type": args.type,
        "flag": args.flag,
    }

    # Rendering docker-compose and Dockerfile templates
    try:
        out = [
            Template(filename=src_files[0]).render(**dict_data),
            Template(filename=src_files[1]).render(**dict_data),
        ]
    except Exception as e:
        print(f"Error rendering templates: {e}")
        return

    # Additional handling based on the type
    if args.type == "ynetd":
        try:
            # Using shutil.copy to copy the ynetd file
            copy(src_files[2], "./ynetd")
        except IOError as e:
            print(f"Error copying ynetd: {e}")
            return

    # Write the rendered templates to the output files
    try:
        for i, output_file in enumerate(output_files):
            with open(output_file, "w") as f:
                f.write(out[i])
    except IOError as e:
        print(f"Error writing output files: {e}")