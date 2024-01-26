# High Card, Low Card
# set high and low point
# Shuffle and draw one card 1-10
# Show the card
# Shuffle again and draw another card
# If the first card is the same as the second
# Shuffle and Draw again
# Ask the user to guess higher or lower
# Present the card and declare a winner
# Here we go!
# from random import randrange


# def addNum(num1, num2):
#    print(num1 + num2)
# addNum(2, 4)

def card_value(first_card, second_card, high_card, low_card):
    first_card
    second_card
    high_card
    low_card
    high_card = first_card + second_card
    print("The First Card is: ", first_card)
    print("The Second Card is: ", second_card)
    print("The High Card is: ", high_card)
    print("The Low Card is: ", low_card)

card_value(1,2,3,4)

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function("America")
my_function("Brazil")

# print(randrange(11))
import random;
# print(random.randint(1, 10))
first_card = random.randint(1, 10)
second_card = random.randint(1, 10)
print("First Random Card from the top is: ", first_card)
print("Second Random Card from the top is: ", second_card)

if first_card == second_card:
    print("Tie")
    print("First Card before is: " , first_card)
    print("Second Card before is: " , second_card)
    second_card = random.randint(1, 10)
    print("First Card after is: ", first_card)
    print("Second Card after is: ", second_card)

# This all works as expected
# We need to check if the numbers are the same and redo the random
#

    while first_card < 11 :
        print("First Card is: " , first_card)
        if first_card == second_card:
            print("We got here")
        break

