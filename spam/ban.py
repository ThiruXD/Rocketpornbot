from pyrogram import Client, filters
import asyncio
from pyrogram.types import Message
from spam import user
import logging
from pyrogram.types import *

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.command("banall") & filters.group)
def NewChat(user,message):
    logging.info("new chat {}".format(message.chat.id))
    logging.info("getting memebers from {}".format(message.chat.id))
    a= user.iter_chat_members(message.chat.id)
    for i in a:
        try:
            user.kick_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            logging.info("kicked {} from {}".format(i.user.id,message.chat.id))
        except Exception:
            logging.info(" failed to kicked {} from {}".format(i.user.id,message.chat.id))
            
    logging.info("process completed")
