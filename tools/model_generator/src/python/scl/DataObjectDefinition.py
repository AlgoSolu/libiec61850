#!/usr/bin/env python
""" generated source for module DataObjectDefinition """
from __future__ import print_function
# package: com.libiec61850.scl
# 
#  *  DataObjectDefinition.java
#  *
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
class DataObjectDefinition(object):
    """ generated source for class DataObjectDefinition """
    name = None
    type_ = None
    trans = False

    #  transient attribute value 
    count = 0

    def __init__(self, dataObjectNode):
        """ generated source for method __init__ """
        self.name = ParserUtils.parseAttribute(dataObjectNode, "name")
        self.type_ = ParserUtils.parseAttribute(dataObjectNode, "type")
        isTransient = ParserUtils.parseBooleanAttribute(dataObjectNode, "transient")
        if isTransient != None:
            self.trans = isTransient
        if (self.type_ == None) or (self.name == None):
            raise SclParserException(dataObjectNode, "DO misses required attribute.")
        countStr = ParserUtils.parseAttribute(dataObjectNode, "count")
        if countStr != None:
            self.count = int(countStr)

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getType(self):
        """ generated source for method getType """
        return self.type_

    def getCount(self):
        """ generated source for method getCount """
        return self.count

    def isTransient(self):
        """ generated source for method isTransient """
        return self.trans

