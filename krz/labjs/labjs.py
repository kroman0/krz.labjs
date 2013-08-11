import re
from Globals import DevelopmentMode as DEBUG
from os.path import join as pjoin, dirname
from zope.interface import implements, Interface
from zope.component import adapts
from plone.transformchain.interfaces import ITransform
from krz.labjs.interfaces import IKrzLabjsLayer


SCRIPTRE = re.compile(
    '(?:<script(?![^>]*?class="nolabjs"[^>]*?)'
    '(?:[^>]*?src="(?P<url>[^"]*?)")?[^>]*?>(?P<code>.*?)</script>)',
    re.I + re.S)
LABJS = pjoin(dirname(__file__), DEBUG and 'LAB-debug.min.js' or 'LAB.min.js')
LABJS = open(LABJS)
LABJS_SCRIPT = LABJS.read()
LABJS.close()
LABJS_INIT = '$LAB.setGlobalDefaults({AlwaysPreserveOrder:true%s})' % (
    DEBUG and ',Debug:true' or '')
LABJS = '<script type="text/javascript">%s%s%%s</script>' % (
    LABJS_SCRIPT, LABJS_INIT)
BEFORE = '</body>'
AFTER = '</title>'


class LABjs(object):
    """LABjs transformation
    """

    implements(ITransform)
    adapts(Interface, IKrzLabjsLayer)

    order = 10 ** 4 + 1

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
        ajax = self.request.get_header('X-Requested-With', '').startswith('XML')
        if ajax or contentType is None or not contentType.startswith('text/html'):
            return None

        res = "\n".join(result)
        scripts = SCRIPTRE.findall(res)
        labresult = SCRIPTRE.sub(lambda x: "", res)
        scripts = [
            i[0] and '.script("%s")' % i[0] or '.wait(function(){%s})' % i[1]
            for i in scripts
        ]
        js = "".join(scripts)
        js = LABJS % js
        #labresult = labresult.replace(BEFORE, js + BEFORE, 1)
        labresult = labresult.replace(AFTER, AFTER + js, 1)
        return labresult
