import logging
import time
from telethon import TelegramClient, events, sync

# Set up logging
logging.basicConfig(level=logging.WARNING)

# Set up the Telegram API
api_id = 'YOUR_API_ID_HERE'
api_hash = 'YOUR_API_HASH_HERE'
client = TelegramClient('session_name', api_id, api_hash)

# Set up the group chat and messages to send
group_chat_id = 'YOUR_GROUP_CHAT_ID_HERE'
messages = [
    'Hello, everyone!',
    'How is everyone doing?',
    'Just checking in!',
]

# Set up the time delay for auto-replying to personal messages
reply_delay = 10  # seconds


@client.on(events.NewMessage(chats=group_chat_id))
async def auto_message(event):
    """Sends messages to the group chat at a given time period."""
    while True:
        for message in messages:
            await client.send_message(group_chat_id, message)
            time.sleep(60*60)  # send messages every hour


@client.on(events.NewMessage())
async def auto_reply(event):
    """Replies to personal messages at a given time delay."""
    time.sleep(reply_delay)
    await event.respond('Sorry, I am a bot and cannot reply to personal messages. Please contact the group chat.')


# Start the client
client.start()
client.run_until_disconnected()
