import tLib.logger
from tLib.level0 import *
from tLib.level1 import *
import sys
sys.path.append('/Users/tomjonas/PycharmProjects/plotEngine')
import plot_engine
try:
    del level0, level1
except NameError:
    pass