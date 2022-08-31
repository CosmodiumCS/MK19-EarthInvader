# IMPORTS
import discord
from discord.ext import commands

# INIT CLASS
# should be the same name as the file
class cc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # callback to shell showing that the cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def cc(self, ctx, action, key, *, text):

        # encodes caesar
        if action == "encode" or action == "e":
            output = ''
            exclude = "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"

            # encryption process
            if text and key:
                for character in text:
                    if character in exclude:
                        output += character
                    elif character.isupper():
                        output += chr((ord(character) + int(key) - 65) % 26 + 65)
                    else:
                        output += chr((ord(character) + int(key) - 97) % 26 + 97)
                await ctx.send(output)
                return [output, True]

        # decodes caesar
        if action == "decode" or action == "d":
            output = ''
            exclude = "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"

            # decryption process
            if text and key:
                for character in text:
                    if character in exclude:
                        output += character
                    elif character.isupper():
                        output += chr((ord(character) - int(key) - 65) % 26 + 65)
                    else:
                        output += chr((ord(character) - int(key) - 97) % 26 + 97)

                await ctx.send(output)
                return [output, True]

    @cc.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="SYNTAX ERROR", color=0xFE060A)
            embed.add_field(name="Syntax:",
                            value="`*cc {encode/decode} {key} {your text}`",
                            inline=False)
            embed.add_field(name="Example 1 - Encode longway:",
                            value="`*cc encode 13 some text`", inline=False)
            embed.add_field(name="Example 2 - Decode shortway:",
                            value="`*cc d 13 fbzr grkg`", )
            await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(cc(client))