import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Dimensions } from 'react-native';

const MeshMapScreen = () => {
  const [nodes, setNodes] = useState([]);

  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const response = await fetch('http://localhost:8000/mesh/nodes'); // We'll add this endpoint
        const data = await response.json();
        setNodes(Object.values(data.nodes));
      } catch (e) { console.log("Mesh fetch failed"); }
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Aegis-X Mesh Topology</Text>
      <View style={styles.mapArea}>
        {nodes.map((node, index) => (
          <View 
            key={node.id} 
            style={[styles.node, { top: 50 + (index * 80), left: 50 + (index * 30) }]}
          >
            <View style={styles.pulse} />
            <Text style={styles.nodeLabel}>{node.id}</Text>
          </View>
        ))}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0a0a0a', padding: 20 },
  title: { color: '#00ff00', fontSize: 18, fontWeight: 'bold', textAlign: 'center' },
  mapArea: { flex: 1, marginTop: 20, borderStyle: 'dashed', borderWidth: 1, borderColor: '#333' },
  node: { position: 'absolute', alignItems: 'center' },
  nodeLabel: { color: '#fff', fontSize: 10, marginTop: 5 },
  pulse: { width: 15, height: 15, borderRadius: 7.5, backgroundColor: '#00ff00', shadowColor: '#00ff00', shadowOpacity: 1, shadowRadius: 10 }
});

export default MeshMapScreen;
