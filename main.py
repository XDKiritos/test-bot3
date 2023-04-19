import logging
import time
from telethon import TelegramClient, events, sync

# Set up logging
logging.basicConfig(level=logging.WARNING)

# Set up the Telegram API
api_id = '25224776'
api_hash = '50ce92629342c68eff57bcbbf43c8047'
client = TelegramClient('1BVtsOG4Bu2f6CnW0GJU7WvNd_HjD9HjM_GMr7Q92ko1YIyRO-X5msFPKh6RYcSJzA5CNAxiKVQtF1Wgt5v_cLqibMorjJ-6sxR4k20jRd51j-pIjfIQk9z3RWtdrtZFwUUlJQPzueS_LuuiDfrbNBKJAxN7ZMMLEkVbUVlt8gIpG_wn5M8hwgMmEB9EHsMANWoJqlzr6uNIq7UzFZJ1e4irEQMpwgnNHjxNdHDyzWb1DEya9htWz-t3InutCcNdXdL8KjL7oQiZtOqbm9SX2BEncAAMRwAWEn1yQFOBE8_WmR9M-GmOVB-XQFT0mrFtDJpIvSoTrbWNomcQCnHQ0M_bB2xJ5mWg=', api_id, api_hash)

# Set up the group chat and messages to send
group_chat_id = '-1001798503017'
messages = [
    'I want a boy for friends with benefits anyone interested please dm me',
    'Real meet available 🥰🫶',
    'Dm me for free fun guys 💋💋',
]

# Set up the time delay for auto-replying to personal messages
reply_delay = 5  # seconds


@client.on(events.NewMessage(chats=group_chat_id))
async def auto_message(event):
    """Sends messages to the group chat at a given time period."""
    while True:
        for message in messages:
            await client.send_message(group_chat_id, message)
            time.sleep(20)  # send messages every 20 sec


@client.on(events.NewMessage())
async def auto_reply(event):
    """Replies to personal messages at a given time delay."""
    time.sleep(reply_delay)
    await event.respond('Hello friends mumbai, pune, goa, chennai, hyderabad, Bengaluru, Kolkata call girls free service 🎈 Jaldi se page open karke apna slot book karlo bilkul free hai koi payment karne ki jarurat nahi hai 👇👇👇👇👇👇 \n\n1 minute nud*** video calling 👇👇👇👇👇👇 \n\nhttps://bit.ly/3IqPuNt \n\nhttps://bit.ly/3IqPuNt \n\nSouth Indian girl sexxxx chatting 👇👇👇👇 \n\nhttps://bit.ly/3l5Tg7c \n\nhttps://bit.ly/3l5Tg7c')


# Start the client
client.start()
client.run_until_disconnected()
