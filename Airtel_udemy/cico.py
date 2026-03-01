import random
from datetime import datetime

class C2Event:
    def __init__(self, encrypted, beacon_score, ioc_match):
        self.encrypted = encrypted
        self.beacon_score = beacon_score
        self.ioc_match = ioc_match

class SOCDecisionEngine:

    def calculate_risk(self, event: C2Event):
        score = 0

        if event.encrypted:
            score += 20
        if event.beacon_score > 70:
            score += 40
        if event.ioc_match:
            score += 40

        return score

    def decide(self, score):
        if score >= 80:
            return "CRITICAL"
        elif score >= 50:
            return "HIGH"
        else:
            return "MONITOR"

def simulate_incident():
    print("=== 03:00 AM Security Incident Simulation ===")
    print(f"Time: {datetime.now()}")
    print("---------------------------------------------")

    # Simulated event
    event = C2Event(
        encrypted=True,
        beacon_score=random.randint(60, 95),
        ioc_match=random.choice([True, False])
    )

    engine = SOCDecisionEngine()
    risk_score = engine.calculate_risk(event)
    decision = engine.decide(risk_score)

    print(f"Encrypted Traffic: {event.encrypted}")
    print(f"Beacon Score: {event.beacon_score}")
    print(f"IOC Match: {event.ioc_match}")
    print(f"Calculated Risk Score: {risk_score}")
    print(f"Decision: {decision}")

    if decision == "CRITICAL":
        print("\nCISO Mode Activated:")
        print("→ Isolate host")
        print("→ Block destination IP")
        print("→ Notify Incident Response")
        print("→ Prepare board-level summary")

    