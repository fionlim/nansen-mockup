from typing import List, Dict
import pandas as pd


def inflows_to_dataframe(items: List[Dict]) -> pd.DataFrame:
    if not items:
        return pd.DataFrame(columns=[
            "chain", "tokenAddress", "symbol", "sectors",
            "volume24hUSD", "volume7dUSD", "volume30dUSD",
            "nofTraders", "tokenAgeDays", "marketCap"
        ])
    df = pd.DataFrame(items)
    if "sectors" in df.columns:
        df["sectors"] = df["sectors"].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)
    for col in ["volume24hUSD", "volume7dUSD", "volume30dUSD", "marketCap"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    if "tokenAgeDays" in df.columns:
        df["tokenAgeDaysNum"] = pd.to_numeric(df["tokenAgeDays"], errors="coerce")
    return df


def holdings_to_dataframe(items: List[Dict]) -> pd.DataFrame:
    if not items:
        return pd.DataFrame(columns=[
            "chain", "tokenAddress", "symbol", "sectors",
            "balanceUsd", "balancePctChange24H", "nofHolders",
            "shareOfHoldings", "tokenAgeDays", "marketCap"
        ])
    df = pd.DataFrame(items)
    if "sectors" in df.columns:
        df["sectors"] = df["sectors"].apply(lambda x: ", ".join(x) if isinstance(x, list) else x)
    if "balancePctChange24H" not in df.columns and "balancePctChange24h" in df.columns:
        df["balancePctChange24H"] = df["balancePctChange24h"]
    for col in ["balanceUsd", "balancePctChange24H", "shareOfHoldings", "marketCap"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    if "tokenAgeDays" in df.columns:
        df["tokenAgeDaysNum"] = pd.to_numeric(df["tokenAgeDays"], errors="coerce")
    return df


def screener_to_dataframe(items: List[Dict]) -> pd.DataFrame:
    if not items:
        return pd.DataFrame(columns=[
            "chain", "tokenAddressHex", "tokenSymbol", "tokenAgeDays",
            "marketCap", "liquidity", "priceUsd", "priceChange", "fdv", "fdvMcRatio",
            "buyVolume", "inflowFdvRatio", "outflowFdvRatio", "sellVolume", "volume", "netflow"
        ])
    df = pd.DataFrame(items)
    numeric_cols = ["marketCap", "fdv", "fdvMcRatio", "buyVolume", "sellVolume", "volume", "netflow"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    for col in ["priceUsd", "priceChange", "liquidity", "inflowFdvRatio", "outflowFdvRatio"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    if "tokenAgeDays" in df.columns:
        df["tokenAgeDaysNum"] = pd.to_numeric(df["tokenAgeDays"], errors="coerce")
    return df


def flow_to_dataframe(items: List[Dict]) -> pd.DataFrame:
    if not items:
        return pd.DataFrame(columns=[
            "publicFigureFlow", "publicFigureAvgAbsFlow", "publicFigureWallets",
            "topPnlFlow", "topPnlAvgAbsFlow", "topPnlWallets",
            "whaleFlow", "whaleAvgAbsFlow", "whaleWallets",
            "smartTraderFlow", "smartTraderAvgAbsFlow", "smartTraderWallets",
            "exchangeFlow", "exchangeAvgAbsFlow", "exchangeWallets",
            "freshWalletsFlow", "freshWalletsAvgAbsFlow", "freshWalletsWallets"
        ])
    df = pd.DataFrame(items)
    for col in [
        "publicFigureAvgAbsFlow", "topPnlAvgAbsFlow", "whaleAvgAbsFlow",
        "smartTraderAvgAbsFlow", "exchangeAvgAbsFlow", "freshWalletsAvgAbsFlow"
    ]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df
