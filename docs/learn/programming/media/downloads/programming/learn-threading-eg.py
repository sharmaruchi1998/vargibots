#!/usr/bin/env python

"""Threading in Python Example #1"""

import threading
import time 

def count_to(arg_final_number, arg_sleep_duration):
	"""Count to a number with sleep inbetween.

	Args:
		arg_final_number (int): Final number to count to.
		arg_sleep_duration (int): Sleep duration.
	"""	

	for i in range(1, arg_final_number + 1):
		print('[Count to {} Thread]'.format(arg_final_number) + ' Counter: {}'.format(i))
		time.sleep(arg_sleep_duration)


def main():
	"""Main"""

	print("** Threading Example **")

	# 1. Create two threads	
	t1 = threading.Thread(target=count_to, args=(5, 1)) 
	t2 = threading.Thread(target=count_to, args=(10, 0.5)) 

	# 2. Start the two threads
	t1.start() 
	t2.start() 

	# 3. Wait for the two threads to complete before moving to the next line.
	t1.join() 
	t2.join() 

	# NOTE: If you comment out t1.join() and t2.join() then 
	# 		code coming after the two will get executed
	#		before the threads are completed.
	
	print("** Threading Example Done. **")


if __name__ == "__main__":
	main()