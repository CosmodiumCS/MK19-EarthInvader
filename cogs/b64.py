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
        print('b64 Online')

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
        elif action == "decode" or "d":
            text = text.encode('ascii')
            b64_bytes = base64.b64decode(text)
            output = b64_bytes.decode('ascii')
            await ctx.send(output)
            return [output, True]

        else:
            # HELP MENU
            embed = discord.Embed(title="__base64 Command Menu__", color=0x2b2a2a)
            embed.add_field(name="Commands", value="**decode** or **d** - decode base64 encoded text \n **encode** or **e** - base64 encode text", inline=False)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(b64(client))