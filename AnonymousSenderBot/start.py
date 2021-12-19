import os
if bool(os.environ.get("WEBHOOK", False)):
    from Config import Config
else:
    from Config import Config
from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await update.reply_text(
        text=Data.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Data.START_BUTTONS
    )
