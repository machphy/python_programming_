set -euo pipefail

FILE="/etc/example.conf"
BACKUP_DIR="/var/backups/remediation"
TS="$(date +%F_%H-%M-%S)"
BACKUP="$BACKUP_DIR/$(basename "$FILE").$TS.bak"

mkdir -p "$BACKUP_DIR"
[[ -f "$FILE" ]] || { echo "File not found: $FILE"; exit 1; }

cp -a "$FILE" "$BACKUP"

# Example remediation: turn ON -> OFF (edit this line for your case)
sed -i 's/^AllowDangerous=true/AllowDangerous=false/g' "$FILE"

# Verify, else rollback
grep -q '^AllowDangerous=false' "$FILE" || { cp -a "$BACKUP" "$FILE"; exit 2; }

echo "Remediation applied. Backup: $new"
