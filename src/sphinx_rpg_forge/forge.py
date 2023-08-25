from collections import namedtuple
from sphinx.util.nodes import make_refnode


class ForgeObject:
    typ_to_ref = {
        "RuleSet": "ruleset",
    }

    def __init__(self, name, signature, typ, docname, anchor, ruleset):
        self.name = name
        self.signature = signature
        self.typ = typ
        self.docname = docname
        self.anchor = anchor
        self.ruleset = ruleset

    def description(self):
        return (self.name, self.signature, self.typ, self.docname, self.anchor, 0)

    def make_refnode(self, builder, fromdocname, contnode):
        return make_refnode(
            builder,
            fromdocname,
            self.docname,
            self.anchor,
            contnode,
            self.docname,
        )
