const { Client, Permissions } = require('discord.js');

/*const client = new Client({
  intents: [Intents.FLAGS.Guilds, Intents.FLAGS.GuildMembers, Intents.FLAGS.Messages],
});*/

module.exports = {
  name: 'explosion',
  description: 'Explode alguém e silencie-os por 10 minutos!',
  cooldown: 86400,
  guildOnly: true,
  permissions: [Permissions.FLAGS.MUTE_MEMBERS],

  async execute({ message, args }) {
    const member = message.mentions.members.first();

    if (!member)
      return message.reply('Você precisa mencionar um membro para explodir!');

    // Verifica se o usuário está em cooldown
    if (cooldowns.has(message.author.id)) {
      const remainingTime = cooldowns.get(message.author.id) - Date.now();
      const remainingHours = Math.floor(remainingTime / 3600000);
      const remainingMinutes = Math.ceil((remainingTime % 3600000) / 60000);

      return message.channel.send(
        `${message.author}, EI EI EI, VOCÊ JÁ EXPLODIU ALGUÉM HOJE! PODERÁ EXPLODIR NOVAMENTE EM ${remainingHours} HORAS E ${remainingMinutes} MINUTOS. MWAHAHAHAHAHA! 💥🔥💣`
      );
    }

    // Aplica o cooldown ao usuário
    cooldowns.set(message.author.id, Date.now() + 86400000);

    // Silencia o usuário mencionado por 10 minutos
    const muteRole = message.guild.roles.cache.find(role => role.name === 'EXPLODIDOS');
    await member.roles.add(muteRole, 'Comando de Explosão');

    message.channel.send(
      `EXPLOOOOOSIOOOON! O usuário ${member} FOI MUTADO POR 10 MINUTOS! BOOOOOM! MWAHAHAHAHAHA! 💥🔥💣 Encomenda de: ${message.author}!`
    );

    // Aguarda 10 minutos antes de remover o silenciamento
    await setTimeout(() => {
      member.roles.remove(muteRole, 'Comando de Explosão');
    }, 600000);

    const logMessage = `[${new Date().toISOString()}] ${message.author} usou o comando !explosion em ${member}`;
    writeLog(logMessage);
  },
};
