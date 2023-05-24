from django.shortcuts import render
from Django_Mem.mem_emp import DaoMem
from django.views.decorators.csrf import csrf_exempt

def MemList(request):
    mylist = DaoMem().selectList()
    return render(request, 'mem_list.html', {'list':mylist})

def MemDetail(request):
    m_id = request.GET.get("m_id", '')
    mem = DaoMem().selectOne(m_id)
    return render(request, 'mem_detail.html', {'mem':mem})

def MemMod(request):
    m_id = request.GET.get("m_id", '')
    mem = DaoMem().selectOne(m_id)
    return render(request, 'mem_mod.html', {'mem':mem})

@csrf_exempt
def MemModAct(request):
    m_id = request.POST['m_id']
    m_name = request.POST['m_name']
    tel = request.POST['tel']
    address = request.POST['address']
    res = DaoMem().update(m_id, m_name, tel, address)
    return render(request, 'mem_mod_act.html', {'res':res})
        
def MemAdd(request):
    return render(request, 'mem_add.html')

@csrf_exempt
def MemAddAct(request):
    m_id = request.POST['m_id']
    m_name = request.POST['m_name']
    tel = request.POST['tel']
    address = request.POST['address']
    res = DaoMem().insert(m_id, m_name, tel, address)
    return render(request, 'mem_add_act.html', {'res':res})

@csrf_exempt
def MemDelAct(request):
    m_id = request.POST['m_id']
    res = DaoMem().delete(m_id)
    return render(request, 'mem_del_act.html', {'res':res})
