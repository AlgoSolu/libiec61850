#!/usr/bin/env python
""" generated source for module DataModelValue """
from __future__ import print_function
# package: com.libiec61850.scl.model
# 
#  *  DataModelValue.java
#  *
#  *  Copyright 2013, 2015 Michael Zillgith
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
class DataModelValue(object):
    """ generated source for class DataModelValue """
    value = None
    unknownEnumValue = None
    enumType = None

    @overloaded
    def __init__(self, type_, enumType, value):
        """ generated source for method __init__ """
        self.unknownEnumValue = value
        self.enumType = enumType

    @__init__.register(object, AttributeType, SclType, str)
    def __init___0(self, type_, sclType, value):
        """ generated source for method __init___0 """
        if type_ == ENUMERATED:
            enumType = sclType
            try:
                self.value = (int(self.enumType.getOrdByEnumString(value)))
            except IllegalValueException as e:
                try:
                    self.value = Integer.parseInt(value)
                    if self.enumType.isValidOrdValue(Integer.parseInt(value)) == False:
                        raise IllegalValueException(value + " is not a valid value of type " + sclType.getId())
                    print("WARNING: Initialization of ENUM with ordinal value!")
                except NumberFormatException as nfe:
                    raise IllegalValueException(value + " is not a valid value of type " + sclType.getId())
        elif type_ == INT8:
            pass
        elif type_ == INT16:
            pass
        elif type_ == INT32:
            pass
        elif type_ == INT8U:
            pass
        elif type_ == INT16U:
            pass
        elif type_ == INT32U:
            pass
        elif type_ == INT24U:
            pass
        elif type_ == INT64:
            trimmedValue = value.trim()
            if trimmedValue != value:
                print("WARNING: value initializer contains leading or trailing whitespace")
            if trimmedValue.isEmpty():
                self.value = long(0)
            else:
                self.value = Long.parseLong(trimmedValue)
        elif type_ == BOOLEAN:
            trimmedValue = value.trim()
            if trimmedValue != value:
                print("WARNING: value initializer contains leading or trailing whitespace")
            if trimmedValue.lower() == "true":
                self.value = bool(True)
            else:
                self.value = bool(False)
        elif type_ == FLOAT32:
            trimmedValue = value.trim()
            if trimmedValue != value:
                print("WARNING: value initializer contains leading or trailing whitespace")
            trimmedValue.replace(',', '.')
            if trimmedValue.isEmpty():
                self.value = float(0)
            else:
                self.value = float(trimmedValue)
        elif type_ == FLOAT64:
            trimmedValue = value.trim()
            if trimmedValue != value:
                print("WARNING: value initializer contains leading or trailing whitespace")
            trimmedValue.replace(',', '.')
            if trimmedValue.isEmpty():
                self.value = float(0)
            else:
                self.value = float(trimmedValue)
        elif type_ == UNICODE_STRING_255:
            self.value = value
        elif type_ == OCTET_STRING_64:
            try:
                self.value = Base64.getDecoder().decode(value)
            except IllegalArgumentException as e:
                raise IllegalValueException("Val element for Octet64 type does not contain a valid base64 encoded string")
        elif type_ == VISIBLE_STRING_32:
            pass
        elif type_ == VISIBLE_STRING_64:
            pass
        elif type_ == VISIBLE_STRING_65:
            pass
        elif type_ == VISIBLE_STRING_129:
            pass
        elif type_ == VISIBLE_STRING_255:
            pass
        elif type_ == CURRENCY:
            self.value = value
        elif type_ == CHECK:
            print("Warning: Initialization of CHECK is unsupported!")
        elif type_ == CODEDENUM:
            self.value = None
            if value == "intermediate-state":
                self.value = int(0)
            elif value == "off":
                self.value = int(1)
            elif value == "on":
                self.value = int(2)
            elif value == "bad-state":
                self.value = int(4)
            elif value == "stop":
                self.value = int(0)
            elif value == "lower":
                self.value = int(1)
            elif value == "higher":
                self.value = int(2)
            elif value == "reserved":
                self.value = int(4)
            else:
                print("Warning: CODEDENUM is initialized with unsupported value " + value.__str__())
        elif type_ == QUALITY:
            self.value = None
            print("Warning: Initialization of QUALITY is unsupported!")
        elif type_ == TIMESTAMP:
            pass
        elif type_ == ENTRY_TIME:
            try:
                modValueString = value.replace(',', '.')
                parser = SimpleDateFormat("yyyy-MM-d'T'HH:mm:ss.SSS")
                parser.setTimeZone(TimeZone.getTimeZone("UTC"))
                date = parser.parse(modValueString)
                self.value = long(date.toInstant().toEpochMilli())
            except java.text.ParseException as e:
                self.value = None
                print("Warning: Val element does not contain a valid time stamp: " + e.getMessage())
        else:
            raise IllegalValueException("Unsupported type " + type_.__str__() + " value: " + value)

    def getValue(self):
        """ generated source for method getValue """
        return self.value

    def getUnknownEnumValue(self):
        """ generated source for method getUnknownEnumValue """
        return self.unknownEnumValue

    def updateEnumOrdValue(self, typeDecls):
        """ generated source for method updateEnumOrdValue """
        if self.enumType != None:
            sclType = typeDecls.lookupType(self.enumType)
            if sclType != None:
                enumType = sclType
                try:
                    self.value = (int(self.enumType.getOrdByEnumString(self.unknownEnumValue)))
                except IllegalValueException as e:
                    e.printStackTrace()
            else:
                print("  failed!")

    def getLongValue(self):
        """ generated source for method getLongValue """
        return long(self.value)

    def getIntValue(self):
        """ generated source for method getIntValue """
        if isinstance(self.value, (long, )):
            longValue = long(self.value)
            return (long(self.value)).intValue()
        if isinstance(self.value, (int, )):
            return (int(self.value)).intValue()
        if isinstance(self.value, (bool, )):
            if (bool(self.value)) == True:
                return 1
            else:
                return 0
        return 0

