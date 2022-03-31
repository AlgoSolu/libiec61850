#!/usr/bin/env python
""" generated source for module PhyComAddress """
from __future__ import print_function
# package: com.libiec61850.scl.communication
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
class PhyComAddress(object):
    """ generated source for class PhyComAddress """
    vlanId = None
    vlanPriority = None
    appId = None
    macAddress = None

    def __init__(self, addressNode):
        """ generated source for method __init__ """
        pNodes = ParserUtils.getChildNodesWithTag(addressNode, "P")
        for pNode in pNodes:
            type_ = ParserUtils.parseAttribute(pNode, "type")
            if type_ == "VLAN-ID":
                self.vlanId = Integer.parseInt(pNode.getTextContent(), 16)
                if self.vlanId > 0xfff:
                    raise SclParserException(addressNode, "VLAN-ID value out of range")
            elif type_ == "VLAN-PRIORITY":
                self.vlanPriority = Integer.parseInt(pNode.getTextContent())
            elif type_ == "APPID":
                self.appId = Integer.parseInt(pNode.getTextContent(), 16)
                if self.appId > 0xffff:
                    raise SclParserException(addressNode, "APPID value out of range")
            elif type_ == "MAC-Address":
                addressElements = pNode.getTextContent().split("-")
                if len(addressElements):
                    raise SclParserException(addressNode, "malformed address " + pNode.getTextContent())
                self.macAddress = [None] * 6
                i = 0
                while len(addressElements):
                    self.macAddress[i] = Integer.parseInt(addressElements[i], 16)
                    i += 1
        if self.vlanId == None:
            self.vlanId = int(0)
        if self.vlanPriority == None:
            self.vlanPriority = int(4)
        if self.macAddress == None:
            self.macAddress = [None] * 6
            #  default MAC address: 01-0C-CD-01-00-00 
            self.macAddress[0] = 0x01
            self.macAddress[1] = 0x0c
            self.macAddress[2] = 0xcd
            self.macAddress[3] = 0x01
            self.macAddress[4] = 0x00
            self.macAddress[5] = 0x00
        if self.appId == None:
            self.appId = int(0)

    def getVlanId(self):
        """ generated source for method getVlanId """
        return self.vlanId

    def getVlanPriority(self):
        """ generated source for method getVlanPriority """
        return self.vlanPriority

    def getAppId(self):
        """ generated source for method getAppId """
        return self.appId

    def getMacAddress(self):
        """ generated source for method getMacAddress """
        return self.macAddress

