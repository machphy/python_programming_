from datetime import datetime, timedelta
from collections import defaultdict

def parse_time(t):
    """
    Parse time from event.
    XSOAR usually gives ISO time.
    """
    try:
        return datetime.fromisoformat(t.replace("Z", "+00:00"))
    except Exception:
        return None


def main():
    args = demisto.args()

    # Inputs
    events = args.get("events")  # should be list/dict
    threshold = int(args.get("threshold", 3))  # default: 3 lockouts
    window_minutes = int(args.get("window_minutes", 10))  # default: 10 minutes

    if not events:
        demisto.results("No events provided.")
        return

    # If events come as JSON string
    if isinstance(events, str):
        events = demisto.get(events, [])

    now = datetime.utcnow()
    window_start = now - timedelta(minutes=window_minutes)

    lockouts_by_user = defaultdict(list)

    for ev in events:
        # Example fields (adjust based on your SIEM mapping)
        username = ev.get("username") or ev.get("user") or ev.get("AccountName")
        event_id = str(ev.get("event_id") or ev.get("EventID") or "")

        # Windows lockout event
        if event_id not in ["4740"]:
            continue

        time_str = ev.get("time") or ev.get("timestamp") or ev.get("_time")
        ev_time = parse_time(time_str)

        if not username or not ev_time:
            continue

        # Filter by time window
        if ev_time >= window_start:
            lockouts_by_user[username].append(ev_time)

    suspicious = []
    for user, times in lockouts_by_user.items():
        if len(times) >= threshold:
            suspicious.append({
                "username": user,
                "lockout_count": len(times),
                "first_lockout": min(times).isoformat(),
                "last_lockout": max(times).isoformat()
            })

    if not suspicious:
        demisto.results(f"No multiple lockouts found (threshold={threshold}, window={window_minutes}m).")
        return

    # Output
    md = "## 🚨 Multiple Account Lockout Detected\n"
    md += f"Threshold: **{threshold}** in **{window_minutes} minutes**\n\n"
    md += "| User | Lockouts | First | Last |\n"
    md += "|------|----------|-------|------|\n"

    for s in suspicious:
        md += f"| {s['username']} | {s['lockout_count']} | {s['first_lockout']} | {s['last_lockout']} |\n"

    demisto.results({
        "Type": 1,
        "ContentsFormat": "json",
        "Contents": suspicious,
        "HumanReadable": md
    })


if __name__ in ("__main__", "builtins"):
    main()
