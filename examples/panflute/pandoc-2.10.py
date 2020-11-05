"""
Pandoc filter using panflute
"""

import panflute as pf


def prepare(doc):
    pass


def action(elem, doc):
    if isinstance(elem, pf.Element) and doc.format == 'latex':
        pass
        # return None -> element unchanged
        # return [] -> delete element


def strong2underline(elem, doc):
	if isinstance(elem, pf.Strong):
		return pf.Underline(*elem.content)


def finalize(doc):
    pass


def main(doc=None):
    return pf.run_filters([action, strong2underline],
                         prepare=prepare,
                         finalize=finalize,
                         doc=doc) 


if __name__ == '__main__':
    main()
