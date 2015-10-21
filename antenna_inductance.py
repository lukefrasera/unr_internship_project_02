#!/usr/bin/env python

'''
Antenna Inductance
Params: <I>, <N1>, <R1>, <N>, <IR>, <a>, <b>, <N2>, <R2>, <r>, <x>
Return: floating point values calculated by the functions using antenna inductance equations (given).
Definition: Calculates the inductance of 3 types of antennas, and the mutual inductance between two types for increments of .05 between a given minimum and maximum distance.
'''

import math

#Line Antenna Inductance Equation
def LineAntennaInductance(r, I):
	return (1.257e-6 * I) / (2 * math.pi * r)

#Coil Antenna Inductance Equation
def CoilAntennaInductance(I, R, x):
	return (1.257e-6 * I * (R)**2 ) / (2 * math.sqrt((R**2 + x**2)**3))

#Rectangular Antenna Inductance Equation
def RectangularAntennaInductance(N, I, a, b, x):
	return ((1.257e-6 * N * I * a * b) / (4 * math.pi * math.sqrt((a/2)**2 + (b/2)**2 + x**2))) * ((((a/2)**2 + x**2)**-1) + ((b/2)**2 + x**2)**-1)

#Mutual Inductance between 2 Coil Antennae Equation
def TwoCoilAntennae (N1, R1, N2, R2, x):
	return (1.257e-6 * N1 * (R1)**2 * N2 * (R2)**2 * math.pi) / (2 * math.sqrt((R2**2 + x**2)**3))

#Mutual Inductance between Rectangular and Line Antennae Equation
def RectangularAndLineAntenna (a, b, x):
	return ((1.257e-6 * a) / (2 * math.pi)) * math.log1p((x + b) / x)



def main():

    '''
    I = current
    N = # of windings
    R = radius of coil antenna
    a = width of rectangular antenna
    b = length of rectangular antenna
    x = distance between 2 antennae
    '''

    #Given Variables:

    #linear antenna
    I = 10

    #coil antenna
    N1 = 200
    R1 = .1

    #rectangular antenna
    N = 1
    IR = 30
    a = .3
    b = .2

    #second coil antenna
    N2 = 200
    R2 = .15

    running = 'Y'

    while running == 'Y':

        #asks user for anntenna type and distance values
        antenna_type = raw_input('Antenna Type: ').lower()
        minimum_distance = float(raw_input('What is the minimum distance value?: '))
        maximum_distance = float(raw_input('What is the maximum distance value?: '))

        if antenna_type == 'line antenna':
            r = minimum_distance
            while (r <= maximum_distance):
                print 'Distance:' , r
                print 'Line Antenna Inductance:' , LineAntennaInductance(r, I)
                r += .05

        if antenna_type == 'coil antenna':
            x = minimum_distance
            while (x <= maximum_distance):
                print 'Distance:' , x 
                print 'Coil Antenna Inductance:' , CoilAntennaInductance(I, R1, x)
                print 'Mutual Inductance' , TwoCoilAntennae(N1, R1, N2, R2, x)
                x += .05

        if antenna_type == 'rectangular antenna':
            x = minimum_distance
            while (x <= maximum_distance):
                print 'Distance:' , x 
                print 'Rectangular Antenna Inductance:' , RectangularAntennaInductance(N, I, a, b, x)
                print 'Mutual Inductance:' , RectangularAndLineAntenna(a, b, x)
                x += .05	

        #asks for user input to continue program
        running = raw_input('Would you like to enter a new value? (Y or N)?')

        #if user inputs variable other than 'Y', program will quit



if __name__ == '__main__':
	main()

