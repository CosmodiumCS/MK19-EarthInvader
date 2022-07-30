#!/usr/bin/python
# reverse cipher package for the the codex project
# created by : C0SM0

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

def setup(client):
    client.add_cog(hex(client))