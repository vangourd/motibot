#!/usr/bin/env python3

import discord
import os
import requests

# modules
from todoist import TDHandler
from ai import OpenAIHandler
from config import Config


class Motibot:

    def __init__(self, c) -> None:
        self.config = c

    # Mock function to fetch tasks from Todoist
    def todoist_report(self) -> list[str]:
        t = TDHandler(self.config)
        return t.get_report().split("\n")

# Mock function to process tasks and create a prompt for OpenAI
def create_openai_prompt(c: Config):
    print("Creating prompt for OpenAI based on tasks...")
    return "OpenAI prompt based on Todoist tasks"

# Mock function to get response from OpenAI
def get_openai_response(c: Config, prompt):
    # Replace with actual API call to OpenAI
    print("Getting response from OpenAI...")
    return "OpenAI response"

def CliQuickStart() -> TDHandler:
    c = Config()
    m = Motibot(c)
    t = TDHandler(c)
    return t


# Mock function to send a message to Discord
async def send_message_to_discord(c: Config, message):
    print("Sending message to Discord...")
    # Initialize Discord client and send message
    client = discord.Client()

    @client.event
    async def on_ready():
        # Logic to send message
        print(f'Logged in as {client.user}')
        # Replace 'channel_id' with actual Discord channel ID
        channel = client.get_channel(channel_id)
        await channel.send(message)
        await client.close()

    await client.start(discord_token)

# Main function flow
def main():
    c = Config()
    m = Motibot(c)
    for line in m.todoist_report():
        print(line)

if __name__ == '__main__':
    main()