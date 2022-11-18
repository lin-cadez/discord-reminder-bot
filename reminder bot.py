import discord
import datetime
import requests
from lxml import html
from discord.ext import commands,tasks
intents = discord.Intents().all()

client = commands.Bot(command_prefix='!',intents=intents)
cajt=datetime.datetime.today().weekday()
myid = '@everyone'
print(cajt)


@client.event
async def on_ready():
	channel = client.get_channel(1040656031807701062) #channel id here
	print(channel)

	if cajt==1 or cajt==0:	
		embed = discord.Embed(
	        title="Opomnik za KROKY ❤😍❤",
	        description="Naroč si malco! Priporočam!!!")
		embed.add_field(name="Urbi priporoča!", value="BUREK❤❤❤")
		await channel.send(embed=embed)
		await channel.send(myid)





if __name__ == "__main__" :
	client.run(token)

