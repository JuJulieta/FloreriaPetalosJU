from django.shortcuts import render
from .models import Flores,Compra
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
import datetime;
from .clases import elemento
from .forms import CustomUserForm

# CREACION DE VISTAS

@login_required(login_url='/login/')
def home(request):
    return render(request,'core/index.html')

@login_required(login_url='/login/')
def home_admin(request):
    return render(request,'core/home_admin.html')

@login_required(login_url='/login/')
def home_usu(request):
    return render(request,'core/home_usu.html')

@login_required(login_url='/login/')
def galeria_admin(request):
    flores=Flores.objects.all()
    #SE TOMAN LAS FLORES QUE SE HAYAN INGRESADO A LA LISTA 
    return render(request,'core/galeria_admin.html',{'listaFlores':flores})
   
def login(request):
    if request.POST:
        u=request.POST.get("txtUsuario")
        c=request.POST.get("txtPass")
                
        us=authenticate(request,username=u,password=c)
        request.session["carrito"] = []        
        request.session["carritox"] = []
        msg=''
        print('realizado')
        if us is not None and us.is_active and us.is_staff:
            request.session["carrito"] = []        
            request.session["carritox"] = []  
            auth_login(request, us)
            arreglo={'nombre':u, 'contrasena':c, 'tipo':'administrador'}
            return render(request,'core/home_admin.html',arreglo)
        if us is not None and us.is_active:
            request.session["carrito"] = []        
            request.session["carritox"] = []  
            auth_login(request,us)
            arreglo={'nombre':u, 'contrasena':c, 'tipo':'cliente'}
            return render(request,'core/home_usu.html',arreglo)
        if us.is_active:
            request.session["carrito"] = []        
            request.session["carritox"] = []  
            auth_login(request,us)
            arreglo={'nombre':u, 'contrasena':c, 'tipo':'cliente'}
            return render(request,'core/home_usu.html',arreglo)

    return render(request,'core/login.html')

@login_required(login_url='/login/')
def carrito(request):
    x=request.session.get("carritox","")
    suma=0
    for item in x:
        suma=suma+int(item["total"])           
    return render(request,'core/carrito.html',{'x':x,'total':suma})

@login_required(login_url='/login/')
def grabar_carro(request):
    x=request.session["carritox"]    
    usuario=request.user.username
    suma=0
    try:
        for item in x:        
            producto=item["nombre"]
            valor=int(item["valor"])
            cantidad=int(item["cantidad"])
            total=int(item["total"])        
            compra=Compra(
                usuario=usuario,
                producto=producto,
                valor=valor,
                cantidad=cantidad,
                total=total,
                fecha=datetime.date.today()
            )
            compra.save()
            suma=suma+int(total)  
            print("reg grabado")                 
        mensaje="Grabado"
        request.session["carritox"] = []
    except:
        mensaje="error al grabar"            
    return render(request,'core/carrito.html',{'x':x,'total':suma,'mensaje':mensaje})

