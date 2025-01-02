#Checks positions not seen with a distance bias to find the position of the treasure
def FindTreasure(tempTreasure):
	treasure = measure()
	path = []
	while True:	
		path.append([get_pos_x(), get_pos_y()])
		playerPos = [get_pos_x(), get_pos_y()]
		foundPositions = [[get_pos_x(), get_pos_y()]]
		prevDirections = []
		while get_entity_type() != Entities.Treasure:
			didMove = False
			didUseBias = False
			posibleMoves = GetPredictedMoves(playerPos, foundPositions)
			if tempTreasure != None:
				posibleMoves = SortPossiblePositions(posibleMoves, tempTreasure)
			for i in range(len(posibleMoves)):
				if CanMoveMaze(FindMoveDir(posibleMoves[i], playerPos)):
					path.append([posibleMoves[i][0], posibleMoves[i][1]])
					didMove = True
					prevDirections.insert(0, FindMoveDir(posibleMoves[i], playerPos))
					playerPos = [get_pos_x(), get_pos_y()]
					foundPositions.append([playerPos[0], playerPos[1]])
					break		
				
			if not didMove:
				MoveBack(prevDirections[0])
				prevDirections.pop(0)
				playerPos = [get_pos_x(), get_pos_y()]
				path.pop(len(path) - 1)
		#If you want to see the path taken to the treasure uncomment print(path)
		#print(path)
		break

#Sorts the horizontal and vertical position next to the drone and sorts them from least to greatest distance from  the treasure		
def SortPossiblePositions(posibleMoves, treasurePos):
	tempMoves = []
	for i in range(len(posibleMoves)):
		tempMoves.append(posibleMoves[i])
		j = len(tempMoves) - 1
		while j >= 1:
			if(FindBias(tempMoves[j], treasurePos) < FindBias(tempMoves[j - 1], treasurePos)):
				tempPos = tempMoves[j - 1]
				tempMoves[j - 1] = tempMoves[j]
				tempMoves[j] = tempPos
			j -= 1
	return tempMoves

			
	