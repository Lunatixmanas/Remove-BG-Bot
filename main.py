import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

REMOVEBG_API = os.environ.get("REMOVEBG_API", "")
UNSCREEN_API = os.environ.get("UNSCREEN_API", "")

Bot = Client(
    "Remove Background Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

START_TEXT = """
<b>𝗛𝗜 {}, 𝗜 𝗔𝗠 𝗔 𝗕𝗚 𝗥𝗘𝗠𝗢𝗩𝗘𝗥 𝗕𝗢𝗧 𝗜 𝗖𝗔𝗡 𝗘𝗔𝗦𝗜𝗟𝗬 𝗥𝗘𝗠𝗢𝗩𝗘 𝗕𝗔𝗖𝗞𝗚𝗥𝗢𝗨𝗡𝗗 𝗢𝗙 𝗧𝗛𝗘 𝗣𝗜𝗖𝗧𝗨𝗥𝗘𝗦</b>

<b>𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗔𝗡𝗗 𝗠𝗔𝗧𝗜𝗡𝗔𝗘𝗗 𝗕𝗬 @KOT_FREE_DE_LA_HOYA_OFF</b>"""
HELP_TEXT = """**More Help**

<b>- Jᴜsᴛ Sᴇɴᴅ Mᴇ ᴀ Pʜᴏᴛᴏ</b></b>
<b>- I Wɪʟʟ Dᴏᴡɴʟᴏᴀᴅ Iᴛ
<b>- I Wɪʟʟ Sᴇɴᴅ Tʜᴇ Pʜᴏᴛᴏ Wɪᴛʜᴏᴜᴛ Bᴀᴄᴋɢʀᴏᴜɴᴅ</b>

<b>𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗔𝗡𝗗 𝗠𝗔𝗧𝗜𝗡𝗔𝗘𝗗 𝗕𝗬 @KOT_FREE_DE_LA_HOYA_OFF</b>"""
ABOUT_TEXT = """
╭──────[@KOT_BOTS]───────〄
│
├ Nᴀᴍᴇ : <a href='https://t.me/KOT_BG_REMOVER_BOT'>Kᴏᴛ Bɢ Rᴇᴍᴏᴠᴇʀ Bᴏᴛ</a>
│
├ Sᴇʀᴠᴇʀ : <a href='https://heroku.com/'>Hᴇʀᴏᴋᴜ</a>
│ 
├ Lᴀɴɢᴜᴀɢᴇ : <a href='https://docs.pyrogram.org/'>Pʏᴛʜᴏɴ 3.9.6</a>
│
├ Vᴇʀꜱɪᴏɴ : <a href='https://t.me/KOT_BG_REMOVER_BOT</a>
│
├ Fʀᴀᴍᴇᴡᴏʀᴋ : <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ 1.2.9</a>
│
├ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/KOT_FREE_DE_LA_HOYA_OFF'>✯°• Kᴏᴛ Fʀᴇᴇ Dᴇ Lᴀ Hᴏʏᴀ Oғғ °•✯ | ✪ Bᴏᴛs CʀᴇᴀᴛᴏR ✪</a>
│
├ Pᴏᴡᴇʀᴇᴅ Bʏ : <a href='https://t.me/KOT_LINKS_TEAM'>Kᴏᴛ Lɪɴᴋs Tᴇᴀᴍ</a>
│
├ Uᴘᴅᴀᴛᴇᴅ Oɴ : [ 19.1.2022 ] 03.00 PM"""
START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('BOTS CHANNEL', url='https://telegram.me/KOT_BOTS'),
            InlineKeyboardButton('SUPPORT GROUP', url='https://telegram.me/KOT_REPORS')
        ],
        [
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)
HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)
ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)
ERROR_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)
BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Join Updates Channel', url='https://telegram.me/KOT_BOTS')
        ]
    ]
)


@Bot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await start(bot, update, cb=True)
    elif update.data == "help":
        await help(bot, update, cb=True)
    elif update.data == "about":
        await about(bot, update, cb=True)
    else:
        await update.message.delete()


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update, cb=False):
    text=START_TEXT.format(update.from_user.mention)
    if cb:
        await update.message.edit_text(
            text=text,
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS,
            quote=True
        )


@Bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update, cb=False):
    if cb:
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )


@Bot.on_message(filters.private & filters.command(["about"]))
async def about(bot, update, cb=False):
    if cb:
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )


@Bot.on_message(filters.private & (filters.photo | filters.video | filters.document))
async def remove_background(bot, update):
    if not REMOVEBG_API:
        await update.reply_text(
            text="Error :- Remove BG Api is error",
            quote=True,
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )
        return
    await update.reply_chat_action("typing")
    message = await update.reply_text(
        text="Processing",
        quote=True,
        disable_web_page_preview=True
    )
    try:
        new_file_name = f"./{str(update.from_user.id)}"
        if update.photo or (
            update.document and "image" in update.document.mime_type
        ):
            new_file_name += ".png"
            file = await update.download()
            await message.edit_text(
                text="Photo downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            new_document = removebg_image(file)
        elif update.video or (
            update.document and "video" in update.document.mime_type
        ):
            new_file_name += ".webm"
            file = await update.download()
            await message.edit_text(
                text="Video downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            new_document = removebg_video(file)
        else:
            await message.edit_text(
                text="Media not supported",
                disable_web_page_preview=True,
                reply_markup=ERROR_BUTTONS
            )
        try:
            os.remove(file)
        except:
            pass
    except Exception as error:
        await message.edit_text(
            text=error,
            disable_web_page_preview=True
        )
    try:
        with open(new_file_name, "wb") as file:
            file.write(new_document.content)
        await update.reply_chat_action("upload_document")
    except Exception as error:
        await message.edit_text(
           text=error,
           reply_markup=ERROR_BUTTONS
        )
        return
    try:
        await update.reply_document(
            document=new_file_name,
            quote=True
        )
        try:
            os.remove(file)
        except:
            pass
    except Exception as error:
        await message.edit_text(
            text=f"Error:- `{error}`",
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )


def removebg_image(file):
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": open(file, "rb")},
        data={"size": "auto"},
        headers={"X-Api-Key": REMOVEBG_API}
    )


def removebg_video(file):
    return requests.post(
        "https://api.unscreen.com/v1.0/videos",
        files={"video_file": open(file, "rb")},
        headers={"X-Api-Key": UNSCREEN_API}
    )


Bot.run()
