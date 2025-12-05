from django.shortcuts import render, redirect
from .forms import GuessNumberForm

# Create your views here.

import random
from django.shortcuts import render, redirect
from .forms import GuessNumberForm

def guess_view(request):

    if "secret_number" not in request.session:
        request.session["secret_number"] = random.randint(1, 5)

    if request.method == "POST":
        form = GuessNumberForm(request.POST)
        if form.is_valid():
            guess = form.cleaned_data["number"]
            request.session["last_guess"] = guess
            return redirect("result")   
    else:
        form = GuessNumberForm()

    return render(request, "guess_form.html", {"form": form})



def result_view(request):
    secret = request.session.get("secret_number")
    guess = request.session.get("last_guess")

    if guess is None:
        return redirect("guess")  

    if guess == secret:
        message = "Correct!"
        request.session["secret_number"] = random.randint(1, 5)
    elif guess < secret:
        message = "Too low!"
    else:
        message = "Too high!"

    return render(request, "result.html", {
        "message": message,
        "guess": guess
    })
