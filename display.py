from machine import Pin, I2C
import ssd1306
import time

class WeatherDisplay:
    def __init__(self, sda_pin=4, scl_pin=5, width=128, height=32):
        """Initialize SSD1306 OLED display"""
        self.width = width
        self.height = height
        
        self.i2c = I2C(0, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=400000)
        
        self.oled = ssd1306.SSD1306_I2C(width, height, self.i2c)
        self.clear()
        
    def clear(self):
        """Clear the display"""
        self.oled.fill(0)
        self.oled.show()
        
    def show_text(self, text, x=0, y=0):
        """Display text at specified position"""
        self.oled.text(text, x, y)
        self.oled.show()
        
    def show_weather(self, weather_data):
        """Display weather information"""
        self.clear()
        
        if weather_data:
            location = weather_data.get('name', 'Unknown')
            self.oled.text(location[:16], 0, 0)
            
            temp = weather_data['main']['temp']
            temp_text = f"{temp:.1f}C"
            self.oled.text(temp_text, 0, 10)
            
            description = weather_data['weather'][0]['description']
            self.oled.text(description[:16], 0, 20)
            
        else:
            self.oled.text("Weather Error", 0, 0)
            self.oled.text("Check connection", 0, 10)
            
        self.oled.show()
        
    def show_status(self, status):
        """Show connection status"""
        self.clear()
        self.oled.text("Status:", 0, 0)
        self.oled.text(status[:16], 0, 10)
        self.oled.show()
        
    def show_loading(self):
        """Show loading animation"""
        self.clear()
        self.oled.text("Loading...", 0, 10)
        self.oled.show()
