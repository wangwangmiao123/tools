import sys; 
import winsound ; 
import time ;
from threading import Thread; 

revolution = int(sys.argv[1]) ;
duration = 100; 
counter = 0 ; 
sep = 100; 
freq = 666 ;
snow ="     \/   \n _\_\/\/_/_\n __\_\/_/__\n __/_/\_\__\n  / /\/\ \ \n     /\ ";


def reset_timer():
	thread2=Thread(target = generous_counter, name ="thread-2")
	Thread.start( thread2 );

	global counter; 
	while(True):
		cmd = sys.stdin.read(1);
		sys.stdin.read(1); 
		if(cmd=='\''):
			counter = 0;
			print(snow);
		else:
			counter=-1;
			sys.exit(0);
			
def generous_counter():
	global counter; 
	while(True):
		time.sleep(1);
		if(counter%7==0): 
			print("\r"+str(counter),end='');
		if(counter == revolution):
			for i in range(5):
				winsound.Beep(freq,duration) ;
				time.sleep(sep/1000) ;
			counter = 0 ;
		elif(counter == -1):
			sys.exit(0);
		else:
			counter = counter + 1; 
	
thread1=Thread(target = reset_timer, name ="thread-1")

try:
   Thread.start( thread1 )
except:
   print("Error: unable to start thread");
   sys.exits(0);
   
thread1.join(); 
