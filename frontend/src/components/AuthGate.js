import React, { useState } from 'react';
import { View, Text, TextInput, StyleSheet, TouchableOpacity } from 'react-native';
import { useTheme } from '../context/ThemeContext';

const AuthGate = ({ children }) => {
  const [pin, setPin] = useState('');
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const { colors } = useTheme();

  const MASTER_PIN = "1337"; // In production, move this to encrypted storage

  const handleAuth = () => {
    if (pin === MASTER_PIN) {
      setIsAuthenticated(true);
    } else {
      alert("ACCESS DENIED: Invalid Credentials");
      setPin('');
    }
  };

  if (!isAuthenticated) {
    return (
      <View style={[styles.container, { backgroundColor: colors.background }]}>
        <Text style={[styles.title, { color: colors.primary }]}>🛡️ AEGIS-X SECURE LOGIN</Text>
        <TextInput
          style={[styles.input, { color: colors.primary, borderColor: colors.primary }]}
          placeholder="ENTER OPERATOR PIN"
          placeholderTextColor={colors.muted}
          secureTextEntry
          keyboardType="numeric"
          maxLength={4}
          value={pin}
          onChangeText={setPin}
        />
        <TouchableOpacity 
          style={[styles.button, { backgroundColor: colors.primary }]} 
          onPress={handleAuth}
        >
          <Text style={styles.buttonText}>INITIALIZE SESSION</Text>
        </TouchableOpacity>
      </View>
    );
  }

  return children;
};

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 40 },
  title: { fontSize: 18, fontWeight: 'bold', marginBottom: 30, fontFamily: 'monospace' },
  input: { width: '100%', borderWidth: 1, padding: 15, textAlign: 'center', fontSize: 24, letterSpacing: 10, marginBottom: 20 },
  button: { width: '100%', padding: 15, borderRadius: 5 },
  buttonText: { textAlign: 'center', fontWeight: 'bold', color: '#000' }
});

export default AuthGate;
