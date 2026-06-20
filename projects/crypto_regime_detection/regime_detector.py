"""
Regime Detector - Klassifiserer markedsregimer basert på volatilitet
"""

import pandas as pd


class RegimeDetector:
    def __init__(self, calm_threshold: float = 0.02, crisis_threshold: float = 0.05):
        """
        Args:
            calm_threshold: Volatilitet under denne verdien = CALM
            crisis_threshold: Volatilitet over denne verdien = CRISIS
        """
        self.calm_threshold = calm_threshold
        self.crisis_threshold = crisis_threshold

    def classify_time_series(self, df: pd.DataFrame) -> pd.DataFrame:
        """Legger til 'regime' kolonne basert på volatilitet."""
        df = df.copy()

        if "volatility_20d" not in df.columns:
            df["return_1d"] = df["price"].pct_change()
            df["volatility_20d"] = df["return_1d"].rolling(window=20).std()

        def get_regime(vol):
            if pd.isna(vol):
                return "UNKNOWN"
            elif vol < self.calm_threshold:
                return "CALM"
            elif vol > self.crisis_threshold:
                return "CRISIS"
            else:
                return "STRESSED"

        df["regime"] = df["volatility_20d"].apply(get_regime)
        return df

    def get_regime_summary(self, df: pd.DataFrame) -> dict:
        """Returnerer oversikt over hvor mye tid som ble brukt i hvert regime."""
        if "regime" not in df.columns:
            df = self.classify_time_series(df)

        summary = {}
        total = len(df)

        for regime in ["CALM", "STRESSED", "CRISIS"]:
            count = len(df[df["regime"] == regime])
            percentage = (count / total) * 100 if total > 0 else 0
            summary[regime] = {"count": count, "percentage": round(percentage, 1)}

        return summary

    def detect_crisis_signal(self, df: pd.DataFrame) -> bool:
        """Returnerer True hvis vi er i CRISIS eller nylig har hatt store endringer."""
        if "regime" not in df.columns:
            df = self.classify_time_series(df)

        latest = df.iloc[-1]["regime"]
        recent_changes = df.iloc[-5:]["regime"].ne(df.iloc[-5:]["regime"].shift()).sum()

        return latest == "CRISIS" or recent_changes >= 2
