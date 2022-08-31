#!/usr/bin/python

# created by : Fyzz
# New Arg Parse
import discord
from discord.ext import commands

class bin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def bin(self, ctx, action, *, text):

        # encode binary
        if action == "encode" or action == "e":
            output = ' '.join(format(ord(x), 'b') for x in text)

            await ctx.send(output)
            return [output, True]

            # decode binary
        if action == "decode" or action == "d":
            binary_list = text.split(' ')
            output = ''
            for binary in binary_list:
                output += chr(int(binary, 2))

            await ctx.send(output)
            return [output, True]

    @bin.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="SYNTAX ERROR", color=0xFE060A)
            embed.add_field(name="Syntax:",
                            value="`*bin {encode/decode} {your text}`",
                            inline=False)
            embed.add_field(name="Example 1 - Encode longway:",
                            value="`*bin encode some text`", inline=False)
            embed.add_field(name="Example 2 - Decode shortway:",
                            value="`*bin d 1110100 1100101 1111000 1110100`", )
            await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(bin(client))