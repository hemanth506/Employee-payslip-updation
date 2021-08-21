from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import *


def home(req):
    if req.method == 'POST':
        # print(req.POST)
        basic_pay = req.POST['basic_pay']
        taxes = SetTaxes.objects.latest('taxPercent')
        print(taxes.taxPercent)
        orginal_tax = int(basic_pay) * taxes.taxPercent/100
        print(orginal_tax)
        duplicate_post = req.POST.copy()
        duplicate_post.update({'Taxes' : orginal_tax}) 

        form = PayForm(duplicate_post)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PayForm()
    return render(req, 'home.html', {'form': form})

def update(req,id):
    obj = get_object_or_404(Payslip, id=id)
    
    if req.method == 'POST':
        basic_pay = req.POST['basic_pay']
        taxes = SetTaxes.objects.latest('taxPercent')
        # print(taxes.taxPercent)
        orginal_tax = int(basic_pay) * taxes.taxPercent/100
        # print(orginal_tax)
        duplicate_post = req.POST.copy()
        duplicate_post.update({'Taxes' : orginal_tax}) 

        form = PayForm(duplicate_post, instance=obj)
        form_values = {}
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form_values = {
            'name' : obj.name,
            'address' : obj.address,
            'pan' : obj.pan,
            'uan': obj.uan,
            'basic_pay': obj.basic_pay,
            'benefites' : obj.benefites
        }
        form = PayForm(initial=form_values)
    return render(req, 'update.html', {'form': form})


def lessThan(req):
    filter_query = Payslip.objects.filter(Taxes__lte = 10000)
    datalessthan = []
    for i in filter_query:
        datalessthan.append(str(i.name) + ": " + str(i.Taxes))
    return render(req, 'comparing.html', {"compare": datalessthan, "text": "Lesser Than 10K"})

def greatThan(req):
    filter_query = Payslip.objects.filter(Taxes__gte = 10000)
    datagreatthan = []
    for i in filter_query:
        datagreatthan.append(str(i.name) + ": " + str(i.Taxes))
    return render(req, 'comparing.html', {"compare": datagreatthan,"text": "Greater Than 10K"})

def updateTax(req):
    obj = get_object_or_404(SetTaxes, id=1)
    if req.method == 'POST':
        form = TaxForm(req.POST, instance=obj)
        print(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/change_user_tax')
    else:
        form = TaxForm()
    return render(req, 'update_tax.html', {'form': form})


def changeUserTax(req):
    #query = Payslip.objects.values_list({'name', 'Taxes'})

    if req.method == 'GET':
        query = Payslip.objects.values('name', 'Taxes')
        print(query)
        dummy = []

        for i in query:
            dummy.append(i)

        # print(dummy)
    elif req.method == 'POST':
        taxes = SetTaxes.objects.latest('taxPercent')
        # print(taxes.taxPercent)

        after_up = Payslip.objects.all()
        # print(after_up)
        for i in after_up:
            new_tax = i.basic_pay * taxes.taxPercent/100
            i.Taxes = new_tax
            i.save()

        query = Payslip.objects.values('name', 'Taxes')
        dummy = []
        for i in query:
            dummy.append(i)
        
    content = {'data' : dummy}
    return render(req,'update_user_tax.html', content)
