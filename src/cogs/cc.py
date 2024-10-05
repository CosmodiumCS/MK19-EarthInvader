# cc [encoding] package for the the Skeleton Key project
# created by : Cosmo

import nextcord
from nextcord.ext import commands
#from main import guild_id

# match file name with classname
class cc(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("CC - Loaded")

    @nextcord.slash_command(description="Caeser Encode / Decode" #guild_ids=[guild_id]
    )
    async def cc(self, interaction: nextcord.Interaction, action,key, text):
        message = ""

        # "encode" or "e" entered
        if action in ["encode", 'e']:
            output = ''
            exclude = "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"

            # encryption process
            if text and key:
                for character in text:
                    if character in exclude:
                        output += character
                    elif character.isupper():
                        output += chr((ord(character) +
                                      int(key) - 65) % 26 + 65)
                    else:
                        output += chr((ord(character) +
                                      int(key) - 97) % 26 + 97)
            message = f"**Encoded:**`\n{output}`"

        # "decode" or "d" entered
        if action in ["decode", 'd']:
            output = ''
            exclude = "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"

            # decryption process
            if text and key:
                for character in text:
                    if character in exclude:
                        output += character
                    elif character.isupper():
                        output += chr((ord(character) -
                                      int(key) - 65) % 26 + 65)
                    else:
                        output += chr((ord(character) -
                                      int(key) - 97) % 26 + 97)
            message = f"**Decoded:**\n`{output}`"

        await interaction.response.send_message(message)
    # Handle Errors

    @cc.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
**Syntax**
> Usage - `/cc`  `<encode/decode>`  `<key>`  `<text>`

**Examples:**
> Shorthand: `/cc`  `e`  '13'  `some text to encode`
> Longhand: `/cc`  `decode`  '11'  `fbzr grkg`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",
                               color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(cc(client))
