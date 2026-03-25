from pysimverse import Drone
import time
'''
from pyimverse import DroneManager
dm = DroneManager(num_drones=2)
'''
#get_drones()
drone = Drone("SkyRaptor")

drone.take_off(1400)
# distance is in cm

drone.move_forward(1500)
time.sleep(1)
drone.move_backward(1500)
time.sleep(1)
drone.move_left(1500)
time.sleep(1)
drone.move_right(1500) 
time.sleep(2)

drone.land()