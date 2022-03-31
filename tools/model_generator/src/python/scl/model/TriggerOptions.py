#!/usr/bin/env python
""" generated source for module TriggerOptions """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  Copyright 2013 Michael Zillgith
#  *
#  *  This file is part of libIEC61850.
#  *
#  *  libIEC61850 is free software: you can redistribute it and/or modify
#  *  it under the terms of the GNU General Public License as published by
#  *  the Free Software Foundation, either version 3 of the License, or
#  *  (at your option) any later version.
#  *
#  *  libIEC61850 is distributed in the hope that it will be useful,
#  *  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  *  GNU General Public License for more details.
#  *
#  *  You should have received a copy of the GNU General Public License
#  *  along with libIEC61850.  If not, see <http://www.gnu.org/licenses/>.
#  *
#  *  See COPYING file for the complete license text.
#  
class TriggerOptions(object):
    """ generated source for class TriggerOptions """
    dchg = False

    #  1 
    qchg = False

    #  2 
    dupd = False

    #  4 
    period = False

    #  8 
    gi = True

    #  16 
    @overloaded
    def __init__(self, trgOpsNode):
        """ generated source for method __init__ """
        dchgVal = ParserUtils.parseBooleanAttribute(trgOpsNode, "dchg")
        if dchgVal != None:
            self.dchg = dchgVal
        qchgVal = ParserUtils.parseBooleanAttribute(trgOpsNode, "qchg")
        if qchgVal != None:
            self.qchg = qchgVal
        dupdVal = ParserUtils.parseBooleanAttribute(trgOpsNode, "dupd")
        if dupdVal != None:
            self.dupd = dupdVal
        periodVal = ParserUtils.parseBooleanAttribute(trgOpsNode, "period")
        if periodVal != None:
            self.period = periodVal
        giVal = ParserUtils.parseBooleanAttribute(trgOpsNode, "gi")
        if giVal != None:
            self.gi = giVal

    #  Constructor for default values when trigger options are not present 
    @__init__.register(object)
    def __init___0(self):
        """ generated source for method __init___0 """
        #  nothing to do

    @__init__.register(object, bool, bool, bool, bool, bool)
    def __init___1(self, dchg, qchg, dupd, period, gi):
        """ generated source for method __init___1 """
        self.dchg = dchg
        self.qchg = qchg
        self.dupd = dupd
        self.period = period
        self.gi = gi

    def getIntValue(self):
        """ generated source for method getIntValue """
        intValue = 0
        if self.dchg:
            intValue += 1
        if self.qchg:
            intValue += 2
        if self.dupd:
            intValue += 4
        if self.period:
            intValue += 8
        if self.gi:
            intValue += 16
        return intValue

    def isDchg(self):
        """ generated source for method isDchg """
        return self.dchg

    def isQchg(self):
        """ generated source for method isQchg """
        return self.qchg

    def isDupd(self):
        """ generated source for method isDupd """
        return self.dupd

    def isPeriod(self):
        """ generated source for method isPeriod """
        return self.period

    def isGi(self):
        """ generated source for method isGi """
        return self.gi

