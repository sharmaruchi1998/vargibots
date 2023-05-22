#!/usr/bin/env python

def sim_score(arg_sim_time):
	score = (60) * ( (1000.0 - arg_sim_time)/1000.0)
	
	if (score < 0):
		return 0

	return score

def main():


	U1 = raw_input('1. How many packages does your UR5#1 is able to pick and place on the conveyor belt? -> ')
	if(U1):
		UR1_pnt = int(U1) * 50
	else:
		UR1_pnt = 0


	U2 = raw_input('2. How many packages does your UR5#2 is able to place in the correct color corresponding bin? -> ')
	if(U2):
		UR2_pnt = int(U2) * 50
	else:
		UR2_pnt = 0


	coll = raw_input('3. Are you able able to avoid any kind of collision? (y/n) -> ')
	if(coll == 'y'):
		coll_pnt = 40
	else:
		coll_pnt = 0


	no_coll = raw_input('4. Total number of collision? (0 or +ve integer) -> ')
	no_coll_pnt = int(no_coll) * (-10)


	sim = raw_input('5. What is your simulation time? (+ve integer) -> ')
	sim_pnt = sim_score( int(sim) )


	t4_score = UR1_pnt + UR2_pnt + coll_pnt + no_coll_pnt + sim_pnt

	if(t4_score < 0):
		t4_score = 0

	print("\n\n Task-4 Self-Eval Score: {}".format(str(t4_score)) )

if __name__ == '__main__':
	main()
