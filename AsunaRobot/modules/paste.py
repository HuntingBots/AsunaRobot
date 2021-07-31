import logging
import os
from datetime import datetime
import requests
TEMP_DOWNLOAD_DIRECTORY = "Paste-File/"
from pyrogram.types import CallbackQuery
from AsunaRobot import LOGGER
from AsunaRobot.events import register
from AsunaRobot import telethn as tbot

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)


def progress(current, total):
    LOGGER.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )


@register(pattern="^/fpaste ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    datetime.now()
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    input_str = event.pattern_match.group(1)
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await tbot.download_media(
                previous_message,
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=progress,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                # message += m.decode("UTF-8") + "\r\n"
                message += m.decode("UTF-8")
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        await event.edit("Give Some Text Or File To Paste")
    py_file = ""
    name = "ok"
    if previous_message.media:
        name = await tbot.download_media(
            previous_message, TEMP_DOWNLOAD_DIRECTORY, progress_callback=progress
        )
    downloaded_file_name = name
    if downloaded_file_name.endswith(".py"):
        py_file += ".py"
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}{py_file}"
        raw = f"https://nekobin.com/raw/{key}{py_file}"
        reply_text = f"Pasted Text [neko]({url})\n Raw ? [View Raw]({raw})"
        await event.edit(reply_text)
    else:
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        raw = f"https://nekobin.com/raw/{key}"
        reply_text = f"Pasted Text [neko]({url})\n Raw ? [View Raw]({raw})"
        await event.edit(reply_text)
1
import logging
2
import os
3
from datetime import datetime
4
import requests
5
TEMP_DOWNLOAD_DIRECTORY = "Paste-File/"
6
from pyrogram.types import CallbackQuery
7
from AsunaRobot import LOGGER
8
from AsunaRobot.events import register
9
from AsunaRobot import telethn as tbot
10
​
11
logging.basicConfig(
12
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
13
)
14
​
15
​
16
def progress(current, total):
17
    LOGGER.info(
18
        "Downloaded {} of {}\nCompleted {}".format(
19
            current, total, (current / total) * 100
20
        )
21
    )
22
​
23
​
24
@register(pattern="^/fpaste ?(.*)")
25
async def _(event):
26
    if event.fwd_from:
27
        return
28
    datetime.now()
29
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
30
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
31
    input_str = event.pattern_match.group(1)
32
    if input_str:
33
        message = input_str
34
    elif event.reply_to_msg_id:
35
        previous_message = await event.get_reply_message()
36
        if previous_message.media:
37
            downloaded_file_name = await tbot.download_media(
38
                previous_message,
39
                TEMP_DOWNLOAD_DIRECTORY,
40
                progress_callback=progress,
41
            )
42
            m_list = None
43
            with open(downloaded_file_name, "rb") as fd:
44
                m_list = fd.readlines()
45
            message = ""
46
            for m in m_list:
47
                # message += m.decode("UTF-8") + "\r\n"
48
                message += m.decode("UTF-8")
49
            os.remove(downloaded_file_name)
50
        else:
51
            message = previous_message.message
52
    else:
53
        await event.edit("Give Some Text Or File To Paste")
54
    py_file = ""
55
    name = "ok"
56
    if previous_message.media:
57
        name = await tbot.download_media(
58
            previous_message, TEMP_DOWNLOAD_DIRECTORY, progress_callback=progress
59
        )
60
    downloaded_file_name = name
61
    if downloaded_file_name.endswith(".py"):
62
        py_file += ".py"
63
        data = message
64
        key = (
65
            requests.post("https://nekobin.com/api/documents", json={"content": data})
66
            .json()
67
            .get("result")
68
            .get("key")
69
        )
70
        url = f"https://nekobin.com/{key}{py_file}"
71
        raw = f"https://nekobin.com/raw/{key}{py_file}"
72
        reply_text = f"Pasted Text [neko]({url})\n Raw ? [View Raw]({raw})"
73
        await event.edit(reply_text)
74
    else:
75
        data = message
76
        key = (
77
            requests.post("https://nekobin.com/api/documents", json={"content": data})
78
            .json()
79
            .get("result")
80
            .get("key")
81
        )
82
        url = f"https://nekobin.com/{key}"
83
        raw = f"https://nekobin.com/raw/{key}"
84
        reply_text = f"Pasted Text [neko]({url})\n Raw ? [View Raw]({raw})"
