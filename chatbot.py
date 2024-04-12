import discord
from config import Config

class DiscordBot:

    def __init__(self, c: Config) -> None:
        self.bot_token = c.discord_bot_token
        self.discord_target_user = c.discord_target_user


    async def send_message_to_discord(self, message):
        print("Sending message to Discord...")
        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        try:
            await client.start(self.bot_token)
            user = client.fetch_user(self.discord_target_user)
            print(f"Found user {user}")
            await user.send(message)
            print("Message sent successfully")
        except Exception as e:
            print(f"Error sending message to  Discord {e}")
        finally:
            await client.close()
