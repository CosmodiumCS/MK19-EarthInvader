# md5 [encoding] package for the the Skeleton Key project
# created by : Boulbalah lahcen

import nextcord
from nextcord.ext import commands
import hashlib
#from main import guild_id


# match file name with classname
class md5(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"MD5 - Loaded")

    @nextcord.slash_command(description="MD5 Encode / Decode" #guild_ids=[guild_id]
    )
    async def md5(self, interaction: nextcord.Interaction, action, text):
        message = ""
        # "encode" or "e" entered
        if action == "encode" or action == 'e':
            output = hashlib.md5(text.encode()).hexdigest() 
            message = f"**Encoded:**\n{output}"

        # "decode" or "d" entered
        if action == "decode" or action == 'd':
            if hashlib.md5(text.encode()).hexdigest() == text:
                message = f"**Decoded:**\n{text}"
            else:
                message = f"**Error**"

        await interaction.response.send_message(message)
    # Handle Errors
    @md5.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
**:X:Syntax**
> Usage - `/md5`  `<encode/decode>`  `<text>`

**Examples:**
> Shorthand: `/md5`  `e`  `some text to encode`
> Longhand: `/md5`  `decode`  `552e21cd4cd9918678e3c1a0df491bc3`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(md5(client))
