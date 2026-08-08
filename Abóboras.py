def plantar():
	while can_harvest() == False:
		plant(Entities.Pumpkin)
		while get_water() < .75:
			use_item(Items.Water)
	move(North)

gws = get_world_size()*0.5
TdM = get_world_size()-1
while get_pos_x() != 0:
	move(West)
while get_pos_y() != 0:
	move(South)

import DroneA

while True:
	if (get_pos_x()==0) and (get_pos_y()==0):
		spawn_drone(DroneA.pegaso)
	if get_ground_type() == Grounds.Grassland:
		till()
	
	if get_pos_y() == (TdM) and get_pos_x() == gws-1:
		plantar()
		while get_pos_x() != 0:
			move(West)
	else:
		if get_pos_y() == (TdM) and get_pos_x() < gws-1:
			plantar()
			move(East)
		else:
			plantar()
	if can_harvest() and (get_pos_y() == TdM) and (get_pos_x() == gws-1):
		while get_pos_y() != 0:
			move(South)
		for i in range(gws-1):
			move(West)
		
		while can_harvest():
			do_a_flip()
		