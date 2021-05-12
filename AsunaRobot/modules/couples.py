from AsunaRobot import pbot as app
from AsunaRobot.utils.errors import capture_err
from AsunaRobot.utils.dbfunc import get_couple, save_couple
from pyrogram import filters
import random
from datetime import datetime

def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(' ')
    return dt_list


def dt_tom():
    a = str(int(dt()[0].split('/')[0]) + 1)+"/" + \
        dt()[0].split('/')[1]+"/" + dt()[0].split('/')[2]
    return a


today = str(dt()[0])
tomorrow = str(dt_tom())


@app.on_message(filters.command("couples") & ~filters.edited)
@capture_err
async def couple(_, message):
    if message.chat.type == "private":
        await message.reply_text("This command only works in groups.")
        return
    try:
        chat_id = message.chat.id
        is_selected = await get_couple(chat_id, today)
        if not is_selected:
            list_of_users = []
            async for i in app.iter_chat_members(message.chat.id):
                if not i.user.is_bot:
                    list_of_users.append(i.user.id)
            if len(list_of_users) < 2:
                await message.reply_text("Not enough users")
                return
            c1_id = random.choice(list_of_users)
            c2_id = random.choice(list_of_users)
            while c1_id == c2_id:
                c1_id = random.choice(list_of_users)
            c1_mention = (await app.get_users(c1_id)).mention
            c2_mention = (await app.get_users(c2_id)).mention

            couple_selection_message = f"""**Couple of the day:**
{c1_mention} + {c2_mention} = ❤️
__New couple of the day may be chosen at 12AM {tomorrow}__"""
            await app.send_message(
                message.chat.id,
                text=couple_selection_message
            )
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
