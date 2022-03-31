#!/usr/bin/env python
""" generated source for module DataAttributeType """
from __future__ import print_function
# package: com.libiec61850.scl.types
# 
#  *  Copyright 2013, 2014 Michael Zillgith
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
class DataAttributeType(SclType):
    """ generated source for class DataAttributeType """
    subDataAttributes = None

    def getDataAttributeByName(self, name):
        """ generated source for method getDataAttributeByName """
        for dad in subDataAttributes:
            if dad.__name__ == name:
                return dad
        return None

    def __init__(self, xmlNode):
        """ generated source for method __init__ """
        super(DataAttributeType, self).__init__(xmlNode)
        elementNodes = xmlNode.getChildNodes()
        if elementNodes != None:
            self.subDataAttributes = LinkedList()
            i = 0
            while i < elementNodes.getLength():
                elementNode = elementNodes.item(i)
                if elementNode.getNodeName() == "BDA":
                    dad = DataAttributeDefinition(elementNode)
                    if self.getDataAttributeByName(dad.__name__) != None:
                        raise SclParserException(xmlNode, "DA type definition contains multiple elements of name \"" + dad.__name__ + "\"")
                    self.subDataAttributes.add(dad)
                i += 1

    def getSubDataAttributes(self):
        """ generated source for method getSubDataAttributes """
        return self.subDataAttributes

