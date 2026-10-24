# LAB FILE - planted for the review gate. Never merge.
import os, subprocess

def run(cmd):
    os.system(cmd)

def parse(expr):
    return eval(expr)

def fetch(url):
    return subprocess.call("curl -s " + url, shell=True)
