from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


def JsonResponse(dic, format=False):
    if format:
        return HttpResponse(json.dumps(dic, indent=4, ensure_ascii=False), content_type="application/json")
    else:
        return HttpResponse(json.dumps(dic, ensure_ascii=False), content_type="application/json")


def get_labels(para):
    return ['B0', '']


def wraph(lev_list):
    return '<h%d>'%(siz) + '.'.join([str(x) for x in lev_list]) + '</h%d>\n'%(len(lev_list))


def wrapp(text):
    return '<p>' + text + '</p>\n'


def labeled2html(para, tag):
    html = ''
    id = range(len(para))
    pre = [-1]
    for i, p, t in zip(id, para, tag):
        if t[0] == 'B':
            change = int(t[1:])
            if change > 0:
                for i in range(change):
                    pre.append(1)
            elif change < 0:
                for i in range(change):
                    pre = pre[:1]
            pre[-1] += 1
            if p[0] != 0:
                html += wraph(pre, now_dep+1)
        html += wrapp(p)
    return html


def para2tag(para):
    return get_labels(para)


def text2para(text):
    return text.split('\n')


@csrf_exempt
def text2sec(request):
    text = json.loads(request.body)["text"]
    para = text2para(text)
    tag = para2tag(para)
    html = labeled2html(para, tag)
    return JsonResponse({'result': html})