#Gets the differance between the selected x position and drone x position
def GetXDif(targetX, playerX):
	return playerX - targetX

#Gets the differance between the selected y position and drone y position
def GetYDif(targetY, playerY):
	return playerY - targetY

#Waits for the spesified amount of time
def WaitForSeconds(waitAmount):
	start = get_time()
	while True:
		if(waitAmount < get_time() - start):
			break

#Tills the ground if its not tilled already					
def TillGround():
	if get_ground_type() == Grounds.Grassland:
		till()