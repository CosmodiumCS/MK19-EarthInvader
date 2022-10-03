# binary [encoding] package for the the Skeleton Key project
# created by : Fyzz

import nextcord
from nextcord.ext import commands
from main import guild_id

# match file name with classname
class bin(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bin - Loaded")

    @nextcord.slash_command(description="Binary Encode / Decode", guild_ids=[guild_id])
    async def bin(self, interaction: nextcord.Interaction, action, text):
        message = ""
        # "encode" or "e" entered
        if action == "encode" or action == 'e':
            output = ' '.join(format(ord(x), 'b') for x in text)
            message = f"**Encoded:**\n{output}"

        # "decode" or "d" entered
        if action == "decode" or action == 'd':
            output = ""
            binary_list = text.split(' ')
            for binary in binary_list:
                output += chr(int(binary, 2))
            message = f"**Decoded:**\n{output}"

        await interaction.response.send_message(message)
    # Handle Errors
    @bin.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
**Syntax**
> Usage - `/bin`  `<encode/decode>`  `<text>`

**Examples:**
> Shorthand: `/bin`  `e`  `some text to encode`
> Longhand: `/bin`  `decode`  `1110100 1100101 1111000 1110100`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(bin(client))
