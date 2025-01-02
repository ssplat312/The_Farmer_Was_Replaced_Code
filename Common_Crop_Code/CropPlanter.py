#PLants pumpkin if their are enough carrots, otherwise plant carrots
def PlantPumkin():
	tempCost = get_cost(Entities.Pumpkin)
	if num_items(Items.Carrot) < tempCost[Items.Carrot]:
		PlantCarrot()
		return
	TillGround()
	plant(Entities.Pumpkin)

#plants carrot if their are enough wood and hay, otherwise plant trees or grass
def PlantCarrot():
	tempCost = get_cost(Entities.Carrot)
	if(num_items(Items.Hay) < tempCost[Items.Hay]):
		plant(Entities.Grass)
	elif(num_items(Items.Wood) < tempCost[Items.Wood]):
		PlantTree()
	else:
		TillGround()
		plant(Entities.Carrot)
		
#Plants a tree if it is not vertically or horizontally next to another true, otherwise plant grass
def PlantTree():
	xPos = get_pos_x()
	yPos = get_pos_y()
	yPos += xPos % 2
	if yPos % 2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Grass)
		