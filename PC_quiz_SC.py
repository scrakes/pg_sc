import pyautogui as pg
import time
import webbrowser

points=0

#Question goes here
answer = pg.prompt(
"""
You are presented with three items. Pick one.

a) Knife
b) Cheese
c) Book
d) Medicine
e) Green Rose

"""
    )

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 5
elif answer == "c":
    points += 10
elif answer == "d":
    points += 15
elif answer == "e":
    points += 20

#Question goes here
answer = pg.prompt(
"""
A little girl is about to be attacked by a rabid dog. Do you

a) Attack the dog
b) Flee and let the little girl be attacked
c) Divert the dogs attention to save the girl
d) Take the girl and runaway
e) Try to calm down the dog and back away slowly with the girl

"""
    )

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 5
elif answer == "c":
    points += 10
elif answer == "d":
    points += 15
elif answer == "e":
    points += 20

#Question goes here
answer = pg.prompt(
"""
You are on a bus and you find a hat. A man then accuses you of stealing it from him. Do you

a) Attack the man verbally or physically for accusing you of stealing
b) Be honest and argue vigorously that you didn't steal it until you win
c) Explain the situation to the man and use logic to prove yourself innocent
d) Apologize for stealing the hat even though you didn't and give it back and accept the consequences of stealing
e) Say that the situation is a misunderstanding and try to calm the man down

"""
    )

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 5
elif answer == "c":
    points += 10
elif answer == "d":
    points += 15
elif answer == "e":
    points += 20

#Question goes here
answer = pg.prompt(
"""
You just came back from the grocery store when a factionless person comes up to you and begs for some food. Do you

a) Push the man out of your way and head home
b) Ignore him and pretend he isn't there
c) Find a logical excuse for why you can't give your food to the factionless
d) Help the factionless person and give them some if not all of your food to them
e) Bless the old man but do not help him

"""
    )

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 5
elif answer == "c":
    points += 10
elif answer == "d":
    points += 15
elif answer == "e":
    points += 20

# END OF SURVEY
pg.alert("Ok, here is your faction.....")

pointlist = [9, 14, 19, 24, 25 , 21, 30, 35, 40, 50, 41, 45, 55, 60, 75, 61, 65, 70, 80, 100, 81, 85, 90, 95]

if points <= 9 or points == 14 or points == 19 or points == 24:
    pg.alert("You are Dauntless.")
    webbrowser.open("https://www.polyvore.com/cgi/img-thing?.out=jpg&size=l&tid=129824271")
elif points == 25 or points == 21 or points == 30 or points == 35 or points == 40:
    pg.alert("You are Candor.")
    webbrowser.open("https://vignette.wikia.nocookie.net/divergent/images/f/fd/Candor_logo.png/revision/latest?cb=20170316120034")
elif points == 50 or points == 41 or points == 45 or points == 55 or points == 60:
    pg.alert("You are Erudite.")
    webbrowser.open("https://vignette.wikia.nocookie.net/divergent/images/e/ee/Erudite_logo.png/revision/latest?cb=20170316110642")
elif points == 75 or points == 61 or points == 65 or points == 70 or points == 80:
    pg.alert("You are Abnegation.")
    webbrowser.open("https://vignette.wikia.nocookie.net/divergent/images/7/7a/Abnegation_logo.png/revision/latest?cb=20170316114853")
elif points == 100 or points == 81 or points == 85 or points == 90 or points == 95:
    pg.alert("You are Amity.")
    webbrowser.open("https://vignette.wikia.nocookie.net/divergent/images/c/cf/Amity_logo.png/revision/latest?cb=20170316105508")
elif points not in pointlist:
    pg.alert("You are Divergent.")
    webbrowser.open("https://i.gr-assets.com/images/S/photo.goodreads.com/hostedimages/1409711690i/11012004.jpg")
