'''open some_file.txt in the same directory as this file, and print the contents to the terminal'''
# with open('some_file.txt') as f:
#     file_data = f.read()
#     print(file_data)

f = open('some_file.txt', 'r')
file_data = f.read()
print(file_data)
f.close()

# write to a file
# f = open('some_file.txt', 'w')
# f.write("Hello there!")
# f.close()