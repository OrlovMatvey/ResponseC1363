import json, ast
from django.http import HttpResponse, JsonResponse
from .models import UserTasks
from django.shortcuts import render


def get_page(request):
    return render(request, "index.html")


def user_task(request):
    data = {}
    req = json.load(request)
    t = int(req["t"])
    nl = list(map(int, req["n"].strip().split(sep=" ")))
    xl = list(map(int, req["x"].strip().split(sep=" ")))
    uvl = list(req["uv"].strip().split(sep=" "))
    csrftoken = req["csrftoken"]
    res = UserTasks.objects.filter(inp=[t, nl, xl, uvl])
    print(res)
    if res:
        print(UserTasks.objects.get(inp=[t, nl, xl, uvl]).sol)
        data = ast.literal_eval(UserTasks.objects.get(inp=[t, nl, xl, uvl]).sol)
        print(type(data))
    else:
        for i in range(t):
            n, x = nl[i], xl[i]
            uv = uvl[i]
            if n > 1:
                if uv.count(f"{x}") == 1:
                    res = "Ayush"
                else:
                    if n % 2 == 0:
                        res = "Ayush"
                    else:
                        res = "Ashish"
            else:
                res = "Ayush"
            data[f"{len(data)+1}"]=res
        new_row = UserTasks(csrftoken=csrftoken, inp=[t, nl, xl, uvl], sol=data)
        new_row.save()
    return JsonResponse(data)
