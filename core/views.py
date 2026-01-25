from django.shortcuts import render, redirect
from .models import BoardSettings, ParentMessage
from .forms import ParentMessageForm


def board_view(request):
    settings = BoardSettings.objects.first()

    # 👇 غيرنا الاسم هنا
    parent_messages = ParentMessage.objects.filter(is_active=True)

    form = ParentMessageForm()

    if request.method == "POST":
        form = ParentMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.is_active = True
            message.save()
            return redirect("board")

    return render(request, "core/board.html", {
        "settings": settings,
        "parent_messages": parent_messages,  # 👈 وهنا
        "form": form,
    })
