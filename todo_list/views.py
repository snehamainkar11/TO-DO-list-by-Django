from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm ,FeedbackForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
        else:
            pass
        all_items = List.objects.all
        messages.success(request, ('Item has been successfully added to the list.'))
        return render(request, 'home.html', {'todo_items': all_items})
    else: 
        all_items = List.objects.all
        return render(request, 'home.html', {'todo_items': all_items})

def contact(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Feedback Submitted.')
            return redirect('contact')
    else:
        f = FeedbackForm()
    return render(request, 'contact_us.html', {'form': f})

def delete(request, item_id):
    item = List.objects.get(pk=item_id)
    item.delete()
    messages.success(request, ('Item has been deleted permanently from the list.'))
    return redirect('home')

def cross_off(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = True
    item.save()
    messages.success(request, ('Item has been marked as completed.'))
    return redirect('home')

def uncross(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = False
    item.save()
    messages.success(request, ('Item has been marked as not completed.'))
    return redirect('home')

def edit(request, item_id):
    if request.method == 'POST':
        item = List.objects.get(pk=item_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been successfully edited.'))
            return redirect('home')
    else: 
        item = List.objects.get(pk=item_id)
        return render(request, 'edit.html', {'item': item})
