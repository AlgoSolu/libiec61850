#!/usr/bin/env python
""" generated source for module DataObjectType """
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
class DataObjectType(SclType):
    """ generated source for class DataObjectType """
    cdc = None
    dataAttributes = None
    subDataObjects = None

    def getDataAttributeByName(self, name):
        """ generated source for method getDataAttributeByName """
        for dad in dataAttributes:
            if dad.__name__ == name:
                return dad
        return None

    def getDataObjectByName(self, name):
        """ generated source for method getDataObjectByName """
        for dod in subDataObjects:
            if dod.__name__ == name:
                return dod
        return None

    def __init__(self, xmlNode):
        """ generated source for method __init__ """
        super(DataObjectType, self).__init__(xmlNode)
        self.cdc = ParserUtils.parseAttribute(xmlNode, "cdc")
        if self.cdc == None:
            raise SclParserException(xmlNode, "cdc is missing!")
        elementNodes = xmlNode.getChildNodes()
        if elementNodes != None:
            self.dataAttributes = LinkedList()
            self.subDataObjects = LinkedList()
            i = 0
            while i < elementNodes.getLength():
                elementNode = elementNodes.item(i)
                if elementNode.getNodeName() == "DA":
                    dad = DataAttributeDefinition(elementNode)
                    otherDefinition = self.getDataAttributeByName(dad.__name__)
                    if otherDefinition != None:
                        if otherDefinition.getFc() == dad.getFc():
                            raise SclParserException(xmlNode, "DO type definition contains multiple elements of name \"" + dad.__name__ + "\"")
                    if self.getDataObjectByName(dad.__name__) != None:
                        raise SclParserException(xmlNode, "DO type definition contains multiple elements of name \"" + dad.__name__ + "\"")
                    self.dataAttributes.add(dad)
                elif elementNode.getNodeName() == "SDO":
                    dod = DataObjectDefinition(elementNode)
                    if (self.getDataAttributeByName(dod.__name__) != None) or (self.getDataObjectByName(dod.__name__) != None):
                        raise SclParserException(xmlNode, "DO type definition contains multiple elements of name \"" + dod.__name__ + "\"")
                    self.subDataObjects.add(dod)
                i += 1

    def getCdc(self):
        """ generated source for method getCdc """
        return self.cdc

    def getDataAttributes(self):
        """ generated source for method getDataAttributes """
        return self.dataAttributes

    def getSubDataObjects(self):
        """ generated source for method getSubDataObjects """
        return self.subDataObjects

