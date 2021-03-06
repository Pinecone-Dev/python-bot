#Vell Bot v0.1 
import os
import youtube_dl
import bs4
# CONFIG
# --------- #
prefix = ["v.", "join.", "mod."]
embed_role = "Vell" # The role in your server used for embedding.
game = "Type v.help" # This will display as the game on Discord.
# ---------- #
from discord.voice_client import VoiceClient
from discord.ext import commands
import asyncio
from discord.ext.commands import Bot
import discord
import requests
global misc_commands
misc_commands = ["supportserver"]
global command_help
command_help = "For more info on a command type v.commandhelp where command is the name of it. Ex: v.nsfwhelp"
global music_commands
music_commands = ["In progress, not available yet..."]
global mod_commands
mod_commands = ["emoji", "text", "nsfw", "kick"]
global ae_commands
ae_commands = ["badgeslist"]
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Use v.help for help menu."))
    print("Bot online")
startup_extensions = ["Music"]
    
class Main_Commands():
 def __init__(self, bot):
  self.bot = bot
  

  


@bot.command(pass_context=True)
async def kick(ctx, user:discord.Member, *, reason:str=None):
    """Kicks someone from the server"""
    if reason is None:
        reason = "{0.mention} has felt the wrath of the boot :boot:"
        try:
            await bot.kick(user)
        except discord.errors.Forbidden:
                await bot.say("Either I do not have permission, or you do not... Please contact server admins if you should be able to.")
                return "{0.mention} has been kicked from the server."
                return reason
@bot.command(pass_context=True)
async def ban(ctx, user:discord.Member, *, reason:str=None):
    """Bans someone from the server"""
    if reason is None:
        reason = "The ban hammer has spoken. :ban:"
        try:
            await bot.kick(user)
        except discord.errors.Forbidden:
                await bot.say("Either I do not have permission, or you do not... Please contact server admins if you should be able to.")
                return "{0.mention} has been banned from the server."
                return reason
          

@bot.event
async def on_member_join(member):
    server = member.server.default_channel
    fmt = 'Hey! {0.mention} Welcome to {1.name} the place to hang out with fellow coders and learn more!! Hope you enjoy your stay!'
    channel = member.server.get_channel("410605613354319872")
    await bot.send_message(channel, fmt.format(member, member.server))

@bot.event
async def on_member_remove(member):
    server = member.server.default_channel
    fmt = '{0.mention} has left/been kicked/banned from the server.'
    channel = member.server.get_channel("429774341152964618")
    await bot.send_message(channel, fmt.format(member, member.server))   
@bot.command(pass_context=True)
async def help(ctx):
    
    embed = discord.Embed(title="Vell Bot Help Menu", description="Here you will find all the help you need. Not satisfied? Type join.supportserver, to join our Official Support Server.", color=0x00a0ea)
    embed.add_field(name="This is my website".format("null"), value="www.jdcoding7.wixsite.com/vellbot")
    embed.add_field(name="My prefixes".format("null"), value="v. for general commands | join. for joining support server |mod. for mod commands")
    embed.set_thumbnail(url = "https://thumb.ibb.co/c1yBAS/icon.jpg")
    embed.add_field(name="Miscellaneous Commands".format("null"), value=misc_commands, inline=False)
    embed.add_field(name="Music Commands".format("null"), value=music_commands, inline=False)
    embed.add_field(name="Commands Help".format("null"), value=command_help, inline=False)
    embed.add_field(name="Moderator Commands".format("null"), value=mod_commands, inline=False)
    embed.add_field(name="Adventure Quest 3D".format("null"), value=ae_commands, inline=False)
    embed.set_footer(text="Vell Bot ~ Developed by Alphi#5113 & Bread#7656")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def badgeslisthelp(ctx):
    
    embed = discord.Embed(title="Info for the <badgeslist> command", description="Displays the badges from the AQ3D game.", color=0x00a0ea)
    embed.set_thumbnail(url = "https://thumb.ibb.co/euN8un/AQ3_D_Logo_T_shirt.png")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def betahelp(ctx):
    embed = discord.Embed(title="Info for the <beta> command", description="Beta command displays a text..", color=0x00a0ea)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def emojihelp(ctx):
    embed = discord.Embed(title="Info for the <emoji> moderator command", description="Sends a text warning regarding the misuse of server emojis.", color=0x00a0ea)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def texthelp(ctx):
    embed = discord.Embed(title="Info for the <text> moderator command", description="Sends a text warning regarding the bad behavior with texts. Like harrasing or bullying.", color=0x00a0ea)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def nsfwhelp(ctx):
    embed = discord.Embed(title="Info for the <nsfw> moderator command", description="Sends a text warning regarding the use of NSFW or innappropiate language outside of the NSFW channel.", color=0x00a0ea)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def kickhelp(ctx):
    embed = discord.Embed(title="Info for the <kick> moderator command", description="Kicks the @mentioned user fom the server. (Only for Admins/Owners/Mods", color=0x00a0ea)
    await bot.say(embed=embed)
