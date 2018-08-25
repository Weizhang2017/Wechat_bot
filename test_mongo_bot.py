from chatterbot import ChatBot
import logging


'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''

# Enable info level logging
class Chatterbot:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

        self.chatbot = ChatBot(
            'Example Bot',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
        )

        # Start by training our bot with the ChatterBot corpus data
        self.chatbot.train(
            'chatterbot.corpus.english'
        )
    def response(self, msg):
        return self.chatbot.get_response(msg)