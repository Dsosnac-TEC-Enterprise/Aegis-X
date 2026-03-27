import subprocess
import shutil

class HackRFManager:
    """
    Manages the HackRF One SDR hardware.
    Requires 'hackrf' tools installed on the host system.
    """
    def __init__(self):
        self.is_present = False
        self.check_tools()

    def check_tools(self):
        """Verifies if hackrf-tools are installed on the OS."""
        if shutil.which("hackrf_info") is not None:
            return True
        print("[-] HackRF tools not found. Install via 'sudo apt install hackrf'")
        return False

    def get_info(self):
        """Runs hackrf_info to detect the device and return hardware specs."""
        try:
            result = subprocess.run(["hackrf_info"], capture_output=True, text=True)
            if result.returncode == 0:
                self.is_present = True
                return result.stdout
            else:
                self.is_present = False
                return "HackRF not detected."
        except Exception as e:
            return f"Error detecting HackRF: {str(e)}"

    def start_rx(self, frequency_hz, filename="capture.iq", timeout=5):
        """
        Triggers a basic IQ signal capture at a specific frequency.
        """
        if not self.check_tools(): return "Tools missing."
        
        # Command: hackrf_transfer -r <file> -f <freq_hz> -l 32 -g 20
        # -l: LNA gain, -g: VGA gain
        command = [
            "hackrf_transfer", 
            "-r", filename, 
            "-f", str(frequency_hz), 
            "-n", "2000000" # Capture 2M samples then stop
        ]
        
        try:
            # We run this as a subprocess
            proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return f"Started RX capture at {frequency_hz} Hz..."
        except Exception as e:
            return f"Failed to start RX: {e}"

# Standalone test
if __name__ == "__main__":
    sdr = HackRFManager()
    print("--- HackRF Status ---")
    print(sdr.get_info())


    def start_sweep(self, start_mhz=2400, end_mhz=2480, bin_width=1000000):
        """
        Performs a rapid frequency sweep (default: 2.4GHz ISM band).
        bin_width: 1MHz steps by default.
        """
        if not self.check_tools(): return "HackRF tools not found."

        # Command: hackrf_sweep -f <start>:<end> -w <bin_width>
        command = [
            "hackrf_sweep",
            "-f", f"{start_mhz}:{end_mhz}",
            "-w", str(bin_width),
            "-n", "1" # Just one sweep for a snapshot
        ]

        try:
            result = subprocess.run(command, capture_output=True, text=True)
            # Parse CSV-style output from hackrf_sweep
            sweep_data = result.stdout.splitlines()
            return {"data": sweep_data[:10], "status": "Sweep complete"} # Send first 10 rows for preview
        except Exception as e:
            return {"error": str(e)}

# Update the start_sweep method in HackRFManager

    def start_sweep(self, start_mhz=2400, end_mhz=2480):
        if not self.check_tools(): return {"error": "Tools missing"}

        command = ["hackrf_sweep", "-f", f"{start_mhz}:{end_mhz}", "-n", "1"]
        
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            labels = []
            values = []

            # hackrf_sweep output is CSV: 
            # date, time, hz_low, hz_high, hz_bin_width, samples, db_1, db_2...
            for line in result.stdout.splitlines():
                parts = line.split(', ')
                if len(parts) > 6:
                    freq_mhz = int(parts[2]) / 1000000
                    db_level = float(parts[6]) # Using the first bin's power level
                    
                    labels.append(f"{freq_mhz:.1f}")
                    values.append(db_level)

            # We'll downsample to 10 points so the chart isn't overcrowded
            step = max(1, len(labels) // 10)
            return {
                "labels": labels[::step],
                "datasets": [{"data": values[::step]}]
            }
        except Exception as e:
            return {"error": str(e)}


