from django.shortcuts import render
from .models import Message
from .forms import AddMessageForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import get_object_or_404
# Create your views here.


def message_list(request):
    msgs = Message.objects.all()
    return render(request, "message_list.html", {'msgs': msgs})


def message_add(request):
    form = AddMessageForm()
    if request.method == 'GET':
        return render(request, "add_message.html", {'form': form})
    if request.method == 'POST':
        form = AddMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('message:message_list'))
        else:
            return render(request, "add_map.html", { 'form': form})


def message_delete(request,msgid):
    get_object_or_404(Message,id=msgid).delete()
    return HttpResponseRedirect(reverse('message:message_list'))


def message_edit(request,msgid):
    msg = get_object_or_404(Message, id=msgid)
    if request.method == 'GET':

        data = {"text": msg.text, "r": msg.r, "g": msg.g, "b": msg.b, "font": msg.font,
                "effect": msg.effect, "x": msg.x, "y": msg.y, "showtime": msg.showtime,"brightness":msg.brightness}

        form = AddMessageForm(initial=data)
        return render(request, 'message_edit.html', {"form": form,'msg':msg})
    else:
        form = AddMessageForm(request.POST or None, instance=msg)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('message:message_list'))
        else:
            return render(request, 'message_edit.html', {"form": form,'msg':msg})


def select_map(request):
    pass
