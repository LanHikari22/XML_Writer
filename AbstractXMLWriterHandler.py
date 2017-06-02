from XMLTag import XMLTag

##
# Can be disabled within function, or overridden. prints to stdout when enabled
# Params:
#   - newLine: determines whether to print a new line or not
# Returns:
#   Nothing
##
def log(s, newLine = bool):
    logEnabled = True
    if logEnabled and newLine:
        print(s)
    elif logEnabled and not newLine:
        print(s, end='')

##
# ParserHandler class.
# This handles what happens when the startElement(), endElement() and characters() functions are called.
# extend this and override its functions for a specialized use of the XML parser.
##
class AbstractXMLWriterHandler:

    _rootTag = None

    ##
    # Perform object initiation logic here, or provide a mechanism of doing so
    ##
    def __init__(self, rootTag = None):
        self._rootTag = rootTag if rootTag.__class__ == XMLTag else None
        pass


    ##
    # Don't Override this. This should return the conversion of your entity model to GPXTag
    # Construct the rootTag object that represents your data during initiation of the handler.
    # Returns:
    #   - root_GpxTag to write from
    ##
    def getData(self):
        return self._rootTag
