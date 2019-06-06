from ctypes import *

lib = cdll.LoadLibrary('./printstr.so')

lib.PrintStr()
lib.PrintStr()
