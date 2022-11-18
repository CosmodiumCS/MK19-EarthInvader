import nextcord
from nextcord.ext import commands

class Test(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @commands.Cog.listener()
    async def on_ready(self):
      print(f"Test - Loaded")

    @nextcord.slash_command(name="test")
    async def test(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("Testing")

def setup(bot):
  bot.add_cog(Test(bot))