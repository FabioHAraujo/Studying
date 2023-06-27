require('dotenv').config(); 
const { Client, Intents } = require('discord.js');

const intents = new Intents();
intents.add(Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES);

const client = new Client({ intents: intents });
client.on("ready", () => { 
    console.log(`Logged in as ${client.user.tag}!`)
}) 
client.on("message", msg => { 
    if (msg.content === "ping") { 
        msg.reply("pong"); 
    } 
}) 
DISCORD_TOKEN="NjA1MjMwNzk4OTQ5NDQ5NzI4.GUBdPQ.gmEcNCdIeQPBA4wulDy8AWr-GDkOrfGrz15FwY";

client.login(process.env.DISCORD_TOKEN);