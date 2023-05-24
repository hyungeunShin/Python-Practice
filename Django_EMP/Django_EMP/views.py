from django.shortcuts import render
from Django_EMP.dao_emp import DaoEmp
from django.views.decorators.csrf import csrf_exempt

def empList(request):
    mylist = DaoEmp().selectList()
    return render(request, 'emp_list.html', {'list':mylist})

def empDetail(request):
    e_id = request.GET.get("e_id", '')
    emp = DaoEmp().selectOne(e_id)
    return render(request, 'emp_detail.html', {'emp':emp})

def empMod(request):
    e_id = request.GET.get("e_id", '')
    emp = DaoEmp().selectOne(e_id)
    return render(request, 'emp_mod.html', {'emp':emp})

@csrf_exempt
def empModAct(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    sex = request.POST['sex']
    addr = request.POST['addr']
    res = DaoEmp().update(e_id, e_name, sex, addr)
    return render(request, 'emp_mod_act.html', {'res':res})
        
def empAdd(request):
    return render(request, 'emp_add.html')

@csrf_exempt 
def empAddAct(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    sex = request.POST['sex']
    addr = request.POST['addr']
    res = DaoEmp().insert(e_id, e_name, sex, addr)
    return render(request, 'emp_add_act.html', {'res':res})

@csrf_exempt
def empDelAct(request):
    e_id = request.POST['e_id']
    res = DaoEmp().delete(e_id)
    return render(request, 'emp_del_act.html', {'res':res})
