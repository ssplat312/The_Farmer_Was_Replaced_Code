#Goes through the maze or makes a maze while the maze size is greater or equal to the number of wierd substances left
def MazeScript(maxTimes, mazeSize):
	while num_items(Items.Weird_Substance) >= mazeSize:
		curTimes = 0
		clear()
		plant(Entities.Bush)
		UseItem(True)	
		treasurePosHolder = measure()
		while curTimes < maxTimes and mazeSize < num_items(Items.Weird_Substance):
			use_item(Items.Weird_Substance, mazeSize)
			FindTreasure(treasurePosHolder)
			treasurePosHolder = measure()
			curTimes += 1
		harvest()