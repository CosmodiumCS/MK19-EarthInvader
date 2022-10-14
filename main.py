from nextcord import Interaction, SlashOption
from nextcord.ext import commands
import os
from discord.ext import commands
from dotenv import load_dotenv
client = commands.Bot()

load_dotenv()

# Uncomment this and the respected guild_id sections in each cog for testing
# Use your guild_id in your .env file
#guild_id = int(os.getenv('GUILD_ID'))

# status
@client.event
async def on_ready():
    print(f"{client.user} standing by on...")
    print('\n'.join(guild.name for guild in client.guilds))
    print(f"Loading Modules...")

# cog loading
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        # cut off the .py from the file name
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(str(os.getenv('TOKEN')))