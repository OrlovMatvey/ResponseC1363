import json
from django.http import HttpResponse
from .models import UserInpSol


def user_task(request):
    data = []
    req = json.load(request)
    t = int(req['t'])
    nl = list(map(int, req['n'].split(sep=' ')))
    xl = list(map(int, req['x'].split(sep=' ')))
    uvl = list(req['uv'].split(sep=' '))
    csrftoken = req['csrftoken']
    res = UserInpSol.objects.filter(inp=req).exists()
    if res:
        data = UserInpSol.objects.get(inp=[t, nl, xl, uvl])
    else:
        for i in range(t):
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
            data.append(res)
        new_row = UserInpSol(csrftoken=csrftoken, inp=[t, nl, xl, uvl], sol=data)
        new_row.save()
    return HttpResponse(data)
