import time
### MAD LIBS ###
### source: http://www.woojr.com/wp-content/uploads/2010/05/funny-mad-libs.gif

print ("Give me an adj")
adj1 = input()

print ("Give me a nationality")
nationality = input()

print ("Give me a name")
name = input()

print ("Give me a noun")
noun1 = input ()

print ("Give me another adj")
adj2 = input()

print ("Give me another noun")
noun2 = input()

print ("Give me another adj")
adj3 = input()

print ("Give me another adj")
adj4 = input()

print ("Give me a plural noun")
pluralnoun= input()

print ("Give me another noun")
noun3 = input()

print ("Give me a number")
number = input ()

print ("Give me a type of shape")
shape = input()

print ("Give me a type of food")
food = input()

print ("Give me another type of food")
food2 = input()

print ("Give me another number")
number2 = input ()



### Begin Madlib ###

print ("Pizza was invented by a " + adj1 + nationality + " chef named")
print ( name + ". To make a pizza, you need to take a lump of " + noun1 + ",")
print (" and make a thin, round " + adj2 + noun2 + ". Then you cover it with ")
print ( adj3 + " sauce, " + adj4 + " cheese, and fresh chopped " + pluralnoun + ".")
print (" Next you have to bake it in a very hot " + noun3 + ". When it is done, cut ")
print (" it into " + number + shape + " . Some kids like" + food + "pizza the best, ")
print (", but my favorite is the " + food2 + " pizza. If I could, I would eat pizza ")
print ( number2 + " times a day")


time.sleep(100)
