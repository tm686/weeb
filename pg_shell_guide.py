#!/usr/bin/env python3
"""Run a fixed set of PostgreSQL discovery commands."""

from __future__ import annotations

import subprocess


COMMANDS = [
    "ps aux | grep postgres",
    "systemctl status postgresql",
    "psql --version",
    "cat /etc/postgresql/*/main/pg_hba.conf",
    "systemctl status postgresql@*",
    "systemctl status *postgres*",
]


def run_command(command: str) -> None:
    print(f"\n$ {command}")
    result = subprocess.run(["/bin/sh", "-c", command], check=False)
    if result.returncode != 0:
        print(f"(command exited with {result.returncode})")


def main() -> None:
    for command in COMMANDS:
        run_command(command)


if __name__ == "__main__":
    main()
