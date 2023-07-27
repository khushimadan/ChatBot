import random

#generating random responses when bot overcomes an input to which it can not respond to

def random_string():
    random_list = [
        "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet.",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."
    ]
    string_length = len(random_list)
    random_index = random.randrange(string_length)
    random_item = random_list[random_index]

    return random_item
