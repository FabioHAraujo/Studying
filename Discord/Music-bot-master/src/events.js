const { ApplicationCommandOptionType, ActionRowBuilder, ButtonBuilder, EmbedBuilder } = require('discord.js');

player.on('error', (queue, error) => {
    console.log(`Error emitted from the queue ${error.message}`);
});

player.on('connectionError', (queue, error) => {
    console.log(`Error emitted from the connection ${error.message}`);
});

player.on('trackStart', (queue, track) => {
    if (!client.config.opt.loopMessage && queue.repeatMode !== 0) return;
    const embed = new EmbedBuilder()
    .setAuthor({name: `Começando a Tocar ${track.title} em ${queue.connection.channel.name} 🎧`, iconURL: track.requestedBy.avatarURL()})
    .setColor('#13f857')

    const back = new ButtonBuilder()
    .setLabel('Back')
    .setCustomId(JSON.stringify({ffb: 'back'}))
    .setStyle('Primary')

    const skip = new ButtonBuilder()
    .setLabel('Skip')
    .setCustomId(JSON.stringify({ffb: 'skip'}))
    .setStyle('Primary')

    const resumepause = new ButtonBuilder()
    .setLabel('Resume & Pause')
    .setCustomId(JSON.stringify({ffb: 'resume&pause'}))
    .setStyle('Danger')

    const loop = new ButtonBuilder()
    .setLabel('Loop')
    .setCustomId(JSON.stringify({ffb: 'loop'}))
    .setStyle('Secondary')
    
    const queuebutton = new ButtonBuilder()
    .setLabel('Queue')
    .setCustomId(JSON.stringify({ffb: 'queue'}))
    .setStyle('Secondary')

    const row1 = new ActionRowBuilder().addComponents(back, loop, resumepause, queuebutton, skip)
    queue.metadata.send({ embeds: [embed], components: [row1] })
});

player.on('trackAdd', (queue, track) => {
    queue.metadata.send(`A magia ${track.title} foi adicionada à fila! Explosion! 💥💣`);
  });
  
  player.on('botDisconnect', (queue) => {
    queue.metadata.send('Eu fui desconectada manualmente do canal de voz, limpando a fila... Explosion! ❌');
  });
  
  player.on('channelEmpty', (queue) => {
    queue.metadata.send('Não há ninguém no canal de voz, saindo do canal de voz... Explosion! ❌');
  });
  
  player.on('queueEnd', (queue) => {
    queue.metadata.send('Terminei de ler toda a fila de músicas. Explosion! ✅');
  });
  
  player.on('tracksAdd', (queue, tracks) => {
    queue.metadata.send(`Todas as músicas da playlist foram adicionadas à fila. Explosion! ✅`);
  });