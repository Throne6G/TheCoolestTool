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

	def main(self):
        	done = False
        	i = 0
        	while not(done):
		    	self.win.addstr(0, 0, frames[i], curses.A_STANDOUT)
		    	self.win.addstr(10, 7, 'InfoSec', curses.A_STANDOUT)
		    	self.win.bkgd(' ', curses.A_STANDOUT)
		    	self.win.refresh()
			if i == 0:
				i = 1
			elif i == 1:
				i = 0 
			key = self.stdscr.getch()
			if key == ord('q'):
		        	done = True
		    	sleep(0.1)
