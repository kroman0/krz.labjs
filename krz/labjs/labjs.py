import re
from zope.interface import implements, Interface
from zope.component import adapts
from plone.transformchain.interfaces import ITransform
from krz.labjs.interfaces import IKrzLabjsLayer

def labjsreplace(matchobj):
    url = matchobj.groupdict().get('url', None)
    code = matchobj.groupdict().get('code', None)
    tp = matchobj.groupdict().get('type', None)
    if url:
        return """<script%s>$LAB.script("%s")</script>"""%(tp,url)
    elif code:
        return """<script%s>$LAB.wait(function(){%s})</script>"""%(tp,url)
    else:
        return matchobj.group()

def labjsmerge(matchobj):
    end = matchobj.groupdict().get('end', "")
    return end + ";"

SCRIPTRE = re.compile("(?P<script><script(?P<type>\s*?type=\"text/javascript\")?(?:\s*?src=\"(?P<url>.*)\")?\s*?>(?P<code>.*)</script>)",re.I)
MERGERE = re.compile("(?P<end>[^>])</script>\s*<script(?:\s*?type=\"text/javascript\")\s*?>",re.I)

LABJS = """<script type="text/javascript" src="++resource++LAB.js"></script>"""
LABJS_INIT = '<script type="text/javascript">$LAB.setOptions({AlwaysPreserveOrder:true})</script>'
SCRIPT = "<script"
LABJSSCRIPT = LABJS + LABJS_INIT + SCRIPT


class LABjs(object):
    """LABjs transformation
    """

    implements(ITransform)
    adapts(Interface, IKrzLabjsLayer)

    order = 10**4

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def transformString(self, result, encoding):
        return self.transformIterable([result], encoding)

    def transformUnicode(self, result, encoding):
        return self.transformIterable([result], encoding)

    def transformIterable(self, result, encoding):
        """Apply the transform
        """
        contentType = self.request.response.getHeader('Content-Type')
        if contentType is None or not contentType.startswith('text/html'):
            return None

        res = "\n".join(result)
        labresult = SCRIPTRE.sub(labjsreplace, res)
        labresult = labresult.replace(SCRIPT, LABJSSCRIPT, 1)
        labresult = MERGERE.sub(labjsmerge, labresult)
        return labresult
