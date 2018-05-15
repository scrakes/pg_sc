print("What's your name?")
name = input()
print("Hey! What's up " + name + "!")
print("What's your favorite color?")
color = input()
color2 = "Ocean Blue"
color3 = "Sky Blue"

if color == "purple":
    print("I love purple!")

elif color == "pink":
    print("Pink is pretty cool")

elif color == "blue":
    print(color2 + " or " + color3 + " ?")
    color4 = input()

    if color4 == color2:
        print("Good choice!")

    elif color4 == color3:
        print("Cool!")

    else:
        ("Okay.")

elif color == "green":
    print("Green was cool until Milli liked it. Then it became uncool. :(")
    
else:
    print(color + " is nice too.")

print("What sport do you like to play most?")
sport = input()

if sport == "Soccer":
    print("What position do you play in soccer?")
    soccerposition = input()

    if soccerposition == "foward":
        print("Cool!")
    else:
        print(soccerposition + " is fun too.")

elif sport == "Archery":
    print("YAS! Archery is da best!")

else:
    print("That's awesome! But Archery is the best sport.")

print("What zodiac sign are you?")
zodiac = input()

if zodiac == "Scorpio":
    print("Cool! I'm Scorpio too!")

else:
    print(zodiac + " is cool too, but Scorpio is the best.")
