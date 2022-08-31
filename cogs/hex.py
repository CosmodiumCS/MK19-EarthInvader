#!/usr/bin/python
# reverse cipher package for the the codex project
# created by : C0SM0
import discord
from discord.ext import commands

class hex(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def hex(self, ctx, action, *, text):

        # encode hex
        if action == "encode" or action == "e":
            # encode to hex
            output = text.encode("utf-8").hex()
            await ctx.send(output)
            return [output, True]

        # decode hex
        if action == "decode" or action == "d":
            # decode to hex
            output = bytes.fromhex(text).decode("utf-8")
            await ctx.send(output)
            return [output, True]

    @hex.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="SYNTAX ERROR", color=0xFE060A)
            embed.add_field(name="Syntax:",
                            value="`*hex {encode/decode} {your text}`",
                            inline=False)
            embed.add_field(name="Example 1 - Encode longway:",
                            value="`*hex encode some text`", inline=False)
            embed.add_field(name="Example 2 - Decode shortway:",
                            value="`*hex d 736f6d652074657874`", )
            await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(hex(client))