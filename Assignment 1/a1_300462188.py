# Course: ITI 1120
# Assignment 1
# Balaji, Aparna
# 300462188

# Importing the math and turtle modules
import math
import turtle
s = turtle.Screen()
t = turtle.Turtle()

# Question 1

def mh2kh(s):

    '''
    1. (float) -> (float) 
    2. s must be a number and s must be greater than or equal to 0.
    3. Converts the speed given in miles per hour to kilometres per hour.
    '''
    
    return (s * 1.60934)

# Question 2

def pythagorean_pair(a, b):

    '''
    1. (int, int) -> (bool)
    2. a and b must be integers.
    3. Takes two integers a and b and returns True if a and b are a pythagorean pair and False otherwise.
    '''
    
    c = math.sqrt((a ** 2) + (b ** 2))
    pair = c % 1 == 0
    return pair

# Question 3

def in_out(xs, ys, side):

    '''
    1. (float, float, float) -> (bool)
    2. xs and ys must be numbers (int or float), and side must be a non-negative number.
    3. Prompts the user for the coordinates (x, y) of a query point and prints True if the point lies inside or on the boundary of the square defined by (xs, ys, side), and False otherwise.
    '''

    xc = float(input("Enter a number for the x coordinate of a query point: "))
    yc = float(input("Enter a number for the y coordinate of a query point: "))

    xsr = (xs + side)
    yst = (ys + side)

    return (xs <= xc <= xsr and ys <= yc <= yst)

    
# Question 4

def safe(n):

    '''
    1. (int) -> (bool)
    2. n must be a non-negative integer with at most 2 digits (0 <= n <= 99).
    3. Returns True if n is a safe number (does not contain digit 9 and is not divisible by 9), otherwise returns False.
    '''
    
    first_digit = n // 10
    second_digit = n % 10
    divisible = n % 9

    return (n < 9) or (first_digit % 9 != 0 and second_digit % 9 != 0 and divisible != 0)

# Question 5

    '''
    1. (str, str, int) -> (str)
    2. quote must be a string, name must be a string, and year must be an integer.
    3. Returns a string in the format: "In year, a person called name said: “quote”".
    '''

def quote_maker(quote, name, year):
    return ("In " + str(year) + ", a person called " + name + ' said: "' + quote + '"')

# Question 6
    
def quote_displayer():

    '''
    1. () -> None
    2. None
    3. Prompts the user for a quote, name, and year, then prints a formatted sentence by calling the quote_maker function.
    '''
    
    quote = input("Give me a quote: ")
    name = input("Who said that? ")
    year = input("What year did she/he say that? ")
    print(quote_maker(quote, name, year))

# Question 7

def rps_winner():

    '''
    1. () -> None
    2. None 
    3. Prompts for the choices of player 1 and player 2, then prints whether player 1 wins, player 2 wins, or if it is a tie.
    '''
    
    print("What choice did player 1 make?")
    first_player = input("Type one of the following options: rock, paper, scissors: ")
    print("What choice did player 2 make?")
    second_player = input("Type one of the following options: rock, paper, scissors: ")

    first_player_rock = "rock" == first_player
    second_player_rock = "rock" == second_player

    first_player_paper = "paper" == first_player
    second_player_paper = "paper" == second_player

    first_player_scissors = "scissors" == first_player
    second_player_scissors = "scissors" == second_player

    first_player_wins = (first_player_rock and second_player_scissors) or (first_player_paper and second_player_rock) or (first_player_scissors and second_player_paper)
    draw = not((first_player_rock and second_player_rock) or first_player_paper and (second_player_paper) or (first_player_scissors and second_player_scissors))

    print("Player 1 wins. That is " + str(first_player_wins))
    print("It is a tie. That is not " + str(draw)) 
    

# Question 8

def fun(x):

    '''
    1. (float) -> (float)
    2. x must be a positive number.
    3. Solves the equation 10^4 * y = x + 3 for y and returns the value of y.
    '''
    
    y = (math.log(x + 3, 10)) / 4
    return y

# Question 9

