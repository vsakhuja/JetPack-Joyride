import numpy as np
import colorama
from colorama import Fore,Back,Style
import os
import time
import sys
colorama.init()
class On_screen:
	def __init__(self,row,col_in,col,inp):
		self.row=row
		self.col=col
		self.inp=inp
		self.col_in=col_in	

	def sky(self,character):
		for i in range(6):
			for j in range(self.col_in,self.col):
				inp[i][j]=character
	def ground(self,character):
		for i in range(self.row-3,self.row):
			for j in range(self.col_in,self.col):
				inp[i][j]=character
		
	def printsky(self):
		for i in range(1,6):
			for j in range(self.col_in,self.col):
				print(Fore.CYAN+inp[i][j],end="")
			print(Style.RESET_ALL)	
	def printbody(self):
		for i in range(6,self.row-3):
			for j in range(self.col_in,self.col):
				print(Back.WHITE+inp[i][j],end="")
			print(Style.RESET_ALL)
	def printground(self):
		for i in range(row-3,row):
			for j in range(self.col_in,self.col):
				print(Fore.RED+inp[i][j],end="")
			if ((i != row-1) or (i !=row-3)):
				print("")
			else:
				print(Style.RESET_ALL)
		
rows, columns =os.popen('stty size', 'r').read().split()
row=int(rows)-2
col=int(columns)-2
inp=np.full((row,col*100),' ')
#inp[35][25]="1"
