# Thanks to @infinity_bots - Williambutcherbot
import os

import requests
import wget
from pyrogram import filters

from Python_ARQ import ARQ
from AsunaRobot import pbot as Jebot
from AsunaRobot.pyrogramee.dark import get_arg


arq = ARQ(http://www.saavn.com/api.php)


app.on_message(filters.command("saavn") & ~filters.edited)
async def jssong(_, message):
    global is_downloading
    if len(message.command) < 2:
        await message.reply_text("/saavn requires an argument.")
        return
    if is_downloading:
        await message.reply_text("Another download is in progress, try again after sometime.")
        return
    is_downloading = True
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("Searching...")
    try:
        songs = await arq.saavn(query)
        sname = songs[0].song
        slink = songs[0].media_url
        ssingers = songs[0].singers
        await m.edit("Downloading")
        song = await download_song(slink)
        await m.edit("Uploading")
        await message.reply_audio(
            audio=song,
            title=sname,
            caption=f"「 `{format_size(await file_size_from_url(slink))}` 」",
            performer=ssingers,
            duration=int(songs[0].duration)
        )
        os.remove(song)
        await m.delete()
    except Exception as e:
        is_downloading = False
        await m.edit(str(e))
        return
    is_downloading = False