def ascii_name_plaque(name):

    '''
    1. (str) -> None
    2. name must be a string.
    3. Prints a name plaque framed with '*' characters, containing the given name.
    '''
    
    length = len(name)
    print((10 * "*") + (length * "*"))
    print(("*") + ((" " * length) + (8 * " ")) + ("*"))
    print(("*") + (" " * 2) + "__" + name + "__" + (" " * 2) + ("*"))
    print(("*") + ((" " * length) + (8 * " ")) + ("*"))
    print((10 * "*") + (length * "*"))

# Question 10

def draw_house():

    '''
    1. () -> None
    2. None
    3. Draws a simple house with a square base, a triangular roof, and at least two distinct filled regions (e.g., windows).
    '''
    
    t.pensize(2)
    t.pendown()
    t.goto(0,0)
    t.goto(-70,100)
    t.goto(-140,0)
    t.goto(-115,0)
    t.goto(-115, -90)
    t.goto(15, -90)
    t.goto(15,0)
    t.goto(0,0)
    t.goto(100,0)
    t.goto(30, 100)
    t.goto(-70, 100)
    t.penup()
    t.goto(75,0)
    t.pendown()
    t.goto(75, -90)
    t.goto(-80, -90)
    t.goto(-80, 0)
    t.goto(-35, 0)
    t.goto(-35, -90)
    t.penup()
    t.goto(-80, -45)
    t.pendown()
    t.goto(-70, -45)
    t.goto(-70, -50)
    t.penup()
    t.goto(15,35)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.penup()
    t.goto(20, 100)
    t.pensize(2)
    t.pendown()
    t.goto(20, 120)
    t.goto(10, 120)
    t.goto(10, 100)
    t.penup()
    t.goto(90, -90)
    t.pendown()
    t.pensize(5)
    t.goto(-130, -90)
    t.penup()
    t.goto(30,-30)    
    t.fillcolor('yellow')
    t.begin_fill()
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.end_fill()
    # window
    t.penup()
    t.goto(60, -60)
    t.pensize(3)
    t.pendown()
    t.goto(30, -60)
    t.goto(30,-30)
    t.goto(60, -30)
    t.goto(60, -60)
    t.goto(45, -60)
    t.goto(45, -30) 
    t.penup()
    t.goto(30, -45)
    t.pendown()
    t.goto(60, -45)
    t.penup()
    t.goto(150, 150)

# Question 11

def alogical(n):

    '''
    1. (float) -> (int)
    2. n must be a number greater than or equal to 1.
    3. Returns the minimum number of times n must be divided by 2 
       to obtain a result less than or equal to 1.
    '''
    
    x = math.log(n, 2)
    number_of_times = math.ceil(x)
    return number_of_times

# Question 12

def cad_cashier(price, payment):
    
    '''
    1. (float, float) -> (float)
    2. price and payment must be non-negative real numbers with two decimal places, payment >= price, and the second decimal of payment must be 0 or 5.
    3. Returns the change owed to the customer, rounded to the nearest 5 cents, as a float with 2 decimal places.
    '''
    
    change = payment - price
    cents = round(change * 100)
    rounded_cents = 5 * round(cents / 5)

    return round(rounded_cents / 100, 2)

# Question 13

def min_CAD_coins(price, payment):

    '''
    1. (float, float) -> (int, int, int, int, int)
    2. price and payment must be non-negative real numbers with two decimal places, 
       payment >= price, and the second decimal of payment must be 0 or 5.
    3. Returns a tuple (t, l, q, d, n) representing the minimum number of 
       toonies, loonies, quarters, dimes, and nickels that make up the change 
       owed to the customer.
    '''
    
    cents = (cad_cashier(price, payment)) * 100
    toonies = cents // 200
    cents = cents - (toonies * 200)
    loonies = cents // 100
    cents = cents - (loonies * 100)
    quarters = cents // 25
    cents = cents - (quarters * 25)
    dimes = cents // 10
    cents = cents - (dimes * 10)
    nickles = cents // 5
    cents = cents - (nickles * 5)
    return (int(toonies), int(loonies), int(quarters), int(dimes), int(nickles))
    

    
    
