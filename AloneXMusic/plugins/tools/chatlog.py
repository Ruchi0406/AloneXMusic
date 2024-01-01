import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import LOGGER_ID as LOG_GROUP_ID
from AloneXMusic import app  

photo = [
    "https://telegra.ph/file/ed48f8f3fb661ce01e1f7.jpg",
]

async def send_welcome_message(chat_id, user_mention, chat_title, username, user_id, member_username, count):
    welcome_msg = (
        f"🌷 𝐇ᴇʟʟᴏ 𝐃ᴇᴀʀ {user_mention} 💘\n\n"
        f"➥ 𝐈 𝐀ᴍ ˹ 𝐕ᴇᴇɴᴀ ✘ 𝐌ᴜꜱɪᴄ ˼ ♪ 𝐏ʀᴇꜱᴇɴᴛ 𝐇ᴇʀᴇ 𝐓ᴏ 𝐖ᴇʟᴄᴏᴍᴇ 𝐘ᴏᴜ 𝐈ɴ 𝐎ᴜʀ 𝐆ʀᴏᴜᴘ {chat_title} \n\n"
        f"📌 𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ: {chat_title}\n"
        f"🔐 𝐂ʜᴀᴛ 𝐔.𝐍: @{username}\n"
        f"💖 𝐔ʀ 𝐈d: {user_id}\n"
        f"✍️ 𝐔ʀ 𝐔.𝐍aмe: @{member_username}\n"
        f"👥 𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬 🎉"
    )
    message = await app.send_photo(chat_id, photo=random.choice(photo), caption=welcome_msg, reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(f"🥺 𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ 🥺", url=f"https://t.me/{app.username}?startgroup=true")]
    ]))
    return message.message_id

async def delete_welcome_message(chat_id, message_id):
    try:
        await app.delete_messages(chat_id, message_id)
    except Exception as e:
        print(f"Error deleting welcome message: {e}")

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    user_mention = message.from_user.mention
    chat_title = message.chat.title
    username = message.chat.username
    user_id = message.from_user.id
    member_username = message.from_user.username
    count = await app.get_chat_members_count(chat.id)

    # Send welcome message
    welcome_message_id = await send_welcome_message(chat.id, user_mention, chat_title, username, user_id, member_username, count)

    # Delete old user's welcome message
    try:
        await delete_welcome_message(chat.id, message.message_id)
    except Exception as e:
        print(f"Error deleting old welcome message: {e}")
