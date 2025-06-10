import json, sys, subprocess, datetime, os

def run_hydra(params):
    ip = params["target"]
    protocol = params["service"]
    user = params["credentials"]["username"]
    wordlist = params.get("wordlist", "/usr/share/wordlists/rockyou.txt")
    result_path = f"results/result_hydra_{ip.replace('.', '_')}.json"
    os.makedirs("results", exist_ok=True)

    cmd = [
        "hydra", "-l", user, "-P", wordlist, "-s", str(params.get("port", 22)),
        "-f", "-o", "hydra_output.txt", protocol, ip
    ]

    subprocess.run(cmd, check=True)

    password = None
    with open("hydra_output.txt") as f:
        for line in f:
            if user in line and "login:" in line and "password:" in line:
                parts = line.strip().split()
                password = parts[-1]
                break

    result = {
        "tool": "hydra",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "target": ip,
        "result": {
            "service": protocol,
            "port": params.get("port"),
            "status": "success" if password else "failed",
            "credentials": {
                "username": user,
                "password": password
            }
        }
    }

    with open(result_path, "w") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        params = json.load(f)
    run_hydra(params)

