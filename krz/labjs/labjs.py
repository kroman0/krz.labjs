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
        return """<script%s>$LAB.wait("%s")</script>"""%(tp,url)
    else:
        matchobj.group()

SCRIPTRE = re.compile("(?P<script><script(?P<type>\s*?type=\"text/javascript\")?(?:\s*?src=\"(?P<url>.*)\")?\s*?>(?P<code>.*)</script>)",re.I)
MERGERE = re.compile("</script>\s*<script(?:\s*?type=\"text/javascript\")\s*?>",re.I)

LABJS_INIT = '<script type="text/javascript">$LAB.setOptions({AlwaysPreserveOrder:true})</script>'
LABJS = """<script type="text/javascript">(function(ak){var aj="string",ac="head",s="body",o="script",ag="readyState",am="preloaddone",aa="loadtrigger",n="srcuri",I="preload",a="complete",X="done",W="which",m="preserve",D="onreadystatechange",aA="onload",l="hasOwnProperty",az="script/cache",g="[object ",af=g+"Function]",ae=g+"Array]",au=null,ap=true,an=false,al=ak.document,ay=ak.location,ax=ak.ActiveXObject,K=ak.setTimeout,aw=ak.clearTimeout,f=function(e){return al.getElementsByTagName(e)},d=Object.prototype.toString,C=function(){},ai={},c={},av=/^[^?#]*\//.exec(ay.href)[0],at=/^\w+\:\/\/\/?[^\/]+/.exec(av)[0],ab=f(o),ar=ak.opera&&d.call(ak.opera)==g+"Opera]",aq=("MozAppearance" in al.documentElement.style),ao=(al.createElement(o).async===true),ad={cache:!(aq||ar),order:aq||ar||ao,xhr:ap,dupe:ap,base:"",which:ac};ad[m]=an;ad[I]=ap;ai[ac]=al.head||f(ac);ai[s]=f(s);function J(e){return d.call(e)===af}function b(h,e){var j=/^\w+\:\/\//,i;if(typeof h!=aj){h=""}if(typeof e!=aj){e=""}i=((/^\/\//.test(h))?ay.protocol:"
")+h;i=(j.test(i)?"":e)+i;return((j.test(i)?"":(i.charAt(0)==="/"?at:av))+i)}function Y(e){return(b(e).indexOf(at)===0)}function V(h){var e,i=-1;while(e=ab[++i]){if(typeof e.src==aj&&h===b(e.src)&&e.type!==az){return ap}}return an}function t(x,E){x=!(!x);if(E==au){E=ad}var j=an,A=x&&E[I],i=A&&E.cache,w=A&&E.order,h=A&&E.xhr,R=E[m],P=E.which,N=E.base,e=C,v=an,z,y=ap,B={},u=[],r=au;A=i||h||w;function T(Z,U){if((Z[ag]&&Z[ag]!==a&&Z[ag]!=="loaded")||U[X]){return an}Z[aA]=Z[D]=au;return ap}function q(Z,U,aC){aC=!(!aC);if(!aC&&!(T(Z,U))){return}U[X]=ap;for(var aB in B){if(B[l](aB)&&!(B[aB][X])){return}}j=ap;e()}function S(U){if(J(U[aa])){U[aa]();U[aa]=au}}function L(Z,U){if(!T(Z,U)){return}U[am]=ap;K(function(){ai[U[W]].removeChild(Z);S(U)},0)}function G(Z,U){if(Z[ag]===4){Z[D]=C;U[am]=ap;K(function(){S(U)},0)}}function p(U,aF,aD,Z,aB,aE){var aC=U[W];K(function(){if("item" in ai[aC]){if(!ai[aC][0]){K(arguments.callee,25);return}ai[aC]=ai[aC][0]}var aG=al.createElement(o);if(typeof aD==aj){aG.type=aD}if(typeof 
Z==aj){aG.charset=Z}if(J(aB)){aG[aA]=aG[D]=function(){aB(aG,U)};aG.src=aF;if(ao){aG.async=an}}ai[aC].insertBefore(aG,(aC===ac?ai[aC].firstChild:au));if(typeof aE==aj){aG.text=aE;q(aG,U,ap)}},0)}function Q(Z,U,aC,aB){c[Z[n]]=ap;p(Z,U,aC,aB,q)}function O(Z,U,aD,aC){var aB=arguments;if(y&&Z[am]==au){Z[am]=an;p(Z,U,az,aC,L)}else{if(!y&&Z[am]!=au&&!Z[am]){Z[aa]=function(){O.apply(au,aB)}}else{if(!y){Q.apply(au,aB)}}}}function M(Z,U,aE,aD){var aB=arguments,aC;if(y&&Z[am]==au){Z[am]=an;aC=Z.xhr=(ax?new ax("Microsoft.XMLHTTP"):new ak.XMLHttpRequest());aC[D]=function(){G(aC,Z)};aC.open("GET",U);aC.send("")}else{if(!y&&Z[am]!=au&&!Z[am]){Z[aa]=function(){M.apply(au,aB)}}else{if(!y){c[Z[n]]=ap;p(Z,U,aE,aD,au,Z.xhr.responseText);Z.xhr=au}}}}function H(Z){if(typeof Z=="undefined"||!Z){return}if(Z.allowDup==au){Z.allowDup=E.dupe}var U=Z.src,aG=Z.type,aE=Z.charset,aB=Z.allowDup,aC=b(U,N),aF,aD=Y(aC);if(typeof aE!=aj){aE=au}aB=!(!aB);if(!aB&&((c[aC]!=au)||(y&&B[aC])||V(aC))){if(B[aC]!=au&&B[aC][am]&&!B[aC][X]&&aD){q(au,B[aC]
,ap)}return}if(B[aC]==au){B[aC]={}}aF=B[aC];if(aF[W]==au){aF[W]=P}aF[X]=an;aF[n]=aC;v=ap;if(!w&&h&&aD){M(aF,aC,aG,aE)}else{if(!w&&i){O(aF,aC,aG,aE)}else{Q(aF,aC,aG,aE)}}}function k(U){if(x&&!w){u.push(U)}if(!x||A){U()}}function F(Z){var U=[],aB;for(aB=-1;++aB<Z.length;){if(d.call(Z[aB])===ae){U=U.concat(F(Z[aB]))}else{U[U.length]=Z[aB]}}return U}z={script:function(){aw(r);var Z=F(arguments),U=z,aB;if(R){for(aB=-1;++aB<Z.length;){if(J(Z[aB])){Z[aB]=Z[aB]()}if(aB===0){k(function(){H((typeof Z[0]==aj)?{src:Z[0]}:Z[0])})}else{U=U.script(Z[aB])}U=U.wait()}}else{for(aB=-1;++aB<Z.length;){if(J(Z[aB])){Z[aB]=Z[aB]()}}k(function(){for(aB=-1;++aB<Z.length;){H((typeof Z[aB]==aj)?{src:Z[aB]}:Z[aB])}})}r=K(function(){y=an},5);return U},wait:function(Z){aw(r);y=an;if(!J(Z)){Z=C}var U=t(x||v,E),aD=U.trigger,aC=function(){try{Z()}catch(aE){}aD()};delete U.trigger;var aB=function(){if(v&&!j){e=aC}else{aC()}};if(x&&!v){u.push(aB)}else{k(aB)}return U}};if(x){z.trigger=function(){var Z,U=-1;while(Z=u[++U]){Z()}u=[]}}else{z.
trigger=C}return z}function ah(h){var e,k={},j={UseCachePreload:"cache",UseLocalXHR:"xhr",UsePreloading:I,AlwaysPreserveOrder:m,AllowDuplicates:"dupe"},i={AppendTo:W,BasePath:"base"};for(e in j){i[e]=j[e]}k.order=!(!ad.order);for(e in i){if(i[l](e)&&ad[i[e]]!=au){k[i[e]]=(h[e]!=au)?h[e]:ad[i[e]]}}for(e in j){if(j[l](e)){k[j[e]]=!(!k[j[e]])}}if(!k[I]){k.cache=k.order=k.xhr=an}k.which=(k.which===ac||k.which===s)?k.which:ac;return k}ak.$LAB={setGlobalDefaults:function(e){ad=ah(e)},setOptions:function(e){return t(an,ah(e))},script:function(){return t().script.apply(au,arguments)},wait:function(){return t().wait.apply(au,arguments)}};(function(h,e,i){if(al[ag]==au&&al[h]){al[ag]="loading";al[h](e,i=function(){al.removeEventListener(e,i,an);al[ag]=a},an)}})("addEventListener","DOMContentLoaded")})(window);</script>"""
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
        labresult = MERGERE.sub(lambda x:";", labresult)
        return labresult
