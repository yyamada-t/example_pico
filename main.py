from machine import Pin
import time
import gc
from display import WeatherDisplay
from network import NetworkManager
from config import DEFAULT_CITY, DEFAULT_COUNTRY, DISPLAY_UPDATE_INTERVAL

class WeatherStation:
    def __init__(self):
        self.display = WeatherDisplay(sda_pin=4, scl_pin=5)
        self.network = NetworkManager()
        
        self.button = Pin(15, Pin.IN, Pin.PULL_UP)
        self.last_button_time = 0
        self.button_debounce = 500  # 500ms debounce
        
        self.last_weather_update = 0
        self.current_weather = None
        
    def button_pressed(self):
        """Check if button was pressed with debouncing"""
        current_time = time.ticks_ms()
        if not self.button.value() and (current_time - self.last_button_time) > self.button_debounce:
            self.last_button_time = current_time
            return True
        return False
        
    def update_weather(self, force=False):
        """Update weather data if needed"""
        current_time = time.time()
        
        if force or (current_time - self.last_weather_update) > DISPLAY_UPDATE_INTERVAL:
            self.display.show_loading()
            
            weather_data = self.network.get_weather(DEFAULT_CITY, DEFAULT_COUNTRY)
            
            if weather_data:
                self.current_weather = weather_data
                self.last_weather_update = current_time
                print("Weather updated successfully")
            else:
                print("Failed to update weather")
                
            self.display.show_weather(self.current_weather)
            
    def run(self):
        """Main application loop"""
        print("Starting Weather Station...")
        
        self.display.show_status("Starting...")
        time.sleep(2)
        
        self.display.show_status("Connecting WiFi")
        if not self.network.connect_wifi():
            self.display.show_status("WiFi Failed")
            return
            
        self.display.show_status("WiFi Connected")
        time.sleep(2)
        
        self.update_weather(force=True)
        
        print("Weather station ready!")
        
        while True:
            try:
                if self.button_pressed():
                    print("Button pressed - updating weather")
                    self.update_weather(force=True)
                
                self.update_weather()
                
                if not self.network.is_connected():
                    self.display.show_status("WiFi Lost")
                    if self.network.connect_wifi():
                        self.display.show_status("WiFi Restored")
                        time.sleep(2)
                        self.display.show_weather(self.current_weather)
                
                gc.collect()
                
                time.sleep(0.1)
                
            except KeyboardInterrupt:
                print("Shutting down...")
                break
            except Exception as e:
                print(f"Error in main loop: {e}")
                self.display.show_status("System Error")
                time.sleep(5)

if __name__ == "__main__":
    station = WeatherStation()
    station.run()
