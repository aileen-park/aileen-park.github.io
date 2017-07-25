#variable(lives)
Lives = 9


character = '''
    Choose which character you would like to be
    a) Hera the human
    b) Neko the cat
    c) Nara the monkey
    '''
print(character)
print("Type a b or c")

user_input = input()

while user_input != "a" and user_input != "b" and user_input != "c":
            print("No... Choose a b or c");
            print("Type a b or c")
            user_input = input()

if user_input == "a" "b" or "c":
    start = '''
        You are stuck in space. Your engine fell off and dropped onto either the planet Alinastro or Venuisa.
        You have to fix your rocket to get back home.
        The choice is all yours; which planet you decide to trudge through?
        Find your engine before you run out of lives; you're only given 9.
        But remember, you will lose 3 at a time.

        Type "left" to go to Alinastro.
        Type "right" to go to Venuisa.

        That's all for now.
        Best wishes!

        ~ Commander
        '''
    print(start)

print("Type 'left' to go left or 'right' to go right.")
user_input = input()

while user_input != "right" and user_input != "left":
            print("No... Choose left or right");
            print("Type 'left' to go left or 'right' to go right.");
            user_input = input()


#Alinastro
if user_input == "left":
    quest = '''
        You decided to go to Alinastro ~ Your journey has just begun!
        You find a cave in the middle of a desert.
        Type start to go into the cave.
        '''
    print(quest)

    print("Type 'go'")
    user_input = input()
    while user_input != "go":
            print("No... Type 'go'")
            print("Type 'go'")
            user_input = input()

#AlinastroTunnel
    if user_input == "start":
        print("Good luck!")

#challenge1
challenge1= '''
    STOP!
    There's a giant spider right up ahead!
    Her web is already set up for you!
    You only have scissors... what will you do?
    You have the option to either stand and fight it
    or
    RUN!

    note: every time you run away from a challenge, you lose 3 lives
    '''
print(challenge1)

print("Type 'x' to fight or 'o' to run.")
user_input = input()

while user_input != "x" and user_input != "o":
            print("No... Choose x or o");
            print("Type 'x' to fight or 'o' to run.");
            user_input = input()

#action1
if user_input == "x":
        action1 = '''
        Congratulations!
        You were able to cut through her trap and run.
        I'm impressed!

        Go on!
        '''
        print(action1)

        print("Press 'c' to continue")
        user_input = input()

elif user_input == "o":
        Lives -= 3
        print("You chose to run... I'm disappointed but it's better than dying... Continue on... HURRY!")
        print("Press 'c' to continue")
        user_input = input()

#challenge2
challenge2= '''
    HALT!!!
    The tunnel is lit up, and you didn't see that enormous chasm?
    There's no way around it...
    What are you going to do?

    You can either try climbing in and out of the chasm,
    but no one knows what's inside
    since no one has survived to tell the tale...
    or
    You could try stealing some of the spider's silk to make a ladder...
    but that's dangerous too...

    It's up to you...

    note: neither option will make you lose a life
    '''
print(challenge2)
print("Type 'd' to climb or 's' to steal.")
user_input = input()

while user_input != "d" and user_input != "s":
        print("No... Choose d or s");
        print("Type 'd' to climb or 's' to steal.")
        user_input = input()

#action2
if user_input == "d":
        action2 = '''
        Congratulations!
        You're making history!

        Go on!
        '''
        print(action2)

        print("Press 'c' to continue")
        user_input = input()

elif user_input == "s":
        print("Risky, but you made it!!")
        print("Press 'c' to continue")
        user_input = input()

advice = '''
        I think I found your engine at the end of this tunnel!
        You have one more obstacle ahead of you.
        Let's get through this and go home!!!
        '''
print(advice)

#challenge3
challenge3 = '''
    Oh no!
    There's a starving 20 foot serpent waiting for you!

    Hey... I have a confession to make.
    I'm not sure anymore that your engine is on this planet...
    BUT
    if it is, then that serpent would be guarding it.

    What will you do?
    You have the option to either stand and fight it
    or
    try going to another planet...

    I'm sorry!

    remember: every time you run away from a challenge, you lose 3 lives
    '''

print(challenge3)
print("Type 'x' to fight or 'o' to run.")
user_input = input()

while user_input != "x" and user_input != "o":
        print("No... Choose left or right");
        print("Type 'x' to fight or 'o' to run.");
        user_input = input()

#action3
if user_input == "x":
        action3 = '''
        You killed the serpent...
        It's a miracle!

        **after a few minutes**
        It's not here...
        '''
        print(action3)

        print("Press 'c' to continue")
        user_input = input()

elif user_input == "o":
    Lives -= 3
print("You chose to run... Get going! HURRY!")
print("Press 'c' to continue")
user_input = input()

apology = '''
    I'm sorry...
    I'll apologize in person when you return, so HURRY!
    '''
print(apology)

#back to the beginning: choose between the two planets

#print("Type 'left' to go left or 'right' to go right.")
#user_input = input()

#while user_input != "right" and user_input != "left":
            #print("No... Choose left or right");
            #print("Type 'left' to go left or 'right' to go right.");
            #user_input = input()

#Venuisa
#if user_input == "right":
    #quest = '''
    #    You've chosen to go to Venuisa ~ Your journey has just begun!
    #    You find an underwater cavern.
    #    You should start as soon as possible.
    #    '''
    #print(quest)
