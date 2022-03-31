#!/usr/bin/env python
""" generated source for module ConnectedAP """
from __future__ import print_function
# package: com.libiec61850.scl.communication
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
class ConnectedAP(object):
    """ generated source for class ConnectedAP """
    iedName = None
    apName = None
    gses = None
    smvs = None
    address = None

    def __init__(self, node):
        """ generated source for method __init__ """
        self.iedName = ParserUtils.parseAttribute(node, "iedName")
        self.apName = ParserUtils.parseAttribute(node, "apName")
        if (self.iedName == None) or (self.apName == None):
            raise SclParserException(node, "ConnectedAP is missing required attribute")
        self.gses = LinkedList()
        gseNodes = ParserUtils.getChildNodesWithTag(node, "GSE")
        for gseNode in gseNodes:
            self.gses.add(GSE(gseNode))
        self.smvs = LinkedList()
        smvNodes = ParserUtils.getChildNodesWithTag(node, "SMV")
        for smvNode in smvNodes:
            self.smvs.add(SMV(smvNode))
        addressNode = ParserUtils.getChildNodeWithTag(node, "Address")
        if addressNode != None:
            self.address = Address(addressNode)

    def getIedName(self):
        """ generated source for method getIedName """
        return self.iedName

    def getApName(self):
        """ generated source for method getApName """
        return self.apName

    def getAddress(self):
        """ generated source for method getAddress """
        return self.address

    def getGses(self):
        """ generated source for method getGses """
        return self.gses

    def getSmvs(self):
        """ generated source for method getSmvs """
        return self.smvs

    def lookupGSE(self, logicalDeviceName, name):
        """ generated source for method lookupGSE """
        for gse in self.getGses():
            if gse.getLdInst() == logicalDeviceName:
                if gse.getCbName() == name:
                    return gse
        return None

    def lookupSMVAddress(self, logicalDeviceName, name):
        """ generated source for method lookupSMVAddress """
        for smv in self.getSmvs():
            if smv.getLdInst() == logicalDeviceName:
                if smv.getCbName() == name:
                    return smv.getAddress()
        return None

