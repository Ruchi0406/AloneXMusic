import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from AloneXMusic import app  

photo = [
    "https://telegra.ph/file/ed48f8f3fb661ce01e1f7.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"📝 ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"____________________________________\n\n"
                f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                f"🍂 ᴄʜᴀᴛ ɪᴅ: {message.chat.id}\n"
                f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{message.chat.username}\n"
                f"🛰 ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                f"🤔 ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.mention}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"🌷 𝐇ᴇʟʟᴏ 𝐃ᴇᴀʀ {message.from_user.mention} 💘\n\n"
                f"➥ 𝐈 𝐀ᴍ ˹ 𝐕ᴇᴇɴᴀ ✘ 𝐌ᴜꜱɪᴄ ˼ ♪ 𝐏ʀᴇꜱᴇɴᴛ 𝐇ᴇʀᴇ 𝐓ᴏ 𝐖ᴇʟᴄᴏᴍᴇ 𝐘ᴏᴜ 𝐈ɴ 𝐎ᴜʀ 𝐆ʀᴏᴜᴘ {message.chat.title} \n\n"
                f"📌 𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ: {message.chat.title}\n"
                f"🔐 𝐂ʜᴀᴛ 𝐔.𝐍: @{message.chat.username}\n"
                f"💖 𝐔ʀ 𝐈d: {member.id}\n"
                f"✍️ 𝐔ʀ 𝐔.𝐍aмe: @{member.username}\n"
                f"👥 𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬 🎉"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
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
    await delete_welcome_message(chat.id, message.message_id)
