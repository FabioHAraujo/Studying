const { ApplicationCommandOptionType, PermissionsBitField, userMention } = require('discord.js');

const cooldowns = new Map();
const roleID = '1123558107021332540'; // ID da função "EXPLODIDOS"

module.exports = {
  name: 'explosion',
  usage: 'explosin <@user>',
  description: 'Explode alguém e o silencia por 10 minutos!',
  cooldown: 86400,
  options: [
    {
        name: 'usuario',
        description: 'O usuário que você quer explodir',
        type: ApplicationCommandOptionType.User,
        required: true,
    }
  ],
  permissions: PermissionsBitField.All,
  async execute({ inter}) {
    const member = inter.options.getUser('usuario');
    if (!member)
      return inter.reply('Você precisa mencionar um membro para explodir!');

    // Verifica se o usuário está em cooldown
    if (cooldowns.has(inter.member)) {
      const remainingTime = cooldowns.get(inter.member) - Date.now();
      const remainingHours = Math.floor(remainingTime / 3600000);
      const remainingMinutes = Math.ceil((remainingTime % 3600000) / 60000);

      return inter.reply(
        `${inter.member}, EI EI EI, VOCÊ JÁ EXPLODIU ALGUÉM HOJE! PODERÁ EXPLODIR NOVAMENTE EM ${remainingHours} HORAS E ${remainingMinutes} MINUTOS. MWAHAHAHAHAHA! 💥🔥💣`
      );
    }

    // Aplica o cooldown ao usuário
    cooldowns.set(inter.user.id, Date.now() + 86400000);

    const role = inter.guild.roles.cache.get(roleID);
    member.roles.add(role, 'Comando de Explosão');

    /*member.roles.add(muteRole, 'Comando de Explosão');
    member.voice.setMute(true, 'Comando de Explosão');
    member.voice.setDeaf(true, 'Comando de Explosão');

    setTimeout(() => {
      member.roles.remove(muteRole, 'Comando de Explosão');
      member.voice.setMute(false, 'Remoção de Silenciamento');
      member.voice.setDeaf(false, 'Remoção de Silenciamento');
    }, 600000);*/
    inter.reply(
      `EXPLOOOOOSIOOOON! O usuário ${member} FOI MUTADO POR 10 MINUTOS! BOOOOOM! MWAHAHAHAHAHA! 💥🔥💣 Encomenda de: ${inter.member}!`
    );

    // Aguarda 10 minutos antes de remover o silenciamento
    await setTimeout(() => {
      member.roles.remove(muteRole, 'Comando de Explosão');
    }, 600000);

    /*const logMessage = `[${new Date().toISOString()}] ${inter.member} usou o comando !explosion em ${member}`;
    writeLog(logMessage);*/
  },
};
