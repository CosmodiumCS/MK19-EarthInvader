#!/usr/bin/python

# created by : Fyzz
# New Arg Parse

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

def setup(client):
    client.add_cog(bin(client))