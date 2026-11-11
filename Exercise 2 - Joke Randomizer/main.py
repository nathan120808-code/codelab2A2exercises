from tkinter import *

main = Tk()
main.title("Joke Generator")
main.geometry("800x500")
main.resizable(0,0)
main.config()

#Global dictionary
JOKES = [
    {"J": "Why did the chicken cross the road?", "A": "To get to the other side."},
    {"J": "What happens if you boil a clown?", "A": "You get a laughing stock."},
    {"J": "Why did the car get a flat tire?", "A": "Because there was a fork in the road!"},
    {"J": "How did the hipster burn his mouth?", "A": "He ate his pizza before it was cool."},
    {"J": "What did the janitor say when he jumped out of the closet?", "A": "SUPPLIES!!!!"},
    {"J": "Have you heard about the band 1023MB?", "A": "It's probably because they haven't got a gig yet…"},
    {"J": "Why does the golfer wear two pants?", "A": "Because he's afraid he might get a \"Hole-in-one.\""},
    {"J": "Why should you wear glasses to maths class?", "A": "Because it helps with division."},
    {"J": "Why does it take pirates so long to learn the alphabet?", "A": "Because they could spend years at C."},
    {"J": "Why did the woman go on the date with the mushroom?", "A": "Because he was a fun-ghi."},
    {"J": "Why do bananas never get lonely?", "A": "Because they hang out in bunches."},
    {"J": "What did the buffalo say when his kid went to college?", "A": "Bison."},
    {"J": "Why shouldn't you tell secrets in a cornfield?", "A": "Too many ears."},
    {"J": "What do you call someone who doesn't like carbs?", "A": "Lack-Toast Intolerant."},
    {"J": "Why did the can crusher quit his job?", "A": "Because it was soda pressing."},
    {"J": "Why did the birthday boy wrap himself in paper?", "A": "He wanted to live in the present."},
    {"J": "What does a house wear?", "A": "A dress."},
    {"J": "Why couldn't the toilet paper cross the road?", "A": "Because it got stuck in a crack."},
    {"J": "Why didn't the bike want to go anywhere?", "A": "Because it was two-tired!"},
    {"J": "Want to hear a pizza joke?", "A": "Nahhh, it's too cheesy!"},
    {"J": "Why are chemists great at solving problems?", "A": "Because they have all of the solutions!"},
    {"J": "Why is it impossible to starve in the desert?", "A": "Because of all the sand which is there!"},
    {"J": "What did the cheese say when it looked in the mirror?", "A": "Halloumi!"},
    {"J": "Why did the developer go broke?", "A": "Because he used up all his cache."},
    {"J": "Did you know that ants are the only animals that don't get sick?", "A": "It's true! It's because they have little antibodies."},
    {"J": "Why did the donut go to the dentist?", "A": "To get a filling."},
    {"J": "What do you call a bear with no teeth?", "A": "A gummy bear!"},
    {"J": "What does a vegan zombie like to eat?", "A": "Graaains."},
    {"J": "What do you call a dinosaur with only one eye?", "A": "A Do-you-think-he-saw-us!"},
    {"J": "Why should you never fall in love with a tennis player?", "A": "Because to them... love means NOTHING!"},
    {"J": "What did the full glass say to the empty glass?", "A": "You look drunk."},
    {"J": "What's a potato's favorite form of transportation?", "A": "The gravy train"},
    {"J": "What did one ocean say to the other?", "A": "Nothing, they just waved."},
    {"J": "What did the right eye say to the left eye?", "A": "Honestly, between you and me something smells."},
    {"J": "What do you call a dog that's been run over by a steamroller?", "A": "Spot!"},
    {"J": "What's the difference between a hippo and a zippo?", "A": "One's pretty heavy and the other's a little lighter"},
    {"J": "Why don't scientists trust Atoms?", "A": "They make up everything."}
]

def joke_gen():
    