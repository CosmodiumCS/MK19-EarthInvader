# base64 cipher [encoding] package for the the codex project

# created by : Fyzz
import discord
from discord.ext import commands
import base64

class b64(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def b64(self, ctx, action, *, text):

        # "encode" or "e" entered
        if action == "encode" or action == "e":
            text = text.encode('ascii')
            b64_bytes = base64.b64encode(text)
            output = b64_bytes.decode('ascii')
            await ctx.send(output)
            return [output, True]

        # "decode" or "d" entered
        elif action == "decode" or action=="d":
            text = text.encode('ascii')
            b64_bytes = base64.b64decode(text)
            output = b64_bytes.decode('ascii')
            await ctx.send(output)
            return [output, True]

    @b64.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="SYNTAX ERROR", color=0xFE060A)
            embed.add_field(name="Syntax:",
                            value="`*b64 {encode/decode} {your text}`",
                            inline=False)
            embed.add_field(name="Example 1 - Encode longway:",
                            value="`*b64 encode some text`", inline=False)
            embed.add_field(name="Example 2 - Decode shortway:",
                            value="`*b64 d c29tZSB0ZXh0`", )
            await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(b64(client))