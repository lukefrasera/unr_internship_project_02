#!/usr/bin/env python

'''
Antenna Inductance
Params: 
Return: ?
Definition:  
'''

import math

def LineAntenna(r, I):
	magnetic_inductance = (1.257e-6 * I) / (2 * math.pi * r)
	return magnetic_inductance


def CoilAntenna(I, R, x):
	return (1.257e-6 * I * (R)**2 ) / (2 * math.sqrt((R**2 + x**2)**3))

def RectangularAntenna(N, I, a, b):
	return ((1.257e-6 * N * I * a * b) / (4 * math.pi * math.sqrt((a/2)**2 + (b/2)**2 + x**2))) * ((((a/2)**2 + x**2)**-1) + ((b/2)**2 + x**2)**-1)

def TwoCoilAntennae (N1, R1, N2, R2, x):
	return (1.257e-6 * N1 * (R1)**2 * N2 * (R2)**2 * math.pi) / (2 * math.sqrt((R2**2 + x**2)**3))


def RectangularAndLineAntenna (a, b, x):
	return ((1.257e-6 * a) / (2 * math.pi)) * math.loglp((x + b) / x)

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
        while (r > minimum_distance):
            print LineAntenna(r, I)
            r -= .05

    if antenna_type == 'Coil Antenna':
        x = maximum_distance
        while (x > minimum_distance):
            print CoilAntenna(I, R1, x)
            print TwoCoilAntennae(N1, R1, N2, R2, x)
            x -= .05	






if __name__ == '__main__':
	main()

