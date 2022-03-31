#!/usr/bin/env python
""" generated source for module ParserUtils """
from __future__ import print_function
# package: com.libiec61850.scl
# 
#  *  ParserUtils.java
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
class ParserUtils(object):
    """ generated source for class ParserUtils """
    @classmethod
    def parseAttribute(cls, lnNode, attributeName):
        """ generated source for method parseAttribute """
        attributes = lnNode.getAttributes()
        attributeValue = None
        if attributes != None:
            attributeNode = None
            i = 0
            while i < attributes.getLength():
                attributeNode = attributes.item(i)
                if attributeNode.getNodeName() == attributeName:
                    attributeValue = attributeNode.getNodeValue()
                i += 1
        return attributeValue

    @classmethod
    def getChildNodeWithTag(cls, node, nodeTag):
        """ generated source for method getChildNodeWithTag """
        elements = node.getChildNodes()
        if elements != None:
            childNode = None
            i = 0
            while i < elements.getLength():
                childNode = elements.item(i)
                if childNode.getNodeName() == nodeTag:
                    return childNode
                i += 1
        return None

    @classmethod
    def getChildNodesWithTag(cls, node, nodeTag):
        """ generated source for method getChildNodesWithTag """
        nodeList = LinkedList()
        elements = node.getChildNodes()
        if elements != None:
            childNode = None
            i = 0
            while i < elements.getLength():
                childNode = elements.item(i)
                if childNode.getNodeName() == nodeTag:
                    nodeList.add(childNode)
                i += 1
        return nodeList

    @classmethod
    def parseBooleanAttribute(cls, xmlNode, attributeName):
        """ generated source for method parseBooleanAttribute """
        valueStr = cls.parseAttribute(xmlNode, attributeName)
        value = bool()
        if valueStr == None:
            return None
        if valueStr.toUpperCase() == "TRUE":
            value = True
        elif valueStr.toUpperCase() == "FALSE":
            value = False
        else:
            raise SclParserException(xmlNode, "Illegal value for boolean attribute \"" + attributeName + "\"")
        return bool(value)

