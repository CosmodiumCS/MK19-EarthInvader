from nextcord import Interaction, SlashOption
from nextcord.ext import commands
import os
from colorama import Fore
from discord.ext import commands
from dotenv import load_dotenv
client = commands.Bot()

load_dotenv()
guild_id = int(os.getenv('GUILD_ID'))

@client.event
async def on_ready():
    print(f"{client.user} standing by on...")
    print('\n'.join(guild.name for guild in client.guilds))
    print(f"Loading Modules...")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        # cut off the .py from the file name
        client.load_extension(f"cogs.{filename[:-3]}")
client.run(str(os.getenv('TOKEN')))