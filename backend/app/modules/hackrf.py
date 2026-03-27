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
