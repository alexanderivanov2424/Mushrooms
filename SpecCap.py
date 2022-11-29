import numpy as np

class SpecCapDefault:
    def set_values(mushroom):
        # Cap Bottom
        mushroom.cap_width = np.random.choice([50, 80, 130, 180]) + mushroom.stem_width_top
        mushroom.cap_lip = np.random.choice([10, 30])


        # Cap Height
        mushroom.cap_height = np.random.choice([50, 100, 150])

        mushroom.cap_bend_width = np.random.choice([20, mushroom.cap_width - 30, mushroom.cap_width, mushroom.cap_width + 30])
        mushroom.cap_bend_height = 10 if mushroom.cap_bend_width == 20 else mushroom.cap_height * .8


class SpecCap1:
    def set_values(mushroom):
        # Cap Bottom
        mushroom.cap_width = np.random.choice([35, 40, 50, 60]) + mushroom.stem_width_top
        mushroom.cap_lip = np.random.choice([5, 10, 15])


        # Cap Height
        mushroom.cap_height = mushroom.cap_width + np.random.choice([0, 5, 10, 15])

        mushroom.cap_bend_width = np.random.choice([10, 15, 20])
        mushroom.cap_bend_height = np.random.choice([10, 15])

class SpecCap2:
    def set_values(mushroom):
        # Cap Bottom
        mushroom.cap_width = np.random.choice([100, 120, 160, 200]) + mushroom.stem_width_top
        mushroom.cap_lip = np.random.choice([15, 20, 30])

        # Cap Height
        mushroom.cap_height = np.random.choice([0, 10, 20]) + mushroom.cap_width * .25

        mushroom.cap_bend_width = mushroom.cap_width
        mushroom.cap_bend_height = mushroom.cap_height * .8

class SpecCap3:
    def set_values(mushroom):
        # Cap Bottom
        mushroom.cap_width = np.random.choice([100, 120, 160, 200]) + mushroom.stem_width_top
        mushroom.cap_lip = np.random.choice([15, 20, 30])

        # Cap Height
        mushroom.cap_height = np.random.choice([0, 10, 20]) + mushroom.cap_width * .25

        mushroom.cap_bend_width = mushroom.cap_width - 30
        mushroom.cap_bend_height = mushroom.cap_height * .8

class SpecCap4:
    def set_values(mushroom):
        # Cap Bottom
        mushroom.cap_width = np.random.choice([100, 120, 160, 200]) + mushroom.stem_width_top
        mushroom.cap_lip = np.random.choice([15, 20, 30])

        # Cap Height
        mushroom.cap_height = np.random.choice([10, 20, 30]) + mushroom.cap_width * .4

        mushroom.cap_bend_width = mushroom.cap_width + 30
        mushroom.cap_bend_height = mushroom.cap_height * .5
