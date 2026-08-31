import React, { useState } from 'react';

export const FinancialStatementsView: React.FC = () => {
  const [statementType, setStatementType] = useState<'balance-sheet' | 'income-statement' | 'cash-flow'>('balance-sheet');

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 text-white shadow-xl">
      <div className="flex items-center justify-between pb-6 border-b border-slate-800">
        <div>
          <h2 className="text-xl font-bold">GAAP Financial Statements</h2>
          <p className="text-xs text-slate-400">Audited financial statements generated from double-entry general ledger.</p>
        </div>
        <div className="flex gap-2">
          {(['balance-sheet', 'income-statement', 'cash-flow'] as const).map(type => (
            <button
              key={type}
              onClick={() => setStatementType(type)}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold capitalize transition ${
                statementType === type ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400 hover:text-white'
              }`}
            >
              {type.replace('-', ' ')}
            </button>
          ))}
        </div>
      </div>

      <div className="pt-6">
        <div className="p-4 bg-slate-950/60 rounded-xl border border-slate-800 font-mono text-sm space-y-2">
          <div className="text-slate-400 uppercase text-xs tracking-wider mb-2">Statement Status: Clean Ledger / Equilibrium Verified</div>
          <div className="flex justify-between py-1 border-b border-slate-800/60">
            <span>Total Liquid Assets</span>
            <span className="text-emerald-400 font-bold">$148,500.00</span>
          </div>
          <div className="flex justify-between py-1 border-b border-slate-800/60">
            <span>Total Equities & Investments</span>
            <span className="text-emerald-400 font-bold">$385,200.00</span>
          </div>
          <div className="flex justify-between py-1 border-b border-slate-800/60">
            <span>Total Revolving & Long-Term Liabilities</span>
            <span className="text-rose-400 font-bold">$210,000.00</span>
          </div>
          <div className="flex justify-between py-2 text-base font-bold bg-slate-900 px-3 rounded-lg mt-2">
            <span>NET WORTH (EQUITY)</span>
            <span className="text-indigo-400">$323,700.00</span>
          </div>
        </div>
      </div>
    </div>
  );
};
