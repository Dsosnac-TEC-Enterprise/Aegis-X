import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import TerminalScreen from './src/screens/TerminalScreen';
import MeshMapScreen from './src/screens/MeshMapScreen';
import SignalVisualizer from './src/screens/SignalVisualizer';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator screenOptions={{ 
        tabBarStyle: { backgroundColor: '#111' }, 
        tabBarActiveTintColor: '#0f0',
        headerStyle: { backgroundColor: '#000' },
        headerTintColor: '#0f0'
      }}>
        <Tab.Screen name="Terminal" component={TerminalScreen} />
        <Tab.Screen name="Mesh Map" component={MeshMapScreen} />
        <Tab.Screen name="SDR View" component={SignalVisualizer} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}
