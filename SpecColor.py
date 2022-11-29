import numpy as np

class SpecColorDefault:
    def set_values(mushroom):
        def pick_random(list):
            return list[int(np.random.rand()*len(list))]

        mushroom.stem_color = pick_random([(222, 221, 164), (222, 204, 164), (249, 250, 205)])
        mushroom.cap_color = pick_random([(166, 126, 70), (163, 87, 29), (61, 140, 186), (186, 30, 66), (173, 139, 14)])
        mushroom.gills_color = (120, 87, 42)
        mushroom.gill_color = (94, 66, 27)
        mushroom.ring_color = (199, 198, 141)
        mushroom.spot_color = pick_random([((255, 255, 255)), (207, 246, 250), (207, 250, 216)])

class SpecColor1:
    def set_values(mushroom):
        def pick_random(list):
            return list[int(np.random.rand()*len(list))]

        mushroom.stem_color = pick_random([(240, 226, 168), (235, 224, 176), (240, 228, 175)])
        mushroom.cap_color = pick_random([(140, 120, 41), (133, 112, 32), (133, 110, 25), (156, 128, 45), (138, 110, 45)])
        mushroom.gills_color = (120, 87, 42)
        mushroom.gill_color = (94, 66, 27)
        mushroom.ring_color = (199, 198, 141)
        mushroom.spot_color = (255, 255, 255)

class SpecColor2:
    def set_values(mushroom):
        def pick_random(list):
            return list[int(np.random.rand()*len(list))]

        mushroom.stem_color = pick_random([(245, 223, 191), (237, 211, 173), (237, 203, 173)])
        mushroom.cap_color = pick_random([(163, 87, 29), (161, 81, 21), (140, 77, 29), (148, 65, 24), (158, 84, 24)])
        mushroom.gills_color = (120, 38, 11)
        mushroom.gill_color = (94, 25, 2)
        mushroom.ring_color = (240, 168, 127)
        mushroom.spot_color = (255, 255, 255)

class SpecColor3:
    def set_values(mushroom):
        def pick_random(list):
            return list[int(np.random.rand()*len(list))]

        mushroom.stem_color = pick_random([(245, 240, 225), (245, 236, 208), (245, 244, 230)])
        mushroom.cap_color = pick_random([(235, 59, 59), (227, 70, 70), (240, 34, 34), (214, 34, 34), (247, 65, 65)])
        mushroom.gills_color = (140, 58, 31)
        mushroom.gill_color = (114, 45, 22)
        mushroom.ring_color = (255, 228, 224)
        mushroom.spot_color = (255, 255, 255)

class SpecColor4:
    def set_values(mushroom):
        def pick_random(list):
            return list[int(np.random.rand()*len(list))]

        mushroom.stem_color = pick_random([(195, 235, 247), (205, 240, 250)])
        mushroom.cap_color = pick_random([(131, 197, 247), (107, 169, 227), (98, 159, 217)])
        mushroom.gills_color = (93, 57, 184)
        mushroom.gill_color = (45, 20, 107)
        mushroom.ring_color = (93, 180, 227)
        mushroom.spot_color = (255, 255, 255)
