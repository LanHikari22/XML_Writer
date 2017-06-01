class XMLTag:
    name = str
    attributes = dict()  # no init and {} or dict() makes this static?!
    characters = str
    # Tag Tree Hierachy
    parent = None
    children = list()  # no init and [] or list() makes this static?!
    # Tag construction: Only valid if both start and end tags are valid
    hasStartElement = False
    hasEndElement = False

    def __init__(self):
        self.name = None
        self.attributes = {}
        self.characters = None
        self.parent = None
        self.children = []
        self.hasStartElement = False
        self.hasEndElement = False

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

    rootTag = None

    def __int__(self, rootTag = XMLTag):
        pass


    ##
    # Override this. This should return the conversion of your entity model to GPXTag
    # Returns: 
    #   - root_GpxTag to write from
    ##
    def to_GPXTag(self):
        s = str
