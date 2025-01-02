#Plants the crop according to the crop variable
def PlantCrop(crop):
	if crop == Entities.Carrot:
		PlantCarrot()
	elif crop == Entities.Pumpkin:
		PlantPumkin()
	elif crop == Entities.Tree:
		PlantTree()
	else:
		plant(crop)