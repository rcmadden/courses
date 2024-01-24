# Why do we need the finally clause in Python? 
# https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python

def run_code1(x):
    print("Code 1")

def run_code2():
    print("Code 2") 

def other_code():
    print("Other code")

try:
    run_code1()
except TypeError:
    run_code2()
finally:
    other_code()