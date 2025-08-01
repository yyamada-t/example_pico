import network
import urequests
import ujson
import time
from config import WIFI_SSID, WIFI_PASSWORD, OPENWEATHER_API_KEY, OPENWEATHER_BASE_URL

class NetworkManager:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.connected = False
        
    def connect_wifi(self):
        """Connect to WiFi network"""
        self.wlan.active(True)
        
        if not self.wlan.isconnected():
            print(f"Connecting to WiFi: {WIFI_SSID}")
            self.wlan.connect(WIFI_SSID, WIFI_PASSWORD)
            
            timeout = 10
            while not self.wlan.isconnected() and timeout > 0:
                time.sleep(1)
                timeout -= 1
                
        if self.wlan.isconnected():
            self.connected = True
            print(f"Connected! IP: {self.wlan.ifconfig()[0]}")
            return True
        else:
            self.connected = False
            print("Failed to connect to WiFi")
            return False
            
    def disconnect_wifi(self):
        """Disconnect from WiFi"""
        if self.wlan.isconnected():
            self.wlan.disconnect()
        self.wlan.active(False)
        self.connected = False
        
    def get_weather(self, city="Tokyo", country="JP"):
        """Fetch weather data from OpenWeatherMap API"""
        if not self.connected:
            print("Not connected to WiFi")
            return None
            
        try:
            url = f"{OPENWEATHER_BASE_URL}?q={city},{country}&appid={OPENWEATHER_API_KEY}&units=metric"
            
            print(f"Fetching weather for {city}, {country}")
            response = urequests.get(url)
            
            if response.status_code == 200:
                weather_data = ujson.loads(response.text)
                response.close()
                return weather_data
            else:
                print(f"API Error: {response.status_code}")
                response.close()
                return None
                
        except Exception as e:
            print(f"Network error: {e}")
            return None
            
    def is_connected(self):
        """Check if connected to WiFi"""
        return self.wlan.isconnected()
