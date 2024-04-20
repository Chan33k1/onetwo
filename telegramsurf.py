from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty

# Replace with your own values
api_id = 123456
api_hash = 'YOUR_API_HASH'
phone_number = '+1234567890'

# Create a Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Connect to the client
client.connect()

# Check if the user is already authorized
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    try:
        client.sign_in(phone_number, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=input('Enter the 2FA password: '))

# Search for channels or chats with keywords
search_query = input('Enter the search query: ')
search_results = client(SearchRequest(
    peer=InputMessagesFilterEmpty(),
    q=search_query,
    limit=10
))

# Print the search results
for result in search_results.results:
    print(result.title, '-', result.id)

# Disconnect the client
client.disconnect()