#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Julie Gardner-Hoag, Logan Gantner
# Student ID: 2299636, 2307470
# Email: gardnerh@chapman.edu, gantner@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 5
###

import cplane

def test_plane():
    cPlane = cplane.ListComplexPlane(0,2,2,0,4,2)
    assert cPlane.plane == [[0,4j],[2,2+4j]]

