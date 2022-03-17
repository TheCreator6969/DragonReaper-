import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot
from telegram.ext import CallbackContext, CallbackQueryHandler

PHOTO = "https://telegra.ph/file/060ea554c591fc5b0b878.jpg"


async def awake(event):
    TEXT = "¤¤ 𝐇𝐞𝐲 𝐌𝐚𝐞𝐬𝐭𝐫𝐨, 𝐈'𝐦 𝐔𝐧𝐦𝐞𝐢! ¤¤\n\n"
    TEXT += f"ø 𝐘𝐞𝐚𝐡!! 𝐃𝐨𝐧'𝐭 𝐛𝐨𝐭𝐡𝐞𝐫 𝐚𝐛𝐨𝐮𝐭 𝐦𝐲 𝐬𝐩𝐞𝐞𝐝 𝐟𝐨𝐫 𝐧𝐨𝐰 ø\n\n"
    TEXT += f"ø 𝐔𝐍𝐌𝐄𝐈 : 𝐋𝐀𝐓𝐄𝐒𝐓 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 ø\n\n"
    TEXT += (
        f"ø 𝐌𝐲 𝐌𝐚𝐞𝐬𝐭𝐫𝐨 (𝐂𝐫𝐞𝐚𝐭𝐨𝐫) : [ 𝐒𝐡𝐨𝐭𝐨](http://t.me/yameteee_yamete_kudasai) ø\n\n"
    )
    TEXT += f"ø ᴀɴʏ ɪ𝓼𝓼ᴜᴇ𝓼 ᴄᴏɴᴛᴀᴄᴛ us ʜᴇʀᴇ : @unmei_support ø\n\n"
    TEXT += "♥ ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ♥ (っ◔◡◔)っ "
    BUTTON = [
        [
            Button.url("📢 Updates", "https://t.me/unmei_updates"),
            Button.url("🚑 Support", "https://t.me/unmei_support"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
