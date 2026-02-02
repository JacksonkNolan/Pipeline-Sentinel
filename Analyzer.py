import collections
import os

LOG_FILE = "pipeline_attacks.log"

def run_analysis():
    print("==========================================")
    print("   PIPELINE-SENTINEL THREAT REPORT")
    print("==========================================\n")

    if not os.path.exists(LOG_FILE):
        print("[!] No log file found. Run honeypot.py and simulate an attack first.")
        return

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    ips = []
    for line in lines:
        if "from " in line:
            # Extract IP between 'from ' and ' |'
            ip = line.split("from ")[1].split(" |")[0]
            ips.append(ip)

    counts = collections.Counter(ips)

    print(f"[+] Total Security Events: {len(lines)}")
    print("\n[+] Top Attacker Sources:")
    for ip, count in counts.most_common(5):
        print(f"    - {ip}: {count} attempts")
    
    print("\n[+] Analysis Complete.")

if __name__ == "__main__":
    run_analysis()
