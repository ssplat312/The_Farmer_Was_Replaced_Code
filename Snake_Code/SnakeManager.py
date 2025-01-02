#Runs snake game until you dont have enough pumpkins
def SnakeScript():
	cost = get_cost(Entities.Apple)
	while cost[Items.Pumpkin] <= num_items(Items.Pumpkin):
		clear()
		if(cost[Items.Pumpkin] * get_world_size()**2 < num_items(Items.Pumpkin)):
			PlantTillEnough(Entities.Pumpkin, cost[Items.Pumpkin] * get_world_size()**2 - num_items(Items.Pumpkin), False)
		change_hat(Hats.Dinosaur_Hat)
		plant(Entities.Apple)
		MoveToApple()
	