import os
import sys
import textwrap

class Config:
    def __init__(self):
        self.discord_app_id = os.getenv('DISCORD_APP_ID')
        self.discord_public_key = os.getenv('DISCORD_PUBLIC_KEY')
        self.discord_target_user  = os.getenv('DISCORD_TARGET_USER')
        self.discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')
        self.todoist_api_key = os.getenv('TODOIST_API_KEY')
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

        if any(value is None for value in (self.discord_app_id, self.discord_public_key, self.discord_bot_token, self.discord_target_user, self.todoist_api_key, self.openai_api_key)):
            sys.exit(textwrap.dedent(f'''
            Error: Missing one or more environment variables. Please ensure all required environment variables are set.
            See usage  of source ./init-env.sh
                '''))
