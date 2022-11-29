import numpy as np

class SpecRingsDefault:
    def set_values(mushroom):
        # Stem Ring
        mushroom.number_of_rings = np.random.choice([0,1,2,3])
        mushroom.ring_height = mushroom.stem_height * np.random.choice([.5, .8])
        mushroom.ring_spacing = np.random.choice([20,30])

        # Frills
        mushroom.ring_width_offset = np.random.choice([5,10,20,30])
        mushroom.ring_bend_offset = np.random.choice([10,20])
        mushroom.frills_width_offset = np.random.choice([0,5])
        mushroom.frills_height_offset = np.random.choice([20,30])
        mushroom.frill_width = np.random.choice([3,5,6])
        mushroom.frill_height = mushroom.frill_width * np.random.choice([.5, 1, 2])

class SpecRings1:
    def set_values(mushroom):
        SpecRingsDefault.set_values(mushroom)
        mushroom.number_of_rings = 0

class SpecRings2:
    def set_values(mushroom):
        SpecRingsDefault.set_values(mushroom)
        mushroom.number_of_rings = 1
