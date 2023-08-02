import React from 'expo-status-bar';
import { Text, View, StyleSheet, StatusBar, SafeAreaView } from 'react-native';
import { useFonts, Montserrat_400Regular, Montserrat_700Bold } from '@expo-google-fonts/montserrat';
import Cesta from './src/views/Cesta';
import mock from './src/mocks/cesta';

export default function App() {
  const [fontesCarregadas] = useFonts({
    'MontserratRegular': Montserrat_400Regular,
    'MontserratBold': Montserrat_700Bold,
  });

  if (!fontesCarregadas) {
     return <View>
       <Text style={styles.carregando} >Carregando...</Text>
       </View>;
  };
  return (
    <SafeAreaView>
      <StatusBar/>
      <Cesta {...mock}/>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  carregando: {
    color: '#fff',
  }
});