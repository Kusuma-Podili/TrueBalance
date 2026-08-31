/**
 * Enterprise Financial Data Types & Domain Models.
 */

export type Currency = 'USD' | 'EUR' | 'GBP' | 'JPY' | 'CAD' | 'AUD' | 'CHF' | 'CNY' | 'INR' | 'SGD' | 'BTC' | 'ETH';

export type AccountType = 
  | 'CHECKING'
  | 'SAVINGS'
  | 'CREDIT_CARD'
  | 'INVESTMENT'
  | 'MORTGAGE'
  | 'STUDENT_LOAN'
  | 'CRYPTO';

export interface Account {
  id: string;
  name: string;
  type: AccountType;
  currency: Currency;
  currentBalanceCents: number;
  availableBalanceCents: number;
  creditLimitCents?: number;
  institutionName: string;
  accountNumberMask: string;
  isClosed: boolean;
}

export interface Transaction {
  id: string;
  accountId: string;
  amountCents: number;
  currency: Currency;
  date: string;
  merchantName: string;
  rawDescription: string;
  categoryName: string;
  categoryColor: string;
  status: 'PENDING' | 'POSTED' | 'VOID';
  isRecurring: boolean;
}

export interface BudgetEnvelope {
  id: string;
  categoryName: string;
  categoryColor: string;
  allocatedCents: number;
  spentCents: number;
  remainingCents: number;
  percentageSpent: number;
  isOverBudget: boolean;
}

export interface PortfolioHolding {
  symbol: string;
  name: string;
  assetClass: 'EQUITY' | 'FIXED_INCOME' | 'CRYPTO' | 'REAL_ESTATE' | 'CASH';
  shares: number;
  costBasis: number;
  currentPrice: number;
  marketValue: number;
  unrealizedGainLoss: number;
  unrealizedGainLossPct: number;
  weightPct: number;
}

export interface MonteCarloSimulationResult {
  iterations: number;
  years: number;
  successRatePercentage: number;
  medianTerminalWealth: number;
  worst10PercentileTerminalWealth: number;
  best10PercentileTerminalWealth: number;
  percentileTrajectory: {
    p10: number[];
    p25: number[];
    p50_median: number[];
    p75: number[];
    p90: number[];
  };
}
