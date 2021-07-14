#importing module
from os import system
from time import sleep
from random import choice
from pyfiglet import figlet_format
#config [Change this]
name = "feli" #nick name
full_name = "lycus felicius" #full name
next_step = ["Good, let's go to the next question.", "Alright, good then.", "Nice answer, let's go then.", "Good job, let's go then."] #responses to next step
yes_var = ["yes", "yep", "sure", "why not?", "why not", "of course"] #if user say yes...
no_var = ["no", "not", "nay", "never", "nix"] #if user say no...
age = 16 #real age
#setting variable
num_lies = 0
congrat = 1
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
        #print("Happy " + str(age) + "th " + "Birthday " + name + "!")
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
        #print("Happy " + str(age) + "th " + "Birthday " + name + "!")
        ascii_text = figlet_format("Happy " + str(age) + "th " + "Birthday " + name + "!")
        print(ascii_text)
        congrat += 1
#end
print("Alright, you can close this now")
print("Thank you " + name + "!!!")
system('PAUSE')