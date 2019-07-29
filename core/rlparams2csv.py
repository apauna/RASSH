import sys
sys.path.append("../../")

import rassh
from zope.interface import implements

from rassh.core import ttylog, fs, utils
from rassh.core.userdb import UserDB
from rassh.core.config import config
from rassh.dblog.rassh_mysql import *
import commands
import ConfigParser
from config import *
from rassh.core.constants import *



for row in getDB().getCases():
    if row["rl_params"] != "" and row["rl_params"] is not None:
        l = row["rl_params"].replace("[", "").replace("]", "")
        l = l.strip().split()
        print ",".join(l)



