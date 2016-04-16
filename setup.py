from distutils.core import setup
import py2exe
import paramiko
import ecdsa
import thread

setup(console=['main.py'])