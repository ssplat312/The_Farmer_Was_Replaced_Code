#Plants Sunflowers and harvest from greatest petals to least petals
def PlantSunflowers():
	while True:
		clear()
		sunflowersPlanted = 0
		AllPetals = {15:0, 14:0, 13:0, 12:0, 11:0, 10:0, 9:0, 8:0, 7:0}
		sortedPositions = []
		while sunflowersPlanted != get_world_size()**2:
			harvest()
			till()
			plant(Entities.Sunflower)
			UseItem(False)
			curPos = [get_pos_x(), get_pos_y()]
			if len(sortedPositions) > 0:
				AddToPositions(AllPetals, sortedPositions, curPos, measure())
			else:
				sortedPositions.append([curPos[0], curPos[1]])
			AllPetals[measure()] += 1
			move(North)
			sunflowersPlanted += 1
			if get_pos_y() == 0:
				move(East)
		WaitForSeconds(9)
		CollectSunFlowers(sortedPositions)
	

#Adds the current position to a list of all sunflowers planted; sorted by the petal amount
def AddToPositions(petals, curPositions, curPos, curPetals):
	addPosition = 0
	i = 15
	while i >= curPetals:
		addPosition += petals[i]
		i -= 1
	if len(curPositions) >= addPosition:
		curPositions.insert(addPosition, curPos)
	else:
		curPositions.append(curPos)

#harvest the sunflower at the given position
def CollectSunFlowers(positions):
	while len(positions) > 0:
		MoveToPos(positions[0])
		positions.pop(0)
		while get_entity_type() == Entities.Sunflower:
			harvest()

#Moves to the given position	
def MoveToPos(position):
	curPos = [get_pos_x(), get_pos_y()]
	while position[0] != curPos[0] or position[1] != curPos[1]:
		curPos = [get_pos_x(), get_pos_y()]
		xDif = GetXDif(position[0], curPos[0])
		yDif = GetYDif(position[1], curPos[1])
		if xDif > 0:
			move(West)
		elif xDif < 0:
			move(East)
			
		if yDif > 0:
			move(South)
		elif yDif< 0:
			move(North)