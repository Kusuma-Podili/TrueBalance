import React from 'react';

export const TaxCenterView: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-black text-white">Tax Optimization & Loss Harvesting Center</h1>
          <p className="text-sm text-slate-400">Monitor taxable investment accounts, wash-sale restrictions, and capital gains liabilities.</p>
        </div>
        <button className="px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white text-sm font-semibold rounded-xl shadow-lg transition">
          Execute Harvest Plan
        </button>
      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 text-white">
        <h3 className="text-lg font-bold mb-4">Detected Tax-Loss Harvesting Opportunities</h3>
        <div className="p-4 bg-emerald-950/40 border border-emerald-800/60 rounded-xl mb-4">
          <p className="text-sm text-emerald-300 font-semibold">
            ✓ Estimated Tax Savings: $450.00 | Total Harvestable Capital Loss: $3,000.00
          </p>
          <p className="text-xs text-emerald-400/80 mt-1">
            Rebalancing security: Sell 500 shares of BND and purchase AGG to maintain target fixed income asset allocation without triggering IRS 30-day wash-sale rules.
          </p>
        </div>
      </div>
    </div>
  );
};
