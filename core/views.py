from django.shortcuts import render, redirect
from .models import Product, Purchase
from .forms import ProductForm, PurchaseForm
from django.db.models import Sum, Count
from django.contrib.auth.decorators import login_required


def refresh(product_id):
    purchases_amount = Purchase.objects.filter(
        product=product_id).aggregate(Sum('amount'))
    purchases_price = Purchase.objects.filter(
        product=product_id).aggregate(Sum('price'))
    purchases_count = Purchase.objects.filter(
        product=product_id).aggregate(Count('id'))
    product = Product.objects.get(pk=product_id)
    product.amount = purchases_amount['amount__sum']
    average_price = (
        purchases_amount['amount__sum'] / purchases_price['price__sum'])
    product.average_price = average_price
    product.save()
    pass


@login_required
def product_list(request):
    context = {
        'products': Product.objects.all()
    }

    return render(request, "product_list.html", context)


@login_required
def purchase_list(request):
    context = {
        'purchases': Purchase.objects.all()
    }

    return render(request, "purchase_list.html", context)


@login_required
def product_form(request):
    if request.method == "GET":
        form = ProductForm()
        context = {
            'form': form
        }
        return render(request, "product_form.html", context)
    else:
        form = ProductForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/product/list')


@login_required
def purchase_form(request):
    if request.method == "GET":
        form = PurchaseForm()
        context = {
            'form': form
        }
        return render(request, "purchase_form.html", context)
    else:
        form = PurchaseForm(request.POST)
        if form.is_valid:
            form.save()
            refresh(request.POST['product'])
        return redirect('/purchase/list')
