# 只是个草稿，但是现在勉强能用，算是V2吧
# [DONE]添加记录功能
# [TODO]规则：
# 	1. 超过Loop三倍以上时间为怠惰分心；
# 	2. 能够自动发布到wordpress博客上;
# 	3. 添加更加丰富的指令,比如放弃。


import sys; 
import os; 
from sys import stdin ; 
import winsound ; 
import time ;
from datetime import datetime; 
from threading import Thread; 

duration = 100; 
counter = 0 ; 
sep = 100; 
freq = 703 ;
total =0 ;
reason = "";
store_dir ="./store/";  
count_hits= 0;
epochlist = list(); 
counter_between = 0 ;
snow ="     \/  \n  _\_\/\/_/_\n __\_\/_/__\n __/_/\_\__\n  / /\/\ \ \n     /\ ";


def reset_timer():
	thread2=Thread(target = generous_counter, name ="thread-2");
	Thread.start( thread2 );
	global counter; 
	global count_hits ; 
	global snow; 
	while(True):
		cmd = stdin.read(1);
		stdin.read(1); 
		if(cmd=='\''):
			counter = 0;
			count_hits = count_hits + 1; 			
			print(snow);
		else:
			counter = -1;
			sys.exit(0);
			
		
def generous_counter():
	global counter; 
	global counter_between ; 
	global record_file; 
	# open a new file for writing 
	while(True):
		if(counter == 0):
			epochlist.append(counter_between);
		time.sleep(1);
		counter_between = counter_between + 1;  
		print("\r            ",end='');
		print("\r"+str(counter),end='');
		if(counter == revolution):
			winsound.Beep(330, 600);
			winsound.Beep(262, 600);
			winsound.Beep(294, 600);
			winsound.Beep(194, 600);
			counter = 0;
		elif(counter == -1):
			epochlist.append(counter_between);
			if(count_hits < total ):
				record_file.write("Assessment:")
				record_file.write("You did not finish your task, you give up!\n");
			else:
				record_file.write("You are nice!\n"); 
			record_file.write("Epoch:\n");
			record_file.write(str(epochlist)+"\n");
			record_file.write("Total Time Used:\n");
			record_file.write(str(sum(epochlist))+"seconds"); 
			if(sum(epochlist) > total*revolution):
				record_file.write("You are being slow, you need to improve yourself honey~");
			sys.exit(0);
		else:
			counter = counter + 1; 

if(len(sys.argv)!=4):
	print("Usage: python multi_clock_v2.py [revolution] [total loops] [\"What task?\"] ");
	exit(0);
reason = str(sys.argv[3]); 
total = int(sys.argv[2]);
revolution = int(sys.argv[1]) ;

if(not os.path.exists(store_dir)):
	os.makedirs(store_dir)

record_file_name = str(time.time());
record_file = open(store_dir+record_file_name,"w");
record_file.write(str(datetime.now()));
record_file.write("Description:");
record_file.write(sys.argv[3]);
record_file.write("Revolotion:");
record_file.write(sys.argv[1]);
record_file.write("Total loops:");
record_file.write(sys.argv[2]);

thread1=Thread(target = reset_timer, name ="thread-1");
try:
   Thread.start( thread1 );
except:
   print("Error: unable to start thread");
   sys.exits(0);
   
try:   
	thread1.join(); 
except:
	sys.exit(0);
