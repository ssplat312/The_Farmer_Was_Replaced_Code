#Plants the selected crop untill it reaches the amountNeeded(also uses fertilizer if fertilzerRequired is True
def PlantTillEnough(crop, amountNeeded, fertilzerRequired):
	clear()
	change_hat(Hats.Straw_Hat)
	rowSize = get_world_size()
	fieldSize = rowSize**2
	mainCrop = crop
	wantFertilzer = fertilzerRequired
	pumpkinAmount = 0
	while num_items(EntitiesToItem(mainCrop)) <= amountNeeded:
		pumpkinAmount = 0
		for i in range(rowSize):
			#Gets the amount of pumpkins in the field
			if get_entity_type() == Entities.Pumpkin:
				pumpkinAmount += 1
	
			if can_harvest() and (get_entity_type() != Entities.Pumpkin or mainCrop != Entities.Pumpkin or (pumpkinAmount == get_world_size() and get_pos_x() == rowSize - 1)):
				harvest()
			PlantCrop(mainCrop)
			UseItem(wantFertilzer)
			move(North)
		if mainCrop != Entities.Pumpkin:
			move(East)
		elif pumpkinAmount == rowSize:
			move(East)
		else:
			WaitForSeconds(2)
		
			
#Conversts the Entities variable to its Item variable
def EntitiesToItem(entity):
	if(entity == Entities.Grass):
		return Items.Hay
	elif(entity == Entities.Bush or entity == Entities.Tree):
		return Items.Wood
	elif(entity == Entities.Carrot):
		return Items.Carrot
	elif(entity == Entities.Pumpkin):
		return Items.Pumpkin
	