from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# About Message
@Client.on_message(filters.private & filters.command(["about"]))
async def about(_, msg):
	await msg.reply(text=Data.ABOUT_TEXT, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(Data.ABOUT_BUTTONS))
