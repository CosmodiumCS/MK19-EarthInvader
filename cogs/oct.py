#!/usr/bin/python
# created by : Boulbalah lahcen
from discord.ext import commands
import discord


class b8(commands.Cog):
    def __init__(self, client):
        self.client = client

    # callback to shell showing that the cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def b8(self, ctx, action, *, text):

        # "encode" or "e" entered
        if action == "encode" or action == "e":

            output = oct(int(text)).replace("0o","")
            # this sends the result
            await ctx.send(output)
            return [output,True]

        # "decode" or "d" entered
        elif action == "decode" or action== "d":
            output = 0
            base = 1
            while (int(text)):
                last_digit = int(text) % 10
                text = int(int(text )/ 10)
                output += last_digit * base
                base = base * 8
            # this sends the result
            await ctx.send(output)
        else:
            # HELP MENU
            embed = discord.Embed(title="__Octal Command Menu__", color=0x2b2a2a)
            embed.add_field(name="Commands", value="**decode** or **d** - decode oct encoded text \n **encode** or **e** - oct encode text \n example *b8 e 45  ",
             inline=False)
            await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(b8(client))