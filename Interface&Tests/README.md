# Drone

# youtube Video:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/8g3Wo9dBc7I/0.jpg)](https://www.youtube.com/watch?v=8g3Wo9dBc7I)

# The Data

The	data	is	a	log	file	from	the	drone	that	contains	the	drone	telemetry	and	the	lidars
(ranges	to	different	directions	)	and	the	wanted	state	that	human	choose	by	vision	for
the	current	situation.
notice	that	the	most	right	column	is	the	one	we	want	to	predict.


# States:
 - The data sample here has just 3 states : safe ,normal and emergency.
 - In our Algorithm 5  states are represented : 

 ###  Rotate C.C.W :slightly rotates counterclockwise(to align with the right wall).
        
 ### Emergency : Drone brakes to avoid crashing
       
 ### Tunnel :Drone centers in between the left and right walls while maintaining the  desired speed.
       
 ### Turn_CW: Drone turns 90 degrees clockwise (to find the right wall)
     
 ### FlyForward: Drone flies forward while making minor adjustments to maintain predefined bounds, i.e., its distance from the right and the desired speed.
       




# Data sample
![alt text](https://github.com/simon-pikalov/deep_drone/blob/main/photo/data_vis.png?raw=true)

# Show how the data was created.
![alt text](https://github.com/simon-pikalov/deep_drone/blob/main/photo/data_gen.png?raw=true)

# source of data sample :
https://github.com/simon-pikalov/deep_drone.git

