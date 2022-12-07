# Drone

# youtube Video:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/8g3Wo9dBc7I/0.jpg)](https://www.youtube.com/watch?v=8g3Wo9dBc7I)

# The	Challenge

We	want	to	fly	a	drone	autonomously	and	without	GPS.	for	that	we	made	a	diffrent
algorithm's	such	as	fly	close	to	one	wall	;	fly	close	to	two	walls	,	hover	,	emergency
break	;	and	more	,	the	ML	part	is	to	choose	the	right	algorithm	for	the	current	situation.
that	is	a	classification	problem	to	classify	the	wanted	state	based	on	the	lidars	data.

# The Data

The	data	is	a	log	file	from	the	drone	that	contains	the	drone	telemetry	and	the	lidars
(ranges	to	different	directions	)	and	the	wanted	state	that	human	choose	by	vision	for
the	current	situation.
notice	that	the	most	right	column	is	the	one	we	want	to	predict.


# Data sample

![alt text](https://github.com/simon-pikalov/deep_drone/blob/main/photo/data_vis.png?raw=true)

# Show how the data was created.
![alt text](https://github.com/simon-pikalov/deep_drone/blob/main/photo/data_gen.png?raw=true)

 


