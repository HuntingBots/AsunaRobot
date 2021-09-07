# Copyright (C) 2021 AsunaRobot
# made by @The_Ghost_Hunter on Telegram.
# github account : https://github.com/HuntingBots/
# This file is part of AsunaRobot (Telegram Bot)

import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from AsunaRobot import telethn
from AsunaRobot.events import register as asuna


@asuna(pattern="^/tagall ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Hi Friends I'm Asuna I Call To All Of You"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


@asuna(pattern="^/users ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Users : "
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


__mod_name__ = "Tagger"
__help__ = """
- /tagall : Tag everyone in a chat
"""
