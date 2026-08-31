import React from 'react';
import { Currency } from '../../types/financial';

interface NetWorthCardProps {
  totalAssets: number;
  totalLiabilities: number;
  netWorth: number;
  monthlyChangePct: number;
  currency?: Currency;
}

export const NetWorthCard: React.FC<NetWorthCardProps> = ({
  totalAssets,
  totalLiabilities,
  netWorth,
  monthlyChangePct,
  currency = 'USD'
}) => {
  const isPositive = netWorth >= 0;
  const isGrowthPositive = monthlyChangePct >= 0;

  const formatCurrency = (val: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: currency,
      maximumFractionDigits: 0
    }).format(val);
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl text-white">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-sm font-medium text-slate-400 uppercase tracking-wider">Total Net Worth</h3>
        <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold ${
          isGrowthPositive ? 'bg-emerald-900/60 text-emerald-400' : 'bg-rose-900/60 text-rose-400'
        }`}>
          {isGrowthPositive ? '↑ +' : '↓ '}{monthlyChangePct.toFixed(1)}% this month
        </span>
      </div>

      <div className="text-4xl font-extrabold tracking-tight mb-6">
        {formatCurrency(netWorth)}
      </div>

      <div className="grid grid-cols-2 gap-4 pt-4 border-t border-slate-800">
        <div>
          <span className="text-xs text-slate-400">Total Assets</span>
          <p className="text-lg font-semibold text-emerald-400">{formatCurrency(totalAssets)}</p>
        </div>
        <div>
          <span className="text-xs text-slate-400">Total Debts / Liabilities</span>
          <p className="text-lg font-semibold text-rose-400">{formatCurrency(totalLiabilities)}</p>
        </div>
      </div>
    </div>
  );
};
