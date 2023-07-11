import React from 'react';
import { StyleSheet, Image, Text, Dimensions, View } from 'react-native';

import topo from '../../assets/topo.png';
import logo from '../../assets/logo.png';

const widht = Dimensions.get('screen').width;

export default function Cesta() {
    return <>
    <Image source={topo} style={estilos.topo} />
    <Text style={estilos.titulo} >Detalhes da Cesta</Text>

    <View style={estilos.cesta}>
        <Text style={estilos.nome}>Cesta de Verduras</Text>
        <View style={estilos.fazenda}>
            <Image source={logo} style={estilos.imagemFazenda} />
            <Text style={estilos.nomeFazenda}>Jenny Jack Farm</Text>
        </View>
        <Text style={estilos.descricao}>Uma cesta com produtos selecionados cuidadosamente. Da fazenda direto para sua cozinha</Text>
        <Text style={estilos.preco}>R$40,00</Text>
    </View>
    </>
}

const estilos = StyleSheet.create({
    topo: {
        width: '100%',
        height: 578/768 * widht,
    },
    titulo: {
        width: '100%',
        position: 'absolute',
        textAlign: 'center',
        fontSize: 16,
        lineHeight: 26,
        color: '#fff',
        fontWeight: 'bold',
        padding: 16,
    },
    cesta: {
        paddingVertical: 8,
        paddingHorizontal: 16,
    },
    nome: {
        fontSize: 26,
        lineHeight: 42,
        fontFamily: 'MontserratBold',
    },
    fazenda: {
        flexDirection: 'row',
        paddingVertical: 12,
    },
    imagemFazenda: {
        width: 32,
        height: 32,
    },
    nomeFazenda: {
        fontSize: 16,
        lineHeight: 26,
        marginLeft: 12,
        fontFamily: 'MontserratRegular',
    },
    descricao: {
        color: '#A3A3A3',
        fontSize: 16,
        lineHeight: 26,
    },
    preco: {
        color: '#2A9F85',
        fontWeight: 'bold',
        fontSize: 26,
        lineHeight: 42,
        marginTop: 8,
    },
});