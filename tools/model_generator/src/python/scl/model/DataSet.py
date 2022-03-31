#!/usr/bin/env python
""" generated source for module DataSet """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  DataSet.java
#  *
#  *  Copyright 2013 Michael Zillgith
#  *
#  *	This file is part of libIEC61850.
#  *
#  *	libIEC61850 is free software: you can redistribute it and/or modify
#  *	it under the terms of the GNU General Public License as published by
#  *	the Free Software Foundation, either version 3 of the License, or
#  *	(at your option) any later version.
#  *
#  *	libIEC61850 is distributed in the hope that it will be useful,
#  *	but WITHOUT ANY WARRANTY; without even the implied warranty of
#  *	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  *	GNU General Public License for more details.
#  *
#  *	You should have received a copy of the GNU General Public License
#  *	along with libIEC61850.  If not, see <http://www.gnu.org/licenses/>.
#  *
#  *	See COPYING file for the complete license text.
#  
class DataSet(object):
    """ generated source for class DataSet """
    name = None
    desc = None
    fcda = None

    def __init__(self, dataSet):
        """ generated source for method __init__ """
        self.name = ParserUtils.parseAttribute(dataSet, "name")
        self.desc = ParserUtils.parseAttribute(dataSet, "desc")
        if self.name == None:
            raise SclParserException(dataSet, "Dataset misses required attribute \"name\"")
        self.fcda = LinkedList()
        fcdaNodes = ParserUtils.getChildNodesWithTag(dataSet, "FCDA")
        for fcdaNode in fcdaNodes:
            self.fcda.add(FunctionalConstraintData(fcdaNode))

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getDesc(self):
        """ generated source for method getDesc """
        return self.desc

    def getFcda(self):
        """ generated source for method getFcda """
        return self.fcda

