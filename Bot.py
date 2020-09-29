import discord
import asyncio
import random
import time
from discord import File 

client=discord.Client()

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("Watching Helluva Boss😈"))
  print("Congrats!")
  print("Logged in as :",client.user.name)
  print("ID ;",client.user.id)
  print (time.strftime("Started At %H:%M"))

##################################################################################################################""
@client.event
async def on_message(message):
 if message.content=="!ping":
    await message.channel.send(":ping_pong:**Pong!**")

 elif message.content=="!testping":
    await message.channel.send(f':signal_strength: {round(client.latency * 1000)}ms')

 elif message.content=="!credits":
     await message.channel.send("Bot Created by :ribbon:@iamdanychock:ribbon:")
     await message.channel.send("Version 2.0")

 elif message.content=="!help":
    await message.channel.send(" +====-Liste De Commandes-====+")
    await message.channel.send("!help : Affiche les commandes")
    await message.channel.send("!ping : Pong")
    await message.channel.send("!credits : Bah les crédits")

 elif message.content=="!hazbinquotes":
      await message.channel.send(random.choice(Hazbin_Quotes))
 
 elif message.content=="!emoji.test":
     await message.channel.send("<:Vaggie:650059908955373597>")
 
 elif message.content=="!gif.test":
     await File.channel.send(fp, filename='Maybe.gif')

###############################################################################
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 649274572033490955:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == "much":
            role = discord.utils.get(guild.roles, name='Angels')
        elif payload.emoji.name == ":smiling_imp:":
            role = discord.utils.get(guilds, name="Sinners")
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 649274572033490955:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == "crown":
            role = discord.utils.get(guild.roles, name="King")
        elif payload.emoji.name == "ok_hand":
            role = discord.utils.get(guilds, name="Sous-King")
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guilds.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("Member not found.")
        else:
            print("Role not found.")

