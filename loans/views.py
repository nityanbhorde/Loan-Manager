from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from loans.form import LoanForm
from loans.models import Loan

def index(request):
	loans = Loan.objects.exclude(money=0)
	return render(request, 'loans/index.html', {
		'loans': loans,
	})

def loan_detail(request,id):
    try:
        loan = Loan.objects.get(id = id)
    except Loan.DoesNotExist:
        raise Http404('There is no loan')
    if request.method == 'GET':
        form = LoanForm()
        return render(request,'loans/loan_detail.html',{
        'form' : form, 'loan' : loan,
          })
    elif request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            loan.money = text
            loan.save()
            args = {'form' : form, 'text' : text, 'loan' : loan}
            return render(request,'loans/loan_detail.html',args)
def post(request):
    f
# Create your views here.
