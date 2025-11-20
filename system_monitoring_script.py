"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON SCRIPT TO DISPLAY CPU, RAM, AND DISK STATS USING psutil 🐍🖥️📊

This script prints real-time system usage information such as
CPU load, memory usage, and disk space. Useful for monitoring
performance or creating simple dashboards.
"""

# Import psutil for system monitoring
import psutil

# Import shutil to format bytes into readable units
import shutil

def format_bytes(size):
    """
    Convert bytes to human-readable units (KB, MB, GB).
    """
    return shutil._ntuple_diskusage((size, 0, 0)).total // (1024 ** 3)  # Quick conversion to GB

# --- Step 1: CPU Usage ---
cpu_usage = psutil.cpu_percent(interval=1)  # 1-second average
print(f"🧠 CPU Usage: {cpu_usage}%")

# --- Step 2: RAM Usage ---
memory = psutil.virtual_memory()
ram_total = memory.total / (1024 ** 3)
ram_used = memory.used / (1024 ** 3)
ram_percent = memory.percent

print(f"💾 RAM: {ram_used:.2f} GB / {ram_total:.2f} GB ({ram_percent}%)")

# --- Step 3: Disk Usage ---
disk = psutil.disk_usage('/')
disk_total = disk.total / (1024 ** 3)
disk_used = disk.used / (1024 ** 3)
disk_percent = disk.percent

print(f"📀 Disk: {disk_used:.2f} GB / {disk_total:.2f} GB ({disk_percent}%)")

# Optional: Display all partitions
# for part in psutil.disk_partitions():
#     print(part.device, psutil.disk_usage(part.mountpoint))
