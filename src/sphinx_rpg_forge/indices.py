from collections import defaultdict
from sphinx.domains import Index


class RuleSetIndex(Index):
    name = "ruleset"
    localname = "Ruleset Index"
    shortname = "Ruleset"

    def generate(self, docnames=None):
        content = defaultdict(list)

        # Sort the list of rulesets in alphabetical order of their display
        # names, lower().
        rulesets = sorted(self.domain.get_rulesets(), key=lambda rs: rs.dispname)

        # Generate the index. Use first letter of the rulesets, lower(), as key
        # to group things:
        # name,subtype,docname,anchor,extra,qualifier,description
        for rs in rulesets:
            content[rs.dispname[0].lower()].append(rs.index_entry())

        content = sorted(content.items())
        return content, True
