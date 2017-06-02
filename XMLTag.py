
class XMLTag:
    """Tree Struct containing XML data"""
    name = str
    attributes = dict()  # no init and {} or dict() makes this static?!
    characters = str
    # Tag Tree Hierachy
    parent = None
    children = list()  # no init and [] or list() makes this static?!
    # Tag construction: Only valid if both start and end tags are valid
    __hasStartElement = False
    __hasEndElement = False

    def __init__(self, name=None, attributes=dict, characters=None, parent=None, children=list, constructed=True):
        self.name = name
        self.attributes = attributes if attributes.__class__ == dict else {}
        self.characters = characters
        self.parent = parent
        # self.children = children or [] # another way; you can define children default to be None
        self.children = children if children.__class__ == list else []
        self.__hasStartElement = constructed
        self.__hasEndElement = constructed
    def addChild(self, child):
        """Adds a child XMLTag to the list children"""
        if not child or (child and child.__class__ != XMLTag):
            raise AttributeError("Illegal child param. Must be an XMLTag")
        self.children.append(child)
    def addAttr(self, key, value):
        """Adds an attribute to the dict attributes"""
        self.attributes[key] = value

##
# Recursive function. Traverses the Tags tree, calling startElement(), endElement() for each.
# characters() is only called when the tag contains characters in between <tag> </tag>
# Params:
#   tag     root rag to echo traverse from
#   handler XML parser handler used for startElement(), endElement(), and characters()
# Returns:
#   Nothing
##
def echoTags(tag=XMLTag, handler=object):
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