import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from AsunaRobot import dispatcher
from AsunaRobot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
      "Why did you come as a runner to remind me of a breakdown into my life full of darkness 😖",
      "Shit, you're killed. You don't exist",
      "So how does it feel after death?",
      "Are you born this stupid or have you done a course?",
      "Don't be a racist, hate everyone.",
      "Two words for you - F.O.",
      
  )

@run_async
def q(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /q  
"""

__mod_name__ = "Killing Commands"

Q_HANDLER = DisableAbleCommandHandler("q", q)

dispatcher.add_handler(Q_HANDLER)
