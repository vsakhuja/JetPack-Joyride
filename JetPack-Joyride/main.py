#9
import numpy as np
import colorama
from colorama import Fore,Back,Style
import os
import random
import string
import time
from background import *
from characters import *
from functionality import *
from player import *

#list storing the bullets that were fired
list_of_bullets=[]
#obj4 is my object for the player
obj4=Player("Mando",24,30,10)
time_start=time.time()
#below mentioned loop is for generating obstacles 
for i in range(10,col*99,55):
	seed=random.randint(0,3)
	if (seed==0):
		obs=np.full((10,10),' ')
		obj2=Slant(10,obs,"left")
		obs=obj2.Straight()
		x_obs=random.randint(6,row-13)
		x_coin=random.randint(6,row-13)
		y_obs=random.randrange(i,i+30)
		y_coin=random.randrange(i,i+30)
		obj3=render(x_obs,y_obs,10,obs,inp)
		obj3.placement()
		obj2.Cleaner()
		obj6=coins(5,'$')
		obj6.make_coin(x_coin,y_coin)
	elif (seed==1):
		obs=np.full((10,10),' ')
		obj2=Slant(10,obs,"left")
		obs=obj2.Horizontal()
		x_obs=random.randint(6,row-13)
		x_coin=random.randint(6,row-13)
		y_obs=random.randrange(i,i+30)
		y_coin=random.randrange(i,i+30)
		obj3=render(x_obs,y_obs,10,obs,inp)
		obj3.placement()
		obj2.Cleaner()
		obj6=coins(5,'$')
		obj6.make_coin(x_coin,y_coin)
	elif (seed==2):
		obs=np.full((10,10),' ')
		obj2=Slant(10,obs,"left")
		obs=obj2.make_slant()
		x_obs=random.randint(6,row-13)
		x_coin=random.randint(6,row-13)
		y_obs=random.randrange(i,i+30)
		y_coin=random.randrange(i,i+30)
		obj3=render(x_obs,y_obs,10,obs,inp)
		obj3.placement()
		obj2.Cleaner()
		obj6=coins(5,'$')
		obj6.make_coin(x_coin,y_coin)
	else:
		obs=np.full((10,10),' ')
		obj2=Slant(10,obs,"right")
		obs=obj2.make_slant()
		x_obs=random.randint(6,row-13)
		x_coin=random.randint(6,row-13)
		y_obs=random.randrange(i,i+30)
		y_coin=random.randrange(i,i+30)
		obj3=render(x_obs,y_obs,10,obs,inp)
		obj3.placement()
		obj2.Cleaner()
		obj6=coins(5,'$')
		obj6.make_coin(x_coin,y_coin)
Time_remaining=250
time_start=time.time()
i=0
#used i as an iterator as cannot use the for loop.(Iterator cannot be updated)
while i<20000:
	i+=obj4.step
	if obj4.lives > 0 and Time_remaining > 0:	
		obj1=On_screen(row,i,(col+i),inp)
		obj1.sky('@')
		obj1.ground('!')
		obj4.render_player()
		current_time=time.time()
		Game_Duration=current_time-time_start
		Time_remaining=int(250.0-Game_Duration)
		if (current_time-obj4.shield_time>10.0):
			obj4.shield_flag=0
			obj4.man=[['O','O','O'],['<','|','>'],['/',' ','\\']]

		if (current_time-obj4.shield_time<60.0):
			obj4.shield_permission=0
		else:
			obj4.shield_permission=1

		if (current_time-obj4.nitros_time>10.0):
			obj4.nitros_flag=0
			obj4.step=1

		if (current_time-obj4.nitros_time<60.0):
			obj4.nitros_permission=0
		else:
			obj4.nitros_permission=1
		obj4.move_player(i,(col+i),list_of_bullets)
		for s in list_of_bullets:
			if s.Ycordinate() > (col+i+1):
				s.clear_bullet()
				list_of_bullets.remove(s)
			else:
				s.clear_bullet()
				s.destroy_inpath()
				if s.life_flag==1:
					s.clear_bullet()
					list_of_bullets.remove(s)
				else:
					s.move_bullet()
				s.Sety(s.Gety()+4)
		temp_arr="lives:{}    Coins:{}  Time_remaining:{}  ".format(obj4.count_life(),obj4.count_coin(),Time_remaining)
		print(temp_arr,end="")
		obj1.printsky()
		obj1.printbody()
		obj1.printground()
		print('\033[H',end="",flush='True')
	else:
		if Time_remaining>0:
			print("Game_Over")
		else:
			print("Winner winner chicken dinner,You WONNNNNN"+Fore.CYAN)






