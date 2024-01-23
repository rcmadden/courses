message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

''' a teacher who needs to send a message to each of your students reminding them of their missing assignments and grade in the class. You have each of their names, number of missing assignments, and grades on a spreadsheet and just have to insert them into placeholders in this message variable.
'''

'''Sample command line input
names =  'chandler bing,phoebe buffay,monica geller,ross geller'
assignments = '3,6,0,2'
grades = '81,77,92,88'
'''

'''get the input from the command line for names, assignments and grades'''
names = input("Enter names separated by commas: ")
assignments = input("Enter assignments separated by commas: ")
grades = input("Enter grades separated by commas: ")

# Splitting the input strings into a list
names = names.split(",")
assignments = assignments.split(",")
grades = grades.split(",")

# Looping through the lists and printing the message for each student
for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
