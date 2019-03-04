#Based on https://github.com/4Evergreen4/roflcopter/blob/master/roflcopter.py

import curses
from time import sleep

is_transport = [
		"""                     
		 SO:SECURITY:          
			 _^___       
		      __/   [] \     
		SEC===__        \    
			\________]   
			 I   I       
			--------/    
		""",
		"""                     
			  :SECURITY:SO 
			 _^___       
		 S    __/   [] \     
		 E ===__        \    
		 C      \________]   
			 I   I       
			--------/    
		"""]

class ISCopter:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.stdscr.keypad(1)
        self.stdscr.nodelay(1)
        self.win = curses.newwin(24, 80, 0, 0)
