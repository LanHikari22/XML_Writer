import os
import sys
from AbstractXMLWriterHandler import AbstractXMLWriterHandler
from XMLTag import XMLTag
from XMLWriter import XMLWriter


if __name__ == '__main__':
    # Building a structure.
    root = XMLTag(name="Pointers",attributes={'Author': 'Lan', 'Game':'MMBN6 Falzar'},parent=None)
    root.addChild(XMLTag("BattleStruct",{"Address":hex(0xDEADBEEF)},"Battle structure pointers",root))
    root.children[0].addChild(XMLTag("Virus1",{"Offset":hex(0x00)},None,root.children[0]))
    root.children[0].addChild(XMLTag("Virus2",{"Offset":hex(0x30)},None,root.children[0]))
    root.children[0].addChild(XMLTag("Virus3",{"Offset":hex(0x60)},None,root.children[0]))
    root.children[0].addChild(XMLTag("Megaman",{"Offset":hex(0x90)},None,root.children[0]))
    root.addChild(XMLTag("ChipStruct",{"Address":hex(0x0FEEDBAE)},"Chip structure pointers",root))
    root.children[1].addChild(XMLTag("Cannon",{"Offset":hex(0x00)},None,root.children[1]))
    root.children[1].addChild(XMLTag("RollM",{"Offset":hex(0x60)},None,root.children[1]))
    root.children[1].addChild(XMLTag("Invis",{"Offset":hex(0xC0)},None,root.children[1]))
    # Constructing to pointers.xml
    handler = AbstractXMLWriterHandler(root)
    writer = XMLWriter("pointers.xml",handler)
    writer.write()