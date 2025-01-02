#Checks to make sure moving left or right is safe
def CheckX(playerPos, snakeBody, xDif, applePos, firstTime):
	xMoves = abs(xDif)
	aX = applePos[0]
	chosenPos = GetClosestX(playerPos, snakeBody, xDif, aX)
		
	if chosenPos + xMoves >= len(snakeBody):
		return True
	else:
		return False

#Gets the snakeBody part closest to the drone in the x position, but has the same y position
def GetClosestX(playerPos, snakeBody, xDif, aX):
	chosenPos = 1000
	x = playerPos[0]
	closestX = 1000
	goRight = xDif > 0
	for i in range(1, len(snakeBody)):
		if xDif != 0:
			if goRight and (x > snakeBody[i][0] or snakeBody[i][0] > aX):
				continue
			elif not goRight and (x < snakeBody[i][0] or snakeBody[i][0] < aX):
				continue
			
		if abs(x - snakeBody[i][0]) < closestX and playerPos[1] == snakeBody[i][1]:
			closestX = snakeBody[i][0]
			chosenPos = i
	return chosenPos
	
#Not being called
def GetYWall(playerPos, snakeBody, yDif, applePos):
	y = 0
	if yDif > 0:
		y = get_world_size()
	predictedPos = [playerPos[0], y]
	if GetClosestX(predictedPos, snakeBody, yDif, applePos[0]) == 1000:
		return True
	else:
		return CheckX(predictedPos, snakeBody, GetXDif(applePos[0], predictedPos[0]), applePos, False)

#Checks to make sure moving up or down is safe	
def CheckY(playerPos, snakeBody, yDif, applePos, firstTime):
	yMoves = abs(yDif)
	aY = applePos[1]
	chosenPos = GetClosestY(playerPos, snakeBody, yDif, aY)
	
		
	if chosenPos + yMoves >= len(snakeBody):
		return True
	else:
		return False
		
#Gets the snakeBody part closest to the drone in the y position, but has the same x position
def GetClosestY(playerPos, snakeBody, yDif, aY):
	chosenPos = 1000
	y = playerPos[1]
	closestY = 1000
	goUp = yDif > 0
	for i in range(1, len(snakeBody)):
		if yDif != 0:
			if goUp and (y > snakeBody[i][1] or snakeBody[i][1] > aY):
				continue
			elif not goUp and (y < snakeBody[i][1] or snakeBody[i][1] < aY):
				continue
			
		if abs(y - snakeBody[i][1]) < closestY and playerPos[0] == snakeBody[i][0]:
			closestY = snakeBody[i][1]
			chosenPos = i
	return chosenPos

#Not being called
def GetXWall(playerPos, snakeBody, xDif, applePos):
	x = 0
	if xDif > 0:
		x = get_world_size()
	predictedPos = [x, playerPos[1]]
	if GetClosestY(predictedPos, snakeBody, xDif, applePos[1]) == 1000:
		return True
	else:
		return CheckX(predictedPos, snakeBody, GetXDif(applePos[0], predictedPos[0]), applePos, False)
		
