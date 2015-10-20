#!/usr/bin/env python

'''
Antenna Inductance
Params: <I>, <N1>, <R1>, <N>, <IR>, <a>, <b>, <N2>, <R2>, <r>, <x>
Return: floating point values calculated by the functions using antenna inductance equations (given).
Definition: Calculates the inductance of 3 types of antennas, and the mutual inductance between two types for increments of .05 between a given minimum and maximum distance.
'''

import math

def LineAntennaInductance(r, I):
	return (1.257e-6 * I) / (2 * math.pi * r)


def CoilAntennaInductance(I, R, x):
	return (1.257e-6 * I * (R)**2 ) / (2 * math.sqrt((R**2 + x**2)**3))

def RectangularAntennaInductance(N, I, a, b, x):
	return ((1.257e-6 * N * I * a * b) / (4 * math.pi * math.sqrt((a/2)**2 + (b/2)**2 + x**2))) * ((((a/2)**2 + x**2)**-1) + ((b/2)**2 + x**2)**-1)

def TwoCoilAntennae (N1, R1, N2, R2, x):
	return (1.257e-6 * N1 * (R1)**2 * N2 * (R2)**2 * math.pi) / (2 * math.sqrt((R2**2 + x**2)**3))


def RectangularAndLineAntenna (a, b, x):
	return ((1.257e-6 * a) / (2 * math.pi)) * math.log1p((x + b) / x)

def main():

    antenna_type = raw_input('Antenna Type: ')
    minimum_distance = float(raw_input('What is the minimum distance value?: '))
    maximum_distance = float(raw_input('What is the maximum distance value?: '))


    #linear
    I = 10

    #coil
    N1 = 200
    R1 = .1

    #rectangular
    N = 1
    IR = 30
    a = .3
    b = .2

    #second coil            
    N2 = 200
    R2 = .15

    '''
    I = current
    N = # of windings
    R = radius of coil antenna
    a = width of rectangular antenna
    b = length of rectangular antenna
    x = distance between 2 antennae
    '''

    if antenna_type == 'Line Antenna':
        r = maximum_distance
        while (r >= minimum_distance):
            print 'Distance:' , r
            print 'Line Antenna Inductance:' , LineAntennaInductance(r, I)
            r -= .05

    if antenna_type == 'Coil Antenna':
        x = maximum_distance
        while (x >= minimum_distance):
            print 'Distance:' , x 
            print 'Coil Antenna Inductance:' , CoilAntennaInductance(I, R1, x)
            print 'Mutual Inductance' , TwoCoilAntennae(N1, R1, N2, R2, x)
            x -= .05
            
            
    if antenna_type == 'Rectangular Antenna':
        x = maximum_distance
        while (x >= minimum_distance):
            print 'Distance:' , x 
            print 'Rectangular Antenna Inductance:' , RectangularAntennaInductance(N, I, a, b, x)
            print 'Mutual Inductance:' , RectangularAndLineAntenna(a, b, x)
            x -= .05	





if __name__ == '__main__':
	main()

