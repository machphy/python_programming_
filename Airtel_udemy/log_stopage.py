from datetime import datetime, timedelta

def parse_time(t):
    """
    Parse ISO time string to datetime.
    """
    if not t:
        return None
    try:
        return datetime.fromisoformat(t.replace("Z", "+00:00"))
    except Exception:
        return None


def main():
    args = demisto.args()

    # Inputs
    devices = args.get("devices")  # list of dicts
    threshold_minutes = int(args.get("threshold_minutes", 30))  # default 30 mins

    if not devices:
        demisto.results("No devices provided.")
        return

    # If devices come as JSON string
    if isinstance(devices, str):
        try:
            devices = demisto.get(devisto, devices)  # fallback
        except Exception:
            pass

    now = datetime.utcnow()
    threshold_time = now - timedelta(minutes=threshold_minutes)

    critical = []

    for d in devices:
        hostname = d.get("hostname") or d.get("host") or d.get("device_name")
        ip = d.get("ip") or d.get("source_ip") or d.get("device_ip")
        device_type = (d.get("type") or d.get("role") or "").lower()

        # last log time field
        last_log_time = parse_time(
            d.get("last_log_time") or d.get("lastSeen") or d.get("last_event_time")
        )

        # Only AD critical devices
        # Example: domain controller / adcs / adfs / dns
        if device_type and device_type not in ["dc", "domain_controller", "adcs", "adfs", "dns"]:
            continue

        if not last_log_time:
            # If no last log time found, treat as stoppage
            critical.append({
                "hostname": hostname,
                "ip": ip,
                "device_type": device_type,
                "status": "NO_LAST_LOG_TIME_FOUND"
            })
            continue

        if last_log_time < threshold_time:
            critical.append({
                "hostname": hostname,
                "ip": ip,
                "device_type": device_type,
                "last_log_time": last_log_time.isoformat(),
                "minutes_since_last_log": int((now - last_log_time).total_seconds() / 60),
                "status": "LOG_STOPPAGE"
            })

    if not critical:
        demisto.results(f"✅ No log stoppage detected on AD critical devices (threshold={threshold_minutes}m).")
        return

    # Human readable
    md = "## 🚨 Log Stoppage Detected – AD Critical Devices\n"
    md += f"Threshold: **{threshold_minutes} minutes**\n\n"
    md += "| Hostname | IP | Type | Status | Minutes Since Last Log |\n"
    md += "|----------|----|------|--------|-------------------------|\n"

    for c in critical:
        md += f"| {c.get('hostname','-')} | {c.get('ip','-')} | {c.get('device_type','-')} | {c.get('status')} | {c.get('minutes_since_last_log','-')} |\n"

    demisto.results({
        "Type": 1,
        "ContentsFormat": "json",
        "Contents": critical,
        "HumanReadable": md
    })


if __name__ in ("__main__", "builtins"):
    main()
