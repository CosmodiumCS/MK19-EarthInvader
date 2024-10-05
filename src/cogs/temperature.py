import nextcord
from nextcord.ext import commands

# match file name with classname
class temperature(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Temperature - Loaded")

    @nextcord.slash_command(description="Convert temperature metrics"
    )
    async def temperature(self, interaction: nextcord.Interaction, unit, value):
        value = float(value)
        if unit.lower() in ["celsius", "c"]:
            converted_value = (value * 9/5) + 32
            response = f"`{value:.1f}°C` \nis \n`{converted_value:.1f}°F`"
        if unit.lower() in ["fahrenheit", "f"]:
            converted_value = (value - 32) / 1.8
            response = f"`{value:.1f}°F` \nis \n`{converted_value:.1f}°C`"
        await interaction.response.send_message(response)

    # Handle Errors
    @temperature.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):
        message = """
**Syntax**
> Usage - `/temperature`  `<unit>` `<value>`

**Examples:**
> Shorthand: `/temperature`  `c`  `-10`
> Longhand: `/temperature`  `fahrenheit`  `20`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",
                               color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(temperature(client))
