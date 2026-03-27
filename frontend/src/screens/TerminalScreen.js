import React, { useState, useEffect, useRef } from 'react';
import { View, Text, TextInput, ScrollView, StyleSheet, TouchableOpacity } from 'react-native';

const TerminalScreen = () => {
  const [history, setHistory] = useState([{ text: 'Aegis-X Terminal Initialized...', type: 'sys' }]);
  const [input, setInput] = useState('');
  const scrollViewRef = useRef();

  const addLog = (text, type = 'output') => {
    setHistory(prev => [...prev, { text, type }]);
  };

  const sendCommand = async () => {
    if (!input.trim()) return;
    const cmd = input.trim();
    addLog(`> ${cmd}`, 'input');
    setInput('');

    try {
        // Example: Logic to route command to Flipper
        const response = await fetch('http://localhost:8000/flipper/exec', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command: cmd }),
        });
        const data = await response.json();
        addLog(data.output || 'Command executed.', 'output');
    } catch (err) {
        addLog('Error: Could not reach Gateway.', 'error');
    }
  };

  return (
    <View style={styles.container}>
      <ScrollView 
        style={styles.terminal}
        ref={scrollViewRef}
        onContentSizeChange={() => scrollViewRef.current.scrollToEnd({ animated: true })}
      >
        {history.map((line, i) => (
          <Text key={i} style={[styles.text, styles[line.type]]}>
            {line.text}
          </Text>
        ))}
      </ScrollView>

      <View style={styles.inputContainer}>
        <Text style={styles.prompt}>#</Text>
        <TextInput
          style={styles.input}
          value={input}
          onChangeText={setInput}
          onSubmitEditing={sendCommand}
          placeholder="Enter command..."
          placeholderTextColor="#444"
          autoCapitalize="none"
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000', padding: 10 },
  terminal: { flex: 1, marginBottom: 10 },
  inputContainer: { flexDirection: 'row', alignItems: 'center', borderTopWidth: 1, borderTopColor: '#333', paddingTop: 10 },
  prompt: { color: '#0f0', fontWeight: 'bold', marginRight: 10 },
  input: { flex: 1, color: '#0f0', fontFamily: 'monospace' },
  text: { fontFamily: 'monospace', fontSize: 14, marginBottom: 2 },
  sys: { color: '#0af' },
  input: { color: '#0f0' },
  output: { color: '#ccc' },
  error: { color: '#f00' }
});

export default TerminalScreen;
