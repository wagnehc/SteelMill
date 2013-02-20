#!/usr/bin/env python3
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
    def getSize(self):
        return self.size
    def setSize(self, size):
        self.size = size
        
        
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


    