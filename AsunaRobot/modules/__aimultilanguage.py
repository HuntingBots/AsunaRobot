import asyncio
import aiohttp
import emoji
import requests
import re
from AsunaRobot.helper_extra.aichat import add_chat, get_session, remove_chat
from AsunaRobot.pyrogramee.pluginshelper import admins_only, edit_or_reply
from AsunaRobot import pbot as asuna

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from google_trans_new import google_translator
url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

translator = google_translator()

BOT_ID = 1746875218

def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)

#Chatbot Modules By  @InukaAsith

en_chats = []

@asuna.on_message(
    filters.text & filters.reply & ~filters.bot & ~filters.via_bot & ~filters.forwarded,
    group=2,
)
async def asuna(client, message):
    if message.reply_to_message.from_user.id != BOT_ID:
        message.continue_propagation()
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        aura = msg
        aura = aura.replace("asuna", "Aco")
        aura = aura.replace("Asuna", "Aco")
        querystring = {
            "bid": "178",
            "key": "sX5A2PcYZbsN5EY6",
            "uid": "mashape",
            "msg": {test},
        }
        headers = {
            "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("Aco", "Asuna")
        result = result.replace("Asuna", "@My_Asuna_Robot")
        result = result.replace("Hi~", "Hello Friend I Am @My_Asuna_Robot")
        result = result.replace("My dear great botmaster, AsunaRobot Team.", "Made By @The_Ghost_Hunter")
        result = result.replace("Have the control right.", "My Father Is @The_Ghost_Hunter")
        result = result.replace("I was created by AsunaRobot Team.", "I was created by  @AsunaRobotSupport Team.")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        red = result
        try:
            await Asuna.send_chat_action(message.chat.id, "typing")
            await message.reply_text(red)
        except CFError as e:
            print(e)
    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if (
            [(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
        ):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            lan = translator.detect(rm)
        aura = rm
        if not "en" in lan and not lan == "":
            aura = translator.translate(aura, lang_tgt="en")

        aura = aura.replace("asuna", "Aco")
        aura = aura.replace("Asuna", "Aco")
        querystring = {
            "bid": "178",
            "key": "sX5A2PcYZbsN5EY6",
            "uid": "mashape",
            "msg": {aura},
        }
        headers = {
            "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("Aco", "Asuna")
        result = result.replace("Asuna", "@My_Asuna_Robot")
        result = result.replace("Hi~", "Hello Friend I Am @My_Asuna_Robot")
        result = result.replace("My dear great botmaster, AsunaRobot Team.", "Made By @The_Ghost_Hunter")
        result = result.replace("Have the control right.", "My Father Is @The_Ghost_Hunter")
        result = result.replace("I was created by AsunaRobot Team.", "I was created by @AsunaRobotSupport Team.")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        red = result
        if not "en" in lan and not lan == "":
            pro = translator.translate(red, lang_tgt=lan[0])
        try:
            await Asuna.send_chat_action(message.chat.id, "typing")
            await message.reply_text(red)
        except CFError as e:
            print(e)



@asuna.on_message(filters.text & filters.private & ~filters.reply & ~filters.bot)
async def redaura(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        lan = translator.detect(rm)
    aura = rm
    if not "en" in lan and not lan == "":
        aura = translator.translate(aura, lang_tgt="en")

   
    aura = aura.replace("asuna", "Aco")
    aura = aura.replace("Asuna", "Aco")
    querystring = {
        "bid": "178",
        "key": "sX5A2PcYZbsN5EY6",
        "uid": "mashape",
        "msg": {aura},
    }
    headers = {
        "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("Aco", "Asuna")
    result = result.replace("Asuna", "@My_Asuna_Robot")
    result = result.replace("Hi~", "Hello Friend I Am @My_Asuna_Robot")
    result = result.replace("My dear great botmaster, AsunaRobot Team.", "Made By @madepranav")
    result = result.replace("Have the control right.", "My Father Is @The_Ghost_Hunter")
    result = result.replace("I was created by AsunaRobot Team.", "I was created by @My_Asuna_Robot Team.")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    red = result
    if not "en" in lan and not lan == "":
        red = translator.translate(red, lang_tgt=lan[0])
    try:
        await LYCIA.send_chat_action(message.chat.id, "typing")
        await message.reply_text(red)
    except CFError as e:
        print(e)


@LYCIA.on_message(
    filters.regex("Asuna|asuna|ASUNA")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel
)
async def redaura(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        lan = translator.detect(rm)
    aura = rm
    if not "en" in lan and not lan == "":
        aura = translator.translate(aura, lang_tgt="en")


    aura = aura.replace("asuna", "Aco")
    aura = aura.replace("Aauna", "Aco")
    querystring = {
        "bid": "178",
        "key": "sX5A2PcYZbsN5EY6",
        "uid": "mashape",
        "msg": {aura},
    }
    headers = {
        "x-rapidapi-key": "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("Aco", "Asuna")
    result = result.replace("Asuna", "@My_Asuna_Robot")
    result = result.replace("Hi~", "Hello Friend I Am @My_Asuna_Robot")
    result = result.replace("My dear great botmaster, AsunaRobot Team.", "Made By @madepranav")
    result = result.replace("Have the control right.", "My Father Is @The_Ghost_Hunter")
    result = result.replace("I was created by Lyciabot Team.", "I was created by @@AsunaRobotSupport Team.")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    pro = result
    if not "en" in lan and not lan == "":
        red = translator.translate(red, lang_tgt=lan[0])
    try:
        await Asuna.send_chat_action(message.chat.id, "typing")
        await message.reply_text(red)
    except CFError as e:
        print(e)
        
       
