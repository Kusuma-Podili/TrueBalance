# ADR 001: Double-Entry Bookkeeping Ledger Engine

## Status
Accepted

## Context
Personal finance systems often treat balances as mutable floating-point counters, leading to silent rounding errors, unaccounted transfers, and impossible audit trails. Enterprise fintech applications require strict mathematical immutability and compliance with US GAAP / IFRS standards.

## Decision
We enforce a strict Double-Entry General Ledger architecture:
1. Every financial transaction is represented as a balanced `JournalEntry` where `Sum(Debits) == Sum(Credits)`.
2. Account balances are computed dynamically from immutable journal lines rather than mutated directly.
3. Arbitrary-precision decimal math (`FinancialDecimal`) with Bankers Rounding (`ROUND_HALF_EVEN`) is used exclusively to eliminate IEEE 754 floating-point drift.
4. Cryptographic hash chaining (`AuditLedgerEngine`) ensures tamper-evident audit trails.

## Consequences
- Guarantees 100% mathematical integrity across all multi-currency accounts and statements.
- Prevents money creation or destruction bugs.
