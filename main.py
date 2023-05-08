import nextcord
from nextcord.ext import commands
import os
import aiohttp
from dotenv import load_dotenv


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

    # boolean that will be set to true when views are added
    bot.persistent_views_added = False

    @bot.event
    async def on_ready():
        print(f"USER: {bot.user} URL:", f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&scope=applications.commands%20bot")
        print(f"{bot.user} standing by on...")
        print('\n'.join(guild.name for guild in bot.guilds))
        print("Loading cogs...")

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

    async def startup():
        bot.session = aiohttp.ClientSession()

    bot.loop.create_task(startup())

    # run the bot
    bot.run(str(os.getenv('TOKEN')))


if __name__ == "__main__":
    main()
