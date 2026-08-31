import React, { useState } from 'react';

export const TaxPlanningSimulator: React.FC = () => {
  const [income, setIncome] = useState(175000);
  const [stateCode, setStateCode] = useState('CA');

  return (
    <div className="space-y-6 text-white">
      <h1 className="text-2xl font-black">50-State Progressive Tax Planning Simulator</h1>
      <div className="grid grid-cols-2 gap-6 bg-slate-900 border border-slate-800 p-6 rounded-2xl">
        <div>
          <label className="text-xs text-slate-400 block mb-1">Gross Annual Household Income ($)</label>
          <input
            type="number"
            value={income}
            onChange={e => setIncome(Number(e.target.value))}
            className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2 text-sm"
          />
        </div>
        <div>
          <label className="text-xs text-slate-400 block mb-1">State Jurisdiction</label>
          <select
            value={stateCode}
            onChange={e => setStateCode(e.target.value)}
            className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2 text-sm"
          >
            <option value="CA">California (Top Marginal: 13.3%)</option>
            <option value="NY">New York (Top Marginal: 10.9%)</option>
            <option value="TX">Texas (0.0% State Income Tax)</option>
            <option value="FL">Florida (0.0% State Income Tax)</option>
            <option value="WA">Washington (Capital Gains: 7.0%)</option>
          </select>
        </div>
      </div>
    </div>
  );
};
