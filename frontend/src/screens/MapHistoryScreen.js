import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import MapView, { Marker, Callout } from 'react-native-maps';
import { useTheme } from '../context/ThemeContext';

const MapHistoryScreen = () => {
  const [history, setHistory] = useState([]);
  const { colors } = useTheme();

  useEffect(() => {
    fetch('https://localhost:8443/system/map-history')
      .then(res => res.json())
      .then(data => setHistory(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <View style={styles.container}>
      <MapView
        style={styles.map}
        initialRegion={{
          latitude: history.length > 0 ? history[0].latitude : 0,
          longitude: history.length > 0 ? history[0].longitude : 0,
          latitudeDelta: 0.05,
          longitudeDelta: 0.05,
        }}
        customMapStyle={darkMapStyle} // Custom Hacker/Dark mode
      >
        {history.map((point, index) => (
          <Marker
            key={index}
            coordinate={{ latitude: point.latitude, longitude: point.longitude }}
            pinColor={point.type === 'FLIPPER' ? colors.primary : colors.secondary}
          >
            <Callout>
              <View style={styles.callout}>
                <Text style={styles.calloutType}>{point.type}</Text>
                <Text style={styles.calloutMsg}>{point.message}</Text>
                <Text style={styles.calloutTime}>{point.timestamp}</Text>
              </View>
            </Callout>
          </Marker>
        ))}
      </MapView>
    </View>
  );
};

const darkMapStyle = [/* Standard Google Maps Dark JSON goes here for that Cyberpunk look */];

const styles = StyleSheet.create({
  container: { flex: 1 },
  map: { width: '100%', height: '100%' },
  callout: { padding: 10, minWidth: 150 },
  calloutType: { fontWeight: 'bold', color: '#000' },
  calloutMsg: { fontSize: 12, color: '#333' },
  calloutTime: { fontSize: 10, color: '#999' }
});

export default MapHistoryScreen;
