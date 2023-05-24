from django.shortcuts import render
from django.http import JsonResponse
from flask import json
from django.views.decorators.csrf import csrf_exempt
from Django_MVVM.dao_emp import DaoEmp

def go(request):
    return render(request, 'index.html')

@csrf_exempt
def ajax(request):
    #menu = request.GET.get("menu", '')
    menu = json.loads(request.body)
    context = {
        'result': menu['menu']
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_list(request):
    mylist = DaoEmp().selectList()
    context = {
        'list':mylist
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_detail(request):
    e_id = request.POST['e_id']
    #id = json.loads(request.body)
    emp = DaoEmp().selectOne(e_id)
    context = {
        'emp' : emp
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_update(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    sex = request.POST['sex']
    addr = request.POST['addr']
    res = DaoEmp().update(e_id, e_name, sex, addr)
    context = {
        'res':res
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_insert(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    sex = request.POST['sex']
    addr = request.POST['addr']
    res = DaoEmp().insert(e_id, e_name, sex, addr)
    context = {
        'res':res
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_del(request):
    e_id = request.POST['e_id']
    res = DaoEmp().delete(e_id)
    context = {
        'res':res
    }
    return JsonResponse(context)
