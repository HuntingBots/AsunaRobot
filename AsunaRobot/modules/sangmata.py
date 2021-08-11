# Copyright (C) 2021 AsunaRobot
# made by @The_Ghost_Hunter on Telegram.
# github account : https://github.com/HuntingBots/
# This file is part of AsunaRobot (Telegram Bot)


import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from AsunaRobot.events import register as Asuna
from AsunaRobot import telethn as tbot


@Asuna(pattern="^/sg ?(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```reply to text message```")
       return
    chat = "@SangMataInfo_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Processing Request```")
    
        async with tbot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()

            except YouBlockedUserError: 
              await event.reply("```Please unblock @sangmatainfo_bot and try again```")
              return
          if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.edit(f"{response.message.message}")




__mod_name__ = "Sangmata"

__help__ = """
 ❍ sangmata *:* /sg - View user name history.
"""
__button__ = ""
__buttons__ = ""
