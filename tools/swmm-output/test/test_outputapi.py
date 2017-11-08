# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017 Bryant E. McDonnell
#
# Licensed under the terms of the MIT License
# See LICENSE.txt for details
# -----------------------------------------------------------------------------
"""Testing SWIG Generated Python Extension

Run to get output:

pytest -s
"""

# Standard library imports

# Local imports
import outputapi as oapi

from data import OUTPUT_FILE_EXAMPLE1

ls = ['subcatch', 'node', 'link', 'pollut']

def test_open():
    """
    Test Opening an Output File
    """
    handle = oapi.smo_init()
    oapi.smo_open(handle, OUTPUT_FILE_EXAMPLE1)
    handle = oapi.smo_close()

def test_get_count():
    """
    Test Opening an Output File
    """
    handle = oapi.smo_init()
    oapi.smo_open(handle, OUTPUT_FILE_EXAMPLE1)
    

    print(oapi.smo_get_version(handle))
    print(oapi.smo_get_flow_units(handle))
    
    handle = oapi.smo_close()

def test_get_ids():
    handle = oapi.smo_init()
    oapi.smo_open(handle, OUTPUT_FILE_EXAMPLE1)
    dict_size = {ls[ind]:int(val) for ind, val in enumerate((oapi.smo_get_project_size(handle)))}
    print(dict_size)

    for ind in range(dict_size['subcatch']):
        print(oapi.smo_get_element_name(handle, oapi.ElementType.NODE, ind))
    
    handle = oapi.smo_close()    








    
