import psutil
import time
import os

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def monitor_resources():
    try:
        while True:
            # Clear terminal screen
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # CPU usage
            cpu_percent = psutil.cpu_percent(interval=1)
            
            # RAM usage
            ram = psutil.virtual_memory()
            ram_percent = ram.percent
            ram_used = get_size(ram.used)
            ram_total = get_size(ram.total)
            
            # Disk usage (root /)
            disk = psutil.disk_usage('/')
            disk_percent = disk.percent
            disk_used = get_size(disk.used)
            disk_total = get_size(disk.total)
            
            # Display status
            print("REAL-TIME SYSTEM RESOURCE MONITOR\n")
            print(f"CPU Usage: {cpu_percent}% ", end="")
            if cpu_percent > 80:
                print("⚠️  High CPU Usage!")
            else:
                print()
                
            print(f"RAM Usage: {ram_used} / {ram_total} ({ram_percent}%) ", end="")
            if ram_percent > 80:
                print("⚠️  High RAM Usage!")
            else:
                print()
                
            print(f"Disk Usage: {disk_used} / {disk_total} ({disk_percent}%)")
            
            # Sleep before next update
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_resources()