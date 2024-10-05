# b8 [encoding] package for the the Skeleton Key project
# created by : Boulbalah lahcen

import nextcord
from nextcord.ext import commands
# from main import guild_id

# match file name with classname
class b8(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("B8 - Loaded")

    @nextcord.slash_command(description="Base8 Encode / Decode" #guild_ids=[guild_id]
    )
    async def b8(self, interaction: nextcord.Interaction, action, number):
        message = ""
        # "encode" or "e" entered
        if action in ["encode", 'e']:
            output = oct(int(number)).replace("0o","")
            message = f"**Encoded:**\n`{output}`"

        # "decode" or "d" entered
        if action in ["decode", 'd']:
            output = 0
            base = 1
            while (int(number)):
                last_digit = int(number) % 10
                number = int(number) // 10
                output += last_digit * base
                base = base * 8
            message = f"**Decoded:**\n`{output}`"

        await interaction.response.send_message(message)
    # Handle Errors
    @b8.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
**Syntax**
> Usage - `/b8`  `<encode/decode>`  `<number>`

**Examples:**
> Shorthand: `/b8`  `e`  `45`
> Longhand: `/b8`  `decode`  `55`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(b8(client))
