from collections import defaultdict
from sphinx.domains import Index


class RuleSetIndex(Index):
    name = 'ruleset'
    localname = 'Ruleset Index'
    shortname = 'Ruleset'

    def generate(self, docnames=None):
        print("generating ze index")
        content = defaultdict(list)

        # Sort the list of rulesets in alphabetical order of their display
        # names, lower().
        rulesets = sorted(self.domain.get_rulesets(),
                          key=lambda rs: rs.display_name)

        # Generate the index. Use first letter of the rulesets, lower(), as key
        # to group things
        #
        # name,subtype,docname,anchor,extra,qualitifer,description
        for name, display_name, docname, anchor in rulesets:
            content[display_name[0].lower()].append(
                (display_name,
                 0,
                 docname,
                 anchor,
                 docname,
                 '', '')
            )

        content = sorted(content.items())
        return content, True
