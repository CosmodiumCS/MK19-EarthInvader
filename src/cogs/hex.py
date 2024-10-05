# hex [encoding] package for the the Skeleton Key project
# created by : Fyzz

import nextcord
from nextcord.ext import commands

# match file name with classname
class hex(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Hex - Loaded")

    @nextcord.slash_command(description="Hex Encode / Decode")
    async def hex(self, interaction: nextcord.Interaction, action, text):
        message = ""
        # "encode" or "e" entered
        if action in ["encode", 'e']:
            output = text.encode("utf-8").hex()
            message = f"**Encoded:**\n`{output}`"

        # "decode" or "d" entered
        if action in ["decode", 'd']:
            output = bytes.fromhex(text).decode("utf-8")
            message = f"**Decoded:**\n`{output}`"

        await interaction.response.send_message(message)
    # Handle Errors
    @hex.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
**Syntax**
> Usage - `/hex`  `<encode/decode>`  `<text>`

**Examples:**
> Shorthand: `/hex`  `e`  `some text to encode`
> Longhand: `/hex`  `decode`  `736f6d652074657874`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(hex(client))
