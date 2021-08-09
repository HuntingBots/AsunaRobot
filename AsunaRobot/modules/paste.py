# recoded by @The_Ghost_Hunter, @My_Asuna_Robot on Telegram

import asyncio
import os
import re

import aiofiles
from pyrogram import filters
from AsunaRobot.modules.sql_extended.paste import paste 
from AsunaRobot import pbot as app

pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")


async def isPreviewUp(preview: str) -> bool:
    for _ in range(7):
        try:
            async with head(preview, timeout=2) as resp:
                status = resp.status
                size = resp.content_length
        except asyncio.exceptions.TimeoutError:
            return False
        if status == 404 or (status == 200 and size == 0):
            await asyncio.sleep(0.4)
        else:
            return True if status == 200 else False
    return False


@app.on_message(filters.command("paste") & ~filters.edited)
async def paste_func(_, message):
    if message.reply_to_message:
        m = await message.reply_text("Pasting...")
        if message.reply_to_message.text:
            content = str(message.reply_to_message.text)

        elif message.reply_to_message.document:
            document = message.reply_to_message.document
            if document.file_size > 1048576:
                return await m.edit("You can only paste files smaller than 1MB.")
            if not pattern.search(document.mime_type):
                return await m.edit("Only text files can be pasted.")
            doc = await message.reply_to_message.download()
            async with aiofiles.open(doc, mode="r") as f:
                content = await f.read()
            os.remove(doc)
        link = await paste(content)
        await m.edit(link)
    else:
        await message.reply_text("Reply To A Message With /paste")
