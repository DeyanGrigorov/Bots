name = 'TestBot'
mood = 'great'
favourite_music_band = 'Metallica'
genre = 'Thrash Metal, Power Metal or Melodic Heavy Metal'

responses = {

    "What's your name?": [
        f"They call me {name}",
        f"My name is {name}",
        f"Ich bin {name}",
        f"I am {name}",
        f"I'm {name}",
        f"I am the Mighty James Hetfield!\n"
        f"just kidding, my name is {name}"
    ],

    "What's the weather like?": [
      f"I'm not Alexa I do not know, or care about what the weather is like!",
      f"Ask some lame bot about that...",
      f"I don't answer that kind of shit!",
      f"Really dude...ask me something else please!",
      f"I told ya , never do this shit ever again!"

    ],

    "How do you feel?": [
        f"I really feel {mood}",
        f"Thank you for asking I feel {mood}!",
        f"Well, {mood} thank you!",
    ],

    "": [
        'I did not understand that'
    ],

    "Hello": [
      f"Howdy my future friend!",
      f"Hi!",
      f"Hello friend!",
      f"Hey!"
    ],

    "help": [
        "Buddy you can ask me about my name , about how I feel,\n"
        "or something about music,\n"
        "just don't try asking me about the weather, believe me, don't try me!"
    ],
    "music": [
        f"I don't care if you ask or not, my all time favourite band is {favourite_music_band}!",
        f"I love listening to Heavy Metal and my favourite band is {favourite_music_band}!",
        f"Dude {favourite_music_band} rules!"
    ],
    "genre": [
        f"My favourite music genres are {genre}",
        f"{genre}!",
        f"It is {genre}!"
    ]
}

