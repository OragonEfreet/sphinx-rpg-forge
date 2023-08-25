from collections import defaultdict
from sphinx.domains import Index

class ForgeIndex(Index):
    name = "forge"
    localname = "Forge Index"
    shortname = "Forge"

    def generate(self, docnames=None):
        content = defaultdict(list)

        # Sort the list of rulesets in alphabetical order of their signature
        # names, lower().
        rulesets = sorted(self.domain.data["objects"], key=lambda rs: rs.signature)

        # Generate the index. Use first letter of the rulesets, lower(), as key
        # to group things:
        # name,subtype,docname,anchor,extra,qualifier,description
        for rs in rulesets:
            content[rs.signature[0].lower()].append((
                rs.signature, 0, rs.docname, rs.anchor, rs.typ, None, ""
            ))

        content = sorted(content.items())
        return content, True
