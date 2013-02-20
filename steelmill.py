#!/usr/bin/env python3
"""
#   Steel Mill Slab Design Problem
#
#   This program attempts various search methods to achieve an
#   optimal solution for the Steel Mill problem without implementing
#   any constraint based solutions.
#
#   Only OO techniques are used.  This is for educational purposes.
#
#   Program should be used from a shell command in the following manner:
#
#   WINDOWS(CMD SHELL):
#       C:\Users\<username>\Documents> type <filename> | pyhton steelmill.py
#
#       This assumes the problem file has been placed in the documents folder
#       of you particular user directory.
#
#   UNIX/LINUX(BASH SHELL):
#       <user>\home\Documents$ cat <filename> | python steelmill.py
#   
#   All output will be placed in the shell window, but can be piped or echo'd into
#   another file.
"""

import sys, string

"""
#  Definition of the Order class
#
#  Contains information related to specific orders
#  Params: Size - total size of the order
#          Color - color of all slabs in the order
"""
class Order(object):
    def __init__(self, size = 0, color = 0):
        self.size = size
        self.color = color    
    def getColor(self):
        return self.color 
    def setColor(self, color):
        self.color = color       
    def getSize(self):
        return self.size
    def setSize(self, size):
        self.size = size

"""
#   Definition of the Slab class
#
#   contains the size of the slab
#   Params: Size - the total size of the slab
"""
class Slab(object):
    def __init__(self, size = 0):
        self.size = size
        self.segments = list()
        self.sizeRemaining = size
    def getSize(self):
        return self.size
    def setSize(self, size):
        self.size = size
        self.sizeRemaining = size
    def getSizeRemaining(self):
        return self.sizeRemaining
        
        
"""
#   Definition of the SteelMill class
#
#   Houses all information pertinent to the Steel Mill problem
"""
class SteelMill(object):
    def __init__(self):
        self.slabs = list()
        self.orders = list()
        self.slabCapacities = 0
        self.totalColors = 0
        self.numOfOrders = 0
        
    def addSlab(self, slab):
        self.slabs.append(slab)
    def addOrder(self, order):
        if(isinstance(order, Order) ):
            self.orders.append(order)
    def setSlabCapacties(self, number):
        self.slabCapacities = number
    def setTotalOrders(self, numOfColors):
        self.totalColors = numOfColors
    def setNumOfOrders(self, numOfOrders):
        self.numOfOrders = numOfOrders
    def getSlabs(self):
        return self.slabs
    def getOrders(self):
        return self.orders
    def getSlabCap(self):
        return self.slabCapacities
    def getTotalColors(self):
        return self.totalColors
    def getNumOrders(self):
        return self.numOfOrders
        
"""
#   Method for parsing the Steel Mill Order from and input file 
#   through a shell call.  
#
#   Output: List of Orders
#           List of Slabs
"""
def ParseSteelMillFile():
    orderInfo = SteelMill()
    lines = sys.stdin.readlines()
    
    for i, line in enumerate(lines):
        orderParams = line.split()
        
        if( i == 0 ):
            for j, slab in enumerate(orderParams):
                if( j == 0 ):
                    orderInfo.setSlabCapacties(slab[0])
                else:
                    orderInfo.addSlab(slab)
        
        elif( i == 1 ):
            orderInfo.setTotalOrders(orderParams)
            
        elif( i == 2 ):
            orderInfo.setNumOfOrders(orderParams)
            
        else:
            orderInfo.addOrder( Order(orderParams[0],orderParams[1]) )
                    
            
    return orderInfo


    