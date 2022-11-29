import numpy as np

class SpecOverride:
    def set_values(mushroom):

      """
      Here mushroom parameters can be overriden. This is applied last after all parameters are generated.
      
      
      """

      pass
      # # Stem Curve
      # mushroom.stem_lean = np.random.choice([-100, 0, 100])
      # mushroom.stem_height = np.random.choice([100, 200, 300]) + 100

      # mushroom.cap_rotation = np.random.choice([-np.pi/8, -np.pi/16, 0, np.pi/16, np.pi/8])

      # # Stem Width
      # mushroom.stem_width_top = np.random.choice([5, 10, 20])
      # mushroom.stem_width_middle = mushroom.stem_width_top + np.random.choice([0, 5, 10])
      # mushroom.stem_width_bottom = mushroom.stem_width_middle + np.random.choice([5, 10, 15])

      # # Cap Bottom
      # mushroom.cap_width = np.random.choice([50, 80, 130, 180]) + mushroom.stem_width_top
      # mushroom.cap_lip = np.random.choice([10, 30])

      # # Cap Height
      # mushroom.cap_height = np.random.choice([50, 100, 150])

      # mushroom.cap_bend_width = np.random.choice([20, mushroom.cap_width - 30, mushroom.cap_width, mushroom.cap_width + 30])
      # mushroom.cap_bend_height = 10 if mushroom.cap_bend_width == 20 else mushroom.cap_height * .8

      # # Cap Gills
      # mushroom.cap_veil_height = 10
      # mushroom.gill_spacing = np.random.choice([3,5])

      # # Stem Ring
      # mushroom.number_of_rings = np.random.choice([0,1,2,3])
      # mushroom.ring_height = mushroom.stem_height * np.random.choice([.5, .8])
      # mushroom.ring_spacing = np.random.choice([20,30])

      # # Frills
      # mushroom.ring_width_offset = np.random.choice([5,10,20,30])
      # mushroom.ring_bend_offset = np.random.choice([10,20])
      # mushroom.frills_width_offset = np.random.choice([0,5])
      # mushroom.frills_height_offset = np.random.choice([20,30])
      # mushroom.frill_width = np.random.choice([3,5,6])
      # mushroom.frill_height = mushroom.frill_width * np.random.choice([.5, 1, 2])

      # # Spots
      # mushroom.has_spots = np.random.choice([True, False])
      # mushroom.spot_width = np.random.choice([5, 10, 20])
      # mushroom.spot_height = np.random.choice([5, 10, 20])

      # mushroom.spot_vertical_spacing = np.random.choice([10, 20, 30]) + mushroom.spot_height

      # mushroom.spot_center_offset = np.random.choice([0, 25, 50, 100])

      # mushroom.spot_even_spacing = np.random.choice([True, False])
      # mushroom.spot_horizontal_spacing = np.random.choice([10, 20, 30]) + mushroom.spot_width
      # mushroom.spot_rotational_spacing = np.random.choice([9, 17, 34])

      # # Colors
      # def pick_random(list):
      #   return list[int(np.random.rand()*len(list))]
      # mushroom.stem_color = pick_random([(222, 221, 164), (222, 204, 164), (249, 250, 205)])
      # mushroom.cap_color = pick_random([(166, 126, 70), (163, 87, 29), (61, 140, 186), (186, 30, 66), (173, 139, 14)])
      # mushroom.gills_color = (120, 87, 42)
      # mushroom.gill_color = (94, 66, 27)
      # mushroom.ring_color = (199, 198, 141)
      # mushroom.spot_color = pick_random([((255, 255, 255)), (207, 246, 250), (207, 250, 216)])
