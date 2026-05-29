# Windows Privacy and Telemetry Remover (Lite Version)
# Developed by: Andrea Falone | CyberScaffolding

import os
import sys
import ctypes
import subprocess

def is_admin():
    try: return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False

def run_powershell_cmd(cmd):
    try:
        subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True, timeout=30)
        return True
    except:
        return False

if not is_admin():
    print("[!] ERROR: This script requires Administrator privileges.")
    input("\nPress Enter to exit..."); sys.exit(1)

print("=" * 60)
print("     WINDOWS PRIVACY & BLOATWARE REMOVER (LITE)     ")
print("=" * 60)

print("\n[*] Disabling Microsoft Telemetry & Tracking Services...")
cmds = [
    'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" -Name "AllowTelemetry" -Value 0 -Force -ErrorAction SilentlyContinue',
    'Set-Service -Name "DiagTrack" -StartupType Disabled -ErrorAction SilentlyContinue',
    'Stop-Service -Name "DiagTrack" -Force -Confirm:$false -ErrorAction SilentlyContinue'
]
for cmd in cmds: run_powershell_cmd(cmd)
print("[+] Telemetry services disabled.")

print("\n[*] Removing preinstalled system bloatware...")
bloatware = ["Microsoft.BingNews", "Microsoft.GetHelp", "Microsoft.YourPhone", "Microsoft.SkypeApp"]
for app in bloatware:
    run_powershell_cmd(f'Get-AppxPackage -Name "{app}*" | Remove-AppxPackage -ErrorAction SilentlyContinue')
print("[+] Bloatware cleanup finished.")

print("\n[✓] Basic optimization completed successfully!")
input("\nPress Enter to close...");
