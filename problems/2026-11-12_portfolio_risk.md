# 2026-11-12: Portfolio Risk (Halyard Capital)

**Data:** `data/halyard_prices.csv` (522 business days, 2024-11-11 to 2026-11-10).
Columns: `MKT_IDX` (the market index), five stocks (`KSTL`, `BRWN`, `VRDA`, `OAKM`, `NIMB`), and `RF_ANNUAL_PCT` (annualized risk-free rate, in percent).

## Conventions

- Use **simple** daily returns.
- Annualize the mean return ×252 and the standard deviation ×√252.
- Daily risk-free rate = `RF_ANNUAL_PCT / 100 / 252`.
- **Sharpe** is computed on **excess** returns (return − daily rf).
- **Beta** = cov(stock, index) / var(index), on **raw** (not excess) returns.

## Part 1: Return, volatility, Sharpe

For each of the five stocks and `MKT_IDX`, compute the annualized return, annualized volatility and Sharpe ratio.

## Part 2: Beta, drawdown, correlation

1. Each stock's beta to `MKT_IDX`.
2. Max drawdown for each stock and the index, with the **peak date** and **trough date**.
3. The correlation matrix of daily returns for the five stocks. Which pair is the **most** correlated, and which is the **least**?

## Part 3: The book

A **$50M** long book, **daily rebalanced** to these weights:

| KSTL | BRWN | VRDA | OAKM | NIMB |
|---|---|---|---|---|
| 25% | 20% | 20% | 20% | 15% |

Compute the book's:

- annualized return, volatility and Sharpe
- beta to `MKT_IDX`
- max drawdown
- 1-day 95% VaR in dollars, both **historical** and **parametric**

## Part 4: Hedging and sizing

**(a)** What size of `MKT_IDX` short (in $) makes the book beta-neutral? Report the hedged book's annualized volatility and return.

**(b)** Build inverse-volatility weights across the five names, then scale the book so its annualized volatility is **12%**. Report the gross dollars per name (on the $50M base).

## Stretch

Compute NIMB's **rolling 63-day beta** to `MKT_IDX`. Report its minimum and maximum, and the date of each.
