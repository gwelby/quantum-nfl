import React, { useState, useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { QueryClient, QueryClientProvider } from 'react-query';
import { ThemeProvider } from './src/theme';
import { 
  HomeScreen, 
  TeamsScreen, 
  PredictionsScreen, 
  QuantumStatsScreen 
} from './src/screens';
import { QuantumProvider } from './src/context/QuantumContext';
import { useQuantumWebSocket } from './src/hooks/useQuantumWebSocket';

const Tab = createBottomTabNavigator();
const queryClient = new QueryClient();

export default function App() {
  const [isLoading, setIsLoading] = useState(true);
  const { connect, disconnect } = useQuantumWebSocket();

  useEffect(() => {
    connect();
    return () => disconnect();
  }, []);

  if (isLoading) {
    return <SplashScreen />;
  }

  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider>
        <QuantumProvider>
          <NavigationContainer>
            <Tab.Navigator>
              <Tab.Screen 
                name="Home" 
                component={HomeScreen} 
                options={{ tabBarIcon: HomeIcon }} 
              />
              <Tab.Screen 
                name="Teams" 
                component={TeamsScreen} 
                options={{ tabBarIcon: TeamsIcon }} 
              />
              <Tab.Screen 
                name="Predictions" 
                component={PredictionsScreen} 
                options={{ tabBarIcon: PredictionsIcon }} 
              />
              <Tab.Screen 
                name="Quantum" 
                component={QuantumStatsScreen} 
                options={{ tabBarIcon: QuantumIcon }} 
              />
            </Tab.Navigator>
          </NavigationContainer>
        </QuantumProvider>
      </ThemeProvider>
    </QueryClientProvider>
  );
}
