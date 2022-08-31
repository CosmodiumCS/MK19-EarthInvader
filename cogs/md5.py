#!/usr/bin/python
# created by : Boulbalah lahcen

from discord.ext import commands
import hashlib
import discord

class md5(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def md5(self, ctx, action, *, text):

        # encode md5
        if action == "encode" or action == "e":
            # encode to md5
            output =  hashlib.md5(text.encode()).hexdigest() 
            await ctx.send(output)
           # return [output, True]

        # decode md5
        elif action == "decode" or action == "d":
            # decode to md5
            if hashlib.md5(text.encode()).hexdigest() == text:
                return [text,True]
            else:
                output = "Error"
                return {output,True}

    @md5.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="SYNTAX ERROR", color=0xFE060A)
            embed.add_field(name="Syntax:",
                            value="`*md5 {encode/decode} {your text}`",
                            inline=False)
            embed.add_field(name="Example 1 - Encode longway:",
                            value="`*md5 encode some text`", inline=False)
            embed.add_field(name="Example 2 - Decode shortway:",
                            value="`*md5 d 552e21cd4cd9918678e3c1a0df491bc3`", )
            await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(md5(client))

