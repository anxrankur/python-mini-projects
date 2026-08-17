import os
import platform
import sys
from datetime import datetime

print("╔════════════════════════════════════════╗")
print("║          🖥️ SYSTEM INFO DASHBOARD      ║")
print("╠════════════════════════════════════════╣")

print(f"║ 🖥️ OS       : {platform.system():<22} ║")
print(f"║ 📦 Version  : {platform.release():<22} ║")
print(f"║ 💻 Machine  : {platform.machine():<22} ║")
print(f"║ 🐍 Python   : {platform.python_version():<22} ║")
print(f"║ 📁 Folder   : {os.getcwd()[:22]:<22} ║")
print(f"║ 🕐 Time     : {datetime.now().strftime('%H:%M:%S'):<22} ║")

print("╚════════════════════════════════════════╝")

print("\n🚀 System information loaded successfully!")
