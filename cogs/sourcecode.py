# sourcecode command

import nextcord
from nextcord.ext import commands

class Sourcecode(commands.Cog):
    def __init__(self,bot):
      self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
      print(f"Sourcecode - Loaded")

    @nextcord.slash_command(name="sourcecode")
    async def sourcecode(self, interaction: nextcord.Interaction):
      embed = nextcord.Embed(title="**Earth Invader | Source Code**", color=0x4287f5)
      embed.add_field(name="**[+] Available on github:**", value="https://github.com/Soulsender/Earth-Invader",inline=False)
      await interaction.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
  bot.add_cog(Sourcecode(bot))
