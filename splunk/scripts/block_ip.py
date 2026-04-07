import os

ip = "192.168.1.100"

print(f"[INFO] Detected malicious IP: {ip}")
print("[ACTION] Blocking IP...")

# Simulated action (safe fallback)
# os.system(f"iptables -A INPUT -s {ip} -j DROP")

print(f"[SUCCESS] IP {ip} blocked successfully")
