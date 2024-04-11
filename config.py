import os

class Config:
    def __init__(self):
        self.discord_app_id = os.getenv('DISCORD_APP_ID')
        self.discord_public_key = os.getenv('DISCORD_PUBLIC_KEY')
        self.todoist_api_key = os.getenv('TODOIST_API_KEY')
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
