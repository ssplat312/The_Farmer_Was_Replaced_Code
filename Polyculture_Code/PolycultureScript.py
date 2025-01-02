#Farms using the Polyculture method
def Polyculture(useFertilizer):
	clear()
	plantChoices = [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot]
	curChoice = 0
	companionPos = []
	companionCrop = []
	while True:
		harvest()
		curPos = [get_pos_x(), get_pos_y()]
		selectedCompanion = CheckPolyExist(curPos, companionPos)
		if selectedCompanion == -1:
			if curChoice > 3:
				curChoice = 0
			elif curChoice == 3:
				TillGround()
			plant(plantChoices[curChoice])
			curChoice += 1
		else:
			if companionCrop[selectedCompanion] == Entities.Carrot:
				TillGround()
			plant(companionCrop[selectedCompanion])
			companionCrop.pop(selectedCompanion)
			companionPos.pop(selectedCompanion)
			
		companionInfo = get_companion()
		if CheckPolyExist(companionInfo[1], companionPos) == -1:
			companionCrop.append(companionInfo[0])
			companionPos.append(companionInfo[1])
		
		UseItem(useFertilizer)
		move(North)
		if get_pos_y() == 0:
			move(East)
		
#Checks if the drone position is in a companion position
def CheckPolyExist(curPos, companionPos):
	for i in range(len(companionPos)):
		if companionPos[i][0] == curPos[0] and companionPos[i][1] == curPos[1]:
			return i
	return -1
		
	
	