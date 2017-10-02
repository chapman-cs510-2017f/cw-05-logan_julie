#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Julie Gardner-Hoag, Logan Gantner
# Student ID: 2299636, 2307470
# Email: gardnerh@chapman.edu, gantner@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 5
###

from abscplane import AbsComplexPlane

class ListComplexPlane(AbsComplexPlane):
    """Class containing a complex grid equipped with methods designed to easily edit grid values simultaneously

    Args:
        xmin (float): the grid's min real value
        xmax (float): the grid's max real value
        xlen   (int): the number of points spanning [xmin, xmax]
        ymin (float): the grid's min imag value
        ymax (float): the grid's max imag value
        ylen   (int): the number of points spanning [ymin, ymax]

    Attributes:
        plane (:obj:`list` of :obj:`list` of :obj:`complex`): A 2D list representing the current state of the
            complex grid (see __create_grid)
        fs (:obj:`list` of :obj:`function`): A list of all functions that have been applied to the plane since
            the latest refresh
    """
    def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen):
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen

        self.plane = self.__create_grid(self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen)
        ### An ordered list of functions that have been applied to the plane points
        self.fs    = []

    def __create_grid(self, xmin, xmax, xlen, ymin, ymax, ylen):
        """
        Private method for producing a grid based on the provided dimensions.
        Grid is stored and accessed in self.plane as a 2D list, such that each row
        in the grid (i.e. self.plane[0]) is the set of points with fixed imaginary coordinate.

        Example:
        self.__create_grid(0,1,2,0,2,3) = [[0+0j, 0+1j, 0+2j],
                                           [1+0j, 1+1j, 1+2j]]
        """

        ### Determine step sizes for the plane grid
        dx = (xmax-xmin)/(xlen-1)
        dy = (ymax-ymin)/(ylen-1)

        ### Create possible x and y values on grid by adding integer amounts of step size
        x_grid_vals = [xmin + i*dx for i in range(xlen)]
        y_grid_vals = [ymin + i*dy for i in range(ylen)]

        plane = []
        for x in x_grid_vals:
            ### Create empty row
            plane.append([])
            for y in y_grid_vals:
                ### Populate the row by modifying the imaginary value only
                plane[-1].append(x + 1j*y)
        return plane

    def refresh(self):
        """Removes all functions from self.fs and restores self.plane to its unmodified grid values"""
        self.fs = []
        self.plane = self.__create_grid(self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen)

    def apply(self, f):
        """
        Given a single-argument function f, replaces all points z in self.plane with f(z).
        Also adds the applied function to list self.fs
        """
        for i in range(self.xlen):
            for j in range(self.ylen):
                ### Replace the current point (z) in the grid with f(z)
                z = self.plane[i][j]
                self.plane[i][j] = f(z)
        ### Store the applied function for future reference
        self.fs.append(f)

    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """Redefines the grid based on new dimensions, then reapplies all functions from self.fs to the grid"""
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        ### Reset the grid
        self.plane = self.__create_grid(self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen)

        ### Apply all functions from self.fs to the new grid.
        ### We need a copy of self.fs or else the list repeatedly appends to itself as it iterates
        fs_copy = list(self.fs)
        self.fs = []
        for f in fs_copy:
            self.apply(f)
