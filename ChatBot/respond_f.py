from responses import responses
import random


def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses[''])
    return bot_message