@bot.command()
async def emoji():
    await bot.say("```Please, do not use an emoji repeatedly or in an annoying way, as this might result in a ban.```")
@bot.command()
async def text():
    await bot.say("```The texts you're sending right now are inappropiate, please stop or you might be kicked from the server.```")
@bot.command()
async def nsfw():
    await bot.say("```That message is considered NSFW, which is not allowed in this channel. It will be removed immediately, if you persist you will earn a kick or ban as the responsible MOD considers it.```")
@bot.command()
async def invite():
    await bot.say("Invite me with this link: " + "https://discordapp.com/oauth2/authorize?client_id=368592012116623362&scope=bot&permissions=8")
@bot.command()
async def supportserver():
    await bot.say("Support server: https://discord.gg/YAZNjbe")

if __name__ == "__main__":
 for extension in startup_extensions:
  try:
   bot.load_extension(extension)
  except Exception as e:
   exc = '{}: {}'.format(type(e).__name__, e)
   print('Failed to load extension {}\n{}'.format(extension, exc))
  

@bot.command()
async def alphaknight(pass_context=True):
    embed = discord.Embed(title="AQ3D Alpha Knight", description="Participated in the Alpha Test. A knight from the days of old... before AdventureQuest 3D was even a game..", color=0x00ff00)
    embed.set_thumbnail(url = "https://thumb.ibb.co/bSkVPn/Alpha_Knight.png")
    await bot.say(embed=embed)
@bot.command()
async def closedbeta(pass_context=True):
    embed = discord.Embed(title="AQ3D Closed Beta", description="Awarded to all players who took part in the closed beta of AdventureQuest 3D.", color=0x00ff00)
    embed.set_thumbnail(url = "https://thumb.ibb.co/mvzX4n/Closed_Beta.png")
    await bot.say(embed=embed)  
 
@bot.command()
async def guardian(pass_context=True):
    embed = discord.Embed(title="AQ3D Guardian", description="Guardian of AdventureQuest 3D! Will include Guardian Class, access to the Guardian tower and special guardian quests & perks.", color=0x00ff00)
    embed.set_thumbnail(url = "https://thumb.ibb.co/dYeoc7/Guardian.png")
    await bot.say(embed=embed) 
    
@bot.command()
async def dragonguardian(pass_context=True):
    embed = discord.Embed(title="AQ3D Dragon Guardian", description="You have answered the call of the Dragon Guardian! Your passion and might are unmatched!", color=0x00ff00)
    embed.set_thumbnail(url = "https://thumb.ibb.co/dofBx7/Dragon_Guardian.png")
    await bot.say(embed=embed) 
@bot.command()
async def prebeta(pass_context=True):
    embed = discord.Embed(title="AQ3D Pre Beta", description="Awarded to every hero who had a character during AQ3D's Pre-Beta testing phase!", color=0x00ff00)
    embed.set_thumbnail(url = "https://thumb.ibb.co/facrx7/Pre_Beta.png")
    await bot.say(embed=embed) 
