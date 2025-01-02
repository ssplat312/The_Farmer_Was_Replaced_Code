#Moves the snake Towards the apple, first by the y position then the x
def MoveToApple():
	
	snakeBody = [[get_pos_x(), get_pos_y()]]
	prevPos = [get_pos_x(), get_pos_y()] 
	startingPos =  [get_pos_x(), get_pos_y()]
	mustStop = False
	isSafe = True
	while CanMoveSnake(snakeBody):
		applePos = measure()
		playerPos = [get_pos_x(), get_pos_y()]
		if mustStop:
			break
		while CanMoveSnake(snakeBody) and (GetXDif(applePos[0], playerPos[0]) != 0 or GetYDif(applePos[1], playerPos[1]) != 0):
			startingPos = [get_pos_x(), get_pos_y()]
			
			prevPos[0] =  get_pos_x()
			prevPos[1] = get_pos_y()
			
			xDif = GetXDif(applePos[0], playerPos[0])
			yDif = GetYDif(applePos[1], playerPos[1])
	
			
			if yDif != 0:
				MoveY(playerPos, snakeBody, yDif, applePos)
				prevPos[0] =  playerPos[0]
				prevPos[1] = playerPos[1]
				playerPos[0] = get_pos_x()
				playerPos[1] = get_pos_y()
				snakeBody = UpdateSnakeBody(snakeBody, prevPos)
				mustWait = False
				
			if yDif == 0:
				MoveX(playerPos, snakeBody, xDif, applePos)
					
				if xDif != 0:
					prevPos[0] =  playerPos[0]
					prevPos[1] = playerPos[1]
					playerPos[0] = get_pos_x()
					playerPos[1] = get_pos_y()
					snakeBody = UpdateSnakeBody(snakeBody, prevPos)
					mustWait = False
			

			
			
			
			if startingPos[0] == playerPos[0] and startingPos[1] == playerPos[1]:
				possibleMovements = GetPossibleMovement(get_pos_x(), get_pos_y(), snakeBody)
				for i in range(len(possibleMovements)):
					move(GetMoveDirection(possibleMovements[i], playerPos))
					playerPos[0] = get_pos_x()
					playerPos[1] = get_pos_y()
					if(startingPos[0] != playerPos[0] or startingPos[1] != playerPos[1]):
						break
					if i == len(possibleMovements) - 1:
						mustStop = True
			
			if mustStop:
				break
						

	#Out of the loop	
		lastPart = len(snakeBody) - 1
		snakeBody.append([snakeBody[lastPart][0], snakeBody[lastPart][1]])

#Moves the drone by the y position	
def MoveY(playerPos, snakeBody, yDif, applePos):
	moveDir = {0:South, 1:North}
	isSafe = CheckY(playerPos, snakeBody, yDif, applePos, True)
	if not isSafe:
		moveDir = {0:North, 1:South}
		
	if yDif > 0:
		move(moveDir[0])
	elif yDif < 0:
		move(moveDir[1])

#Moves the drone by the x position	
def MoveX(playerPos, snakeBody, xDif, applePos):
	moveDir = {0:West, 1:East}
	isSafe = CheckX(playerPos, snakeBody, xDif, applePos, True)
	if not isSafe:
		moveDir = {0:East, 1:West}
	if xDif > 0:
		move(moveDir[0])
	elif xDif < 0:
		move(moveDir[1])	

#converst the differance in the x value of 2 positions to a direction 
def GetXDir(x):
	if x > 0:
		return West
	elif x < 0:
		return East
	else: 
		return None
		
#converst the differance in the y value of 2 positions to a direction 
def GetYDir(y):
	if yDif > 0:
		return South
	elif yDif < 0:
		return North
	else:
		return None

#Checks to see if the drone can avoid runing into the snkaes bodyPart
def CanMoveSnake(sB):
	possibleMovements = GetPossibleMovement(get_pos_x(), get_pos_y(), sB)
	
	return len(possibleMovements) > 0

#Gets the possible positions the drone can move 
def GetPossibleMovement(x, y, sB):
	possibleMoves = [] 
	curAdd = -1
	for i in range(2):
		if x + curAdd >= 0 and x + curAdd <= get_world_size():
			if CheckPossiblity(sB, [x + curAdd, y]):
				possibleMoves.append([x + curAdd, y])
		
		if y + curAdd >= 0 and y + curAdd <= get_world_size():
			if CheckPossiblity(sB, [x, y + curAdd]):
				possibleMoves.append([x, y + curAdd])
		curAdd = 1
	
	return possibleMoves


#Sees if a future movement is not a movement that will hit the snakes bodyPart
def CheckPossiblity(sB, curMovement):
	for j in range(len(sB)):
			bodyPart = sB[j]
			if(bodyPart[0] == curMovement[0] and bodyPart[1] == curMovement[1]):
				return False
	return True

#Gets the direction of the drone and a future movement option
def GetMoveDirection(moveSpace, playerPos):
	if playerPos[0] - 1 == moveSpace[0]:
		return West
	elif playerPos[0] + 1 == moveSpace[0]:
		return East
	
	if playerPos[1] - 1 == moveSpace[1]:
		return South
	elif playerPos[1] + 1 == moveSpace[1]:
		return North
	
#Updates the snakes body positions by removing the last position and moving everything up by the next position until the previous drone position
def UpdateSnakeBody(snakeB, pPos):
	
	newSnake = [[pPos[0], pPos[1]]]
	for i in range(len(snakeB) - 1):
		newSnake.append(snakeB[i])
		
	return newSnake
			
	
		
	
	
	
	
	
	