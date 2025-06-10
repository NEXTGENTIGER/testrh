from read_input import read_targets
from run_hydra import run_hydra

if __name__ == "__main__":
    targets = read_targets("input.json")
    for target in targets:
        service = target.get("service")
        if service == "ssh":
            run_hydra(target["destination_ip"], target["port"])
