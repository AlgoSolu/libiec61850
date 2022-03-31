#!/usr/bin/env python
""" generated source for module SmvOpts """
from __future__ import print_function
# package: com.libiec61850.scl.model
class SmvOpts(object):
    """ generated source for class SmvOpts """
    refreshTime = False

    #  1 
    sampleSynchronized = False

    #  2 
    sampleRate = False

    #  4 
    dataSet = False

    #  8 
    security = False

    #  16 
    def __init__(self, smvOptsNode):
        """ generated source for method __init__ """
        refreshTime = ParserUtils.parseBooleanAttribute(smvOptsNode, "refreshTime")
        if refreshTime != None:
            self.refreshTime = refreshTime
        sampleRate = ParserUtils.parseBooleanAttribute(smvOptsNode, "sampleRate")
        if sampleRate != None:
            self.sampleRate = sampleRate
        dataSet = ParserUtils.parseBooleanAttribute(smvOptsNode, "dataSet")
        if dataSet != None:
            self.dataSet = dataSet
        security = ParserUtils.parseBooleanAttribute(smvOptsNode, "security")
        if security != None:
            self.security = security
        sampleSynchronized = ParserUtils.parseBooleanAttribute(smvOptsNode, "sampleSynchronized")
        if sampleSynchronized != None:
            self.sampleSynchronized = sampleSynchronized

    def getIntValue(self):
        """ generated source for method getIntValue """
        intValue = 0
        if self.refreshTime:
            intValue += 1
        if self.sampleSynchronized:
            intValue += 2
        if self.sampleRate:
            intValue += 4
        if self.dataSet:
            intValue += 8
        if self.security:
            intValue += 16
        return intValue

