# RedTeamCrashKit

**A collection of resource exhaustion techniques, fork bombs, and system crash PoCs for red teamers and security researchers.**

🔴 **For educational purposes only.** 🔴

---

## 📚 What is a Fork Bomb?
A **fork bomb** is a type of **denial-of-service (DoS) attack** where a process repeatedly replicates itself, consuming all available system resources (CPU, memory, and process slots). It exploits the operating system's process management, causing the system to become unresponsive or crash.

### How It Works
1. A process **spawns copies of itself** in an infinite loop.
2. Each copy does the same, creating an **exponential growth** of processes.
3. The system runs out of **PIDs (Process IDs)** or memory, leading to a crash.

### Example (Bash)
```bash
:(){ :|:& };:
```
- :() defines a function named :.
- { :|:& } calls the function and pipes its output to another instance, running in the background.
- ; separates commands.
- The final : executes the function, starting the bomb.

## 📁 Directory Structure
```
RedTeamCrashKit/
├── /fork-bombs/          # Fork bomb examples in various languages
│   ├── python_fork_bomb.py
│   ├── bash_fork_bomb.sh
│   ├── powershell_fork_bomb.ps1
│   ├── cmd_fork_bomb.bat
│   └── zsh_fork_bomb.zsh
│   └── README.md
|
├── /mitigations/          # Defenses against these attacks
│
├── README.md              # This file
└── LICENSE                # License (MIT recommended)
```
## ⚠️ Legal & Ethical Disclaimer

**This repository is for educational and research purposes only.**
- Do not run these scripts on systems you do not own or without explicit permission.
- Unauthorized use against production systems is illegal and unethical.
- Always test in isolated environments (e.g., VMs, containers, or sandboxed systems).
- The author is not responsible for any misuse or damage caused by these scripts.

## 🛠️ How to Test Safely

1.**Use a Virtual Machine (VM):**
  - Tools: VirtualBox, VMware, or Hyper-V.
  - Assign limited resources (e.g., 1 CPU core, 512MB RAM).

2.**Use Containers:**
  - Docker with resource limits:
    ```
    docker run --memory=512m --cpus=1 -it ubuntu bash
    ```
3.**Set Process Limits:**
  - Linux: Use ```ulimit -u 100 to limit``` user processes.
  - Windows: Use Task Manager or Group Policy to restrict process creation.

## 📜 License
This project is licensed under the **MIT License**. See LICENSE for details.
