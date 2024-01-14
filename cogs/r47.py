# Rot47 [encoding] package for the the Skeleton Key project
# created by : Fyzz

import nextcord
from nextcord.ext import commands
import base64
#from main import guild_id

# match file name with classname
class r47(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("R47 - Loaded")

    @nextcord.slash_command(description="Rot46 Encode / Decode" #guild_ids=[guild_id]
    )
    async def r47(self, interaction: nextcord.Interaction, action, text):
        message = ""
        # "encode" or "e" entered
        if action in ["encode", 'e']:
            output = ''

            for index in text:
                encoded = ord(index)
                if encoded >= 33 and encoded <= 126:
                    output += chr(33 + ((encoded + 14) % 94))
                else:
                    output += index
            message = f"**Encoded:**\n`{output}`"

        # "decode" or "d" entered
        if action in ["decode", 'd']:
            output = ''

            for index in text:
                encoded = ord(index)
                if encoded >= 33 and encoded <= 126:
                    output += chr(33 + ((encoded + 14) % 94))
                else:
                    output += index
            message = f"**Decoded:**\n`{output}`"

        await interaction.response.send_message(message)
    # Handle Errors
    @r47.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
**Syntax**
> Usage - `/r47`  `<encode/decode>`  `<text>`
**Examples:**
> Shorthand: `/r47`  `e`  `some text to encode`
> Longhand: `/r47`  `decode`  `D@>6 E6IE`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(r47(client))
