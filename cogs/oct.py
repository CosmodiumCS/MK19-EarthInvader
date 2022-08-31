#!/usr/bin/python
# created by : Boulbalah lahcen
from discord.ext import commands
import discord


class oct(commands.Cog):
    def __init__(self, client):
        self.client = client

    # callback to shell showing that the cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def oct(self, ctx, action, *, text):

        # "encode" or "e" entered
        if action == "encode" or action == "e":

            output = oct(int(text)).replace("0o","")
            # this sends the result
            await ctx.send(output)
            return [output,True]

        # "decode" or "d" entered
        elif action == "decode" or action == "d":
            output = 0
            base = 1
            while (int(text)):
                last_digit = int(text) % 10
                text = int(int(text )/ 10)
                output += last_digit * base
                base = base * 8
            # this sends the result
            await ctx.send(output)

    @oct.error
    async def on_command_error(self, ctx, error):
        if isinstance(error):
            embed = discord.Embed(title="WIP COMMAND", color=0xFE060A)
            embed.add_field(name="ERROR - This command is WIP",
                            inline=False)
            await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(oct(client))