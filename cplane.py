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
        dx = (xmax-xmin)/(xlen-1)
        dy = (ymax-ymin)/(ylen-1)

        ### Create possible x and y values on grid by adding integer amounts of step size
        x_grid_vals = [xmin + i*dx for i in range(xlen)]
        y_grid_vals = [ymin + i*dy for i in range(ylen)]

        plane = []
        for x in x_grid_vals:
            plane.append([])
            for y in y_grid_vals:
                plane[-1].append(x + 1j*y)
        return plane
    
    def refresh(self):
        """Removes all functions from self.fs and restores self.plane to its original grid values"""
        self.fs = []
        self.plane = self.__create_grid(self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen)

    def apply(self, f):
        for i in range(self.xlen):
            for j in range(self.ylen):
                ### Replace the current point (z) in the grid with f(z)
                z = self.plane[i][j]
                self.plane[i][j] = f(z)
        self.fs.append(f)

    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen

        self.plane = self.__create_grid(self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen)
        
        ### Need a copy of self.fs for the list repeatedly adds to itself
        fs_copy = list(self.fs)
        self.fs = []
        for f in fs_copy:
            self.apply(f)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    