#!/usr/bin/env python
""" generated source for module ModelViewer """
from __future__ import print_function
# package: com.libiec61850.tools
class ModelViewer(object):
    """ generated source for class ModelViewer """
    @classmethod
    def showTypes(cls, stream, icdFile, output, iedName, accessPointName, unusedOnly):
        """ generated source for method showTypes """
        sclParser = SclParser(stream, False)
        typeDecl = sclParser.getTypeDeclarations()
        for type_ in typeDecl.getTypeDeclarations():
            if unusedOnly:
                if type_.isUsed() == True:
                    continue 
            output.print_(type_.getId())
            if type_.__class__ == LogicalNodeType.__class__:
                output.print_(" : LogicalNode")
            elif type_.__class__ == DataObjectType.__class__:
                output.print_(" : DataObject")
            elif type_.__class__ == DataAttributeType.__class__:
                output.print_(" : DataAttribute")
            elif type_.__class__ == EnumerationType.__class__:
                output.print_(" : Enumeration")
            if not unusedOnly:
                if type_.isUsed() == False:
                    print("  UNUSED TYPE!", end="")
            output.println()

    @classmethod
    def printSubAttributes(cls, attribute, output, indent, add):
        """ generated source for method printSubAttributes """
        if attribute.getSubDataAttributes() != None:
            for attr in attribute.getSubDataAttributes():
                output.println(indent + add + attr.__name__)
                cls.printSubAttributes(attr, output, indent + add, add)

    @classmethod
    def printDataObjects(cls, dataObjects, output, indent, add):
        """ generated source for method printDataObjects """
        for dObject in dataObjects:
            output.println(indent + dObject.__name__)
            cls.printDataObjects(dObject.getSubDataObjects(), output, indent + add, add)
            for dAttribute in dObject.getDataAttributes():
                output.println(indent + add + dAttribute.__name__ + " [" + dAttribute.getFc().__str__() + "]")
                cls.printSubAttributes(dAttribute, output, indent + add, add)

    @classmethod
    def printModelStructure(cls, stream, icdFile, output, iedName, accessPointName):
        """ generated source for method printModelStructure """
        sclParser = SclParser(stream, False)
        ied = None
        if iedName == None:
            ied = sclParser.getFirstIed()
        else:
            ied = sclParser.getIedByName(iedName)
        ap = ied.getFirstAccessPoint()
        server = ap.getServer()
        devices = server.getLogicalDevices()
        for device in devices:
            output.println(device.getInst())
            lNodes = device.getLogicalNodes()
            for lNode in lNodes:
                output.println("  " + lNode.__name__)
                cls.printDataObjects(lNode.getDataObjects(), output, "    ", "  ")

    @classmethod
    def printSubAttributeList(cls, attribute, output, prefix):
        """ generated source for method printSubAttributeList """
        if attribute.getSubDataAttributes() != None:
            for attr in attribute.getSubDataAttributes():
                nextPrefix = prefix + "." + attr.__name__
                output.println(nextPrefix + " [" + attr.getFc() + "]")
                cls.printSubAttributeList(attr, output, nextPrefix)

    @classmethod
    def printObjectList(cls, dataObjects, output, prefix):
        """ generated source for method printObjectList """
        for dataObject in dataObjects:
            dOPrefix = prefix + "." + dataObject.__name__
            cls.printObjectList(dataObject.getSubDataObjects(), output, dOPrefix)
            for dAttribute in dataObject.getDataAttributes():
                daPrefix = dOPrefix + "." + dAttribute.__name__
                output.println(daPrefix + " [" + dAttribute.getFc().__str__() + "]")
                cls.printSubAttributeList(dAttribute, output, daPrefix)

    @classmethod
    def printAttributeList(cls, stream, icdFile, output, iedName, accessPointName):
        """ generated source for method printAttributeList """
        sclParser = SclParser(stream, False)
        ied = None
        if iedName == None:
            ied = sclParser.getFirstIed()
        else:
            ied = sclParser.getIedByName(iedName)
        ap = ied.getFirstAccessPoint()
        server = ap.getServer()
        devices = server.getLogicalDevices()
        for device in devices:
            devPrefix = ied.__name__ + device.getInst() + "/"
            lNodes = device.getLogicalNodes()
            for lNode in lNodes:
                lNodePrefix = devPrefix + lNode.__name__
                cls.printObjectList(lNode.getDataObjects(), output, lNodePrefix)
                #                 for (DataObject dObject : lNode.getDataObjects()) {
                #                     
                #                     String dOPrefix = lNodePrefix + "." + dObject.__name__;
                #                     
                #                     for (DataAttribute dAttribute : dObject.getDataAttributes()) {
                #                         
                #                         String daPrefix = dOPrefix + "." + dAttribute.__name__;
                #                         
                #                         output.println(daPrefix  + " [" + dAttribute.getFc().__str__() + "]");
                #                         
                #                         printSubAttributeList(dAttribute, output, daPrefix);
                #                     }
                #                     
                #                 }

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        if len(args):
            print("SCL model viewer")
            print("Usage: scltool <SCL file> [-ied <ied-name>] [-ap <access-point-name>] [-t] [-s] [-a] [<output filename>]")
            print("  -ied select IED")
            print("  -ap select AP")
            print("  -t print type list")
            print("  -u print list of unused types")
            print("  -s print IED device model structure")
            print("  -a print list of data attributes (object references)")
            System.exit(1)
        icdFile = args[0]
        outputStream = System.out
        accessPointName = None
        iedName = None
        printTypeList = False
        printUnusedTypes = False
        printModelStructure = False
        printDataAttribtues = False
        if len(args):
            i = 1
            while len(args):
                if args[i] == "-ap":
                    accessPointName = args[i + 1]
                    print("Select access point " + accessPointName)
                    i += 1
                elif args[i] == "-ied":
                    iedName = args[i + 1]
                    print("Select IED " + iedName)
                    i += 1
                elif args[i] == "-t":
                    printTypeList = True
                    i += 1
                elif args[i] == "-s":
                    printModelStructure = True
                    i += 1
                elif args[i] == "-a":
                    printDataAttribtues = True
                    i += 1
                elif args[i] == "-u":
                    printUnusedTypes = True
                    i += 1
                else:
                    outputStream = PrintStream(FileOutputStream(File(args[i])))
                i += 1
        stream = FileInputStream(icdFile)
        try:
            if printTypeList:
                cls.showTypes(stream, icdFile, outputStream, iedName, accessPointName, False)
            if printUnusedTypes:
                cls.showTypes(stream, icdFile, outputStream, iedName, accessPointName, True)
            if printModelStructure:
                printModelStructure(stream, icdFile, outputStream, iedName, accessPointName)
            if printDataAttribtues:
                cls.printAttributeList(stream, icdFile, outputStream, iedName, accessPointName)
        except SclParserException as e:
            System.err.println("ERROR: " + e.getMessage())


if __name__ == '__main__':
    import sys
    ModelViewer.main(sys.argv)

