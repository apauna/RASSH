from rassh.core.constants import *
import rassh
import time

def getCommandReward(command):
    l = ["wget", "scp", "ftp", "sftp", "curl", "axel"]
    for c in l:
	if c in command:
	    return 0.5
    if command.startswith("./"):
	return 1
    l2 = ["python", "php", "sh", "bash"]
    for c in l2:
	if command.startswith(c):
	    return 1
    return 0

def getCommandType(command):
    l = ["wget", "scp", "ftp", "sftp", "curl", "axel"]
    for c in l:
	if c in command:
	    return 1
    if command.startswith("./"):
	return 2
    l2 = ["python", "php", "sh", "bash"]
    for c in l2:
	if command.startswith(c):
	    return 1
    return 0

def getCurrentCommand():
    #global current_command
    #global current_reward
    #global prev_command
    while True:
	print "get current command -============================", rassh.core.constants.current_command
	if not rassh.core.constants.current_command:
	    time.sleep(1)
	else:
	    rassh.core.constants.prev_command = rassh.core.constants.current_command
	    rassh.core.constants.current_command = None
	    rassh.core.constants.current_reward = getCommandReward(rassh.core.constants.prev_command)
	    return getCommandType(rassh.core.constants.prev_command)

def getCurrentReward():
    return rassh.core.constants.current_reward

def doAction(action):
    print "do action ==================================="
    rassh.core.constants.rl_action = action
