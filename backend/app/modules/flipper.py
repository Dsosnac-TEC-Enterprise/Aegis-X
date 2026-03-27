import serial
import serial.tools.list_ports
import time

class FlipperManager:
    """
    A class to manage serial communication with a Flipper Zero device.
    """
    def __init__(self, port=None, baudrate=115200, timeout=2):
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None
        # If no port is provided, we will try to auto-detect it
        self.port = port or self._auto_detect_flipper()

    def _auto_detect_flipper(self):
        """Scans available serial ports to find the Flipper Zero."""
        ports = serial.tools.list_ports.comports()
        for port in ports:
            # Flipper Zeros usually identify themselves with 'Flipper' in the description
            if "Flipper" in port.description or "usbmodem" in port.device:
                print(f"[+] Flipper Zero auto-detected on port: {port.device}")
                return port.device
        print("[-] Flipper Zero not found. Please specify the port manually.")
        return None

    def connect(self):
        """Establishes the serial connection to the Flipper."""
        if not self.port:
            return False
        
        try:
            self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            time.sleep(1) # Give it a moment to initialize
            
            # Send a dummy command to clear the buffer and get to the prompt
            self.serial_conn.write(b"\r\n")
            self.serial_conn.read_until(b">: ")
            print(f"[+] Successfully connected to Flipper on {self.port}")
            return True
        except serial.SerialException as e:
            print(f"[-] Failed to connect to Flipper: {e}")
            return False

    def send_command(self, command):
        """
        Sends a CLI command to the Flipper and returns the output.
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            print("[-] Not connected to Flipper.")
            return None

        try:
            # Encode command to bytes and add carriage return + newline
            full_command = f"{command}\r\n".encode('ascii')
            self.serial_conn.write(full_command)
            
            # Read the response until the Flipper prompt appears again
            response = self.serial_conn.read_until(b">: ")
            
            # Decode and clean up the output
            decoded_response = response.decode('ascii', errors='ignore')
            # Strip out the command echo and the trailing prompt for a clean output
            clean_output = decoded_response.replace(command, "").replace(">:", "").strip()
            
            return clean_output
        except Exception as e:
            print(f"[-] Error sending command: {e}")
            return None

    def disconnect(self):
        """Safely closes the serial connection."""
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()
            print("[+] Disconnected from Flipper.")

# --- Standalone Testing ---
# If you run this file directly, it will test the connection.
if __name__ == "__main__":
    print("Testing Flipper Zero Integration...")
    
    # Initialize the manager
    flipper = FlipperManager()
    
    if flipper.connect():
        print("\nSending 'info' command...")
        output = flipper.send_command("info")
        print("\n--- Flipper Output ---")
        print(output)
        print("----------------------\n")
        
        flipper.disconnect()
