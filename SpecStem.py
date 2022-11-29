import numpy as np

class SpecStemDefault:
    def set_values(mushroom):
        # Stem Curve
        mushroom.stem_lean = np.random.choice([-100, 0, 100])
        mushroom.stem_height = np.random.choice([100, 200, 300]) + 100

        mushroom.cap_rotation = np.random.choice([-np.pi/8, -np.pi/16, 0, np.pi/16, np.pi/8])

        # Stem Width
        mushroom.stem_width_top = np.random.choice([5, 10, 20])
        mushroom.stem_width_middle = mushroom.stem_width_top + np.random.choice([0, 5, 10])
        mushroom.stem_width_bottom = mushroom.stem_width_middle + np.random.choice([5, 10, 15])

class SpecStem1:
    def set_values(mushroom):
        # Stem Curve
        mushroom.stem_lean = np.random.choice([-100, 0, 100])
        mushroom.stem_height = np.random.choice([100, 200, 300]) + 100

        mushroom.cap_rotation = np.random.choice([-np.pi/8, -np.pi/16, 0, np.pi/16, np.pi/8])

        # Stem Width
        mushroom.stem_width_top = np.random.choice([3, 5, 7])
        mushroom.stem_width_middle = mushroom.stem_width_top + np.random.choice([0, 2, 4])
        mushroom.stem_width_bottom = mushroom.stem_width_middle + np.random.choice([2, 4, 6])

class SpecStem2:
    def set_values(mushroom):
        # Stem Curve
        mushroom.stem_lean = np.random.choice([-80, 0, 80])
        mushroom.stem_height = np.random.choice([100, 125, 150]) + 75

        mushroom.cap_rotation = np.random.choice([-np.pi/8, -np.pi/16, 0, np.pi/16, np.pi/8])

        # Stem Width
        mushroom.stem_width_top = np.random.choice([10, 15, 20])
        mushroom.stem_width_middle = mushroom.stem_width_top + np.random.choice([0, 5, 10])
        mushroom.stem_width_bottom = mushroom.stem_width_middle + np.random.choice([15, 20, 25])
