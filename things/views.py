from django.shortcuts import render

# Create your views here.


def one(request):
    num_visits = request.session.get('visit_counter', 0)
    request.session['visit_counter'] = num_visits + 1
    items_list = request.session.get('cart', [])
    if request.method == 'POST':
        item = request.POST.get('product')
        items_list.append(item)
        return render(request, 'bunty/one.html', {'visit': num_visits, 'cart': items_list})
    return render(request, 'bunty/one.html', {'visit': num_visits, 'cart': items_list})


def two(request):
    return render(request, 'bunty/one.html', {})


def three(request):
    return render(request, 'bunty/one.html', {})
