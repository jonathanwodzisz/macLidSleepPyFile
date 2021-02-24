import os
import time

answer = input("would you like to turn lid sleep on or off?: ")
if answer == "off":
    os.system("sudo pmset -a disablesleep 1")
else:
    os.system("sudo pmset -a disablesleep 0")
