import pyautogui as pg
import webbrowser
import time

pet = pg.confirm(text="What pet do you want?", title="Adopt a Pet", buttons=['dog', 'cat', 'fish', 'guinea pig/hamster', 'rabbit', 'bird'])

if pet == "dog":
    dog = pg.confirm(text="How old do you want your dog to be?", title="Dog Age", buttons=['puppy', 'young', 'adult', 'senior'])
    if dog == "puppy":
        webbrowser.open("https://www.adoptapet.com/shelter71590-pets.html#current_page=1#clanId=1#age=puppy")
    elif dog == "young":
        webbrowser.open("https://www.adoptapet.com/shelter71590-pets.html#current_page=1#clanId=1#age=young")
    elif dog == "adult":
        webbrowser.open("https://www.adoptapet.com/shelter71590-pets.html#current_page=1#clanId=1#age=adult")
    elif dog == "senior":
        webbrowser.open("https://www.adoptapet.com/shelter71590-pets.html#current_page=1#clanId=1#age=senior")
elif pet == "cat":
    cat = pg.confirm(text="How old do you want your cat to be?", title="Cat Age", buttons=['kitten', 'young', 'adult', 'senior']
    if cat == "kitten":
        webbrowser.open("http://kittenrescue.org/age/baby/")
    elif cat == "young":
        webbrowser.open("http://kittenrescue.org/age/young/")
    elif cat == "adult":
        webbrowser.open("http://kittenrescue.org/age/adult/")
    elif cat == "senior":
        webbrowser.open("http://kittenrescue.org/age/senior/")
elif pet == "fish":
    fish = pg.confirm(text="What type of fish do you want?", title="Type of Fish", buttons=['goldfish', 'tropical fish', 'aquarium fish']
    if fish == "goldfish":
        webbrowser.open("https://nextdaykoi.com/koi-fish/goldfish/fancy-imported-goldfish/?gclid=EAIaIQobChMI17XVk-3k2gIVDo_ICh1mawC2EAAYAyAAEgK7PvD_BwE")
    elif fish == "tropical fish":
        webbrowser.open("https://www.petfishforsale.com/?gclid=EAIaIQobChMIteGjxu3k2gIVjGSGCh0F8QYREAAYAiAAEgJupvD_BwE")
    elif fish == "aquarium fish":
        webbrowser.open("http://www.worldanimalfoundation.org/adopt-a-fish.html")
elif pet == "guinea pig/hamster":
    webbrowser.open("https://www.petfinder.com/member/us/nj/budd-lake/north-jersey-guinea-pig-and-hamster-rescue-inc-nj431/")
elif pet == "rabbit":
    webbrowser.open("http://www.saveabunny.org/adopt")
elif pet == "bird":
    bird = pg.confirm(text="What type of bird do you want?", title="Type of Bird", buttons=['parrot', 'other birds']
    if bird == "parrot":
        webbrowswer.open("http://www.companionparrots.org/index-content-adoption.htm")
    elif bird == "other birds":    
        webbrowser.open("https://www.petfinder.com/search/birds-for-adoption/")
