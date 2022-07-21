from django.shortcuts import redirect, render
from django.urls import is_valid_path
from django.views import View
from . import forms
from .models import User, Game
from django.contrib.auth import authenticate, login, logout

class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        context = {
            "form" : form
        }
        return render(request, "cardgame/login.html", context)

    def post(self, request):
        form = forms.LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username = username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("cardgame:main")

        context = {
            "form" : form
        }
        return render(request, "cardgame/login.html", context)
# Create your views here.
def main (request):
    return render(request, "cardgame/main.html")

def sign_up(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("cardgame:main")

        return redirect("cardgame:sign_up")

    else:
        form = forms.SignupForm()
        context = {
            "form" : form
        }
        return render(request, "cardgame/sign_up.html", context)

def log_out(request):
    logout(request)
    return redirect("cardgame:main")

def defend(request, pk):
    game = Game.objects.get(pk = pk) 
    
    if request.method == "POST":
        form = forms.DefendForm(request.POST, instance=game)
        
        if form.is_valid():
            if game.attack_card == game.defend_card : #공격카드와 방어카드가 같은 수라면
                game.tie_flag = 1 #무승부 표시
            else :
                if game.game_mode == 'big_num' : #큰 수가 이기는 게임이라면
                    #공격 카드가 큰 수이면 공격자가 이기고, 아니면 방어자가 이긴다
                    game.victory_user = game.attacker if game.attack_card > game.defend_card else game.defender
                else : #작은 수가 이기는 게임이라면
                    #공격 카드가 작은 수이면 공격자가 이기고, 아니면 방어자가 이긴다
                    game.victory_user = game.attacker if game.attack_card < game.defend_card else game.defender
            form.save()
            return redirect('/')
        else :
            return redirect('/')
    else :
        form = forms.DefendForm()
        context = {
            'form' : form,
            'game' : game
        }
        return render(request, 'cardgame/defend.html', context=context)