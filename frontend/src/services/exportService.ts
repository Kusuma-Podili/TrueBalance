/**
 * Financial Reports & Statements Export Service.
 * Generates formatted CSV, Excel, and JSON financial statements.
 */

import { Transaction, Account } from '../types/financial';

export class FinancialExportService {
  static exportTransactionsToCSV(transactions: Transaction[], filename: string = 'transactions_export.csv'): void {
    const headers = ['Transaction ID', 'Date', 'Merchant / Description', 'Category', 'Amount', 'Currency', 'Status'];
    const rows = transactions.map(tx => [
      tx.id,
      tx.date,
      `"${tx.merchantName.replace(/"/g, '""')}"`,
      `"${tx.categoryName}"`,
      (tx.amountCents / 100).toFixed(2),
      tx.currency,
      tx.status
    ]);

    const csvContent = [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', filename);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  static generateBalanceSheetReport(assets: Record<string, number>, liabilities: Record<string, number>, equity: Record<string, number>): string {
    let report = '=== ENTERPRISE BALANCE SHEET ===\n\n';
    report += 'ASSETS:\n';
    let totalAssets = 0;
    for (const [k, v] of Object.entries(assets)) {
      report += `  - ${k}: $${v.toLocaleString('en-US', { minimumFractionDigits: 2 })}\n`;
      totalAssets += v;
    }
    report += `TOTAL ASSETS: $${totalAssets.toLocaleString('en-US', { minimumFractionDigits: 2 })}\n\n`;

    report += 'LIABILITIES:\n';
    let totalLiabilities = 0;
    for (const [k, v] of Object.entries(liabilities)) {
      report += `  - ${k}: $${v.toLocaleString('en-US', { minimumFractionDigits: 2 })}\n`;
      totalLiabilities += v;
    }
    report += `TOTAL LIABILITIES: $${totalLiabilities.toLocaleString('en-US', { minimumFractionDigits: 2 })}\n\n`;

    const netWorth = totalAssets - totalLiabilities;
    report += `NET WORTH (EQUITY): $${netWorth.toLocaleString('en-US', { minimumFractionDigits: 2 })}\n`;
    return report;
  }
}
