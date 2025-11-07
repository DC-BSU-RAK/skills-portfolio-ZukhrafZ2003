import tkinter as tk
import random

# ===== List of jokes (simulating randomJokes.txt file) =====
jokes_data = [
    "Why did the chicken cross the road?To get to the other side.",
    "What happens if you boil a clown?You get a laughing stock.",
    "Why did the car get a flat tire?Because there was a fork in the road!",
    "How did the hipster burn his mouth?He ate his pizza before it was cool.",
    "What did the janitor say when he jumped out of the closet?SUPPLIES!!!!",
    "Have you heard about the band 1023MB?It's probably because they haven't got a gig yet…",
    "Why does the golfer wear two pants?Because he's afraid he might get a 'Hole-in-one.'",
    "Why should you wear glasses to maths class?Because it helps with division.",
    "Why does it take pirates so long to learn the alphabet?Because they could spend years at C.",
    "Why did the woman go on the date with the mushroom?Because he was a fun-ghi.",
    "Why do bananas never get lonely?Because they hang out in bunches.",
    "What did the buffalo say when his kid went to college?Bison.",
    "Why shouldn't you tell secrets in a cornfield?Too many ears.",
    "What do you call someone who doesn't like carbs?Lack-Toast Intolerant.",
    "Why did the can crusher quit his job?Because it was soda pressing.",
    "Why did the birthday boy wrap himself in paper?He wanted to live in the present.",
    "What does a house wear?A dress.",
    "Why couldn't the toilet paper cross the road?Because it got stuck in a crack.",
    "Why didn't the bike want to go anywhere?Because it was two-tired!",
    "Want to hear a pizza joke?Nahhh, it's too cheesy!",
    "Why are chemists great at solving problems?Because they have all of the solutions!",
    "Why is it impossible to starve in the desert?Because of all the sand which is there!",
    "What did the cheese say when it looked in the mirror?Halloumi!",
    "Why did the developer go broke?Because he used up all his cache.",
    "Did you know that ants are the only animals that don't get sick?It's true! It's because they have little antibodies.",
    "Why did the donut go to the dentist?To get a filling.",
    "What do you call a bear with no teeth?A gummy bear!",
    "What does a vegan zombie like to eat?Graaains.",
    "What do you call a dinosaur with only one eye?A Do-you-think-he-saw-us!",
    "Why should you never fall in love with a tennis player?Because to them... love means NOTHING!",
    "What did the full glass say to the empty glass?You look drunk.",
    "What's a potato's favorite form of transportation?The gravy train",
    "What did one ocean say to the other?Nothing, they just waved.",
    "What did the right eye say to the left eye?Honestly, between you and me something smells.",
    "What do you call a dog that's been run over by a steamroller?Spot!",
    "What's the difference between a hippo and a zippo?One's pretty heavy and the other's a little lighter",
    "Why don't scientists trust Atoms?They make up everything."
]

# ===== FUNCTIONS =====

def tell_joke():
    """Randomly select a joke and display setup"""
    global current_joke
    current_joke = random.choice(jokes_data)
    setup, punchline = current_joke.split("?")
    punchline_label.config(text="")  # Hide punchline initially
    joke_label.config(text=setup.strip() + "?")
    show_button.config(state="normal")
    next_button.config(state="normal")


def show_punchline():
    """Display the punchline of the current joke"""
    if current_joke:
        setup, punchline = current_joke.split("?")
        punchline_label.config(text=punchline.strip())
        show_button.config(state="disabled")


def next_joke():
    """Display another random joke"""
    tell_joke()


# ===== GUI SETUP =====
root = tk.Tk()
root.title("Alexa Joke Assistant")
root.geometry("600x400")
root.configure(bg="#9ed3e1")

title_label = tk.Label(root, text=" Alexa Joke Assistant ",
                       font=("Arial", 20, "bold"), bg="#afe0ef", fg="#33375f")
title_label.pack(pady=20)

# Label for joke setup
joke_label = tk.Label(root, text="", font=("Arial", 16, "italic"), wraplength=500, bg="#9ed3e1")
joke_label.pack(pady=20)

# Label for punchline
punchline_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="#060606", wraplength=500, bg="#9ed3e1")
punchline_label.pack(pady=10)

# Buttons
alexa_button = tk.Button(root, text="Alexa tell me a Joke", font=("Arial", 14, "bold"), bg="#8a7c6a", command=tell_joke)
alexa_button.pack(pady=10)

show_button = tk.Button(root, text="Show Punchline", font=("Arial", 14), bg="#0c0c0c", command=show_punchline, state="disabled")
show_button.pack(pady=5)

next_button = tk.Button(root, text="Next Joke", font=("Arial", 14), bg="#9bf6ff", command=next_joke, state="disabled")
next_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit", font=("Arial", 14), bg="#ffc6ff", command=root.destroy)
quit_button.pack(pady=20)

current_joke = None

# Start the GUI
root.mainloop()
