import React from 'react';
import {
  LineChart,
  BarChart,
  ScatterPlot,
  HeatMap,
  NetworkGraph
} from './charts';
import { 
  useQuantumData, 
  useTeamStats, 
  useHistoricalTrends 
} from '../hooks';
import { 
  Card, 
  Grid, 
  Select, 
  DateRangePicker,
  Button 
} from '../ui';

export const QuantumDashboard: React.FC = () => {
  const { quantumData, isLoading: isQuantumLoading } = useQuantumData();
  const { teamStats, isLoading: isStatsLoading } = useTeamStats();
  const { trends, isLoading: isTrendsLoading } = useHistoricalTrends();

  return (
    <div className="quantum-dashboard">
      <header className="dashboard-header">
        <h1>Quantum NFL Analytics</h1>
        <div className="controls">
          <Select
            label="Team"
            options={teamOptions}
            onChange={handleTeamChange}
          />
          <DateRangePicker
            startDate={startDate}
            endDate={endDate}
            onChange={handleDateChange}
          />
          <Button onClick={refreshData}>
            Refresh Data
          </Button>
        </div>
      </header>

      <Grid>
        {/* Quantum State Overview */}
        <Card title="Quantum State">
          <LineChart
            data={quantumData.stateHistory}
            xAxis="timestamp"
            yAxis="quantumRating"
            color="primary"
          />
        </Card>

        {/* Team Performance */}
        <Card title="Performance Metrics">
          <BarChart
            data={teamStats.performance}
            xAxis="metric"
            yAxis="value"
            color="secondary"
          />
        </Card>

        {/* Entanglement Network */}
        <Card title="Team Entanglement">
          <NetworkGraph
            nodes={quantumData.teams}
            edges={quantumData.entanglements}
            config={{
              nodeSize: 'quantumRating',
              edgeWidth: 'entanglementStrength'
            }}
          />
        </Card>

        {/* Historical Trends */}
        <Card title="Quantum Trends">
          <ScatterPlot
            data={trends.quantumHistory}
            xAxis="date"
            yAxis="value"
            size="impact"
            color="category"
          />
        </Card>

        {/* Rivalry Analysis */}
        <Card title="Rivalry Quantum States">
          <HeatMap
            data={quantumData.rivalryMatrix}
            xAxis="team1"
            yAxis="team2"
            value="quantumResonance"
            colorScale="viridis"
          />
        </Card>
      </Grid>

      {/* Real-time Updates */}
      <div className="real-time-feed">
        <h2>Live Updates</h2>
        <div className="updates-container">
          {quantumData.recentUpdates.map(update => (
            <UpdateCard
              key={update.id}
              type={update.type}
              content={update.content}
              timestamp={update.timestamp}
            />
          ))}
        </div>
      </div>

      {/* Performance Metrics */}
      <div className="metrics-section">
        <Card title="System Performance">
          <Grid columns={3}>
            <MetricCard
              title="API Response Time"
              value={metrics.apiLatency}
              unit="ms"
              trend={metrics.apiTrend}
            />
            <MetricCard
              title="Quantum Calculations"
              value={metrics.quantumOps}
              unit="ops/s"
              trend={metrics.opsTrend}
            />
            <MetricCard
              title="Prediction Accuracy"
              value={metrics.accuracy}
              unit="%"
              trend={metrics.accuracyTrend}
            />
          </Grid>
        </Card>
      </div>
    </div>
  );
};
