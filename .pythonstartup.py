import atexit
import readline
import rlcompleter
import os

readline.parse_and_bind('tab: complete')

histfile = os.path.join(os.environ['HOME'], '.pyhistory')

try:
    readline.read_history_file(histfile)
except IOError:
    print ('Can not read history file %s' % (histfile,))


atexit.register(readline.write_history_file, histfile)

del atexit, readline, rlcompleter, os, histfile
