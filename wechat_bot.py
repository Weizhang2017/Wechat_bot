from wxpy import *
import time

from chatterbot import ChatBot
import logging


class Wechat_bot:
	
	def __init__(self):
		bot = Bot()
		my_friend = ensure_one(bot.friends().search('Xiaoyuan'))
		my_group = ensure_one(bot.groups().search('candy*'))
		myself = bot.self
		chatterbot = Chatterbot()
#xiaoi = XiaoI('7i729KXqXqcZ', 'qSJt2E6zGtAxXexHfqYU')

		@bot.register(chats=my_group, except_self=False)
		def reply_my_friend(msg):
			# if isinstance(msg.chat, my_group) and not msg.is_at:
			# 	return
			# else:
			print(msg.text)
			chatterbot.response(msg.text)
				# print(xiaoi.reply_text(msg))
				# return xiaoi.reply_text(msg)

		@bot.register(my_friend)
		def friend(msg):
			my_friend.send(str(chatterbot.response(msg.text)))
		# my_friend.send(xiaoi.reply_text(msg))
	
	def run(self):
		embed()


'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''
# Enable info level logging
class Chatterbot:

	def __init__(self):
		logging.basicConfig(level=logging.DEBUG)

		self.chatbot = ChatBot(
		    'Example Bot',
		    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
		    trainer='chatterbot.trainers.ListTrainer',
		    # trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
		    database='chatterbot-db-list'
		)

		# Start by training our bot with the ChatterBot corpus data
		# self.chatbot.train(
		#     'chatterbot.corpus.english'
		# )

	def response(self, msg_text):
		return self.chatbot.train([msg_text])