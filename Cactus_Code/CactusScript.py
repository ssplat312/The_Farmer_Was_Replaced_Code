#Plants, sorts, and harvest the cactus
def PlantCactus(amountNeeded):
	while amountNeeded > num_items(Items.Cactus):
		clear()
		change_hat(Hats.Straw_Hat)
		size = get_world_size()
		totalSize = size**2
		needFer = True
		cost = get_cost(Entities.Cactus)
		while True:
			if(cost[Items.Pumpkin] * totalSize > num_items(Items.Pumpkin)):
				PlantTillEnough(Entities.Pumpkin, cost[Items.Pumpkin] * totalSize - num_items(Items.Pumpkin), needFer)
			for i in range(size):
				for j in range(size):
					UseItem(needFer)
					TillGround()
					plant(Entities.Cactus)
					move(North)
				move(East)
			
			for i in range(size):
				for j in range(size):
					SortCactusY(measure(), j)
					move(North)
				move(East)
			
			move(East)
			for i in range(size):
				for j in range(size):
					SortCactusX(measure(), j)
					move(East)
				move(North)
		
			move(South)
			move(West)
			harvest()
			move(North)
			move(East)
	
	
#Sorts the Cacti vertically	
def SortCactusY(curSize, startingPos):
	if startingPos == 0:
		return
	while curSize < measure(South):
		swap(South)
		move(South)
		if get_pos_y() == 0:
			break
	while get_pos_y() != startingPos:
		move(North)

#Sorts the Cacti horizontally
def SortCactusX(curSize, startingPos):
	if startingPos == 0:
		return
	while curSize < measure(West):
		swap(West)
		move(West)
		if get_pos_x() == 0:
			break
	while get_pos_x() != startingPos:
		move(East)