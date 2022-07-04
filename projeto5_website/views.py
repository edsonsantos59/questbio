from django.shortcuts import render
from projeto5_website.models import Aluno, CHOICES_ALTERNATIVA, Alternativa, Pergunta, Resultado
from datetime import datetime
from django.http import HttpResponseRedirect
from projeto5_website.forms import PerguntaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home(request):
  return render(request, "projeto5_website/home.html")

@login_required(login_url='/login/')
def pergunta_form(request):
  if request.method == "POST":
    form = PerguntaForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  else:
    form = PerguntaForm()
  return render(request, "projeto5_website/pergunta_form.html",
  {"perguntas": Pergunta.objects.all(),
  "alternativas": Alternativa.objects.filter(pergunta=1)})

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
          if user.is_active:
            if user.is_staff == True:
              login(request, user)
              return HttpResponseRedirect('/resultado/admin/c5052cf355e48dc43b7a21bfc38e2dd1/')
            else:
                login(request, user)
                return HttpResponseRedirect('/test/' + username)
    return render(request, 'projeto5_website/login.html')

@login_required(login_url='/login/')
def obrigado(request, id, cpf, instituicao):
    return render(request, "projeto5_website/obrigado.html",
            {"resultados": Resultado.objects.filter(aluno = id),
              "navbar_resultados" : "active"})

@login_required(login_url='/login/')
def resultado(request):
  username = password = ''
  if request.POST:
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
          if user.is_active:
            if user.is_staff == False:
                return render(request, 'projeto5_website/login.html')
  if request.method == 'POST':
        busca = request.POST['buscaAluno']
        if not busca:
            alunos = Aluno.objects.all()
            return render(request, "projeto5_website/resultado.html",
                          {"resultados": Resultado.objects.all(),
                           "navbar_resultados": "active"})
        else:
            alunos = Aluno.objects.all()
            return render(request, "projeto5_website/resultado.html",
                          {"resultados": Resultado.objects.all(),
                           "navbar_resultados": "active"})
  else:
      alunos = Aluno.objects.all()

  return render(request, "projeto5_website/resultado.html",
                {"resultados": Resultado.objects.all(),
                  "navbar_resultados" : "active"})

@login_required(login_url='/login/')
def test(request, teste):
  try:
    #TODO:
    perguntas_dict = {}
    username = request.POST.get('username', True);
    if username in request.POST:
        return render(request, "projeto5_website/login.html")
    if request.method == "GET":
        for pergunta in Pergunta.objects.filter():
            perguntas_dict[pergunta.enunciado] = Alternativa.objects.filter(pergunta=pergunta)
        return render(request, "projeto5_website/test.html",
                      {"perguntas": perguntas_dict, "navbar_teste" : "active"})
    elif request.method == "POST":
        if len(request.POST) > 0:
            totalRespostas = 0
            respostas_dict = {
                "1" : 0,
                "2" : 0,
                "3" : 0,
                "4" : 0,
            }

            def save(self, *args, **kwargs):
              maior = self.dominancia
              self.resultado_final = 'dominancia'
              if self.cautela > maior:
                maior = self.cautela
                self.resultado_final = 'cautela'
              if self.influencia > maior:
                maior = self.influencia
                self.resultado_final = 'influencia'
              if self.estabilidade > maior:
                maior = self.estabilidade
                self.resultado_final = 'estabilidade'
              super(test, self.maior).save(*args, **kwargs)
            print(request.POST)
            ra = request.POST["ra"]
            email = request.POST["email"]
            nome = request.POST["nome"]

            for chave, conteudo in request.POST.items():
                if chave not in ["csrfmiddlewaretoken", 'ra', 'email', 'nome']:
                    respostas_dict[conteudo[0]] += 1
                    totalRespostas += 1

            for chave, conteudo in respostas_dict.items():
                respostas_dict[chave] = respostas_dict[chave] / totalRespostas

            try:
                aluno = Aluno.objects.get(ra=ra)

            except Aluno.DoesNotExist:
                aluno = Aluno()
                aluno.ra = ra
                aluno.nome = nome
                aluno.email = email
                aluno.instituicao = teste
                aluno.save()
                id = aluno.id

            resultado = Resultado()
            for escolha, nome in CHOICES_ALTERNATIVA:
                setattr(resultado, nome, respostas_dict[str(escolha)])

            resultado.data_fim = resultado.data_ini = datetime.now()
            resultado.aluno = aluno
            resultado.instituicao = teste
            resultado.save()
            id = resultado.aluno.id

            return HttpResponseRedirect("/obrigado/" + str(id) + "/" + str(ra) + "/" + str(teste))
  except:
    return HttpResponseRedirect('/test/' + str(teste))

def index(request):
  return render (request, "projeto5_website/index.html")

@login_required(login_url='/login/')
def logout_user(request):
  logout(request)
  return render (request, "projeto5_website/logout.html")

def logout(request):
  return render(request, "projeto5_website/logout.html")