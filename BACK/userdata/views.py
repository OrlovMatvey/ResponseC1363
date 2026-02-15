from .models import UserInpSol
from django.http import HttpResponse
import json


def user_task(request):
    A = []
    req = json.load(request)
    t = int(req['t'])
    nl = list(req['n'].split(sep=' '))
    xl = list(req['x'].split(sep=' '))
    uvl = list(req['uv'].split(sep=' '))
    csrftoken = req['csrftoken']
    res = UserInpSol.objects.filter(inp=req).exists()
    if res:
        data = UserInpSol.objects.get(inp=req)
    else:
        for i in range(t-1):
            n, x = nl[i], xl[i]
            uv = uvl[i]
            if n > 1:
                if uv.count(f'{x}') == 1:
                    res = 'Ayush'
                else:
                    if n % 2 == 0:
                        res = 'Ayush'
                    else:
                        res = 'Ashish'
            else:
                res = 'Ayush'
            A.append(res)
        data = A
        new_row = UserInpSol(csrftoken=csrftoken, inp=req, sol=data)
        new_row.save()
    return HttpResponse(data)
