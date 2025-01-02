#Gets the bias of a tile by getting the the tiles position distance from the treasure position
def FindBias(nP, tP):
	return GetDistance(nP, tP)

#Get the disance from the treasure position from the movement position by getting the absolute value of the subtracted x and y positions, and then sqaure rooting the x^2 + y^2
def GetDistance(nextPos, treasurePos):
	x = abs(nextPos[0] - treasurePos[0])
	y = abs(nextPos[1] - treasurePos[1])
	return sqrt(x**2 + y**2)

#Gets the sqaure root of a number
def sqrt(baseNum):
	if baseNum <= 1:
		return baseNum
	
	powNum = 1
	maxNum = powNum + 1
	while baseNum > maxNum**2:
		powNum += 1
		maxNum = powNum + 1
	
	if baseNum/powNum == powNum:
		return baseNum/powNum
	elif baseNum/maxNum == maxNum:
		return baseNum/maxNum
	
	closestNum = baseNum
	
	if baseNum - powNum**2 < baseNum - maxNum**2:
		closestNum = powNum**2
	else:
		closestNum = maxNum**2
	
	return (baseNum + closestNum)/(2 * sqrt(closestNum))	
	
#Gets all of the posibe positions the drone can move to while excluding the positions the drone has already been to
def GetPredictedMoves(curPos, foundPos):
	posiblePos = []
	for i in range(-1, 2, 2):
		newPos = [curPos[0] + i, curPos[1]]
		if not SeenPosition(newPos, foundPos):
			posiblePos.append(newPos)
		
		newPos = [curPos[0], curPos[1] + i]
		if not SeenPosition(newPos, foundPos):
			posiblePos.append(newPos)
	
	return posiblePos
			
#Moves the opposite dricection given
def MoveBack(prevDir):
	if prevDir == East:
		move(West)
	elif prevDir == West:
		move(East)
	elif prevDir == North:
		move(South)
	elif prevDir == South:
		move(North)
		
#Gets the direction of a specific position compared to the drone position
def FindMoveDir(newPos, curPos):
	
	if(newPos[0] != curPos[0]):
		if newPos[0] > curPos[0]:
			return East
		else:
			return West
	else:
		if newPos[1] > curPos[1]:
			return North
		else:
			return South
			
#Sees if the drone can move a certain direction
def CanMoveMaze(direction):
	return move(direction)

#Sees if the given direction is a horizontal direction
def isXDir(direction):
	return direction == West or direction == East

#Sees if the given direction is a vertical direction
def isYDir(direction):
	return direction == North or direction == South

#Checks to see if the drone position is in a position that has already been checked
def SeenPosition(curPos, foundPos):
	for i in range(len(foundPos)):
		if curPos[0] == foundPos[i][0] and curPos[1] == foundPos[i][1]:
			return True
			
	return False 