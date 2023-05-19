import os
from dotenv import load_dotenv
import aiohttp
import nextcord
from nextcord.ext import commands
import glob


load_dotenv()


def create_bot():
    intents = nextcord.Intents.default()
    intents.guilds = True
    intents.members = True
    intents.message_content = True

    activity = nextcord.Activity(
        type=nextcord.ActivityType.listening, name="/help"
    )

    return commands.Bot(
        command_prefix="/",
        intents=intents,
        activity=activity,
        owner_id="null",
    )


def load_cogs(bot):
    for file in glob.glob("cogs/*.py"):
        cog_name = os.path.basename(file)[:-3]  # Remove the extension
        bot.load_extension(f"cogs.{cog_name}")

    print("Cogs loaded.")


async def startup(bot):
    async with aiohttp.ClientSession() as session:
        bot.session = session


def get_bot_token():
    if token := os.getenv('TOKEN'):
        return token
    else:
        raise ValueError("Bot token not found. Make sure to set TOKEN environment variable.")


def main():
    bot = create_bot()

    @bot.event
    async def on_ready():
        print(f"USER: {bot.user} URL:", f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&scope=applications.commands%20bot")
        print(f"{bot.user} standing by on...")
        print('\n'.join(guild.name for guild in bot.guilds))
        print("Loading cogs...")
        load_cogs(bot)

    bot.loop.create_task(startup(bot))

    # Run the bot
    bot.run(get_bot_token())


if __name__ == "__main__":
    main()