################################################################################
Hazbin_Quotes = ["Hel...lo! May I speak now? <:Alastor:650048983426662411>", "Dear, if I wanted to hurt anyone here, I would have done so already... <:Alastor:650048983426662411>","Help! Hahaha! Hello? Ha, is this thing on? Testing, testing! <:Alastor:650048983426662411>", "Hahaha! Why does anyone do anything? Sheer, absolute boredom!  <:Alastor:650048983426662411>", "Smile, my dear! You know, you're never fully dressed without one!  <:Alastor:650048983426662411>", "Do I know you?  <:Alastor:650048983426662411>", "HA! No.  <:Alastor:650048983426662411>", "Well, I'm starved! Who wants some Jambalaya?  <:Alastor:650048983426662411>",
 "It was a quick cash grab, ya got it?  <:Angel_Dust:650048954095894549>", "Ouch! Oooh~! Such an insult. Let me know when you find something creative to call me, you sack of poorly packaged horse shit!  <:Angel_Dust:650048954095894549>", "Oh my god! My drugs! Dammit!  <:Angel_Dust:650048954095894549>", "I can suck your dick.  <:Angel_Dust:650048954095894549>", "Wait. Would that make me double-dead? Then where exactly where do I go? To double-hell?! Hahaha, sorry, you're stuck with me bitch. Get used to it.  <:Angel_Dust:650048954095894549>", "He looks like a strawberry pimp!  <:Angel_Dust:650048954095894549>" , "Nonono, babe, jokes are funny. I made you look, uh, sad, and pathetic! Like an orphan, with no arms or legs...uh, oh! With Progeria!  <:Angel_Dust:650048954095894549>", "Everyone wants some of me, and I got the creepy fan letters to prove it~  <:Angel_Dust:650048954095894549>" ,"Ooooh! Harder daddy!  <:Angel_Dust:650048954095894549>", "Only if you watch me~  <:Angel_Dust:650048954095894549>", "I've been clean for two weeks! Well...Sorta clean. Just clean as you can get while doing a SHITLOAD of Bolivian marching powder.  <:Angel_Dust:650048954095894549>", "Would that make your hat the top and you the bottom?  <:Angel_Dust:650048954095894549>", 
 "Stop right there! Cabrón hijo de perra! I know your game! And I'm not gonna let you hurt anyone! You pompous, cheesy talk show shitlord!  <:Vaggie:650059908955373597>", "Your credibility? What about the hotel's? Your little stunt made us look like a fucking joke!  <:Vaggie:650059908955373597>", "Was that you trying to be sexist, or racist?  <:Vaggie:650059908955373597>", 
 "Not so cocky now, Are We!?  <:Sir_Pentious:650060721689722890>", "HAHAHA! I'm so evil!  <:Sir_Pentious:650060721689722890>", "No other demon can compare to the likes of I!  <:Sir_Pentious:650060721689722890>", "WHAT did you just say to ME, you fried chicken FETUSES?!  <:Sir_Pentious:650060721689722890>", "Oh, you want to go, Missy? Well, I'm happy to oblige!  <:Sir_Pentious:650060721689722890>", "You whores have no class! In war, the side remembered is the side with the most...style!  <:Sir_Pentious:650060721689722890>", "Oh, well, THAT'S none of your goddamn business! Now, is it?  <:Sir_Pentious:650060721689722890>", "Oh, not like that, pervert.  <:Sir_Pentious:650060721689722890>","SON?!  <:Sir_Pentious:650060721689722890>",
  "Go fuck yourself.  <:Husk:650063020638208060>", "I've lost the ability to love years ago.  <:Husk:650063020638208060>", "Don't you 'Husker' me you son of a bitch! I was about to win the whole damn pot!  <:Husk:650063020638208060>", "You thought it would be some kind of big fucking riot just to pull me out of nowhere? You think I'm some kind of fucking clown!?  <:Husk:650063020638208060>", 
  "Hi, I'm Niffty! It's nice to meet you! It's been a while since I've made new friends!  <:Niffty:650063079429636096>", "This place is awful! It really needs a lady's touch! Which is weird because you're ladies, no offense.  <:Niffty:650063079429636096>", 
  "Where've you been anyway? I thought you up and died or some shit.  <:Cherri:650059971454566431>", "EdgeLord!  <:Cherri:650059971454566431>", "You looking for a FIGHT, old man?  <:Cherri:650059971454566431>", "Why don't you get that tinker toy BULLSHIT off my turf before I SMASH it!...More.  <:Cherri:650059971454566431>", 
  "You are a limpdick jackass, Tom. Or should I say, no dick?  <:Katie:650046476008816650>", "Suck it up, you little bitch.  <:Katie:650046476008816650>", "I d say its a pleasure to meet you, but that would be a lie.  You can put that away, I don t touch the gays. I have standards.  <:Katie:650046476008816650>","What in the nine circles makes you think a single denizen of hell would give two shits about becoming a better person?  <:Katie:650046476008816650>", "You want people to be good, just... because?!  <:Katie:650046476008816650>", "Im sure you can get that hooker to do anything with enough booger sugar and lube.  <:Katie:650046476008816650>", "Well, it sure looks like your little project is dead on arrival. Tell us, how does it feel to be such a total failure?  <:Katie:650046476008816650>",
   "How does it feel that I got your pen, hum!? BITCH!  <:Charlie:650059939699490827> ", "As Princess of Hell and heir to the throne I...er...herby order that you help with this hotel...For as long as you desire.  <:Charlie:650059939699490827>" ,  "I picked up ONE thing from my dad: (deep voice) You don t take shit from other demons!  <:Charlie:650059939699490827>", "Ladies and gentlemen, I m opening the first of its kind, a hotel that rehabilitates sinners!  <:Charlie:650059939699490827>", "Ya know...Cause hotels are for people passing through...temporarily...  <:Charlie:650059939699490827>"]

#####################################################################################################################


client.run('NjI3NDUzODUxNDA2MDQxMTM5.XY837w.CCON0uQ0AoZ7ula8PwpTuMb5QeQ')
