#!/usr/bin/env python

# OOP in Python Example: Get Classy!

class Participant:
	def __init__(self, arg_team_id, arg_first_name, arg_last_name, arg_age, arg_uni):
		self.competition = "eYRC 2020-21"

		self.team_id = arg_team_id
		self.first_name = arg_first_name
		self.last_name = arg_last_name
		self.age = arg_age
		self.university = arg_uni

		self.task_scores = {'task1': 0, 'task2': 0, 'task3': 0}


	def updateName(self, arg_new_first_name, arg_new_last_name):
		self.first_name = arg_new_first_name
		self.last_name = arg_new_last_name

	def updateAge(self, arg_new_age):
		self.age = arg_new_age

	def updateUniversity(self, arg_new_uni):
		self.university = arg_new_uni


	def updateTaskScore(self, arg_task, arg_score):
		if(arg_task == 1):
			self.task_scores['task1'] = arg_score
		elif(arg_task == 2):
			self.task_scores['task2'] = arg_score
		elif(arg_task == 3):
			self.task_scores['task3'] = arg_score
		else:
			print("Invalid Task")
			return -1

		return 0

	def printDetails(self):
		print('------------')
		print('Competition: ' + self.competition)
		print('Team ID: ' + str(self.team_id))
		print('Name: ' + self.first_name + ' ' + self.last_name)
		print('Age: ' + str(self.age))
		print('University: ' + self.university)
		print('Task Scores: ') 
		print(self.task_scores)
		print('------------')




if __name__ == "__main__":
	print("** Get Classy! **")
	
    # Participant 1
	p1 = Participant(101, "Jon", "Doe", "19", "Jon Doe University")

	p1.updateName("John", "Doe")

	p1.updateTaskScore(1, 100)
	p1.updateTaskScore(2, 100)
	p1.updateTaskScore(3, 100)

	p1.printDetails()

    
	# Particapant 2
	p2 = Participant(102, "Virat", "Kholi", "19", "Delhi University")

	p2.updateName("Virat", "Gupta")

	p2.updateTaskScore(1, 80)
	p2.updateTaskScore(2, 90)
	p2.updateTaskScore(3, 100)

	p2.printDetails()

