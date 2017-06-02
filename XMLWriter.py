from AbstractXMLWriterHandler import AbstractXMLWriterHandler
from XMLTag import XMLTag
import io

##
# Parser class.
# Parses through XML files and called abstractParserHandler functions
# startElement(), endElement(), and characters() reporting the data found.
##
class XMLWriter:
    # File to be parsed
    file = None
    # AbstractXMLWriterHandler used to construct XML file
    handler = None
    # Static counter for recusrive writing of the XMLTag. this tabs things appropriately.
    _tabCount = 0
    # Character limit for when characters are written to file, before
    _CHARLIMIT = 200

    ##
    # Sets the filename to be parsed
    # Params:
    #   filename - file path to the file to be parsed
    #   handler - used to retrieve XMLTag data to be written
    # Returns:
    #   Nothing
    ##
    def __init__(self, filename=str, handler=None):
        self.file = open(str(filename), "w") if filename.__class__ == str else open("default.xml", "w")
        self.handler = handler

    ##
    # Recursive function.
    # Writes the content of a tag to specified file
    # Params:
    #   tag     tag to be written
    ##
    def _writeTag(self, tag):
        """Recursively writes a tag and all of its children to a file"""

        # write '<name' in a new TABBED line. All new tags start on a new line with proper tabbing.
        tabNL = '\n' + self._tabCount*'\t'
        self.file.write(tabNL + '<' + str(tag.name))
        # If any attributes are available, add to <name ...> in format ' key="value"'
        for attr in tag.attributes:
            self.file.write(' ' + str(attr) + '="' + str(tag.attributes[attr]) + '"')
        # Close start element with '>'
        self.file.write('>')
        # If there are any characters in tag, Write them.
        if tag.characters:
            # Can't just write the characters as is. Gotta format them. This has a defined character limit per line.
            self.file.write(self._formatCharacters(tag.characters, charLimit=self._CHARLIMIT))
        # If any children are present, perform this functionality to them, with an increased tabbing
        if tag.children:
            self._tabCount += 1
            for child in tag.children:
                self._writeTag(child)
            self._tabCount -= 1
        # The end of this tag. </name> should be added
        tabNL = '\n' + self._tabCount*'\t'
        if tag.children:
            self.file.write(tabNL)
        self.file.write('</' + str(tag.name) + '>')


    ##
    # Writes data in handler to specified file
    # Returns:
    #   Nothing
    ##
    def write(self):
        rootTag = self.handler.getData()
        self.file.write('<?xml version="1.0"?>')
        self._writeTag(rootTag)

    def _formatCharacters(self, characters, charLimit=None):
        """Formats characters nicely, with tabbed lines and a set character limit per line"""
        if not charLimit:
            charLimit = self._CHARLIMIT
        # Replace all '\n' with tabbed new line.
        tabNL = '\n' + self._tabCount*'\t'
        str(characters).replace('\n', tabNL)
        # Ensure that a tabbed new line is present every CharLimit characters.
        newChars = ''
        for i in range(len(characters)):
            if i != 0 and i % charLimit == 0:
                newChars += tabNL
            newChars += characters[i]
        return newChars
