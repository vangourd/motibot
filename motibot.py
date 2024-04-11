#!/usr/bin/env python3

import discord
import os
import requests
from openai import OpenAI

# modules
from todoist import TDHandler
from config import Config


class Motibot:

    def __init__(self, c) -> None:
        self.config = c
    
    def check_in(self):
        t = TDHandler(self.config)
        report = t.get_report()
        print(self.openai_prompt(report).choices[0].message.content)


    # Mock function to process tasks and create a prompt for OpenAI
    def openai_prompt(self, report):
        prompt = f'''
        You are a tough no bullshit motivator reviewing project and tasks lists for the user. 

        Summarize current task status, note any accomplishments, and 
        make it clear what are the most important next actions.

        Ignore shared projects and menial recurring tasks unless they're 
        egregiously overdue.
        '''

        client = OpenAI(api_key=self.config.openai_api_key)

        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "system", "content": report}
            ],
        )
        return response


    # Mock function to send a message to Discord
    async def send_message_to_discord(self, message):
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
    m.check_in()

if __name__ == '__main__':
    main()