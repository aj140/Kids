# This is a game that will test you on your times table! Just change the variables below.
from random import randint

# These are the variables to change - no cheating!
which_times_table = 4
how_many_questions = 10
min_num = 1
max_num = 12
right_answer_pts = 100
wrong_answer_pts = 50
starting_points = 0

points = starting_points

player_name = input('Hello, welcome to the game. What is your name?\n')
host_name = input("Who do you want asking you questions?\n")

curr_q = 1

print ("Well, hello there " + str(player_name))
print (str(host_name) + " is now going to ask you some questions about the " + str(which_times_table) + " times table!")

# Run this loop as many times as the number of questions to be asked
while curr_q < (how_many_questions + 1):
    random_num = int(randint(min_num, max_num))
    user_answer = int(input("\nQuestion " + str(curr_q) + ": What is " + str(which_times_table) + " x " + str(random_num) + "?\n"))
    actual_answer = which_times_table * random_num
    if user_answer == actual_answer:
        print (str(host_name) + ": That's right - well done!")
        points = points + right_answer_pts
    else:
        print (str(host_name) + ": Sorry, but that's wrong :(")
        print (str(host_name) + ": The actual answer was " + str(actual_answer))
        points = points - wrong_answer_pts
    print ("You now have " + str(points) + " points")
    curr_q += 1

print ("\n\n" + str(host_name) + ": Good going " + str(player_name) + ", your final score is " + str(points) + " points")
