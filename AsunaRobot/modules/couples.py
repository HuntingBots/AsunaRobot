from AsunaRobot import pbot as app
from AsunaRobot.utils.errors import capture_err
from AsunaRobot.utils.dbfunc import get_couple, save_couple
from pyrogram import filters
import random
from datetime import datetime

name: Japanese
couple: 本日のカップル
shipped: 本日のカップルはもう選ばれています
update: カップルをまた選べるまでは後
few: カップルを選ぶためにデータが足りません。
hours:
  - 時
minutes:
  - 分
seconds:
  - 秒間
select_lang: 👋 言語をお選びください。
set_lang: 👍 チャット言語は日本語に設定されています。ありがとうございます。
chat_only: 😅 Sorry, this command is only for chats.
admin_lang: Only admins can change current language.
help: |
  💕 <b>SHIPPERING</b> is a bot that will choose a couple of the day in your chat. Everyone who writes a message in your chat will be added to the list of candidates for a couple of the day. Add this bot to your chat and wait for it to gather enough participants before sending shipping command.

  /help — This message
  /shipping — Choose a couple of the day
  /last — Last chosen couples
  /lang — Choose a language for the bot (in chat only for admins)
  /top — Top lovers
  /autopin — Autopin (silently) when pair was chosen (bot must be admin)
  /setminusers — Set minimum users to choose a pair
start: |
  👋 Hello! <b>SHIPPERING</b> is a bot that will choose a couple of the day in your chat.

  Use /help for more info.
last_couples: Last chosen couples
times:
  - times
chats:
  - chats
