import React, { useState, useEffect } from 'react';
import { View, Text, Dimensions, StyleSheet, TouchableOpacity } from 'react-native';
import { LineChart } from 'react-native-chart-kit';

const SignalVisualizer = () => {
  const [chartData, setChartData] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchSweep = async () => {
    setLoading(true);
    try {
      const response = await fetch('https://localhost:8443/sdr/sweep?start=2400&end=2500');
      const data = await response.json();
      if (!data.error) setChartData(data);
    } catch (e) {
      console.error("Failed to fetch sweep:", e);
    }
    setLoading(false);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Aegis-X Spectrum Analyzer</Text>
      
      {chartData ? (
        <LineChart
          data={chartData}
          width={Dimensions.get('window').width - 40}
          height={256}
          chartConfig={{
            backgroundColor: '#000',
            backgroundGradientFrom: '#000',
            backgroundGradientTo: '#111',
            decimalPlaces: 1,
            color: (opacity = 1) => `rgba(0, 255, 0, ${opacity})`,
            labelColor: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
            style: { borderRadius: 16 },
            propsForDots: { r: '4', strokeWidth: '2', stroke: '#0f0' }
          }}
          bezier
          style={styles.chart}
        />
      ) : (
        <View style={styles.placeholder}><Text style={{color: '#555'}}>No Data Captured</Text></View>
      )}

      <TouchableOpacity style={styles.button} onPress={fetchSweep} disabled={loading}>
        <Text style={styles.buttonText}>{loading ? 'SWEEPING...' : 'RUN RF SWEEP'}</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000', padding: 20, alignItems: 'center' },
  title: { color: '#0f0', fontSize: 20, fontWeight: 'bold', marginBottom: 20 },
  chart: { marginVertical: 8, borderRadius: 16 },
  placeholder: { height: 256, justifyContent: 'center', alignItems: 'center', width: '100%', borderStyle: 'dashed', borderWidth: 1, borderColor: '#333' },
  button: { backgroundColor: '#0f0', padding: 15, borderRadius: 10, width: '100%', marginTop: 20 },
  buttonText: { color: '#000', textAlign: 'center', fontWeight: 'bold' }
});

export default SignalVisualizer;
