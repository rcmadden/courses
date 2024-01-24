def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
    '''add a try excpet block to make sure ZeroDivisionError does not halt the program'''
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero")
        # return None, None
    # NOTE: copilot could not handle the exception 10/10 were wrong
    # chatGPT prompt used for above code also threy error: write a try except block that does crash if a ZeroDividionsError occurs
    # based on error self corrected return to None, None
    # UPDATE: the two lines below needed to be removed for the ChatGPT Solutions to work
    # TODO: try to get chatgpt to solve that issue
    # num_each = cookies // people
    # leftovers = cookies % people

    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")