# TODO: First import the `random` module
import random

# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

            
# TODO: Add your function generate_password below
def generate_password(word_list):
    random_list = random.choices(word_list, k=3)
    return ''.join(random_list)
# It should return a string consisting of three random words 
# concatenated together without spaces

# Now we test the function
password = generate_password(word_list)
print(password)



result = math.exp(3)

print(result)