from bot.utils import not_subscribed
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant


@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**𝚂𝙾𝚁𝚁𝚈 𝙳𝚄𝙳𝙴, 𝚈𝙾𝚄 𝙲𝙰𝙽'𝚃 𝚄𝚂𝙴 𝙼𝙴!\n𝙸'𝙼 𝙰 𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙱𝙾𝚃 🤖\n𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝚃𝙷𝙸𝚂 𝙶𝚄𝚈, 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴!**",
       reply_markup=InlineKeyboardMarkup([
           [ InlineKeyboardButton(text="😬😈𝚂𝚃𝙰𝚁 𝙻𝙾𝚁𝙳😈😬", url='https://t.me/JOHN748')]
           ])
       )
