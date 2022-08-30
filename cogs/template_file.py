# IMPORTS
from discord.ext import commands
import discord

# INIT CLASS
# should be the same name as the file
class x(commands.Cog):
    def __init__(self, client):
        self.client = client

    # callback to shell showing that the cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        #print('cog name Online')
        print(__file__, ' Online')

    # the actual command
    # x should be the name of the command which should optimally be the same name as the file
    @commands.command()
    async def x(self, ctx, action, *, text):

        # "encode" or "e" entered
        if action == "encode" or action == "e":

            # do the cipher code here

            output = "output of the cipher"
            # this sends the result
            await ctx.send(output)

        # "decode" or "d" entered
        elif action == "decode" or action== "d":

            # do the cipher code here
           

            output = "output of the cipher"
            # this sends the result
            await ctx.send(output)
        else:
            # HELP MENU
            embed = discord.Embed(title="__x Command Menu__", color=0x2b2a2a)
            embed.add_field(name="Commands", value="**decode** or **d** - decode x encoded text \n **encode** or **e** - x encode text \n example *x  ",
             inline=False)
            await ctx.send(embed=embed)

# x should be the same name as the init class
async def setup(client):
    await client.add_cog(x(client))