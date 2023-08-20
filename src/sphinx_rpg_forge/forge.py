from collections import namedtuple
from sphinx.util.nodes import make_refnode

class ForgeObject:

    typ_to_ref = {
        'RuleSet': 'ruleset',
    }



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

    def make_refnode(self, builder, fromdocname, contnode):
        return make_refnode(builder, fromdocname, self.docname, self.anchor, contnode, self.docname)

    def reftype(self):
        return ForgeObject.typ_to_ref.get(self.typ, 'ref')

