def related(x_text):
    if 'name' in x_text:
        y_text = "What's your name?"
    elif 'feel' in x_text or 'mood' in x_text:
        y_text = "How do you feel?"
    elif 'weather' in x_text:
        y_text = "What's the weather like?"
    elif 'hi' in x_text or 'hello' in x_text or 'hey' in x_text:
        y_text = "Hello"
    elif 'help' in x_text:
        y_text = "help"
    elif 'music' in x_text:
        y_text = "music"
    elif 'genre' in x_text:
        y_text = 'genre'
    elif 'bye' in x_text or 'goodbye' in x_text or 'see ya' in x_text or 'see you' in x_text:
        y_text = 'bye'
    elif 'are you' in x_text:
        y_text = 'Who are you?'
    else:
        y_text = ""
    return y_text
