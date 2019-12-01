#!/usr/bin/env python3

# - Importing all needed modules needed in the Main bot file.
import os
import discord
from discord.ext import commands

# - PUT YOUR DISCORD ACCOUNT ID HERE, DO NOT PUT YOUR ACCOUNT ID IN QUOTES!
# - EXAMPLE: account_id = 546812331213062144
account_id = "PUT YOUR DISCORD ACCOUNT ID HERE"

# - Information for our client (bot)
client = commands.Bot(command_prefix="r!", owner_id=account_id, case_insensitive=False, self_bot=False)
client.remove_command('help')
line_divide = "\n———————————————————————————————"

bot_token = ""

# - When bot is ready a status message will be printed to the console.
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=3, name="Nothing :("))
    print(f"---------------PyRaidBot----------------------------"
          f"\nBot is online and connected to {str(client.user)}"
          f"\nConnected to {str(len(client.guilds))} Guilds."
          f"\n----------------------------------------------------")

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# - Load a file while the bot is online.
@client.command(pass_context=True)
@commands.is_owner()
async def load_cogs(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="→ Information")
    embed.add_field(name="• Cog command", value=ctx.author.mention + " → One of the cogs has been loaded!")
    await ctx.send(embed=embed)


# - Catch an error that happens from loading a file.
@load_cogs.error
async def load_cogs_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Invalid Argument",
                        value="Please put a valid option! Example: `l!load_cogs raid`")
        await ctx.send(embed=embed)


# - Unload a file while the bot is online.
@client.command(pass_contxt=True)
@commands.is_owner()
async def unload_cogs(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="→ Information")
    embed.add_field(name="• Cog command",
                    value=ctx.author.mention + " → One of the cogs has been unloaded!")
    await ctx.send(embed=embed)


# - Catch an error that happens from unloading a file.
@unload_cogs.error
async def unload_cogs_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Invalid Argument",
                        value="Please put a valid option! Example: `l!unload_cogs raid`")
        await ctx.send(embed=embed)


# - Reload a file while the bot is online.
@client.command(pass_context=True)
@commands.is_owner()
async def reload_cogs(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    embed = discord.Embed(
        color=discord.Color.from_rgb(241, 90, 36)
    )
    embed.set_author(name="→ Information")
    embed.add_field(name="• Cog command",
                    value=ctx.author.mention + " → One of the cogs has been reloaded!")
    await ctx.send(embed=embed)


# - Catch an error that happens while reloading a file.
@reload_cogs.error
async def reload_cogs_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36)
        )
        embed.add_field(name="→ Invalid Argument",
                        value="Please put a valid option! Example: `l!reload_cogs raid`")
        await ctx.send(embed=embed)


# - Loading all files inside the cogs folder when the bot turns on.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")


# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


# - Running the bot token.
client.run(bot_token)
