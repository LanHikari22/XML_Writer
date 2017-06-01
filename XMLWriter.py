from AbstractXMLWriterHandler import AbstractXMLWriterHandler, XMLTag
import io


##
# Recursive function. Traverses the Tags tree, calling startElement(), endElement() for each.
# characters() is only called when the tag contains characters in between <tag> </tag>
# Returns:
#   Nothing
##
def echoTags(tag=XMLTag, handler=AbstractXMLWriterHandler):
    # Call startElement() and pass attributes
    handler.startElement(tag.name, tag.attributes)
    # Call characters() if possible
    if tag.characters.strip(' ') != None and not tag.characters.isspace():
        handler.characters(tag.characters.strip(' '))
    # Traverse down, if there are children
    for child in tag.children:
        echoTags(child, handler)
        # Call endElement()
        handler.endElement(tag.name)


##
# Parser class.
# Parses through XML files and called abstractParserHandler functions
# startElement(), endElement(), and characters() reporting the data found.
##
class XMLWriter:
    # File to be parsed
    _filename = None

    ##
    # Sets the filename to be parsed
    # Params:
    #   filename - file path to the file to be parsed
    # Returns:
    #   Nothing
    ##
    def __init__(self, filename=str):
        self._filename = filename

    ##
    # Parses _file and calls startElement(), endElement() and characters()
    # from a parser handler class.
    # Returns:
    #   Nothing
    ##
    def write(self):
        file = open(self._filename, "r")
        # rootTag = _handleParsing(file)
        # echoTags(rootTag,AbstractXMLParserHandler()) # Calls the appropriate startElement(), endElement() and characters() functions
        # print(rootTag)
