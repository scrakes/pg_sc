name = "Scarlett"

subjects = ["English","Math","Science","History","Chinese"]

print("Hello " + name)

for i in subjects:
    print("One of your subjects is " + i)
    


desserts = ["Cake","Ice Cream","Cupcakes","Tarts","Pie","Vegetables","Tiramisu","Cookies","Brownies"]

for i in desserts:
    if i == "Vegetables":
        print(i + " taste horrible")
    elif i == "Cake":
        print(i + " is delicious")
    else:
        print("You love to eat " + i)

movies = []

while True:
    print("What's one of your favorite movies? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)


for i in movies:
    print("One of your favorite movies is " + i)
    
    
    
