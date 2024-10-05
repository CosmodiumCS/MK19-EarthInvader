# base64 [encoding] package for the Skeleton Key project
# created by : Fyzz

import nextcord
from nextcord.ext import commands
import base64
#from main import guild_id

# match file name with classname
class b64(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("B64 - Loaded")

    @nextcord.slash_command(description="Base64 Encode / Decode" #guild_ids=[guild_id]
    )
    async def b64(self, interaction: nextcord.Interaction, action, text):
        message = ""
        # "encode" or "e" entered
        if action in ["encode", 'e']:
            text = text.encode('ascii')
            b64_bytes = base64.b64encode(text)
            output = b64_bytes.decode('ascii')
            message = f"**Encoded:**\n`{output}`"

        # "decode" or "d" entered
        if action in ["decode", 'd']:
            text = text.encode('ascii')
            b64_bytes = base64.b64decode(text)
            output = b64_bytes.decode('ascii')
            message = f"**Decoded:**\n`{output}`"

        await interaction.response.send_message(message)
    # Handle Errors
    @b64.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
**Syntax**
> Usage - `/b64`  `<encode/decode>`  `<text>`

**Examples:**
> Shorthand: `/b64`  `e`  `some text to encode`
> Longhand: `/b64`  `decode`  `c29tZSB0ZXh0`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(b64(client))
