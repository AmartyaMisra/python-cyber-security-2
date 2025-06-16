import subprocess

def scan_wifi():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=bssid"], shell=True, text=True)
        print("[+] WiFi Networks Found:\n")
        print(result)
    except Exception as e:
        print(f"[-] Error scanning WiFi: {e}")

if __name__ == "__main__":
    scan_wifi()
