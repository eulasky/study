from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect("articles:index")
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # auth_login(request, 로그인 인증된 유저 객체)
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect("articles:index")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # 회원가입 템플릿과 회원정보 작성을 위한 form을 응답
        form = CustomUserCreationForm()
    
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    # 유저 객체를 삭제
    # 유저를 조회해야 할까?
    # -> 탈퇴 전에 로그인이 되어 있어야 함
    # -> 게시글 삭제랑 다르게 봐야 함
    # -> 굳이 유저를 조회해야 하는가?
    # -> 로그인 된 사용자 어디에 있을까?
    # -> request, 모든 view 함수는 요청을 받는다
    # 애초에 탈퇴라는 건 로그인이 되어있는 상태로 요청을 보내기 때문
    # 그래서 요청 객체 안에 이미 어떤 사용자가 요청을 보내는 건지 정보가 들어있음
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == "POST":
        # 기존 유저 정보 (request.user)
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request, user_pk):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # 비밀번호 변경 완료한 유저가 들어가야 함 
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
        # 왜 instance = request.user 은 안 되고 request.user만 되는 거지?
    context = {
        'form':form
    }
    return render(request, 'accounts/change_password.html', context)
