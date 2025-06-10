import json
import sys
import subprocess
import datetime
import os

def run_wireshark(params):
    ip = params.get("target")
    interface = params.get("interface", "eth0")
    capture_filter = params.get("filter", f"host {ip}") if ip else ""
    packet_count = params.get("packet_count", 100)
    result_path = f"results/result_wireshark_{ip.replace('.', '_') if ip else 'unknown'}.json"
    capture_file = f"captures/capture_{ip.replace('.', '_') if ip else 'unknown'}.pcapng"

    os.makedirs("results", exist_ok=True)
    os.makedirs("captures", exist_ok=True)

    # Capture tshark
    cmd_capture = [
        "tshark",
        "-i", interface,
        "-c", str(packet_count),
    ]
    if capture_filter:
        cmd_capture.extend(["-f", capture_filter])
    cmd_capture.extend(["-w", capture_file])

    subprocess.run(cmd_capture, check=True)

    # Analyse sommaire avec tshark (exemple: nombre de paquets)
    cmd_analyze = ["tshark", "-r", capture_file, "-q", "-z", "io,stat,0"]
    analyze_result = subprocess.run(cmd_analyze, capture_output=True, text=True)
    summary = analyze_result.stdout.strip()

    result = {
        "tool": "wireshark",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "target": ip,
        "result": {
            "interface": interface,
            "filter": capture_filter,
            "packet_count": packet_count,
            "capture_file": capture_file,
            "analysis_summary": summary
        }
    }

    with open(result_path, "w") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        params = json.load(f)
    run_wireshark(params)

