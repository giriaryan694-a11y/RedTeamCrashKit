# Mitigations Against Fork Bombs & Resource Exhaustion Attacks

This guide provides **defensive techniques** to prevent, detect, and mitigate fork bombs and other resource exhaustion attacks.

---

## 🛡️ Prevention Techniques

### 1. Limit User Processes

Restrict the number of processes a user can spawn.

#### **Linux (using `ulimit`)**

* Edit `/etc/security/limits.conf`:

  ```conf
  * soft nproc 100
  * hard nproc 200
  ```
* Apply limits to a specific user:

  ```conf
  username soft nproc 50
  username hard nproc 100
  ```
* Verify with:

  ```bash
  ulimit -u
  ```

#### **Windows (Group Policy)**

1. Open **Local Group Policy Editor** (`gpedit.msc`).
2. Navigate to:
   **Computer Configuration → Windows Settings → Security Settings → Local Policies → Security Options**.
3. Set **"Limit the number of processes"** (if available) or use third-party tools like **Process Explorer** to monitor and restrict processes.

---

### 2. Use Control Groups (cgroups) (Linux)

* Limit CPU, memory, and process creation for users or containers.
* Example: Create a cgroup to limit processes:

  ```bash
  sudo cgcreate -g memory,cpu:/forkbomb_limit
  sudo cgset -r memory.limit_in_bytes=512M forkbomb_limit/
  sudo cgset -r cpu.shares=512 forkbomb_limit/
  ```
* Run untrusted scripts inside the cgroup:

  ```bash
  cgexec -g memory,cpu:forkbomb_limit bash
  ```

---

### 3. Use Docker/Container Limits

* Run untrusted code in containers with strict resource limits:

  ```bash
  docker run --memory=512m --cpus=1 --pids-limit=100 -it ubuntu bash
  ```

---

### 4. Disable Fork Bombs in Shells

#### **Bash/Zsh**

* Add this to `~/.bashrc` or `~/.zshrc`:

  ```bash
  ulimit -u 100  # Limit user processes
  ```

#### **PowerShell**

* Use `Set-Item` to limit process creation:

  ```powershell
  $ProcessLimit = 100
  $CurrentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
  Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" -Name "MaxProcesses" -Value $ProcessLimit
  ```

---

## 🚨 Detection Techniques

### 1. Monitor Process Count

#### **Linux**

* Use `ps` or `top` to monitor process count:

  ```bash
  ps aux | wc -l
  ```
* Set up alerts with `cron`:

  ```bash
  */5 * * * * root if [ $(ps aux | wc -l) -gt 500 ]; then echo "Fork bomb detected!" | mail -s "Alert" admin@example.com; fi
  ```

#### **Windows**

* Use Task Manager or PowerShell:

  ```powershell
  Get-Process | Measure-Object | Select-Object -ExpandProperty Count
  ```

---

### 2. Use Intrusion Detection Systems (IDS)

* Tools like **OSSEC**, **AIDE**, or **Wazuh** can detect abnormal process spikes.
* Example OSSEC rule:

  ```xml
  <rule id="100001" level="10">
    <if_sid>502</if_sid>  <!-- Process creation -->
    <match>^ossec: output: 'Process .* created'</match>
    <check_diff></check_diff>
    <frequency>10</frequency>  <!-- Alert if 10 processes created in a short time -->
  </rule>
  ```

---

## 🛑 Mitigation Techniques

### 1. Kill Rogue Processes

#### **Linux**

* Find and kill all processes owned by a user:

  ```bash
  pkill -9 -u username
  ```
* Kill processes by name:

  ```bash
  pkill -9 -f "fork_bomb"
  ```

#### **Windows**

* Use Taskkill:

  ```powershell
  taskkill /F /IM cmd.exe
  ```

---

### 2. Automate Response with Scripts

#### **Linux (Bash Script)**

```bash
#!/bin/bash
# Kill all processes for a user if they exceed 200 processes
USER="username"
MAX_PROCESSES=200

if [ $(ps -u $USER | wc -l) -gt $MAX_PROCESSES ]; then
  echo "Fork bomb detected for $USER! Killing processes..."
  pkill -9 -u $USER
fi
```

#### **Windows (PowerShell Script)**

```powershell
$User = "username"
$MaxProcesses = 200

$ProcessCount = (Get-WmiObject Win32_Process | Where-Object { $_.GetOwner().User -eq $User }).Count
if ($ProcessCount -gt $MaxProcesses) {
  Write-Host "Fork bomb detected for $User! Killing processes..."
  Get-WmiObject Win32_Process | Where-Object { $_.GetOwner().User -eq $User } | ForEach-Object { $_.Terminate() }
}
```

---

## 🔧 System Hardening

### 1. Disable Unnecessary Shell Features

* Restrict shell access for untrusted users.
* Use `rbash` (restricted Bash) for limited environments.

### 2. Use Mandatory Access Control (MAC)

* **Linux**: Use **SELinux** or **AppArmor** to restrict process creation.
* **Windows**: Use **Software Restriction Policies (SRP)** or **AppLocker**.

### 3. Regular Audits

* Audit user privileges and process limits.
* Review logs for unusual activity.

---

## 📚 Further Reading

* [Linux Process Limits](https://linux.die.net/man/2/setrlimit)
* [Docker Security](https://docs.docker.com/engine/security/)
* [Windows Process Management](https://docs.microsoft.com/en-us/windows/win32/procthread/process-creation-flags)

---
