import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix="*", activity = discord.Game(name="*help"))
client.remove_command('help')


@client.command()
async def load(ctx, extension):
  client.load_extension('cogs.{extension}')

@client.command()
async def unload(ctx, extension):
  client.unload_extension('cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
  print('{0.user} standing by'.format(client))
  # DO NOT DO ANYTHING IN on_ready!

@client.command()
async def sourcehelp(ctx):
  embed = discord.Embed(title="__Source Code__", color=0x4287f5)
  embed.add_field(name="Source code available on github", value="https://github.com/Soulsender/Earth-Invader", inline=False)
  await ctx.send(embed=embed)

# cryptography help menu
@client.command()
async def help(ctx):
  embed = discord.Embed(title="Earth Invader", color=0x2b2a2a)
  embed.url = 'https://github.com/CryptexProject/Earth-Invader'
  embed.set_author(name='Soulsender#3162', url='https://soulsender.github.io')
  embed.description = 'Basic Cryptography Commands'

  embed.add_field(name="Base64", value="`b64 {encode/e & decode/d} {\"string\"}`\n"
                                       "Encoding and decoding from base64.", inline=False)
  embed.add_field(name="133T 5P34K", value="`leet {encode/e & decode/d} {\"string\"}`\n"
                                       "Encoding and decoding from 133T 5P34K (Leet Speak).", inline=False)
  embed.add_field(name="Hex", value="`hex {encode/e & decode/d} {\"string\"}`\n"
                                       "Encoding and decoding from Hex.", inline=False)
  embed.add_field(name="Caesar Cipher", value="`cc {encode/e & decode/d} {\"string\"} {key 1}`\n"
                                    "Encoding and decoding with Caesar Cipher. *Requires a Key as an integer.*", inline=False)

  embed.set_footer(text='Created by the Cryptex Project. See the wiki for documentation.')
  await ctx.send(embed=embed)


# mimic
@client.command()
@commands.has_role('Bot Admin') # Checks for Administrator rank.
async def mimic(ctx, *, question):
    await ctx.message.delete()
    await ctx.send(f'{question}')

client.run(str(os.getenv('TOKEN')))
