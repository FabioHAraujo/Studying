const { Client, Intents } = require('discord.js');

const client = new Client({ intents: ["GUILDS", "GUILD_MESSAGES"] });


client.on('ready', () => {
 console.log(`Logged in as ${client.user.tag}!`);
 });

client.on('message', msg => {
 if (msg.content === '!bakuretsu') {
 msg.reply('BAKURESTU MAHOOOOOU! EEEEKUUSPROOOOGIOOOOON! *BOOM*');
 }
 });

client.login('NjA1MjMwNzk4OTQ5NDQ5NzI4.GUBdPQ.gmEcNCdIeQPBA4wulDy8AWr-GDkOrfGrz15FwY');