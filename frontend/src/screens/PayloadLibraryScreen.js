import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, TouchableOpacity, StyleSheet, Alert } from 'react-native';

const PayloadLibraryScreen = () => {
  const [payloads, setPayloads] = useState([]);

  useEffect(() => {
    fetch('https://localhost:8443/payloads')
      .then(res => res.json())
      .then(data => setPayloads(data));
  }, []);

  const triggerPayload = async (id, name) => {
    try {
      const res = await fetch(`http://localhost:8000/payloads/launch/${id}`, { method: 'POST' });
      if (res.ok) Alert.alert("Success", `Sent ${name} signal.`);
    } catch (e) {
      Alert.alert("Error", "Could not reach Gateway.");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>PAIRED PAYLOADS</Text>
      <FlatList
        data={payloads}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <TouchableOpacity 
            style={styles.card} 
            onPress={() => triggerPayload(item.id, item.name)}
          >
            <View>
              <Text style={styles.name}>{item.name}</Text>
              <Text style={styles.meta}>{item.frequency} MHz | {item.type}</Text>
            </View>
            <Text style={styles.launchBtn}>▶</Text>
          </TouchableOpacity>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000', padding: 20 },
  header: { color: '#0f0', fontSize: 18, fontWeight: 'bold', marginBottom: 20, textAlign: 'center' },
  card: { 
    backgroundColor: '#111', padding: 15, borderRadius: 8, marginBottom: 10, 
    flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center',
    borderWidth: 1, borderColor: '#222'
  },
  name: { color: '#fff', fontSize: 16, fontWeight: 'bold' },
  meta: { color: '#666', fontSize: 12 },
  launchBtn: { color: '#0f0', fontSize: 24 }
});

export default PayloadLibraryScreen;
