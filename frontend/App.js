import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, FlatList, TouchableOpacity } from 'react-native';

export default function App() {
  const [gatewayStatus, setGatewayStatus] = useState('Connecting to Aegis-X...');
  const [devices, setDevices] = useState([]);

  // Fetch data from our Python backend
  const fetchGatewayData = async () => {
    try {
      // Note: Replace this IP with your computer's local IP when testing on a real mobile device
      const response = await fetch('https://127.0.0.1:8443/devices'); 
      const data = await response.json();
      setGatewayStatus('Aegis-X ONLINE 💪🏾');
      setDevices(data.devices);
    } catch (error) {
      setGatewayStatus('Gateway Offline');
    }
  };

  useEffect(() => {
    fetchGatewayData();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Aegis-X Terminal</Text>
      <Text style={styles.status}>{gatewayStatus}</Text>
      
      <Text style={styles.subHeader}>Detected Nodes:</Text>
      <FlatList
        data={devices}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <View style={styles.deviceCard}>
            <Text style={styles.deviceText}>{item.type} - {item.status}</Text>
          </View>
        )}
      />
      <TouchableOpacity style={styles.button} onPress={fetchGatewayData}>
        <Text style={styles.buttonText}>Scan Network</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#121212', padding: 40 },
  header: { color: '#00FF00', fontSize: 28, fontWeight: 'bold', marginBottom: 10 },
  status: { color: '#AAAAAA', fontSize: 16, marginBottom: 30 },
  subHeader: { color: '#FFFFFF', fontSize: 20, marginBottom: 15 },
  deviceCard: { backgroundColor: '#1E1E1E', padding: 15, marginBottom: 10, borderRadius: 5, borderLeftWidth: 4, borderLeftColor: '#00FF00' },
  deviceText: { color: '#FFFFFF', fontSize: 16 },
  button: { backgroundColor: '#00FF00', padding: 15, borderRadius: 5, alignItems: 'center', marginTop: 20 },
  buttonText: { color: '#000000', fontWeight: 'bold', fontSize: 16 }
});

import { ThemeProvider } from './src/context/ThemeContext';
import AuthGate from './src/components/AuthGate';

export default function App() {
  return (
    <ThemeProvider>
      <AuthGate>
        <NavigationContainer>
          {/* ... all your Tab screens go here ... */}
        </NavigationContainer>
      </AuthGate>
    </ThemeProvider>
  );
}

