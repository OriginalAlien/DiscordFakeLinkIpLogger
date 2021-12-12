import discord
from discord.ext import commands

client = commands.Bot(command_prefix="dw about this :D")
#ignore above

print("""
____ ____ _  _ ____    _    _ _  _ _  _    _ ___     _    ____ ____ ____ ____ ____ 
|___ |__| |_/  |___    |    | |\ | |_/     | |__]    |    |  | | __ | __ |___ |__/ 
|    |  | | \_ |___    |___ | | \| | \_    | |       |___ |__| |__] |__] |___ |  \ 
\n""")
#PLEASE NOTE THAT IF YOU USE THIS AS A SELF BOT THEN YOUR ACC CAN GET BANNED I'M NOT RESPONSIBLE IF ANYTHING BAD HAPPENS TO YOU
#theres a **VERY** **VERY** small chance of you getting banned when using it as a self bot/ using it on ur main, anyways enjoy! :)
continue0 = True
print("Made By kunai#5936 (aka sigma#4268, it got disabled)\nGithub: https://github.com/OriginalAlien\nEnjoy And Contact For Help")
tkn = input("\nWorks For Both Bot And Main/Alts\nToken: ")
message = input("Message To Send: ")
website_name = input("Website's Name: ")
website_description = input("Website's Embedded Description: ")
website_img = input("Website's Embedded Image Link:  ")
ip_link = input("IP Grabber Link: ")

fakelink=discord.Embed(title=website_name, url=ip_link, description=website_description) #creating embed with given/input
fakelink.set_thumbnail(url=website_img) #adding the website's embedded img on discord to the embed
print("\nEmbed Created!\n")

@client.event
async def on_ready():
	try: #error catch
		server_id = int(input("Enter Server ID: "))
		channel_id = int(input("Enter Channel ID: "))
	except ValueError: #error solve
		print("\nError: ValueError\nPlease Enter Valid Server/Channel ID Without Quotes And In Only Integers/Whole Numbers.")
		server_id = int(input("Enter Server ID: "))
		channel_id = int(input("Enter Channel ID: "))

	server = client.get_guild(server_id) #access server by id
	channel = client.get_channel(channel_id) #access server's channel by id
	send = input("\nAll Set!\nSend Fake Link?\nType \"y\" To Send: ")
	if send.lower() == "y": #if you type yes then
		await channel.send(message, embed=fakelink) #sends message and embed
		print(f'\nSent in {server.name}, #{channel.name}') #shows where it sent
		while continue0 == True: #turn to False to stop the code below from executing
			again = input("\nSend Again?\nType \"y\" To Send Again\nType \"n\" To Stop\n\nSend Again?: ")
			if again.lower() == "y": #if you typed "y" then it sends again
				await channel.send(message, embed=fakelink) #sends message and embed
				print(f'Sent in {server.name}, #{channel.name}') #shows where it sent
			elif again.lower() == "n": #or else if u type "n" it breaks the loop and since its the end, it also ends.
				print("\nGood Bye Have A Good Day/Night! :) 👋")
				break
				
	elif send.lower() == "":
		while send == "":
			send = input("\nSend Fake Link?\nType \"y\" To Send: ")
			if send.lower() == "y":
				break
		await channel.send(message, embed=fakelink) #sends message and embed
		print(f'\nSent in {server.name}, #{channel.name}') #shows where it sent
		while continue0 == True: #turn to False to stop the code below from executing
			again = input("\nSend Again?\nType \"y\" To Send Again\nType \"n\" To Stop\n\nSend Again?: ")
			if again.lower() == "y": #if you typed "y" then it sends again
				await channel.send(message, embed=fakelink) #sends message and embed
				print(f'Sent in {server.name}, #{channel.name}') #shows where it sent
			elif again.lower() == "n": #or else if u type "n" it breaks the loop and since its the end, it also ends.
				print("\nGood Bye Have A Good Day/Night! :) 👋")
				break

client.run(tkn, bot=False) #runs code when executed
