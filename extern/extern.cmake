#
# CMakeLists.txt - CMake configuration file for swmm-solver/extern
#
# Created: 3/16/2020
# Updated:
#
# Author: Michael E. Tryby
#         US EPA - ORD/CESER
#


set(BOOST_ROOT ${CMAKE_SOURCE_DIR}/extern/boost_1_67_0)

find_package(Boost 1.67.0
    COMPONENTS
        unit_test_framework
    )

include_directories (${Boost_INCLUDE_DIRS})
