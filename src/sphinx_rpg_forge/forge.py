from collections import namedtuple


class ForgeObject:
    def __init__(self, name, dispname, typ, docname, anchor):
        self.name = name
        self.dispname = dispname
        self.typ = typ
        self.docname = docname
        self.anchor = anchor

    def description(self):
        return (self.name, self.dispname, self.typ, self.docname, self.anchor, 0)

    def index_entry(self):
        return (self.dispname, 0, self.docname, self.anchor, '', '', '')


class RuleSet(ForgeObject):

    def __init__(self, name, dispname, docname, anchor):
        ForgeObject.__init__(self, name, dispname, 'RuleSet', docname, anchor)
