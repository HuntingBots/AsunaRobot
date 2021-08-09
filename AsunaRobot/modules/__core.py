# Copyright (C) 2021 AsunaRobot
# made by @The_Ghost_Hunter on Telegram.
# github account : https://github.com/HuntingBots/
# This file is part of AsunaRobot (Telegram Bot)


import asyncio
import traceback
import os
from datetime import datetime
from AsunaRobot.services.telethon import tbot 
from AsunaRobot.events import register as Asuna


DELETE_TIMEOUT = 5


# Send_Module

@Asuna(pattern="^/send ?(.*)")
async def Prof(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    the_plugin_file = "./AsunaRobot/modules/{}.py".format(input_str)
    start = datetime.now()
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        force_document=True,
        allow_cache=False,
        reply_to=message_id
    )
    end = datetime.now()
    time_taken_in_ms = (end - start).seconds
    await event.edit("Uploaded {} in {} seconds".format(input_str, time_taken_in_ms))
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()

# Install_Module

@Asuna(pattern="^/install ?(.*)")  # pylint:disable=E0602
async def Prof(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(),
                tbot.n_module_path  # pylint:disable=E0602
            )
            if "(" not in downloaded_file_name:
                tbot.load_plugin_from_file(downloaded_file_name)  # pylint:disable=E0602
                await event.edit("Installed module `{}`".format(os.path.basename(downloaded_file_name)))
            else: 
                os.remove(downloaded_file_name)
                await event.edit("Errors! Cannot install this module.")
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()
