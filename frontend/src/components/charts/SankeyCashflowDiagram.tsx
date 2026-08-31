import React from 'react';

interface SankeyCashflowProps {
  incomeSources: { name: string; amount: number }[];
  expenseCategories: { name: string; amount: number }[];
}

export const SankeyCashflowDiagram: React.FC<SankeyCashflowProps> = ({ incomeSources, expenseCategories }) => {
  const totalIncome = incomeSources.reduce((s, i) => s + i.amount, 0);
  const totalExpenses = expenseCategories.reduce((s, e) => s + e.amount, 0);

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 text-white shadow-xl">
      <h3 className="text-lg font-bold mb-2">Cash Flow Sankey Flow</h3>
      <p className="text-xs text-slate-400 mb-6">Visualizes income streams flowing through allocations, expenses, and retained savings.</p>

      <div className="grid grid-cols-3 gap-8 items-center py-6">
        <div className="space-y-3">
          <span className="text-xs uppercase text-slate-400 font-bold">Gross Inflows</span>
          {incomeSources.map(inc => (
            <div key={inc.name} className="p-3 bg-slate-800 rounded-xl border border-slate-700 flex justify-between text-sm">
              <span>{inc.name}</span>
              <span className="font-bold text-emerald-400">${inc.amount.toLocaleString()}</span>
            </div>
          ))}
        </div>

        <div className="p-6 bg-indigo-950/60 border border-indigo-700/60 rounded-2xl text-center">
          <span className="text-xs uppercase text-indigo-300 font-bold">Total Inflow Flow</span>
          <p className="text-2xl font-black text-indigo-400 mt-1">${totalIncome.toLocaleString()}</p>
        </div>

        <div className="space-y-3">
          <span className="text-xs uppercase text-slate-400 font-bold">Outflow Allocations</span>
          {expenseCategories.map(exp => (
            <div key={exp.name} className="p-3 bg-slate-800 rounded-xl border border-slate-700 flex justify-between text-sm">
              <span>{exp.name}</span>
              <span className="font-bold text-rose-400">${exp.amount.toLocaleString()}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
