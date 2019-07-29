from pybrain.rl.environments.environment import Environment
from scipy import zeros
from utils import *

class HASSHEnv(Environment):
    
    indim = 5
    
    outdim = 4
    
    def getSensors(self):
	val = getCurrentCommand()
	return [val,]
    
    def performAction(self, action):
	doAction(action)
	print "Action performed: ", action
    
    def reset(self):
	pass

