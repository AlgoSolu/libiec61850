#!/usr/bin/env python
""" generated source for module FunctionalConstraint """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  Copyright 2013, 2014 Michael Zillgith
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
class FunctionalConstraint:
    """ generated source for enum FunctionalConstraint """
    #  not specified 
    intValue = int()

    def __init__(self, intValue):
        """ generated source for method __init__ """
        self.intValue = intValue

    def getIntValue(self):
        """ generated source for method getIntValue """
        return self.intValue

    @classmethod
    def createFromString(cls, fc):
        """ generated source for method createFromString """
        return FunctionalConstraint.valueOf(fc)

FunctionalConstraint.ST = FunctionalConstraint(0)

FunctionalConstraint.MX = FunctionalConstraint(1)

FunctionalConstraint.SP = FunctionalConstraint(2)

FunctionalConstraint.SV = FunctionalConstraint(3)

FunctionalConstraint.CF = FunctionalConstraint(4)

FunctionalConstraint.DC = FunctionalConstraint(5)

FunctionalConstraint.SG = FunctionalConstraint(6)

FunctionalConstraint.SE = FunctionalConstraint(7)

FunctionalConstraint.SR = FunctionalConstraint(8)

FunctionalConstraint.OR = FunctionalConstraint(9)

FunctionalConstraint.BL = FunctionalConstraint(10)

FunctionalConstraint.EX = FunctionalConstraint(11)

FunctionalConstraint.CO = FunctionalConstraint(12)

FunctionalConstraint.ALL = FunctionalConstraint(99)

FunctionalConstraint.NONE = FunctionalConstraint(-1)

