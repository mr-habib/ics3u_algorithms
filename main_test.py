
from main import *

def test_area_of_circle():
  assert area_of_circle(1) == 3.14
  assert area_of_circle(5) == 78.54
  assert area_of_circle(3.72) == 43.47
  
def test_volume_of_sphere():
  assert volume_of_sphere(1) == 4.19
  assert volume_of_sphere(57) == 775734.62
  assert volume_of_sphere(6.2832) == 1039.04
  
def test_hypervolume_of_4D_sphere():
  assert hypervolume_of_4D_sphere(1) == 4.93
  assert hypervolume_of_4D_sphere(4) == 1263.31
  assert hypervolume_of_4D_sphere(3.1415) == 480.64
  
def test_area_of_rect():
  assert area_of_rect(2, 3) == 6
  assert area_of_rect(32.56, 78.777) == 2564.98
  assert area_of_rect(3.14, 20) == 62.8


def test_volume_of_rect_prism():
  assert volume_of_rect_prism(2, 3, 1) == 6
  assert volume_of_rect_prism(32.56, 78.777, 17) == 43604.65
  assert volume_of_rect_prism(3.14, 20, 0.3333) == 20.93

def test_hypervolume_of_4D_prism():
  assert hypervolume_of_4D_prism(2, 2, 3, 3) == 36
  assert hypervolume_of_4D_prism(32.56, 78.777, 1, 7) == 17954.85
  assert hypervolume_of_4D_prism(3, 1, 4, 2) == 24
