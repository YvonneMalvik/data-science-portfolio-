"""
Alert System - Genererer varsler når regime endres
"""

from datetime import datetime
from typing import Optional


class AlertSystem:
    def __init__(self):
        self.alert_log = []

    def check_and_alert(self, current_regime: str, previous_regime: str,
                        price: float, timestamp: datetime) -> Optional[str]:
        """
        Sjekker om regime har endret seg og lager en alert hvis nødvendig.
        """
        if current_regime == previous_regime:
            return None

        message = self._format_alert(current_regime, previous_regime, price, timestamp)
        self.alert_log.append({
            "timestamp": timestamp,
            "message": message,
            "change": f"{previous_regime} → {current_regime}"
        })

        return message

    def _format_alert(self, new_regime: str, old_regime: str,
                      price: float, timestamp: datetime) -> str:
        """Lager en fin formatert alert-melding."""
        if new_regime == "CRISIS":
            severity = "🚨 KRITISK"
            action = "Vurder redusert eksponering"
        elif new_regime == "STRESSED":
            severity = "⚠️ OBSERVASJON"
            action = "Økt beredskap"
        else:
            severity = "✅ RO"
            action = "Normal drift"

        return f"""{severity} - Regime Endring
Tid: {timestamp.strftime('%Y-%m-%d %H:%M')}
Fra: {old_regime} → Til: {new_regime}
Pris: ${price:,.2f}
Anbefaling: {action}"""
