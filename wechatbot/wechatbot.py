from wxpy import *
import time
from .config import Config
import logging
logger = logging.getLogger(__name__)

class Wechat_bot:
	
	def __init__(self, ai, friend_name='', group_name=''):
		bot = Bot()
		if not (friend_name or group_name):
			raise ValueError('specify friend_name or group_name')
		if friend_name and group_name:
			raise ValueError('cannot add both friend_name and group_name ')
		if ai == 'ibot':
			ai_chat = XiaoI(Config.IBOT_KEY, Config.IBOT_SECRET)
			logging.info('ai_chat connected')
		if friend_name:
			target = ensure_one(bot.friends().search(friend_name))
			logging.info('target {}'.format(friend_name))
		if group_name:
			target = ensure_one(bot.groups().search(group_name))
			logging.info('target {}'.format(group_name))
		myself = bot.self

		@bot.register(chats=target, except_self=False)
		def reply_target(msg):
			if msg.text and msg.text.find('@Kyle') != -1:
				ai_chat.do_reply(msg)

	
	def run(self):
		embed()