@bot.command()
async def backer(pass_context=True):
    embed = discord.Embed(title="AQ3D Backer", description="\"I've got your back!\" Backed the AdventureQuest 3D project on Kickstarter.",color=0x00ff00)
    embed.set_thumbnail(url = "https://thumb.ibb.co/naDQPn/backer.png")
    await bot.say(embed=embed)     
@bot.command()
async def undersworn(pass_context=True):
    embed = discord.Embed(title="Undersworn T-Shirt", description="You have spoken the oath in Undertongue. You are of the Undead Legion now and forever.",color=0x00ff00)
    embed.set_thumbnail(url = "https://thumb.ibb.co/bMbtun/Undersworn.png")
    await bot.say(embed=embed)
@bot.command()
async def dagecollector2018(pass_context=True):
    embed = discord.Embed(title="Dage's Collector 2018", description="You have purchased Dage's entire 2018 Dage Collection! Visit Melodia to access your undead items at any time! For the Legion!",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/dQLmEn/Dage_Collection1.jpg")
    await bot.say(embed=embed)
@bot.command()
async def undeadlegiontshirt(pass_context=True):
    embed = discord.Embed(title="Undead Legion T-shirt", description="Let the world know that you are one of the mighty. FOR THE LEGION!",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/i37u0S/Legion_Legend.png")
    await bot.say(embed=embed)
@bot.command()
async def bluemoglinplushhat(pass_context=True):
    embed = discord.Embed(title="Zorbak Blue Moglin Plush Hat", description="The blue moglin ears on your head hear nothing but the ebil that surrounds you. *sigh* No, that's not a typo.",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/iPVmEn/PureEbil.png")
    await bot.say(embed=embed)
@bot.command()
async def frostvalcollector2017(pass_context=True):
    embed = discord.Embed(title="Frostval Collector 2017 ", description="You have purchased the entire 2017 Frostval Collection! Visit Melodia to access your festive items at any time! Happy Frostval!",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/j7L8S7/Frostval_Collection2017.jpg")
    await bot.say(embed=embed)
@bot.command()
async def calendar2018(pass_context=True):
    embed = discord.Embed(title="2018 Calendar - Eternal Chronomancer", description="Shop unlocked with the purchase of the AE 2018 Calendar. ",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/n0xcLS/Eternal_Chronomancer.jpg")
    await bot.say(embed=embed)
@bot.command()
async def legionpledgescroll(pass_context=True):
    embed = discord.Embed(title="Legion Pledge Scroll", description="Dage has found you worthy. The contact... the oath... follows you wherever you go.",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/n3C2LS/Worthy_Soul.png")
    await bot.say(embed=embed)
@bot.command()
async def aprilfoolsday(pass_context=True):
    embed = discord.Embed(title="April Fools Day", description="Visited the Dricken Cave during April Fools Day",color=0x00ff00)
    embed.set_thumbnail(url = "")
    await bot.say(embed=embed)
@bot.command()
async def founder(pass_context=True):
    embed = discord.Embed(title="Founder", description="Founder of AdventureQuest 3D. Grants Early Access to Beta game releases.",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/mFMVqS/founder.jpg")
    await bot.say(embed=embed)
@bot.command()
async def epicfounder(pass_context=True):
    embed = discord.Embed(title="Epic Founder", description="Epic Founder of AdventureQuest 3D. Grants Early Access to AQ3D as well as other in-game perks detailed on the AQ3D Kickstarter!",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/hUzdc7/epicfounder.jpg")
    await bot.say(embed=embed)
@bot.command()
async def legendaryfounder(pass_context=True):
    embed = discord.Embed(title="Legendary Founder", description="Legendary Founder of AdventureQuest (Not live yet. In development) Also includes pre-order pack of Paladin, DragonSlayer, Necromancer and Ninja classes and early access to them!!",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/ndk1x7/legendaryfounder.jpg")
    await bot.say(embed=embed)
@bot.command()
async def swimsuitcontest2016(pass_context=True):
    embed = discord.Embed(title="Contest Swimsuit Edition 2016", description="Winner of the 2016 Artix Entertainment Swimsuit Art Contest",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/ejB8c7/contestswim2016.jpg")
    await bot.say(embed=embed)
@bot.command()
async def determined(pass_context=True):
    embed = discord.Embed(title="Determined", description="Awarded to those who managed to cross the impossibly large gap to level 15 in the Open Beta, before levels were normalized.",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/nEgYc7/determined15.jpg")
    await bot.say(embed=embed)
@bot.command()
async def aq3dtlogoshirt(pass_context=True):
    embed = discord.Embed(title="AQ3D Logo T-shirt", description="Purchased AQ3D Logo T-Shirt from Heromart",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/kSvbx7/aq3dlogoteeshirt.jpg")
    await bot.say(embed=embed)
@bot.command()
async def calendar2017(pass_context=True):
    embed = discord.Embed(title="AE 2017 Calendar", description="Purchased the Artix Entertainment 2017 Calendar",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/c6mc4n/2017calendar.jpg")
    await bot.say(embed=embed)
@bot.command()
async def riverstone(pass_context=True):
    embed = discord.Embed(title="River Stone", description="You are like a smooth stone pulled from a river… all your hard edges worn away by time and experience leaving only perfected form.",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/itaOAS/River_Stone.jpg")
    await bot.say(embed=embed)
@bot.command()
async def burningmanchallenge(pass_context=True):
    embed = discord.Embed(title="Burning Man Challenge", description="You have been to the secret battle area of the Burning Man and left unburned.",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/b31Kjn/The_Unburned.jpg")
    await bot.say(embed=embed)
@bot.command()
async def littledread(pass_context=True):
    embed = discord.Embed(title="Little Dread Bested", description="You faced Little Dread Riding Hood in single combat near her lodge in Darkovia Forest and proven that you're not a Lycan. At least… not yet.",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/kmAjH7/Dreadly_Serious.jpg")
    await bot.say(embed=embed)
@bot.command()
async def firezillachallenge(pass_context=True):
    embed = discord.Embed(title="Firezilla Challenge", description="You have gone to the lair of the giant monster known as Firezilla and you didn't even need a giant mech.",color=0x00ff00)
    embed.set_thumbnail(url = "https://image.ibb.co/mMToc7/Kaiju_Killer.jpg")
    await bot.say(embed=embed)
@bot.command()
async def badgeslist(pass_context=True):
    embed = discord.Embed(title="Badges List", description="Here you will find all the badges from AQ3D (Still in development)", color=0x00a0ea)
    embed.set_thumbnail(url = "https://thumb.ibb.co/euN8un/AQ3_D_Logo_T_shirt.png")
    embed.add_field(name="Badges (Loyalty)".format("null"), value="Alpha Knight ~ Closed Beta ~ Guardian ~ Dragon Guardian ~ Pre Beta ~ Backer ~ Founder ~ Epic Founder ~ Legendary Founder ~ Determined ~")
    embed.add_field(name="Badges (Special)".format("null"), value="Undersworn T-shirt ~ Dage Collection 2018 ~ Zorbak Blue Moglin Plush Hat ~ 2018 Calendar ~ Eternal Chronomancer ~ Frostval Collector 2017 ~ Contest Swimsuit Edition 2016 ~ April Fools Day ~ Legion Pledge Scroll ~ AE 2017 Calendar ~ AQ3D Logo T-shirt ~")
    embed.add_field(name="Badges (Lore)".format("null"), value="Little Dread Bested ~ Firezilla Challenge ~ Burning Man Challenge ~ River Stone ~")
    embed.add_field(name="Important!".format("null"), value="Type v.\"badgename\" for more details. name must be lowercase and cannot contain spaces, example: v.alphaknight.")
    await bot.say(embed=embed)
@bot.command()
async def hello():
    await bot.say("Hi :wave:")
    
    
#https://game.aq3d.com/account/Character
@bot.command()
async def echo(*, message: str):
    await bot.say(message)
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
token = os.environ.get("mybot")
bot.run(f'{token}')

