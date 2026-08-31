import React, { useState } from 'react';
import { BudgetEnvelope } from '../types/financial';

export const BudgetPlannerView: React.FC = () => {
  const [selectedMonth, setSelectedMonth] = useState('2026-08');

  const mockEnvelopes: BudgetEnvelope[] = [
    { id: 'env_1', categoryName: 'Housing & Rent', categoryColor: '#EF4444', allocatedCents: 220000, spentCents: 220000, remainingCents: 0, percentageSpent: 100.0, isOverBudget: false },
    { id: 'env_2', categoryName: 'Groceries & Dining', categoryColor: '#F59E0B', allocatedCents: 85000, spentCents: 62450, remainingCents: 22550, percentageSpent: 73.5, isOverBudget: false },
    { id: 'env_3', categoryName: 'Transportation & Fuel', categoryColor: '#3B82F6', allocatedCents: 35000, spentCents: 28900, remainingCents: 6100, percentageSpent: 82.6, isOverBudget: false },
    { id: 'env_4', categoryName: 'Utilities & Bills', categoryColor: '#6366F1', allocatedCents: 30000, spentCents: 24500, remainingCents: 5500, percentageSpent: 81.7, isOverBudget: false },
    { id: 'env_5', categoryName: 'Entertainment & Leisure', categoryColor: '#8B5CF6', allocatedCents: 25000, spentCents: 29800, remainingCents: -4800, percentageSpent: 119.2, isOverBudget: true },
    { id: 'env_6', categoryName: 'Emergency Savings Fund', categoryColor: '#10B981', allocatedCents: 100000, spentCents: 100000, remainingCents: 0, percentageSpent: 100.0, isOverBudget: false },
  ];

  const totalAllocated = mockEnvelopes.reduce((s, e) => s + e.allocatedCents, 0) / 100;
  const totalSpent = mockEnvelopes.reduce((s, e) => s + e.spentCents, 0) / 100;

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-black text-white">Zero-Based Budget Planner</h1>
          <p className="text-sm text-slate-400">Assign every dollar a job with digital envelope rollover management.</p>
        </div>
        <div className="flex items-center gap-4">
          <input
            type="month"
            value={selectedMonth}
            onChange={e => setSelectedMonth(e.target.value)}
            className="bg-slate-800 border border-slate-700 text-white text-sm rounded-xl px-3 py-2"
          />
          <button className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold rounded-xl transition">
            + New Envelope
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 text-white">
          <span className="text-xs text-slate-400 uppercase">Total Monthly Allocated</span>
          <p className="text-2xl font-black text-indigo-400 mt-1">${totalAllocated.toLocaleString('en-US', { minimumFractionDigits: 2 })}</p>
        </div>
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 text-white">
          <span className="text-xs text-slate-400 uppercase">Total Spent to Date</span>
          <p className="text-2xl font-black text-amber-400 mt-1">${totalSpent.toLocaleString('en-US', { minimumFractionDigits: 2 })}</p>
        </div>
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 text-white">
          <span className="text-xs text-slate-400 uppercase">Remaining Buffer</span>
          <p className="text-2xl font-black text-emerald-400 mt-1">${(totalAllocated - totalSpent).toLocaleString('en-US', { minimumFractionDigits: 2 })}</p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {mockEnvelopes.map(env => (
          <div key={env.id} className="bg-slate-900 border border-slate-800 rounded-2xl p-5 text-white shadow-lg space-y-4">
            <div className="flex items-center justify-between">
              <span className="font-bold">{env.categoryName}</span>
              <span className={`text-xs px-2 py-0.5 rounded font-semibold ${
                env.isOverBudget ? 'bg-rose-900/60 text-rose-400' : 'bg-emerald-900/60 text-emerald-400'
              }`}>
                {env.percentageSpent.toFixed(1)}%
              </span>
            </div>

            <div className="w-full bg-slate-800 h-2.5 rounded-full overflow-hidden">
              <div
                className={`h-full transition-all ${env.isOverBudget ? 'bg-rose-500' : 'bg-indigo-500'}`}
                style={{ width: `${Math.min(100, env.percentageSpent)}%` }}
              />
            </div>

            <div className="flex items-center justify-between text-xs text-slate-400 pt-2 border-t border-slate-800">
              <span>Spent: ${(env.spentCents / 100).toFixed(2)}</span>
              <span>Allocated: ${(env.allocatedCents / 100).toFixed(2)}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
