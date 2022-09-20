import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["kickall", "banall"], [".", "!"]))
async def kickall(client: Client, message: Message):
    await message.reply_text("kick all chat members!")
    member = client.get_chat_members(message.chat.id)
    async for alls in member:
        try:
            await client.ban_chat_member(message.chat.id, alls.user.id, 0)
        except:
            pass


@Client.on_message(filters.command('kickall_hide', ["."]))
async def kickall_hide(client: Client, message: Message):
    await message.delete()
    member = client.get_chat_members(message.chat.id)
    async for alls in member:
        try:
            await client.ban_chat_member(message.chat.id, alls.user.id, 0)
        except:
            pass


@Client.on_message(filters.command("kickall_withbot", ["."]))
async def tagall(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    icm = client.get_chat_members(chat_id)
    async for member in icm:
        string = f"/ban {member.user.mention}\n"
        await client.send_message(chat_id, text=string)
