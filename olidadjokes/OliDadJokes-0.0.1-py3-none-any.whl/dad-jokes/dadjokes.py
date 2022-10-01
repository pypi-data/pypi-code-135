import random
from unittest import removeResult


def joke():
    dad_jokes = [
        "I'm afraid for the calendar. Its days are numbered.",
        "My wife said I should do lunges to stay in shape. That would be a big step forward.",
        "Why do fathers take an extra pair of socks when they go golfing?, In case they get a hole in one!",
        "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
        "What do a tick and the Eiffel Tower have in common? They're both Paris sites.",
        "What do you call a fish wearing a bowtie? Sofishticated.",
        "What do you call a factory that makes okay products? A satisfactory.",
        "What did the ocean say to the beach? Nothing, it just waved.",
        "Why do seagulls fly over the ocean?Because if they flew over the bay, we'd call them bagels.",
        "Where do boats go when they're sick? To the boat doc.",
        "I don't trust those trees. They seem kind of shady.",
        "Why couldn't the bicycle stand up by itself? It was two tired.",
        "This graveyard looks overcrowded. People must be dying to get in.",
        "What kind of car does an egg drive? A yolkswagen.",
        "What time did the man go to the dentist? Tooth hurt-y.",
        "My dad told me a joke about boxing. I guess I missed the punch line.",
        "When two vegans get in an argument, is it still called a beef?",
        "I ordered a chicken and an egg from Amazon. I'll let you know...",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "What's brown and sticky? A stick.",
        "What do you call an elephant that doesn't matter? An irrelephant.",
        "It takes guts to be an organ donor.",
        "What do you call a fake noodle? An impasta.",
        "Wanna hear a joke about paper? Never mind—it's tearable.",
        "Don't trust atoms. They make up everything!",
        "Why are elevator jokes so classic and good? They work on many levels.",
    ]
    return random.choice(dad_jokes)