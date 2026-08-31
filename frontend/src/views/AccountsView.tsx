import React from 'react';
import { Account } from '../types/financial';

interface AccountsViewProps {
  accounts: Account[];
  onAddAccount: () => void;
}

export const AccountsView: React.FC<AccountsViewProps> = ({ accounts, onAddAccount }) => {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-black text-white">Bank & Investment Accounts</h1>
          <p className="text-sm text-slate-400">Manage connected banking institutions, credit cards, and brokerages.</p>
        </div>
        <button
          onClick={onAddAccount}
          className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold rounded-xl shadow-lg transition"
        >
          + Link New Account
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {accounts.map(acc => (
          <div key={acc.id} className="bg-slate-900 border border-slate-800 rounded-2xl p-5 text-white shadow-lg">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">{acc.institutionName}</span>
              <span className="text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-mono">{acc.accountNumberMask}</span>
            </div>
            <h3 className="text-lg font-bold mb-1">{acc.name}</h3>
            <p className="text-xs text-indigo-400 mb-4">{acc.type}</p>
            <div className="pt-3 border-t border-slate-800 flex items-end justify-between">
              <div>
                <span className="text-[10px] text-slate-500 uppercase">Available Balance</span>
                <p className="text-xl font-black text-emerald-400">
                  ${(acc.availableBalanceCents / 100).toLocaleString('en-US', { minimumFractionDigits: 2 })}
                </p>
              </div>
              <span className="text-xs text-slate-400">{acc.currency}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
