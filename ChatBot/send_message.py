from respond_f import respond
from related_f import related
import time


bot_name = 'Bot'

print("Hello I am AI chat bot, you can chat with me,\n"
      "and ask me different questions.\n"
      "if you want to quit the chat session, just write 'quit', 'exit' or 'stop'."
      )


def get_response(message):
    related_text = related(message)
    response = respond(related_text)

    return response


# if __name__ == "__main__":
#
#     while True:
#         my_input = input('type here: ')
#         my_input = my_input.lower()
#         related_text = related(my_input)
#         if my_input == "exit" or my_input == "stop" or my_input == 'quit':
#             print('Typing...')
#             time.sleep(3)
#             print('It was nice chatting with ya, bye!')
#             break
#         send_message(related_text)
#         print('\nAsk me another thing or write "help" to see what i can tell you')
