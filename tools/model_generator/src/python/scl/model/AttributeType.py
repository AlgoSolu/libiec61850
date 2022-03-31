#!/usr/bin/env python
""" generated source for module AttributeType """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  AttributeType.java
#  *
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
class AttributeType:
    """ generated source for enum AttributeType """
    intValue = int()

    def __init__(self, intValue):
        """ generated source for method __init__ """
        self.intValue = intValue

    def getIntValue(self):
        """ generated source for method getIntValue """
        return self.intValue

    @classmethod
    def createFromSclString(cls, typeString):
        """ generated source for method createFromSclString """
        if typeString == "BOOLEAN":
            return BOOLEAN
        elif typeString == "INT8":
            return INT8
        elif typeString == "INT16":
            return INT16
        elif typeString == "INT32":
            return INT32
        elif typeString == "INT64":
            return INT64
        elif typeString == "INT128":
            return INT128
        elif typeString == "INT8U":
            return INT8U
        elif typeString == "INT16U":
            return INT16U
        elif typeString == "INT24U":
            return INT24U
        elif typeString == "INT32U":
            return INT32U
        elif typeString == "FLOAT32":
            return FLOAT32
        elif typeString == "FLOAT64":
            return FLOAT64
        elif typeString == "Enum":
            return ENUMERATED
        elif typeString == "Dbpos":
            return CODEDENUM
        elif typeString == "Check":
            return CHECK
        elif typeString == "Tcmd":
            return CODEDENUM
        elif typeString == "Octet64":
            return OCTET_STRING_64
        elif typeString == "Quality":
            return QUALITY
        elif typeString == "Timestamp":
            return TIMESTAMP
        elif typeString == "Currency":
            return CURRENCY
        elif typeString == "VisString32":
            return VISIBLE_STRING_32
        elif typeString == "VisString64":
            return VISIBLE_STRING_64
        elif typeString == "VisString65":
            return VISIBLE_STRING_65
        elif typeString == "VisString129":
            return VISIBLE_STRING_129
        elif typeString == "ObjRef":
            return VISIBLE_STRING_129
        elif typeString == "VisString255":
            return VISIBLE_STRING_255
        elif typeString == "Unicode255":
            return UNICODE_STRING_255
        elif typeString == "OptFlds":
            return OPTFLDS
        elif typeString == "TrgOps":
            return TRGOPS
        elif typeString == "EntryID":
            return OCTET_STRING_8
        elif typeString == "EntryTime":
            return ENTRY_TIME
        elif typeString == "PhyComAddr":
            return PHYCOMADDR
        elif typeString == "Struct":
            return CONSTRUCTED
        else:
            raise SclParserException("unsupported attribute type " + typeString)

AttributeType.BOOLEAN = AttributeType(0)

AttributeType.INT8 = AttributeType(1)

AttributeType.INT16 = AttributeType(2)

AttributeType.INT32 = AttributeType(3)

AttributeType.INT64 = AttributeType(4)

AttributeType.INT128 = AttributeType(5)

AttributeType.INT8U = AttributeType(6)

AttributeType.INT16U = AttributeType(7)

AttributeType.INT24U = AttributeType(8)

AttributeType.INT32U = AttributeType(9)

AttributeType.FLOAT32 = AttributeType(10)

AttributeType.FLOAT64 = AttributeType(11)

AttributeType.ENUMERATED = AttributeType(12)

AttributeType.OCTET_STRING_64 = AttributeType(13)

AttributeType.OCTET_STRING_6 = AttributeType(14)

AttributeType.OCTET_STRING_8 = AttributeType(15)

AttributeType.VISIBLE_STRING_32 = AttributeType(16)

AttributeType.VISIBLE_STRING_64 = AttributeType(17)

AttributeType.VISIBLE_STRING_65 = AttributeType(18)

AttributeType.VISIBLE_STRING_129 = AttributeType(19)

AttributeType.VISIBLE_STRING_255 = AttributeType(20)

AttributeType.UNICODE_STRING_255 = AttributeType(21)

AttributeType.TIMESTAMP = AttributeType(22)

AttributeType.QUALITY = AttributeType(23)

AttributeType.CHECK = AttributeType(24)

AttributeType.CODEDENUM = AttributeType(25)

AttributeType.GENERIC_BITSTRING = AttributeType(26)

AttributeType.CONSTRUCTED = AttributeType(27)

AttributeType.ENTRY_TIME = AttributeType(28)

AttributeType.PHYCOMADDR = AttributeType(29)

AttributeType.CURRENCY = AttributeType(30)

AttributeType.OPTFLDS = AttributeType(31)

AttributeType.TRGOPS = AttributeType(32)

