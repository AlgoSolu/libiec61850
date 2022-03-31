#!/usr/bin/env python
""" generated source for module LogicalDevice """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
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
class LogicalDevice(object):
    """ generated source for class LogicalDevice """
    inst = None
    ldName = None
    logicalNodes = None

    def __init__(self, ldNode, typeDeclarations):
        """ generated source for method __init__ """
        self.inst = ParserUtils.parseAttribute(ldNode, "inst")
        if self.inst == None:
            raise SclParserException(ldNode, "Logical devices misses inst attribute.")
        self.ldName = ParserUtils.parseAttribute(ldNode, "ldName")
        parseLogicalNodes(ldNode, typeDeclarations)

    def parseLogicalNodes(self, ldNode, typeDeclarations):
        """ generated source for method parseLogicalNodes """
        ln0Node = ParserUtils.getChildNodeWithTag(ldNode, "LN0")
        if ln0Node == None:
            raise SclParserException(ldNode, "Logical device misses LN0.")
        self.logicalNodes = LinkedList()
        self.logicalNodes.add(LogicalNode(ln0Node, typeDeclarations, self))
        lnNodes = ParserUtils.getChildNodesWithTag(ldNode, "LN")
        for lnNode in lnNodes:
            self.logicalNodes.add(LogicalNode(lnNode, typeDeclarations, self))

    def getInst(self):
        """ generated source for method getInst """
        return self.inst

    def getLdName(self):
        """ generated source for method getLdName """
        return self.ldName

    def getLogicalNodes(self):
        """ generated source for method getLogicalNodes """
        return self.logicalNodes

