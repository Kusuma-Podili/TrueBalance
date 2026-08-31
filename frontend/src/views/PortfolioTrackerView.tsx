import React, { useState } from 'react';
import { PortfolioHolding } from '../types/financial';

export const PortfolioTrackerView: React.FC = () => {
  const [selectedAssetClass, setSelectedAssetClass] = useState<string>('ALL');

  const mockHoldings: PortfolioHolding[] = [
    { symbol: 'VOO', name: 'Vanguard S&P 500 ETF', assetClass: 'EQUITY', shares: 140.5, costBasis: 420.00, currentPrice: 512.40, marketValue: 71992.20, unrealizedGainLoss: 12981.00, unrealizedGainLossPct: 22.0, weightPct: 42.5 },
    { symbol: 'QQQ', name: 'Invesco QQQ Trust', assetClass: 'EQUITY', shares: 75.0, costBasis: 380.50, currentPrice: 485.20, marketValue: 36390.00, unrealizedGainLoss: 7852.50, unrealizedGainLossPct: 27.5, weightPct: 21.5 },
    { symbol: 'BND', name: 'Vanguard Total Bond Market', assetClass: 'FIXED_INCOME', shares: 320.0, costBasis: 74.50, currentPrice: 73.10, marketValue: 23392.00, unrealizedGainLoss: -448.00, unrealizedGainLossPct: -1.8, weightPct: 13.8 },
    { symbol: 'VNQ', name: 'Vanguard Real Estate ETF', assetClass: 'REAL_ESTATE', shares: 150.0, costBasis: 82.00, currentPrice: 89.40, marketValue: 13410.00, unrealizedGainLoss: 1110.00, unrealizedGainLossPct: 9.0, weightPct: 7.9 },
    { symbol: 'BTC', name: 'Bitcoin Digital Asset', assetClass: 'CRYPTO', shares: 0.35, costBasis: 45000.00, currentPrice: 68500.00, marketValue: 23975.00, unrealizedGainLoss: 8225.00, unrealizedGainLossPct: 52.2, weightPct: 14.3 },
  ];

  const filteredHoldings = selectedAssetClass === 'ALL' 
    ? mockHoldings 
    : mockHoldings.filter(h => h.assetClass === selectedAssetClass);

  const totalPortfolioValue = mockHoldings.reduce((sum, h) => sum + h.marketValue, 0);

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-black text-white">Investment Portfolios & Holdings</h1>
          <p className="text-sm text-slate-400">Real-time asset allocation, cost basis tracking, and performance analytics.</p>
        </div>
        <div className="text-right">
          <span className="text-xs text-slate-400 uppercase">Total Portfolio Value</span>
          <p className="text-3xl font-black text-emerald-400">${totalPortfolioValue.toLocaleString('en-US', { minimumFractionDigits: 2 })}</p>
        </div>
      </div>

      <div className="flex gap-2">
        {['ALL', 'EQUITY', 'FIXED_INCOME', 'REAL_ESTATE', 'CRYPTO'].map(assetClass => (
          <button
            key={assetClass}
            onClick={() => setSelectedAssetClass(assetClass)}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold uppercase tracking-wider transition ${
              selectedAssetClass === assetClass ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400 hover:text-white'
            }`}
          >
            {assetClass.replace('_', ' ')}
          </button>
        ))}
      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-xl">
        <table className="w-full text-left text-sm text-white">
          <thead className="bg-slate-950/80 text-xs uppercase text-slate-400 border-b border-slate-800">
            <tr>
              <th className="p-4">Symbol / Asset</th>
              <th className="p-4">Class</th>
              <th className="p-4 text-right">Shares</th>
              <th className="p-4 text-right">Cost Basis</th>
              <th className="p-4 text-right">Current Price</th>
              <th className="p-4 text-right">Market Value</th>
              <th className="p-4 text-right">Unrealized Gain/Loss</th>
              <th className="p-4 text-right">Weight</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800">
            {filteredHoldings.map(h => (
              <tr key={h.symbol} className="hover:bg-slate-800/40 transition">
                <td className="p-4 font-bold">{h.symbol} <span className="text-xs font-normal text-slate-400 block">{h.name}</span></td>
                <td className="p-4"><span className="text-xs px-2 py-0.5 rounded bg-slate-800 text-indigo-300">{h.assetClass}</span></td>
                <td className="p-4 text-right font-mono">{h.shares}</td>
                <td className="p-4 text-right font-mono">${h.costBasis.toFixed(2)}</td>
                <td className="p-4 text-right font-mono font-semibold">${h.currentPrice.toFixed(2)}</td>
                <td className="p-4 text-right font-mono font-bold">${h.marketValue.toLocaleString('en-US', { minimumFractionDigits: 2 })}</td>
                <td className={`p-4 text-right font-mono font-semibold ${h.unrealizedGainLoss >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
                  {h.unrealizedGainLoss >= 0 ? '+' : ''}${h.unrealizedGainLoss.toLocaleString('en-US', { minimumFractionDigits: 2 })} ({h.unrealizedGainLossPct >= 0 ? '+' : ''}{h.unrealizedGainLossPct.toFixed(1)}%)
                </td>
                <td className="p-4 text-right font-mono">{h.weightPct.toFixed(1)}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
