# base64 [encoding] package for the the Skeleton Key project
# created by : Fyzz

import nextcord
from nextcord.ext import commands

# match file name with classname
class help(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help - Loaded")

    @nextcord.slash_command(description="Help menu")
    async def help(self, interaction: nextcord.Interaction):
        message = """
**[+] Getting Started:**
> `/help                                           ` - Shows this message.
> `/sourcecode                                     ` - Gets github url.

**[+] Current Ciphers:**
> `/b8      <encode/decode>     <number>           ` - Base8
> `/b64     <encode/decode>     <text>             ` - Base64
> `/bin     <encode/decode>     <text>             ` - Binary
> `/cc      <encode/decode>     <key>    <text>    ` - Caeser
> `/hex     <encode/decode>     <text>             ` - Hex
> `/leet    <encode/decode>     <text>             ` - L337 $P33K
> `/mor     <encode/decode>     <text>             ` - Morse Code
> `/r47     <encode/decode>     <text>             ` - Rotation 47
> `/r13     <encode/decode>     <text>             ` - Rotation 13

**[+]Example:**
`/b64 e some text` where `e` is to encode and `some text` is to be encoded.

**[+] Miscellaneous Functions:**
> `/replace  o   5    Hello World    ` - Replaces "o" with "5" in "Hello World"
> `/temp     c   -10                 ` - Converts -10C to fahrenheit
> `/metric   kg  200                 ` - Converts 200kg to pounds

[For more information, see the wiki.](https://github.com/CosmodiumCS/Earth-Invader/wiki)
"""
        embed = nextcord.Embed(title="Earth Invader  |  Help", color=0x4287f5, description=message)
        await interaction.response.send_message(embed=embed)


def setup(client) -> None:
    client.add_cog(help(client))
