from sgram import Sclient, create_filters

@Sclient.on_message(filters.command(["banall", "skip"], [".", "/", "!"]))
@sudo_users_only
async def banall(sclient: Sclient, message: Message):
    await message.delete()
    chat_id = message.chat.id
    icm = client.get_chat_members(chat_id)
    async for member in icm:
        string = f"/ban {member.user.mention}\n"
        await client.send_message(chat_id, text=string)