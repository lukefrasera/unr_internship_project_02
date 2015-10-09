#!/usr/bin/env python

'''
Antenna Inductance
Params: 
Return: ?
Definition:  
'''

import math

def LineAntenna(radius):
	magnetic_inductance = (.000001257 * 10) / (2 * math.pi * radius)
	return magnetic_inductance


def CoilAntenna (radius):
	magnetic_inductance = (.000001257 * 10 * (radius)**2 ) / (2 * math.sqrt((radius ** 2 + ))



def main():
	antenna_type = raw_input('Antenna Type: ')
	minimum_distance = float(raw_input('What is the minimum distance value?: '))
	maximum_distance = float(raw_input('What is the maximum distance value?: '))
	
	radius = maximum_distance - minimum_distance
	r = radius
	x = radius
	
	if antenna_type == 'Line Antenna':
		print LineAntenna (r)
	
	






if __name__ == '__main__':
	main()

