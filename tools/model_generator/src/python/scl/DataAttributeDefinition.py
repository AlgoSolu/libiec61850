#!/usr/bin/env python
""" generated source for module DataAttributeDefinition """
from __future__ import print_function
# package: com.libiec61850.scl
# 
#  *  DataAttributeDefinition.java
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
class DataAttributeDefinition(object):
    """ generated source for class DataAttributeDefinition """
    name = None
    bType = None
    type_ = None
    count = 0
    fc = None
    attributeType = None
    triggerOptions = None
    value = None

    def __init__(self, node):
        """ generated source for method __init__ """
        self.name = ParserUtils.parseAttribute(node, "name")
        self.bType = ParserUtils.parseAttribute(node, "bType")
        self.type_ = ParserUtils.parseAttribute(node, "type")
        fcString = ParserUtils.parseAttribute(node, "fc")
        if self.name == None:
            raise SclParserException(node, "attribute name is missing")
        if fcString != None:
            self.fc = FunctionalConstraint.createFromString(fcString)
        if self.bType == None:
            raise SclParserException(node, "attribute bType is missing")
        else:
            if self.bType == "Tcmd":
                self.type_ = "Tcmd"
            elif self.bType == "Dbpos":
                self.type_ = "Dbpos"
            elif self.bType == "Check":
                self.type_ = "Check"
            self.attributeType = AttributeType.createFromSclString(self.bType)
        dchgTrigger = False
        qchgTrigger = False
        dupdTrigger = False
        dchg = ParserUtils.parseAttribute(node, "dchg")
        if dchg != None:
            dchgTrigger = bool(dchg)
        dupd = ParserUtils.parseAttribute(node, "dupd")
        if dupd != None:
            dupdTrigger = bool(dupd)
        qchg = ParserUtils.parseAttribute(node, "qchg")
        if qchg != None:
            qchgTrigger = bool(qchg)
        self.triggerOptions = TriggerOptions(dchgTrigger, qchgTrigger, dupdTrigger, False, False)
        countStr = ParserUtils.parseAttribute(node, "count")
        if countStr != None:
            self.count = int(countStr)
        if self.bType != None:
            elementNodes = node.getChildNodes()
            if elementNodes != None:
                i = 0
                while i < elementNodes.getLength():
                    elementNode = elementNodes.item(i)
                    if elementNode.getNodeName() == "Val":
                        value = elementNode.getTextContent()
                        if self.attributeType == AttributeType.ENUMERATED:
                            self.value = DataModelValue(self.attributeType, self.type_, self.value)
                        else:
                            try:
                                self.value = DataModelValue(self.attributeType, None, self.value)
                            except IllegalValueException as e:
                                #  TODO Auto-generated catch block
                                e.printStackTrace()
                    i += 1

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getbType(self):
        """ generated source for method getbType """
        return self.bType

    def getType(self):
        """ generated source for method getType """
        return self.type_

    def getFc(self):
        """ generated source for method getFc """
        return self.fc

    def getAttributeType(self):
        """ generated source for method getAttributeType """
        return self.attributeType

    def getCount(self):
        """ generated source for method getCount """
        return self.count

    def getValue(self):
        """ generated source for method getValue """
        return self.value

    def getTriggerOptions(self):
        """ generated source for method getTriggerOptions """
        return self.triggerOptions

