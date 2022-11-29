import numpy as np

class SpecGillsDefault:
    def set_values(mushroom):
        # Cap Gills
        mushroom.cap_veil_height = 10
        mushroom.gill_spacing = np.random.choice([3,5])

class SpecGills1:
    def set_values(mushroom):
        # Cap Gills
        mushroom.cap_veil_height = np.random.choice([10, 15])
        mushroom.gill_spacing = np.random.choice([3, 4, 5])
