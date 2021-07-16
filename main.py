#importing module
import sys
from os import system
from time import sleep
from random import choice
from pyfiglet import figlet_format
from termcolor import colored
#arguments
config_arg = sys.argv[1]
config_type = sys.argv[2]
config_value = sys.argv[3]
count_arg = (len(sys.argv)-1)
#config [Change this]
name = "feli" #nick name
full_name = "lycus felicius" #full name
next_step = ["Good, let's go to the next question.", "Alright, good then.", "Nice answer, let's go then.", "Good job, let's go then."] #responses to next step
yes_var = ["yes", "yep", "sure", "why not?", "why not", "of course", "absolutely", "definitely", "yup"] #if user say yes...
no_var = ["no", "not", "nay", "never", "nix", "nope"] #if user say no...
age = 16 #real age
is_color = 0 #colored ascii
random_color = 0 #randomize ascii color (ignore this, if color disabled)
color = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"] #random color (ignore this, if color disabled)
r_color = "blue" #set color (ignore this, if color disabled)
#setting variable
num_lies = 0
congrat = 1
double_quote = ""
#config arguments
if config_arg == "--set":
    if config_type == "-color":
        if config_value == "false":
            is_color = 0
            print("Successfully disable color")
            sleep(2)
            system('cls')
        elif config_value == "random":
            is_color = 1
            random_color = 1
            print("Successfully changed color to random")
            sleep(2)
            system('cls')
        elif config_value in color:
            is_color = 1
            r_color = config_value
            random_color = 0
            print("Successfully changed color to " + config_value)
            sleep(2)
            system('cls')
        else:
            print("Make sure you use the right arguments!")
            sleep(2)
            sys.exit()
    elif config_type == "-full-name":
            if count_arg > 3:
                print("Use quotation marks for full name that has more than one words!")
                sleep(2)
                sys.exit()
            full_name = config_value
            print("Successfully changed full name")
            sleep(2)
            system('cls')
#opening
print("Hello, thank you for opening this file ;)")
sleep(2)
#inputing username
print("What is your name?")
input_name = str.lower(input(">> "))
#if user not lies
if input_name in full_name:
    print("Alright, i will call you " + input_name + " from now on" + ".")
    name = input_name
    sleep(2)
    system('cls')
#if user lies
else:
    print("Don't lie to me!")
    print("I will call you " + name + " from now on" + ".")
    num_lies += 1
    sleep(2)
    system('cls')
#asking birthday
print("Is today your birthday " + name + "?")
is_birthday = str.lower(input(">> "))
if  is_birthday in yes_var:
    print(choice(next_step))
    sleep(2)
    system('cls')
elif is_birthday in no_var:
    if num_lies == 0:
        print("Dont lie to me, " + name + "!")
        print("Today is your birthday, huh...")
        num_lies += 1
        sleep(3)
        system('cls')
    elif num_lies >= 1:
        print("Why are you lies to me again " + name + "?")
        print("Today is your birthday, huh...")
        num_lies += 1
        sleep(3)
        system('cls')
else: #if programs not recognize the input
    print("I don't understand the word yet, but I'll assume today is your birthday...")
    sleep(2)
    system('cls')
#asking age
print("So, how old are you now " + name + "?")
iage = int(input(">> "))
#if age same
if iage == age:
    print(choice(next_step))
    sleep(2)
    system('cls')
#if too old
elif iage > age:
    if num_lies == 0:
        print("Are you sure " + name + "? I thought you weren't that old huh...")
        num_lies += 1
        sleep(2)
        system('cls')
    elif num_lies == 1:
        print("Why are you lies to me again " + name + "?")
        print("You're " + str(age) + " y.o. now huh...")
        num_lies += 1
        sleep(3)
        system('cls')
    elif num_lies > 1:
        print("Hey, why are you a liar " + name + "?")
        print("You're " + str(age) + " y.o. now huh...")
        num_lies += 1
        sleep(3)
        system('cls')
#if too young
elif iage < age:
    if num_lies == 0:
        print("Are you sure " + name + "? I thought you weren't that young huh...")
        num_lies += 1
        sleep(2)
        system('cls')
    elif num_lies == 1:
        print("Why are you lies to me again " + name + "?")
        print("You're " + str(age) + " y.o. now huh...")
        num_lies += 1
        sleep(3)
        system('cls')
    elif num_lies > 1:
        print("Hey, why are you a liar " + name + "?")
        print("You're " + str(age) + " y.o. now huh...")
        num_lies += 1
        sleep(3)
        system('cls')
#while loop
print("How many times do you want me to congratulate you " + name + "?")
icongrat = int(input(">> "))
print("Sure, i will...")
sleep(2)
print("Please wait a few second")
sleep(2)
system('cls')
while congrat <= icongrat:
        print("Happy " + str(age) + "th " + "Birthday " + name + "!")
        congrat += 1
sleep(1)
print("Don't close this windows, i have something...")
sleep(2)
#ASCII loop
print("Do you like some art?")
is_art = str(input(">> "))
if is_art in yes_var:
    congrat = 1
    while congrat <= icongrat:
        if is_color == 1:
            if random_color == 1:
                r_color = choice(color)
            ascii_text = colored(figlet_format("Happy " + str(age) + "th " + "Birthday " + name + "!"), color=r_color)
            print(ascii_text)
            congrat += 1
        else:
            ascii_text = figlet_format("Happy " + str(age) + "th " + "Birthday " + name + "!")
            print(ascii_text)
            congrat += 1
elif is_art in no_var:
    sleep(1)
else:
    print("I don't understand the word yet, but I'll assume you like it...")
    sleep(2)
    congrat = 1
    while congrat <= icongrat:
        if is_color == 1:
            if random_color == 1:
                r_color = choice(color)
            ascii_text = colored(figlet_format("Happy " + str(age) + "th " + "Birthday " + name + "!"), color=r_color)
            print(ascii_text)
            congrat += 1
        else:
            ascii_text = figlet_format("Happy " + str(age) + "th " + "Birthday " + name + "!")
            print(ascii_text)
            congrat += 1
#end
print("Alright, you can close this now")
print("Thank you " + name + "!!!")
system('PAUSE')