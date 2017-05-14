""" This is a Terminal-based program that allows a user to create, view the entire, or view a 
random compliment from the compliment list """

""" Borrowed so much from the todo_list workshop code """ 

import random 

def add_compliment_list(my_list):
    """takes user input and adds it as a new item to the end of the list"""
    compliment = raw_input("Give a compliment: ")
    my_list.append(compliment)
    return my_list 

def view_all_compliments(my_list): 
    """iterates though the list containing compliments and prints each item out""" 
    for compliment in my_list: 
        print compliment 

def view_random_compliment(my_list): 
    end = my_list - 1 
    random_num = random.randint(0,end)
    print my_list[random_num]

def display_main_menu(my_list): 
    """Displays main option, takes in user input, calls view all, view random, or
    add function """ 

    user_options = """ 
        \nWould you like to: 
        A. Add a compliment
        B. View all the compliments 
        C. View a random compliment 
        D. Quit the program 
        >>> """ 

        while True: 
            user_input = raw_input(user_options) 
            if user_input == "A": 
            elif user_input == "B": 
            elif user_input == "C": 
            elif user_input == "D": 
            else: 
                print "Thats not a valid option, please enter A, B, C, or D"
