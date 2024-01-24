def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open('flying_circus_cast.txt') as f:
        #use the for loop syntax to process each line
        for line in f:
            #and add the actor name to cast_list
            cast_list.append(line.split(',')[0])
          
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    return cast_list
cast_list = create_cast_list('flying_circus_cast.txt')
print(cast_list)