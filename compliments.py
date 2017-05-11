""" This is a Terminal-based program that allows a user to create, view the entire, or view a 
random compliment from the compliment list """

def add_compliment_list(my_list):
    """takes user input and adds it as a new item to the end of the list"""
    compliment = raw_input("Give a compliment: ")
    my_list.append(compliment)
    return my_list 
