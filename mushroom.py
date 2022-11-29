import pygame
from pygame.locals import *
import numpy as np


from SpecStem import *
from SpecCap import *
from SpecGills import *
from SpecRings import *
from SpecSpots import *
from SpecColor import *

def left_vector(v):
    return v @ np.array([[0, -1], [1, 0]])

def rotate(v, theta):
    return v @ np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta),  np.cos(theta)]])

def rotate_points(points, center, theta):
    out = []
    for time, P, T, N in points:
        P_ = center + rotate(P - center, theta)
        T_ = rotate(T, theta)
        N_ = rotate(N, theta)
        out.append((time, P_, T_, N_))
    return out

def shift_points(points, v):
    out = []
    for time, P, T, N in points:
        out.append((time, P + v, T, N))
    return out

def evaluate_cubic_spline(points, tangents, t):
    if t == 1.0:
        T = tangents[-1]
        N = left_vector(T)
        return points[-1], T / np.linalg.norm(T), N / np.linalg.norm(N)
    idx = int(t * (len(points) - 1))

    t = (len(points) - 1) * (t -  idx / (len(points) - 1))

    p1 = points[idx]
    p2 = points[idx + 1]
    d = np.linalg.norm(p2 - p1)
    t1 = d * tangents[idx] / np.linalg.norm(tangents[idx])
    t2 = d * tangents[idx + 1] / np.linalg.norm(tangents[idx + 1])

    a = p1
    b = t1
    c = -3 * p1 + 3 * p2 - 2 * t1 - t2
    d = 2* p1 - 2 * p2 + t1 + t2

    P = a + b * t + c * t * t + d * t * t * t
    T = b + 2 * c * t + 3 * d * t * t
    N = 2 * c + 6 * d * t
    return P, T / np.linalg.norm(T), N / np.linalg.norm(N)

def get_cubic_spline_points(points, tangents, dt=.001):
    out = []
    for t in np.arange(0,1+dt,dt):
        P, T, N = evaluate_cubic_spline(points, tangents, t)
        out.append((t, P, T, N))
    return out


