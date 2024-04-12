import discord
from config import Config
import discord


class DiscordBot:

    def __init__(self, c: Config, m: str):
        self.bot_token = c.discord_bot_token
        self.discord_target_user = c.discord_target_user
        self.client = discord.Client(intents=discord.Intents.default())
        self.message = m

        @self.client.event
        async def on_ready():
            print(f"Logged in as {self.client.user}")
            user = await self.client.fetch_user(self.discord_target_user)
            await user.send(m)
            await self.client.close()  # Close after sending message, or remove if the bot should stay online

        
    def run(self):
        self.client.run(self.bot_token)