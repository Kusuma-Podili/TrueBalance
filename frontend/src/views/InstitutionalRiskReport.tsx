import React from 'react';

export const InstitutionalRiskReport: React.FC = () => {
  return (
    <div className="space-y-6 text-white">
      <div className="flex justify-between items-center pb-4 border-b border-slate-800">
        <div>
          <h1 className="text-2xl font-black">Institutional Risk & Stress Testing Report</h1>
          <p className="text-xs text-slate-400">Basel III Capital Adequacy & Econometric Factor Decomposition</p>
        </div>
        <button className="px-4 py-2 bg-emerald-600 font-bold text-xs rounded-xl">
          Export Basel III Audit PDF
        </button>
      </div>
      <div className="grid grid-cols-3 gap-6">
        <div className="p-5 bg-slate-900 border border-slate-800 rounded-2xl">
          <span className="text-xs text-slate-400 uppercase font-bold">Value at Risk (99% 10-Day)</span>
          <p className="text-2xl font-black text-rose-400 mt-1 font-mono">$14,250.00</p>
        </div>
        <div className="p-5 bg-slate-900 border border-slate-800 rounded-2xl">
          <span className="text-xs text-slate-400 uppercase font-bold">Conditional VaR (Expected Shortfall)</span>
          <p className="text-2xl font-black text-amber-400 mt-1 font-mono">$19,820.00</p>
        </div>
        <div className="p-5 bg-slate-900 border border-slate-800 rounded-2xl">
          <span className="text-xs text-slate-400 uppercase font-bold">Sharpe / Sortino Ratio</span>
          <p className="text-2xl font-black text-indigo-400 mt-1 font-mono">2.14 / 3.08</p>
        </div>
      </div>
    </div>
  );
};
