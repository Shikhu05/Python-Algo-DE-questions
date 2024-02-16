# grade calculator

# Given different scored marks of students. We need to find a Grade Calculator in Python. 
# The test score is an average of the respective marks scored in assignments, tests, and lab work. 
# The final test score is assigned using the below formula.

# 10% of marks scored from submission of Assignments
# 70% of marks scored from Test
# 20% of marks scored in Lab-Works
# The grade will be calculated according to the:

# 1. score >= 90 : "A"
# 2. score >= 80 : "B"
# 3. score >= 70 : "C"
# 4. score >= 60 : "D"
# Also, calculate the total class average and letter grade of the class.


# Creating a dictionary which
# consists of the student name,
# assignment result test results
# and their respective lab results
 
# 1. Jack's dictionary
jack = {"name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
        }
 
# 2. James's dictionary
james = {"name": "James Potter",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "lab": [67.90, 78.72]
         }
 
# 3. Dylan's dictionary
dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 23, 39],
         "test": [78, 77],
         "lab": [80, 80]
         }
 
# 4. Jessica's dictionary
jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
        }

# 5. Tom's dictionary
tom = {"name": "Tom Hanks",
       "assignment": [29, 89, 60, 56],
       "test": [65, 56],
       "lab": [50, 40.6]
       }
 

def get_avg(marks_avg):
	total_sum = sum(marks_avg)
	avg1 = float(total_sum)/len(students_marks)
	return avg1


def total_avg_val(students_name):
	assignment = get_avg ( students_name ['assignment'])
	test = get_avg ( students_name ['test'])
	lab = get_avg ( students_name ['lab'])
	val = (.1 * assignment + .7 * test + .2 * lab)
	return val 

def letter_score(v):	
	if v >= 90:
		return 'A'
	elif v>= 80 and v <= 89:
		return 'B'
	elif v>= 70 and v <= 79:
		return 'C'
	elif v>= 60 and v <= 69:
		return 'D'
	else:
		return 'E'

def class_avg(list_students):
	temp_list = []
	avg_dct = {}
	for i in list_students:
		avg_individual = total_avg_val(i)
		temp_list.append(avg_individual)
		avg_dct[i] = avg_individual

	class_avg = get_avg(temp_list)
	return class_avg


students = [jack, james, dylan, jess, tom]
for name in students:
	print ('name' , name)
	res_avg = total_avg_val(name)
	print (name, ' avg is ', res_avg)
	print (name, ' letter grade is ',letter_score(res_avg) )

print ('class avg is ',class_avg(students) )



