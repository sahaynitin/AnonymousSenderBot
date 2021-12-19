from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Data(object):



    START_TEXT = """
Hey {} 

I am Anonymous Sender Bot

I can help you to remove caption and Tags by hiding your Username

Use Help Command to Know How to Use me

Made With 💕 By @Tellybots_4u
"""
    HELP_TEXT = """
Recommended
➠ Just Send Anythings To Get Started

Recommended
➠ If You Want To Delete Caption Click on Remove Caption Button

Made With 💕 By @Tellybots_4u
"""
    ABOUT_TEXT = """
 **🤖 Bot :** Anonymous Sender\n
 **👲 Developer :** [Tellybots_4u](https://telegram.me/tellybots_4u)\n
 **👥 Channel :** [Tellybots_4u](https://telegram.me/tellybots_4u)\n
 **❄️ Credits :** Everyone in this journey\n
 **🍴 Source :** [Click here](https://t.me/tellybots_digital)\n
 **📝 Language :** [Python3](https://python.org)\n
 **📚 Library :** [Pyrogram v1.2.0](https://pyrogram.org)\n
 **🌟 Server :** [Heroku](https://heroku.com)\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help')
        ]]
    )
    HELP_BUTTONS = [[
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('🏡 Home', callback_data='home')
        ]]
    )
    ABOUT_BUTTONS = [[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('🏡 Home', callback_data='home')
        ]]
    )

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Remove Caption Button
    remove_button = [InlineKeyboardButton("� Remove Caption �", callback_data="remove")]

    # Add caption button
    add_button = [InlineKeyboardButton("💬 Re-Add Caption 💬", callback_data="add")]


