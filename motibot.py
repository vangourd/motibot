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
    
    def check_in(self) -> str:
        t = TDHandler(self.config)
        report = t.get_report()
        response = self.openai_prompt(report).choices[0].message.content
        return response


    # Mock function to process tasks and create a prompt for OpenAI
    def openai_prompt(self, report):
        prompt = f'''
        Below is a report of information. Analyze it and make a short
        and snarky comment in the form of a drill sergeant focusing on
        criticism and motivation.
        '''

        client = OpenAI(api_key=self.config.openai_api_key)

        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "system", "content": report}
            ],
            max_tokens=300
        )
        return response


# Main function flow
def main():
    c = Config()
    m = Motibot(c)
    response = m.check_in()
    d = DiscordBot(c, response)
    d.run()
    
    

if __name__ == '__main__':
    main()