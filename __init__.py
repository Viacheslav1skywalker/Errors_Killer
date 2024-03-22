import subprocess
import importlib
import sys
import io

sys.stdout = io.StringIO
if not importlib.util.find_spec('colorama'):
    subprocess.call(['pip', 'install', 'colorama==0.4.6'])
if not importlib.util.find_spec('black'):
    subprocess.call(['pip', 'install', 'black==24.1.1'])
sys.stdout = sys.__stdout__

