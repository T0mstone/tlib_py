"""
import sys
sys.path.append('/path/to/pythonPackages')
import tlib
"""


from .devtools import logging
from .basic_tools import *

try:
    del level0, devtools
except NameError:
    pass