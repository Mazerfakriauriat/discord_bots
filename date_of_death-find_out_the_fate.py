# -*- coding: utf8 -*-

'''!Run through the console!'''

import discord
import random

dsa = [804395649210646589] #liost of users who tried the bot (I am in it). The list is automatically updated, and if the bot is turned off, I will add your IDs to list.

def death():
	date = [str(random.randint(1,28)),str(random.randint(1,12)),str(random.randint(2021, 2117))] #generating death date
	reason = "Тебя собьет машина", "Ты умрешь от сердечного приступа в полном одиночестве", "Ты будешь бороться с раком и не сможешь его победить", \
	"Тебя съедят дикие звери на прогулке в лесу", "Тебя похитят и убьют", "Твой дом ограбят и убьют тебя пока ты будешь спать", "Ты разобьешся на велосипеде", \
	"В твоем доме начнется пожар и ты сгоришь заживо", "Ты полетишь на самолете и он упадет", "Ты умрешь от ХОБЛ (загугли если не знаешь)", \
	"Ты закончишь жизнь самоубийством", "Ты умрешь в уличной драке", "Ты будешь воевать на войне и будешь взорван/застрелен", "Террористы взорвут/застрелят тебя", \
	"Ты умрешь от некачественной медицины", "Ты отравишься шавухой на вокзале и подхватишь холеру, от которой тебя не вылечат", \
	"Ты заболеешь гриппом и из-за осложнений умрешь", "Ты подскользнешься и ударишься головой", "Ты умрешь во время операции", "Тебя изобьют в тюрьме", \
	"Ты перевернешься на машине", "Ты умрешь от туберкулеза", "Ты будешь ремонтировать крышу и грохнешься" #list of death reasons
	return '.'.join(date), random.choice(reason)
class MyClient(discord.Client):

	async def on_ready(self):
		print("bot {0} started!".format(self.user))
		print("users who tried id: ")
		for i in dsa:
			print(i)
	async def on_message(self, message):
		global dsa
		if message.author.id == self.user.id:
			return
		elif message.author.id in dsa and message.content.startswith('!датасмерти'): #if you have already used the command, then you have already tested your fate
			await message.channel.send("Ты уже испытал свою судьбу!")
			print("{0} try to use command '!датасмерти' again. ID: {1}".format(message.author, message.author.id))
		elif message.content.startswith('!датасмерти') and not message.author.id in dsa: #if you entered the command '!датасмерти' 
			dsa.append(message.author.id)
			reason = death()[1]
			date = death()[0]
			await message.channel.send("Мои пророки говорят, что ты умрешь {0}. {1}!".format(date, reason)) #bot writes you a random date and reason
			print("{0} used command '!датасмерти'. date: {1} reason: {2} ID: {3}".format(message.author, date, reason, message.author.id))
		else:
			print("user {0} says: '{1}' ID: {2}".format(message.author, message.content,message.author.id))
client = MyClient()
client.run('token')