class Mushroom:

    def __init__(self):
        self.stem_list = [SpecStemDefault, SpecStem1, SpecStem2]
        self.cap_list = [SpecCapDefault, SpecCap1, SpecCap2, SpecCap3, SpecCap4]
        self.gills_list = [SpecGillsDefault, SpecGills1]
        self.rings_list = [SpecRingsDefault, SpecRings1, SpecRings2]
        self.spots_list = [SpecSpotsDefault]
        self.color_list = [SpecColorDefault, SpecColor1, SpecColor2, SpecColor3, SpecColor4]

        self.choose_spec(default=True)
        self.generate_constants()
        self.generate_data()

    def choose_spec(self, default=True):
        if default:
            self.STEM = SpecStemDefault
            self.CAP = SpecCapDefault
            self.GILLS = SpecGillsDefault
            self.RINGS = SpecRingsDefault
            self.SPOTS = SpecSpotsDefault
            self.COLOR = SpecColorDefault
        else:
            self.STEM = np.random.choice(self.stem_list[1:])
            self.CAP = np.random.choice(self.cap_list[1:])
            self.GILLS = np.random.choice(self.gills_list[1:])
            self.RINGS = np.random.choice(self.rings_list[1:])
            self.SPOTS = np.random.choice(self.spots_list[1:])
            self.COLOR = np.random.choice(self.color_list[1:])

        # self.STEM = SpecStem2
        # self.CAP = SpecCap4
        # self.GILLS = SpecGills1
        # self.RINGS = SpecRings1
        # self.COLOR = SpecColor1

    def generate_constants(self):
        self.STEM.set_values(self)
        self.CAP.set_values(self)
        self.GILLS.set_values(self)
        self.RINGS.set_values(self)
        self.SPOTS.set_values(self)
        self.COLOR.set_values(self)

    def generate_colors(self):
        self.COLOR.set_values(self)

    def generate_data(self):
        # Stem Curve
        p1 = np.array([0, 0])
        p2 = np.array([self.stem_lean * .8, -self.stem_height * 2/3])
        p3 = np.array([self.stem_lean, -self.stem_height ])
        t1 = np.array([0, -1])
        t2 = np.array([.5 * self.stem_lean/100, -1])
        t3 = rotate(np.array([0, -1]), self.cap_rotation)
        self.stem_points = get_cubic_spline_points([p1, p2, p3], [t1, t2, t3])
        self.stem_top = np.array([self.stem_lean, -self.stem_height ])

        # Stem Width
        p1 = np.array([0, self.stem_width_bottom])
        p2 = np.array([.5, self.stem_width_middle])
        p3 = np.array([1, self.stem_width_top])
        t1 = np.array([1, 0])
        t2 = np.array([1, 0])
        t3 = np.array([1, 0])
        self.stem_width_points = get_cubic_spline_points([p1, p2, p3], [t1, t2, t3])
        self.stem_width_values = [x[1][1] for x in self.stem_width_points]

        # Cap Bottom
        p1 = np.array([self.cap_width/2, self.cap_lip])
        p2 = np.array([0, 0])
        p3 = np.array([-self.cap_width/2, self.cap_lip])
        t1 = np.array([0, 1])
        t2 = np.array([-1, 0])
        t3 = np.array([0, -1])
        self.cap_bottom_points_non_rot = get_cubic_spline_points([p1, p2, p3], [t1, t2, t3])
        self.cap_bottom_points_non_rot = shift_points(self.cap_bottom_points_non_rot, np.array([0, self.cap_veil_height]))
        self.cap_bottom_points = rotate_points(self.cap_bottom_points_non_rot, np.array([0, 0]), self.cap_rotation)

        # Cap Height
        p1 = np.array([self.cap_width/2, self.cap_lip])
        p2 = np.array([self.cap_bend_width / 2, -self.cap_height + self.cap_bend_height])
        p3 = np.array([0, -self.cap_height])
        p4 = np.array([-self.cap_bend_width / 2, -self.cap_height + self.cap_bend_height])
        p5 = np.array([-self.cap_width/2, self.cap_lip])
        t1 = np.array([0, -1])
        t2 = np.array([-1, -1])
        t3 = np.array([-1, 0])
        t4 = np.array([-1, 1])
        t5 = np.array([0, 1])
        self.cap_top_points = get_cubic_spline_points([p1, p2, p3, p4, p5], [t1, t2, t3, t4, t5])
        self.cap_top_points = shift_points(self.cap_top_points, np.array([0, self.cap_veil_height]))
        self.cap_top_points = rotate_points(self.cap_top_points, np.array([0, 0]), self.cap_rotation)

        # Cap Gills
        p1 = np.array([self.cap_width/2, self.cap_lip])
        p2 = np.array([0, -self.cap_veil_height])
        p3 = np.array([-self.cap_width/2, self.cap_lip])
        t1 = np.array([-.5, -1])
        t2 = np.array([-1, 0])
        t3 = np.array([-.5, 1])
        self.cap_gills_points_non_rot = get_cubic_spline_points([p1, p2, p3], [t1, t2, t3])
        self.cap_gills_points_non_rot = shift_points(self.cap_gills_points_non_rot, np.array([0, self.cap_veil_height]))
        self.cap_gills_points = rotate_points(self.cap_gills_points_non_rot, np.array([0, 0]), self.cap_rotation)


        self.gill_lines = []
        cur_x = self.cap_width/2
        for i in range(len(self.cap_gills_points_non_rot)):
            if self.cap_gills_points_non_rot[i][1][0] < cur_x - self.gill_spacing:
                self.gill_lines.append((self.cap_gills_points[i], self.cap_bottom_points[i]))
                cur_x = self.cap_gills_points_non_rot[i][1][0]

        # Rings and Frills
        self.ring_point_lists = []
        for ring_idx in range(self.number_of_rings):
            idx = self.get_stem_point_idx_at_height(-self.ring_height + self.ring_spacing * ring_idx)
            points = self.get_frill_points(self.stem_points[idx][1], self.stem_width_values[idx], np.arctan2(*self.stem_points[idx][2]) + np.pi)
            self.ring_point_lists.append(points)
        self.ring_point_lists.reverse()

    def draw(self, screen):
        w,h = screen.get_size()
        offset = np.array([w/2, h])

        self.draw_gills(screen, offset)
        self.draw_stem(screen, offset)
        self.draw_rings(screen, offset)
        self.draw_cap(screen, offset)
        self.draw_spots(screen, offset)

    def darken_color(self, color, itter):
        r, g, b = color[0], color[1], color[2]
        r -= 10 * itter
        g -= 10 * itter
        b -= 10 * itter
        return (r, g, b)


    def get_stem_point_idx_at_height(self, height):
        for i in range(len(self.stem_points)):
            if self.stem_points[i][1][1] <= height:
                return i
        return len(self.stem_point) - 1

    def get_frill_points(self, stem_point, width, theta):
        ring_top_right = np.array([stem_point[0] + width, stem_point[1]])
        ring_top_left = np.array([stem_point[0] - width, stem_point[1]])
        ring_bottom_right = ring_top_right + np.array([self.ring_width_offset, self.ring_bend_offset])
        ring_bottom_left = ring_top_left + np.array([-self.ring_width_offset, self.ring_bend_offset])

        frill_points = []
        frill_tangents = []

        frills_width = (2 * self.ring_width_offset + 2 * self.frills_width_offset + 2 * width)
        number_of_frills = int((frills_width // self.frill_width) - 2)
        if number_of_frills % 2 == 0:
            number_of_frills += 1
        actual_frill_width = frills_width / (1 + number_of_frills)

        for i in range(number_of_frills):
            k = self.frill_height/2 if i % 2 == 0 else -self.frill_height/2
            frill_points.append(np.array([ring_bottom_right[0] + self.frills_width_offset - (i+1) * actual_frill_width, stem_point[1] + self.frills_height_offset + k]))
            frill_tangents.append(np.array([-1,0]))

        points = [ring_top_right, ring_bottom_right] + frill_points + [ring_bottom_left, ring_top_left]
        tangents = [np.array([0,1]), np.array([0,1])] + frill_tangents + [np.array([0,-1]), np.array([0,-1])]

        ring_points_non_rot = get_cubic_spline_points(points, tangents)
        ring_points = rotate_points(ring_points_non_rot, stem_point, theta)

        return ring_points

    def draw_rings(self, screen, offset):
        for i, ring_points in enumerate(self.ring_point_lists):
            points = [x[1] + offset for x in ring_points]
            #pygame.draw.aalines(screen, (0, 255, 0), True, points)
            pygame.draw.polygon(screen, self.darken_color(self.ring_color, i), points)

    def draw_spots(self, screen, offset):
        if not self.has_spots:
            return

        mask = screen.copy().convert_alpha()
        mask.fill((0,0,0,1))
        self.draw_cap(mask, offset, (255, 255, 255))

        spots = screen.copy().convert_alpha()
        spots.fill((0,0,0,1))

        spot_center = offset + self.stem_top + rotate(np.array([0,- self.cap_height - self.spot_center_offset]), self.cap_rotation)

        spot_size = np.array([self.spot_width, self.spot_height])

        def draw_spot(location, size):
            rotation = np.arctan2(*(spot_center - location))
            shape_surface = pygame.Surface(size, pygame.SRCALPHA)
            pygame.draw.ellipse(shape_surface, self.spot_color, (0, 0, *size))
            rotated_surface = pygame.transform.rotate(shape_surface, 180 * rotation / np.pi)
            spots.blit(rotated_surface, rotated_surface.get_rect(center = location))

        for i, r in enumerate(np.arange(30, 2 * self.cap_height + self.spot_center_offset, self.spot_vertical_spacing)):
            if self.spot_even_spacing:
                layer_rotation_step = 2 * np.pi * r / self.spot_horizontal_spacing
            else:
                layer_rotation_step = self.spot_rotational_spacing
            layer_rotation_offset = np.pi + self.cap_rotation + (i % 2) * np.pi / layer_rotation_step
            for theta in np.arange(layer_rotation_offset, layer_rotation_offset + 2 * np.pi, 2 * np.pi / layer_rotation_step):
                location = spot_center + rotate(np.array([0,r]), theta)
                draw_spot(location, spot_size)

        spots.blit(mask, (0, 0), None, pygame.BLEND_RGBA_MULT)
        screen.blit(spots, (0, 0))


    def draw_cap(self, screen, offset, color_override=None):
        cap_gills_points = [x[1] + offset + self.stem_top for x in self.cap_gills_points]
        cap_top_points = [x[1] + offset + self.stem_top for x in self.cap_top_points]
        cap_top_points.reverse()

        #pygame.draw.aalines(screen, (0, 255, 0), False, cap_bottom_points)
        #pygame.draw.aalines(screen, (0, 0, 255), False, cap_top_points)
        c = color_override if (not color_override is None) else self.cap_color
        pygame.draw.polygon(screen, c, cap_gills_points + cap_top_points)

    def draw_gills(self, screen, offset):
        cap_bottom_points = [x[1] + offset + self.stem_top for x in self.cap_bottom_points]
        cap_gills_points = [x[1] + offset + self.stem_top for x in self.cap_gills_points]
        cap_gills_points.reverse()
        #pygame.draw.aalines(screen, (0, 0, 0), False, cap_gills_points)
        pygame.draw.polygon(screen, self.gills_color, cap_bottom_points + cap_gills_points)


        for p1, p2 in self.gill_lines:
            pygame.draw.line(screen, self.gill_color, p1[1] + offset + self.stem_top, p2[1] + offset + self.stem_top)

    def draw_stem(self, screen, offset):
        points = [x[1] + offset for x in self.stem_points]
        tangents = [x[2] for x in self.stem_points]

        left_points = []
        for i in range(len(points)):
            left_points.append(points[i] + self.stem_width_values[i] * left_vector(tangents[i]))

        right_points = []
        for i in range(len(points)):
            right_points.append(points[i] - self.stem_width_values[i] * left_vector(tangents[i]))
        right_points.reverse()

        #pygame.draw.aalines(screen, (0, 0, 0), False, points)
        #pygame.draw.aalines(screen, (255, 0, 0), False, left_points)
        #pygame.draw.aalines(screen, (255, 0, 0), False, right_points)
        pygame.draw.polygon(screen, self.stem_color, left_points + right_points)
