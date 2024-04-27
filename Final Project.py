from machine import ADC, Pin,
import utime
#tells the pi pico that the input from the moisture sensor will be recieved through pin 28 and that the relay will be connected to pin 13
soil_probe = ADC(Pin(28))
relay = Pin(13, Pin.OUT)

#sets the values recieved from the sensor at maximum and minimum moisture
max_moisture = 27574
min_moisture = 57100
#changes the value recieved from the moisture sensor into a percentage
def get_moisture_percentage(moisture_level):
    point_1_x = min_moisture
    point_2_x = max_moisture
    point_1_y = 0
    point_2_y = 100
    m = ((point_2_y - point_1_y) / (point_2_x - point_1_x))
    return int((m*moisture_level) - (m*min_moisture) + point_1_y)
#displays the moisture percentage value to the shell and turns the relay off and on based on that percentage
while True: 
    moisture_level = soil_probe.read_u16()
    
    moisture_level_percentage = get_moisture_percentage(moisture_level)
    
    print(moisture_level_percentage)
    
    if moisture_level_percentage <= 20:
        relay.value(1)
    if moisture_level_percentage > 20:
        relay.value(0)
    utime.sleep(0.8)
        
    
    
    
    