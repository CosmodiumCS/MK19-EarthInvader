# base64 [encoding] package for the the Skeleton Key project
# created by : Fyzz

import nextcord
from nextcord.ext import commands
#from main import guild_id

# match file name with classname
class sourcecode(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Sourcecode - Loaded")

    @nextcord.slash_command(description="Source Code" #guild_ids=[guild_id]
    )
    async def sourcecode(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(title="**Earth Invader | Source Code**", color=0x4287f5)
        embed.add_field(name="**[+] Available on github:**", value="https://github.com/Soulsender/Earth-Invader",inline=False)
        await interaction.response.send_message(embed=embed)


def setup(client) -> None:
    client.add_cog(sourcecode(client))
