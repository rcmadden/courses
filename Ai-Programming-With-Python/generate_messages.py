names =  'chandler bing,phoebe buffay,monica geller,ross geller'
assignments = '3,6,0,2'
grades = '81,77,92,88'


# names =  (input('Enter names seperated by commas: ')) # get and process input for a list of names
# assignments = (input('Enter assignments: ')) # get and process input for a list of the number of assignments
# grades = (input('Enter grades: ')) # get and process input for a list of grades

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {name},\n\nThis is a reminder that you have {assignment} assignments left to \
submit before you can graduate. Your current grade is {grade} and can increase \
to {grade} if you submit all assignments before the due date.\n\n"

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
# convert string to list
names = names.split(',')
assignments = assignments.split(',') 
grades = grades.split(',') # convert string to list

# use f string to print message
for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name=name, assignment=(int(assignment)-6), grade=grade))
