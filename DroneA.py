def plantar():
	while can_harvest() == False:
		plant(Entities.Pumpkin)
		while get_water() < .75:
			use_item(Items.Water)
	move(North)
	
def pegaso():
	gws = get_world_size()*0.5
	TdM = get_world_size()-1
	
	while get_pos_x() != gws:
		move(East)
	while get_pos_y() != 0:
		move(South)
		
	while True:
		if get_ground_type() == Grounds.Grassland:
			till()
			
		if get_pos_y() == (TdM) and get_pos_x() == TdM:
			plantar()
			while get_pos_x() != gws:
				move(West)
		else:
			if get_pos_y() == TdM:
				plantar()
				move(East)
			else:
				plantar()
		if can_harvest() and (get_pos_x()==gws) and (get_pos_y()==0):
			for i in range(gws):
				do_a_flip()
			harvest()
	
	