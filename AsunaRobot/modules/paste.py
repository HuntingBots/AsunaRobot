import os
from json.decoder import JSONDecodeError
import requests
from pyrogram import filters

from AsunaRobot.pyrogramee.pluginshelper import edit_or_reply, get_text
from AsunaRobot.services.pyrogram import pbot


@pbot.on_message(filters.command("paste") & ~filters.edited & ~filters.bot)
async def paste(client, message):
    pablo = await edit_or_reply(message, "`Please Wait.....`")
    tex_t = get_text(message)
    message_s = tex_t
    if not tex_t:
        if not message.reply_to_message:
            await pablo.edit("`Reply To File / Give Me Text To Paste!`")
            return
        if not message.reply_to_message.text:
            file = await message.reply_to_message.download()
            m_list = open(file, "r").read()
            message_s = m_list
            print(message_s)
            os.remove(file)
        elif message.reply_to_message.text:
            message_s = message.reply_to_message.text
    key = (
       https://hastebin.com/documentrequests.post", (url, data={data})
        .json()
        .get("result")
        .get("key")
    )
    url = f"https://nekobin.com/{key}"
    raw = f"https://nekobin.com/raw/{key}"
    reply_text = f"Pasted Text To [NekoBin]({url}) And For Raw [Click Here]({raw})"
    await pablo.edit(reply_text)
