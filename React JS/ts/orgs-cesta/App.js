import React from 'expo-status-bar';
import { Text, View, StyleSheet, StatusBar, SafeAreaView } from 'react-native';
import Cesta from './src/views/Cesta';
import { useFonts, Montserrat_400Regular, Montserrat_700Bold } from '@expo-google-fonts/montserrat';

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
      <Cesta />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  carregando: {
    color: '#fff',
  }
});