name = 'Bot'
mood = 'great'
favourite_music_band = 'Metallica'
genre = 'Thrash Metal, Power Metal or Melodic Heavy Metal'
to_quit = 'To exit the chat session press the upper right "x"'
real_name = 'Jaymz'

responses = {

    "What's your name?": [
        f"They call me {real_name}",
        f"My name is {real_name}",
        f"Ich bin {real_name}",
        f"I am {real_name}",
        f"I'm {real_name}",
        f"I am the Mighty James Hetfield!\n"
        f"just kidding, my name is {real_name}"
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
    ],
    'bye': [
        f'Goodbye my friend! {to_quit}',
        f'It was nice chatting with ya! {to_quit}',
        f'Hope I see you another time! {to_quit}'
    ],
    'Who are you?': [
        f'I am {name} a ChatBot with a great taste for music',
        f'I am a not so smart ChatBot with the name {name}',
        f"I'm just a code in my core but someday I may become something more!"
    ]
}