@login_required(login_url='/login/')
def agregar_carro(request,id):
    f=Flores.objects.get(name=id)
    x=request.session.get("carritox","")
    el=elemento(1,f.name,f.valor,1)
    sw=0
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            sw=1
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["valor"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    

    if sw==0:
        clon.append(el.toString())
    x=clon    
    request.session["carritox"]=x
    flores=Flores.objects.all()
    return HttpResponse("<script> ;window.location.href='/galeria_usu/',{'flores':flores,'total':suma};</script>")

@login_required(login_url='/login/')
def carro_compras_mas(request,id):
    f=Flores.objects.get(name=id)
    x=request.session["carritox"]
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            cantidad=int(cantidad)+1
        ne=elemento(1,item["nombre"],item["valor"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]        
    return render(request,'core/carrito.html',{'x':x,'total':suma})

    #sesion=request.session.get("carro","")
    #request.session["carro"]=sesion+str(id)+" "
    #flores=Flores.objects.all()
    #msg='agregó flores'
    #return render(request, 'core/galeria_usu.html',{'listaFlores':flores,'msg':msg})

@login_required(login_url='/login/')
def carro_compras_menos(request,id):
    f=Flores.objects.get(name=id)
    x=request.session["carritox"]
    suma=0
    clon=[]
    for item in x:        
        cantidad=item["cantidad"]
        if item["nombre"]==f.name:
            cantidad=int(cantidad)-1
        ne=elemento(1,item["nombre"],item["valor"],cantidad)
        suma=suma+int(ne.total())
        clon.append(ne.toString())
    x=clon    
    request.session["carritox"]=x
    x=request.session["carritox"]        
    return render(request,'core/carrito.html',{'x':x,'total':suma})

@login_required(login_url='/login/')
def galeria_usu(request):
    flores=Flores.objects.all()
    #SE TOMAN LAS FLORES QUE SE HAYAN INGRESADO A LA LISTA 
    return render(request,'core/galeria_usu.html',{'listaFlores':flores})

@login_required(login_url='/login/')
def vaciar_carrito(request):
    request.session["carritox"]=""
    lista=request.session.get("caritox","")
    return render(request,"core/carrito.html",{'contenido':lista})

@login_required(login_url='/login/')
def formulario(request):
    florr=Flores.objects.all()
    if request.POST: 
        Name=request.POST.get("txtNombre")
        Valor=request.POST.get("txtValor")
        Descripcion=request.POST.get("txtDesc")
        Estado=request.POST.get("txtEstado")
        Stock=request.POST.get("txtStock")
        Imagen=request.FILES.get("txtImagen")
        flor=Flores(
            name=Name,
            valor=Valor,
            descripcion=Descripcion,
            estado=Estado,
            stock=Stock,
            imagen=Imagen
        )
        flor.save() #graba el objeto en bdd
        return render(request,'core/formulario.html',{'lista':florr,'msg':'grabo','sw':True})
        #pasa los datos a la web
    return render(request,'core/formulario.html',{'lista':florr})

@login_required(login_url='/login/')
def eliminar_flor(request,id): 
    flor=Flores.objects.get(name=id)
    flor.delete()
    #SE RETORNA A LA PAGINA QUE SE COLOCA EN EL HREF LUEGO DE REALIZAR LA ACCION
    return HttpResponse("<script> ;window.location.href='/galeria_admin/';</script>")

def login_inicio(request):
    if request.POST:
        u=request.POST.get("txtUsuario")
        c=request.POST.get("txtPassword")
         
        #VALIDACION DEL USUARIO
        us=authenticate(request,username=u,password=c)
        
        msg=''
        request.session["carrito"] = []        
        request.session["carritox"] = [] 
        if us is not None and us.is_active and us.is_staff:
            request.session["carrito"] = []        
            request.session["carritox"] = []  
            auth_login(request,us)
            arreglo={'nombre':u, 'contrasena':c, 'tipo':'administrador'}
            return render(request,'core/home_admin.html',arreglo)
        if us is not None and us.is_active:
            request.session["carrito"] = []        
            request.session["carritox"] = []  
            auth_login(request,us)
            arreglo={'nombre':u, 'contrasena':c, 'tipo':'cliente'}
            return render(request,'core/home_usu.html',arreglo)
        if us.is_active:
            request.session["carrito"] = []        
            request.session["carritox"] = []  
            auth_login(request,us)
            arreglo={'nombre':u, 'contrasena':c, 'tipo':'cliente'}
            return render(request,'core/home_usu.html',arreglo)
def registro(request):
    data={
        'form':CustomUserForm()
    }
    if request.method=='POST': 
        formulario=CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request, user)
            return redirect(to='home')
    return render(request,'core/registro.html',data)


def cerrar_sesion(request):
    logout(request)
    return HttpResponse("<script>;window.location.href='/';</script>")


######################################################################
def isset(variable):
	return variable in locals() or variable in globals()        


