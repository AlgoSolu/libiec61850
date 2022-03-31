#!/usr/bin/env python
""" generated source for module LogicalNodeType """
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
class LogicalNodeType(SclType):
    """ generated source for class LogicalNodeType """
    lnClass = None
    dataObjects = None

    def __init__(self, lnNode):
        """ generated source for method __init__ """
        super(LogicalNodeType, self).__init__(lnNode)
        parseAttributes(lnNode)
        parseDataObjectNodes(lnNode)

    def getObjectDefinitionByName(self, name):
        """ generated source for method getObjectDefinitionByName """
        for dod in dataObjects:
            if dod.__name__ == name:
                return dod
        return None

    def parseDataObjectNodes(self, lnNode):
        """ generated source for method parseDataObjectNodes """
        self.dataObjects = LinkedList()
        doNodeList = ParserUtils.getChildNodesWithTag(lnNode, "DO")
        for doNode in doNodeList:
            dod = DataObjectDefinition(doNode)
            if self.getObjectDefinitionByName(dod.__name__) != None:
                raise SclParserException(lnNode, "Logical node contains multiple data objects with name \"" + dod.__name__ + "\"")
            self.dataObjects.add(dod)

    def parseAttributes(self, lnNode):
        """ generated source for method parseAttributes """
        self.lnClass = ParserUtils.parseAttribute(lnNode, "lnClass")
        if self.lnClass == None:
            raise SclParserException(lnNode, "no lnClass attribute")

    def getDataObjectDefinitions(self):
        """ generated source for method getDataObjectDefinitions """
        return self.dataObjects

