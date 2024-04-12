#!/usr/bin/env python3

import chatbot
import os
import requests
import discord
import asyncio
from openai import OpenAI

# modules
from todoist import TDHandler
from config import Config
from chatbot import DiscordBot


class Motibot:

    def __init__(self, c) -> None:
        self.config = c
    
    async def check_in(self):
        t = TDHandler(self.config)
        report = t.get_report()
        response = self.openai_prompt(report).choices[0].message.content
        d = DiscordBot(self.config)
        await d.send_message_to_discord(
            message=response,
        )


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


# Main function flow
async def main():
    c = Config()
    m = Motibot(c)
    await m.check_in()

if __name__ == '__main__':
    asyncio.run(main())