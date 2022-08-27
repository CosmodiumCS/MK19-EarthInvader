import discord
import os
from colorama import Fore
from discord.ext import commands
from dotenv import load_dotenv
from daemonize import Daemonize
import asyncio

load_dotenv()

pid = "/tmp/gokano_botd.pid"

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="*", activity=discord.Game(name="I'm in fucking alpha don't expect much"),
                      intents=intents)
client.remove_command('help')

async def main():
    async with client:

        async def load_extensions():
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    # cut off the .py from the file name
                    await client.load_extension(f"cogs.{filename[:-3]}")

        @client.event
        async def on_ready():
            # init sequence, only print statements allowed
            print("===== BOT INITILIZATION =====")
            print(Fore.GREEN, '{0.user} standing by'.format(client), Fore.RESET)
            print("===== SERVERS LOADED =====")
            print(Fore.BLUE, '\n'.join(guild.name for guild in client.guilds), Fore.RESET)
            print("===== MODULES LOADED =====", Fore.YELLOW)


        @client.command()
        async def sourcecode(ctx):
            embed = discord.Embed(title="__Source Code__", color=0x4287f5)
            embed.add_field(name="Source code available on github", value="https://github.com/Soulsender/Earth-Invader",
                            inline=False)
            await ctx.send(embed=embed)


        # cryptography help menu
        @client.command()
        async def help(ctx):
            embed = discord.Embed(title="Codex Bot", color=0x2b2a2a)
            embed.url = 'https://github.com/Soulsender/Codex-Bot'
            embed.set_author(name='Soulsender#3162', url='https://soulsender.github.io')
            embed.description = 'Basic Cryptography Commands'

            embed.add_field(name="Base64", value="`b64 {encode/e & decode/d} {\"string\"}`\n"
                                                 "Encoding and decoding from base64.", inline=False)
            embed.add_field(name="133T 5P34K", value="`leet {encode/e & decode/d} {\"string\"}`\n"
                                                     "Encoding and decoding from 133T 5P34K (Leet Speak).", inline=False)
            embed.add_field(name="Hex", value="`hex {encode/e & decode/d} {\"string\"}`\n"
                                              "Encoding and decoding from Hex.", inline=False)
            embed.add_field(name="Caesar Cipher", value="`cc {encode/e & decode/d} {\"string\"} {key 1}`\n"
                                                        "Encoding and decoding with Caesar Cipher. *Requires a Key as an integer.*",
                            inline=False)
            embed.add_field(name="Rot47", value="`r47 {encode/e & decode/d} {\"string\"}`\n"
                                                "Encoding and decoding with Rotation 47.", inline=False)
            embed.add_field(name="Rot13", value="`r13 {encode/e & decode/d} {\"string\"}`\n"
                                                "Encoding and decoding with Rotation 13.", inline=False)
            embed.add_field(name="Binary", value="`bin {encode/e & decode/d} {\"string\"}`\n"
                                                 "Encoding and decoding with binary.", inline=False)
            embed.add_field(name="MD5", value="`md5 {encode/e & decode/d} {\"string\"}`\n"
                                                 "Encoding and decoding with md5.", inline=False)
            embed.add_field(name="Morse", value="`mor {encode/e & decode/d} {\"string\"}`\n"
                                                 "Encoding and decoding Morse code.", inline=False)                                     

            embed.set_footer(text='Created by Soulsender. See the wiki for documentation.')
            await ctx.send(embed=embed)


        # mimic
        @client.command()
        @commands.has_role('Bot Admin')  # Checks for Administrator rank.
        async def m(ctx, *, question):
            await ctx.message.delete()
            await ctx.send(f'{question}')


        @client.command()
        async def servers(ctx):
            servers = list(client.guilds)
            await ctx.send(f"Connected on {str(len(servers))} servers:")
            await ctx.send('\n'.join(guild.name for guild in client.guilds))

        await load_extensions()
        await client.start(str(os.getenv('TOKEN')))

asyncio.run(main())
daemon = Daemonize(app="gokano_botd", pid=pid, action=main)
daemon.start()
