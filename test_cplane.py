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

def f(z):
    return z+2

def test_plane():
    cPlane = cplane.ListComplexPlane(0,2,2,0,4,2)
    assert cPlane.plane == [[0,4j],[2,2+4j]]

def test_apply():
    cPlane = cplane.ListComplexPlane(0,2,2,0,4,2)
    assert cPlane.plane == [[0,4j],[2,2+4j]]
    cPlane.apply(f)
    assert cPlane.plane == [[2,2+4j],[4,4+4j]]

def test_zoom():
    cPlane = cplane.ListComplexPlane(0,2,2,0,4,2)
    cPlane.apply(f)
    cPlane.zoom(1,2,2,1,2,2)
    assert cPlane.plane == [[3+1j,3+2j],[4+1j,4+2j]]

def test_refresh():
    cPlane = cplane.ListComplexPlane(0,2,2,0,4,2)
    cPlane.apply(f)
    cPlane.refresh()
    assert cPlane.plane == [[0,4j],[2,2+4j]]
