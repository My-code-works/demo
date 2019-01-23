from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


def JsonResponse(dic, format=False):
    if format:
        return HttpResponse(json.dumps(dic, indent=4, ensure_ascii=False), content_type="application/json")
    else:
        return HttpResponse(json.dumps(dic, ensure_ascii=False), content_type="application/json")


@csrf_exempt
def text2sec(request):
    text = json.loads(request.body)["text"]
    html = "<h1>" + text + "</h1>\n"
    html += 'hello'
    return JsonResponse({'result': html})