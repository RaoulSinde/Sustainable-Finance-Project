# %%
import yfinance as yf
import pandas as pd 
import numpy as np 

# %%
tickers=["MSFT","OR","EN.PA","CA","UL","SU","SAP","ALV.DE","EART.L","PAWD.L"]
start_date="2019-01-01"
end_date="2024-12-31"

# %%
def data_products(tickers, start=start_date, end=end_date):
    
    data = yf.download(tickers, start=start, end=end)["Close"]
    
    returns = data.ffill().pct_change().dropna().replace([np.inf, -np.inf], 0)  # Remplacement des valeurs infinies par 0

    return returns
returns=data_products(tickers,start_date,end_date)
returns

# %%

def get_stock_statistics(tickers, start=start_date, end=end_date):
    
    data = yf.download(tickers, start=start, end=end)["Close"]
    
    returns = data.ffill().pct_change().dropna().replace([np.inf, -np.inf], 0)  # Remplacement des valeurs infinies par 0
    
    mean_returns = returns.mean()*252
    var_matrix = returns.var()*252
    cov_matrix = returns.cov()*np.sqrt(252)
    corr_matrix = returns.corr()

    return {
        "returns": returns,
        "mean_returns": mean_returns,
        "variance": var_matrix,
        "covariance_matrix": cov_matrix,
        "correlation_matrix": corr_matrix
    }

stats = get_stock_statistics(tickers)
print("Mean Returns:\n", stats["mean_returns"])
print("\nCovariance Matrix:\n", stats["covariance_matrix"])
print("\nCorrelation Matrix:\n", stats["correlation_matrix"])


# %%

def get_wallet_statistics(tickers, start=start_date, end=end_date,returns=stats):
    data = yf.download(tickers, start=start, end=end)["Close"]

    returns = data.ffill().pct_change().replace([np.inf, -np.inf], 0)
    
    weights = np.array([1/len(tickers)] * len(tickers))

    annual_factor = 252

    mean_daily_returns = returns.mean()
    mean_annual_returns = mean_daily_returns * annual_factor

    cov_matrix_daily = returns.cov()
    cov_matrix_annual = cov_matrix_daily * annual_factor
    corr_matrix = returns.corr()

    port_daily_return = np.dot(weights, mean_daily_returns)
    port_annual_return = port_daily_return * annual_factor

    port_annual_variance = np.dot(weights.T, np.dot(cov_matrix_annual, weights))
    port_annual_volatility = np.sqrt(port_annual_variance)

    port_sharpe_ratio = (port_annual_return - 0.02) / port_annual_volatility

    return {
        "daily_returns": returns,
        "mean_annual_returns": mean_annual_returns,
        "cov_matrix_annual": cov_matrix_annual,
        "correlation_matrix": corr_matrix,
        "portfolio_annual_return": port_annual_return,
        "portfolio_annual_volatility": port_annual_volatility,
        "portfolio_annual_variance": port_annual_variance,
        "portfolio_sharpe_ratio": port_sharpe_ratio
    }

# Run and print
stats = get_wallet_statistics(tickers)

print("=== Mean Annual Returns ===\n", stats["mean_annual_returns"])
print("\n=== Annual Covariance Matrix ===\n", stats["cov_matrix_annual"])
print("\n=== Correlation Matrix ===\n", stats["correlation_matrix"])
print("\n=== Portfolio Annual Return ===\n", stats["portfolio_annual_return"])
print("\n=== Portfolio Annual Volatility (Std Dev) ===\n", stats["portfolio_annual_volatility"])
print("\n=== Portfolio Annual Variance ===\n", stats["portfolio_annual_variance"])



