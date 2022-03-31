#!/usr/bin/env python
""" generated source for module SclParser """
from __future__ import print_function
# package: com.libiec61850.scl
# 
#  *  SclParser.java
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
class SclParser(object):
    """ generated source for class SclParser """
    ieds = None
    communication = None
    typeDeclarations = None
    withOutput = True

    def getTypeDeclarations(self):
        """ generated source for method getTypeDeclarations """
        return self.typeDeclarations

    scl = None

    @overloaded
    def __init__(self, stream, withOutput):
        """ generated source for method __init__ """
        self.withOutput = withOutput
        doc = parseXmlDocument(stream)
        self.scl = getRootNode(doc)
        if withOutput:
            print("parse data type templates ...")
        self.typeDeclarations = parseTypeDeclarations()
        if withOutput:
            print("parse IED section ...")
        parseIedSections()
        if withOutput:
            print("parse communication section ...")
        self.communication = parseCommunicationSection()
        if self.communication == None:
            if withOutput:
                print("WARNING: No communication section found!")

    @__init__.register(object, InputStream)
    def __init___0(self, stream):
        """ generated source for method __init___0 """
        self.__init__(stream, True)

    def getIedByName(self, iedName):
        """ generated source for method getIedByName """
        for ied in ieds:
            if ied.__name__ == iedName:
                return ied
        return None

    def getIeds(self):
        """ generated source for method getIeds """
        return self.ieds

    def getFirstIed(self):
        """ generated source for method getFirstIed """
        return self.ieds.get(0)

    def getCommunication(self):
        """ generated source for method getCommunication """
        return self.communication

    @classmethod
    def parseXmlWithLineNumberInformation(cls, xmlInputStream):
        """ generated source for method parseXmlWithLineNumberInformation """
        xmlDocument = None
        saxParser = None
        try:
            factory = SAXParserFactory.newInstance()
            saxParser = factory.newSAXParser()
            docBuilderFactory = DocumentBuilderFactory.newInstance()
            documentBuilder = docBuilderFactory.newDocumentBuilder()
            xmlDocument = documentBuilder.newDocument()
        except ParserConfigurationException as e:
            raise RuntimeException(e)
        elementStack = Stack()
        handler = DefaultHandler()
        saxParser.parse(xmlInputStream, handler)
        return xmlDocument

    def parseXmlDocument(self, stream):
        """ generated source for method parseXmlDocument """
        xmlDocument = None
        try:
            xmlDocument = self.parseXmlWithLineNumberInformation(stream)
        except IOError as e:
            #  TODO Auto-generated catch block
            e.printStackTrace()
        except SAXException as e:
            #  TODO Auto-generated catch block
            e.printStackTrace()
        return xmlDocument

    def parseCommunicationSection(self):
        """ generated source for method parseCommunicationSection """
        comSection = ParserUtils.getChildNodeWithTag(self.scl, "Communication")
        com = None
        if comSection != None:
            com = Communication(comSection)
        return com

    def parseIedSections(self):
        """ generated source for method parseIedSections """
        iedNodes = ParserUtils.getChildNodesWithTag(self.scl, "IED")
        self.ieds = LinkedList()
        for iedNode in iedNodes:
            self.ieds.add(IED(iedNode, self.typeDeclarations))

    def parseTypeDeclarations(self):
        """ generated source for method parseTypeDeclarations """
        typeDeclarations = TypeDeclarations()
        dataTypeTemplateSection = ParserUtils.getChildNodeWithTag(self.scl, "DataTypeTemplates")
        if dataTypeTemplateSection == None:
            raise SclParserException("No DataTypeTemplates section found in SCL file!")
        typeTemplates = dataTypeTemplateSection.getChildNodes()
        i = 0
        while i < typeTemplates.getLength():
            element = typeTemplates.item(i)
            nodeName = element.getNodeName()
            if nodeName == "LNodeType":
                typeDeclarations.addType(LogicalNodeType(element))
            elif nodeName == "DOType":
                typeDeclarations.addType(DataObjectType(element))
            elif nodeName == "DAType":
                typeDeclarations.addType(DataAttributeType(element))
            elif nodeName == "EnumType":
                typeDeclarations.addType(EnumerationType(element))
            i += 1
        return typeDeclarations

    @classmethod
    def getRootNode(cls, doc):
        """ generated source for method getRootNode """
        sclSections = doc.getElementsByTagName("SCL")
        if sclSections.getLength() != 1:
            raise SclParserException("Document contains more then one SCL section!")
        return sclSections.item(0)

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        fileName = args[0]
        stream = FileInputStream(fileName)
        sclParser = SclParser(stream)

    @overloaded
    def getConnectedAP(self, ied, accessPointName):
        """ generated source for method getConnectedAP """
        self.communication = self.getCommunication()
        if self.communication != None:
            subNetworks = self.communication.getSubNetworks()
            for subNetwork in subNetworks:
                connectedAPs = subNetwork.getConnectedAPs()
                for connectedAP in connectedAPs:
                    if connectedAP.getIedName() == ied.__name__:
                        if connectedAP.getApName() == accessPointName:
                            if self.withOutput:
                                print("Found connectedAP " + accessPointName + " for IED " + ied.__name__)
                            return connectedAP
        return None

    @getConnectedAP.register(object, str, str)
    def getConnectedAP_0(self, iedName, accessPointName):
        """ generated source for method getConnectedAP_0 """
        self.communication = self.getCommunication()
        if self.communication != None:
            subNetworks = self.communication.getSubNetworks()
            for subNetwork in subNetworks:
                connectedAPs = subNetwork.getConnectedAPs()
                for connectedAP in connectedAPs:
                    if connectedAP.getIedName() == iedName:
                        if connectedAP.getApName() == accessPointName:
                            if self.withOutput:
                                print("Found connectedAP " + accessPointName + " for IED " + iedName)
                            return connectedAP
        return None


if __name__ == '__main__':
    import sys
    SclParser.main(sys.argv)

