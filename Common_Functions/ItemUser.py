#Uses every avialible item and if var is true then uses fertilizer
def UseItem(usingFertilizer):
	UseWater()
	
	if usingFertilizer:
		UseFertilizer()

#Uses water to spesified amount
def UseWater():
	if get_entity_type() != None and get_water() < .5:
		use_item(Items.Water)
		
#Uses fertilizer if crop is on ground
def UseFertilizer():
	if(get_entity_type() != None):
		use_item(Items.Fertilizer)