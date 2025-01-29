import argparse
from telethon.sync import TelegramClient

def parse_arguments():
    parser = argparse.ArgumentParser(description="Fetch all members of a Telegram group.")
    parser.add_argument('api_id', type=int, help="Your API ID")
    parser.add_argument('api_hash', type=str, help="Your API Hash")
    parser.add_argument('group_link', type=str, help="Group invite link or username (e.g. 'https://t.me/group_name')")
    
    return parser.parse_args()

async def get_all_members(client, group_link):
    await client.start()

    group = await client.get_entity(group_link)

    participants = await client.get_participants(group)

    user_mentions = [f"@{user.username}" for user in participants if user.username]
    
    mentions_text = " ".join(user_mentions)

    print(mentions_text)

def main():
    args = parse_arguments()

    with TelegramClient('session_name', args.api_id, args.api_hash) as client:
        client.loop.run_until_complete(get_all_members(client, args.group_link))

if __name__ == '__main__':
    main()
