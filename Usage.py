from brping import Ping360
myPing = Ping360()
myPing.connect_serial("/dev/ttyS0")
# For UDP
# myPing.connect_udp("192.168.2.2", 9092)

while (myPing.initialize() is False):
    
    if myPing.initialize() is False:
        print("Failed to initialize Ping!")

    else:
        print("Success to initialize Ping!")

if myPing.initialize() is False:
    print("Failed to initialize Ping!")
    exit(1)

data = myPing.get_distance()
if data:
    print("Distance: %s\tConfidence: %s%%" % (data["distance"], data["confidence"]))
else:
    print("Failed to get distance data")

# set the speed of sound to use for distance calculations to
# 1450000 mm/s (1450 m/s)
myPing.set_speed_of_sound(1450000)
