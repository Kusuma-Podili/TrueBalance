import React from 'react';
import { MonteCarloSimulationResult } from '../../types/financial';

interface MonteCarloFanChartProps {
  simulationData: MonteCarloSimulationResult;
}

export const MonteCarloFanChart: React.FC<MonteCarloFanChartProps> = ({ simulationData }) => {
  const { years, successRatePercentage, medianTerminalWealth, percentileTrajectory } = simulationData;

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 text-white shadow-xl">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="text-lg font-bold">Retirement Wealth Projection</h3>
          <p className="text-xs text-slate-400">10,000-path stochastic Monte Carlo simulation ({years}-year horizon)</p>
        </div>
        <div className="text-right">
          <span className="text-xs text-slate-400">Plan Success Probability</span>
          <p className="text-2xl font-black text-emerald-400">{successRatePercentage}%</p>
        </div>
      </div>

      <div className="h-64 flex items-end justify-between gap-1 pt-6 pb-2 border-b border-slate-800">
        {percentileTrajectory.p50_median.map((val, idx) => {
          const maxVal = Math.max(...percentileTrajectory.p90);
          const heightPct = (val / maxVal) * 100;
          return (
            <div key={idx} className="flex-1 flex flex-col items-center group relative">
              <div
                className="w-full bg-indigo-500/80 hover:bg-indigo-400 rounded-t transition-all"
                style={{ height: `${Math.max(4, heightPct)}%` }}
              />
              <span className="text-[10px] text-slate-500 mt-2">Y{idx}</span>
              <div className="hidden group-hover:block absolute -top-10 bg-slate-800 text-xs px-2 py-1 rounded shadow pointer-events-none">
                ${val.toLocaleString()}
              </div>
            </div>
          );
        })}
      </div>

      <div className="flex items-center justify-between text-xs text-slate-400 mt-4">
        <div>
          <span className="block font-medium text-slate-300">Worst Case (10th Percentile)</span>
          <span>${simulationData.worst10PercentileTerminalWealth.toLocaleString()}</span>
        </div>
        <div className="text-center">
          <span className="block font-medium text-slate-300">Median Expected Wealth</span>
          <span className="text-indigo-400 font-bold">${medianTerminalWealth.toLocaleString()}</span>
        </div>
        <div className="text-right">
          <span className="block font-medium text-slate-300">Best Case (90th Percentile)</span>
          <span>${simulationData.best10PercentileTerminalWealth.toLocaleString()}</span>
        </div>
      </div>
    </div>
  );
};
