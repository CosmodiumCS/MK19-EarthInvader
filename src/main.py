import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from dotenv import load_dotenv
import aiohttp
import nextcord
from nextcord.ext import commands
from src.webhook import send_webhook


load_dotenv()

def main():
    # allows privileged intents for monitoring members joining, roles editing, and role assignments
    intents = nextcord.Intents.default()
    intents.guilds = True
    intents.members = True
    intents.message_content = True
    activity = nextcord.Activity(
        type=nextcord.ActivityType.listening, name="/help"
    )

    bot = commands.Bot(
        command_prefix="/",
        intents=intents,
        activity=activity,
        owner_id="null",
    )

    bot.remove_command('help')
    bot.persistent_views_added = False

    @bot.event
    async def on_ready():
        print(f"USER: {bot.user} \nURL:", f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&scope=applications.commands%20bot")
        print(f"{bot.user} standing by on...")
        print('\n'.join(guild.name for guild in bot.guilds))
        print("Loading cogs...")

    # logging when the bot joins a server
    @bot.event
    async def on_guild_join(guild):
        send_webhook("Earth Invader Joined Server", f"""
        **Server:** {guild.name}
        **Shard ID:** {guild.shard_id}
        **Description:** {guild.description}
        **Owner Name:** {guild.owner} 
        **Owner ID:** {guild.owner_id}
        **Member Count:** {guild.member_count}
        **Region:** {guild.region}
        """)

    try:
        for filename in os.listdir('cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')
    except Exception:
        print("There was an error loading the bot's cogs.")

    async def startup():
        bot.session = aiohttp.ClientSession()

    bot.loop.create_task(startup())

    try:
        # run the bot
        bot.run(str(os.getenv('TOKEN')))
    except nextcord.errors.LoginFailure:
        print("There was an error logging into the bot account. Please make sure the appropriate token is in your .env file.") 

if __name__ == "__main__":
    main()