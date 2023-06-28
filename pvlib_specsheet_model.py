# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 20:00:07 2023

@author: liame
"""

import pvlib

from pvlib.location import Location

import pandas as pd

celltype = 'monoSi'
pdc0 = 345
v_mp = 38.9
i_mp = 8.87
v_oc = 47.3
i_sc = 9.85
aplha_sc = 0.00048 * i_mp
beta_voc = -0.0029 * v_mp
gamma_pdc = -0.0037
cells_in_series = 12*12
temp_ref = 25

location = Location(latitude = -20.75, longitude = 144.5,
                    tz = 'Australia/Queensland', altitude = 400,
                    name = 'Kennedy Energy Park (Solar)')

surface_tilt = 0
surface_azimuth = 0

start = '2020-07-01 00:00:00'
end = '2020-07-07 23:00:00'

