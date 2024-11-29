###############################################
# The MIT License (MIT)
# Copyright (c) 2023 Kevin Walchko
# see LICENSE for full details
##############################################
# -*- coding: utf-8 -*-
import jinja2
import argparse
import yaml
import sys
import os
import datetime as dt
from colorama import Fore

def cpp(info):
    pass

def pico(info):
    pass

def python(info):
    pass

def gen_yaml():
    data = {
        "project": "full name",
        "author": "author name",
        "year": dt.date.today().year
        "license": "license type: MIT"
    }
    with open("project.yaml", "w") as f:
        yaml.dump(data, f)

def read_yaml(filename):
    try:
        data = None
        with open(filename, "r") as fd:
            data = yaml.safe_load(fd)
    except Exception as e:
        print(f"{Fore.RED}*** {e} ***{Fore.RESET}")
    return data

DESCRIPTION = f"""
Generate cpp and python project layout from a yaml template.
"""
# Author:  {spacedock.__author__}
# Version: {spacedock.__version__}
# License: {spacedock.__license__}
# """

def handle_args():
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-b','--build', help='build project layout from yaml file', type=str)
    parser.add_argument('-y','--yaml', help='generate project template yaml file', action='store_true')

    args = vars(parser.parse_args())
    return args

if __name__ == "__main__":
    args = handle_args()
    print(args)

    if args["yaml"] == True:
        gen_yaml()
    elif args["build"] is not None:
        data = read_yaml(args["build"])
        if data is None:
            sys.exit(1)
        print(data)
