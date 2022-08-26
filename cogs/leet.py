#!/usr/bin/python

# leetspeek for [cryptex] project
# created by : Fyzz

from discord.ext import commands

class leet(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def leet(self, ctx, action, *, text):
        # leetspeek for [cryptex] project
        # created by : Fyzz

        # leet chr
        leet_dictionary_enc = {
            "a": "4",
            "b": "8",
            "e": "3",
            "g": "6",
            "i": "1",
            "o": "0",
            "s": "5",
            "t": "7"
        }

        # invert leet chr
        leet_dictionary_dec = dict((v, k) for (k, v) in leet_dictionary_enc.items())

        # encode leet
        if action == "encode" or action == "e":
            text = text.lower()
            output = ''

            for character in text:
                if character in leet_dictionary_enc:
                    output += leet_dictionary_enc[character]
                else:
                    output += character
            await ctx.send(output)
            return [output.capitalize(), True]

        # decode leet
        elif action == "decode" or action == "d":
            text = text.lower()
            output = ''

            for character in text:
                if character in leet_dictionary_dec:
                    output += leet_dictionary_dec[character]
                else:
                    output += character
            await ctx.send(output)
            return [output.capitalize(), True]

        # # HELP MENU
        # embed = discord.Embed(title="__leet Command Menu__", color=0x2b2a2a)
        # embed.add_field(value="**decode** or **d** - decode leet encoded text", inline=False)
        # embed.add_field(value="**encode** or **e** - leet encode text", inline=False)
        # await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(leet(client))