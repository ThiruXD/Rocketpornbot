import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from spam.decorators import sudo_users_only

@Client.on_mes"hi"], [".", "/", "!", "`"]))
@sudo_users_only
async def banall(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    icm = client.get_chat_members(chat_id)
    async for member in icm:
        string = f"/ban {member.user.mention}\n"
        await client.s text=string)
