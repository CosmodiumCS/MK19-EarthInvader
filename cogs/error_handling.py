# Error handling for different errors
# created by Soulsender
import discord
from discord.ext import commands

class error_handling(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embed = discord.Embed(title="SYNTAX ERROR", color=0xFE060A)
        embed.add_field(name="Help menu:",
                        value="`*help`",
                        inline=False)
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(error_handling(client))