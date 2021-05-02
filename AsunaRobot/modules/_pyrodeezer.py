# Thanks to @infinity_bots - Williambutcherbot
import os

import requests
import wget
from pyrogram import filters

from AsunaRobot import pbot as Jebot
from AsunaRobot.pyrogramee.dark import get_arg

@App.on_message(filters.command("deezer") & ~filters.edited)

async def deezsong(_, message):
    global is_downloading
    if len(message.command) < 2:
        await message.reply_text("/deezer requires an argument.")
        return
    if is_downloading:
        await message.reply_text("Another download is in progress, try again after sometime.")
        return
    is_downloading = True
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("Searching...")
    try:
        songs = await arq.deezer(query, 1)
        title = songs[0].title
        url = songs[0].url
        artist = songs[0].artist
        await m.edit("Downloading")
        song = await download_song(url)
        await m.edit("Uploading")
        await message.reply_audio(
            audio=song,
            title=title,
            performer=artist,
            duration=songs[0].duration,
            caption=f"「 `{format_size(await file_size_from_url(url))}` 」")
        os.remove(song)
        await m.delete()
    except Exception as e:
        is_downloading = False
        await m.edit(str(e))
        return
    is_downloading = False
