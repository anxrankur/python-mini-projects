import os
import time
from datetime import datetime

while True:
    os.system("cls" if os.name == "nt" else "clear")

    now = datetime.now()

    print("╔══════════════════════════════════╗")
    print("║         DIGITAL CLOCK            ║")
    print("║                                  ║")
    print(f"║          {now.strftime('%I:%M:%S %p')}             ║")
    print(f"║          {now.strftime('%A'):<10}              ║")
    print(f"║          {now.strftime('%d %B %Y'):<16}      ║")
    print("║                                  ║")
    print("║       Python Mini Project        ║")
    print("╚══════════════════════════════════╝")
    print("\nPress Ctrl+C to stop.")

    time.sleep(1)
