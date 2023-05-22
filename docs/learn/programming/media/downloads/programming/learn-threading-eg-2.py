#!/usr/bin/env python

"""Threading in Python Example #2"""

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
	
	print('[Count to {} Thread]'.format(arg_final_number) + ' Thread is complete.')


def main():
	"""Main"""

	print("** Threading Example #2 **")

	# 1. Create two threads	
	t1 = threading.Thread(target=count_to, args=(5, 1)) 
	t2 = threading.Thread(target=count_to, args=(10, 0.5))
	t3 = threading.Thread(target=count_to, args=(20, 0.25)) 

	# 2. Start the two threads
	t1.start()
	t1.join() 

	t2.start()
	t3.start() 

	while(1):
		print(time.time())
		time.sleep(1)

	# print("** Code won't reach here. **")
	# t2.join()
	# t3.join()


if __name__ == "__main__":
	main()