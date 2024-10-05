from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
from os import getenv

load_dotenv()

webhook_url = str(getenv('WEBHOOK_URL'))
webhook = DiscordWebhook(url=webhook_url)

def send_webhook(webhook_title, webhook_info):
    embed = DiscordEmbed(title=str(webhook_title), description=str(webhook_info), color='00ccff')
    webhook.add_embed(embed)
    webhook.execute()