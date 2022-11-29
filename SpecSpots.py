import numpy as np

class SpecSpotsDefault:
    def set_values(mushroom):
        # Spots
        mushroom.has_spots = np.random.choice([True, False])
        mushroom.spot_width = np.random.choice([5, 10, 20])
        mushroom.spot_height = np.random.choice([5, 10, 20])

        mushroom.spot_vertical_spacing = np.random.choice([10, 20, 30]) + mushroom.spot_height

        mushroom.spot_center_offset = np.random.choice([0, 25, 50, 100])

        mushroom.spot_even_spacing = np.random.choice([True, False])
        mushroom.spot_horizontal_spacing = np.random.choice([10, 20, 30]) + mushroom.spot_width
        mushroom.spot_rotational_spacing = np.random.choice([9, 17, 34])
