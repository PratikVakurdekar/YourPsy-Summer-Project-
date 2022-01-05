from django.shortcuts import render
from django.http import HttpResponse
from .models import Users_Info
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,'home.html')

def end(request):
    val1 = int(request.POST['no'])
    val2 = int(request.POST['o'])
    val3 = int(request.POST['n'])
    val4 = int(request.POST['ola'])
    val5 = int(request.POST['nola'])
    val6 = int(request.POST['nole'])
    val7 = int(request.POST['nose'])
    val8 = int(request.POST['non'])
    val9 = int(request.POST['norm'])
    val10 = int(request.POST['nova'])

    res = val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8 + val9 + val10
  
    return render(request,"result.html",{'result':res})   

def ned(request):
    val11 = int(request.POST['a'])
    val12 = int(request.POST['f'])
    val13 = int(request.POST['lion'])
    val14 = int(request.POST['you'])
    val15 = int(request.POST['of'])
    val16 = int(request.POST['ox'])
    val17 = int(request.POST['ow'])

    resu = val11 + val12 + val13 + val14 + val15 + val16 + val17 
    
    return render(request,"result.html",{'resu':resu}) 

def gol(request):
    user_name = request.POST["Name"]
    user_email = request.POST["Email"]
    user_test = request.POST["detail1"]
    user_age = request.POST["age"]
    user_gender = request.POST["gender"]
   
    user_info = Users_Info(user_name=user_name,user_email=user_email,user_test=user_test,user_age=user_age,user_gender=user_gender)
    user_info.save()
    return render(request,"test/personalities.html") 


def ogl(request):
    user_name = request.POST["Name"]
    user_email = request.POST["Email"]
    user_test = request.POST["detail2"]
    user_age = request.POST["age"]
    user_gender = request.POST["gender"]
    user_info = Users_Info(user_name=user_name,user_email=user_email,user_test=user_test,user_age=user_age,user_gender=user_gender)
    user_info.save()
    return render(request,"test/depression.html")   
         
        

def log(request):
    user_name = request.POST["Name"]
    user_email = request.POST["Email"]
    user_test = request.POST["detail3"]
    user_age = request.POST["age"]
    user_gender = request.POST["gender"]
    user_info = Users_Info(user_name=user_name, user_email=user_email, user_test=user_test, user_age=user_age, user_gender=user_gender)
    user_info.save()
    return render(request,"test/anxiety.html")         

def glo(request):
    user_name = request.POST["Name"]
    user_email = request.POST["Email"]
    user_test = request.POST["detail4"]
    user_age = request.POST["age"]
    user_gender = request.POST["gender"]
    user_info = Users_Info(user_name=user_name,user_email=user_email,user_test=user_test,user_age=user_age,user_gender=user_gender)
    user_info.save()
    return render(request,"test/adhd.html")   


    

def sub(request):
    vala = int(request.POST['a'])
    valb = int(request.POST['b'])
    valc = int(request.POST['c'])
    vald = int(request.POST['d'])
    vale = int(request.POST['e'])
    valf = int(request.POST['f'])
    valg = int(request.POST['g'])
    valh = int(request.POST['h'])
    vali = int(request.POST['i'])
    valj = int(request.POST['j'])
    valk = int(request.POST['k'])
    vall = int(request.POST['l'])
    valm = int(request.POST['m'])
    valn = int(request.POST['n'])
    valo = int(request.POST['o'])
    valp = int(request.POST['p'])
    valq = int(request.POST['q'])
    valr = int(request.POST['r'])
    vals = int(request.POST['s'])
    valt = int(request.POST['t'])
    
    IE = vala + vale + vali + valm + valq
    NS = valb + valf + valj + valn + valr
    FT = valc + valg + valk + valo + vals
    PJ = vald + valh + vall + valp + valt


    if (IE < 0 and NS < 0  and FT < 0 and PJ < 0):
        return render(request,"personalities/estj/estj.html") 

    if (IE<0 and NS<0 and FT<0 and PJ>0):
        return render(request,"personalities/estp/estp.html") 

    if(IE<0 and NS<0 and FT>0 and PJ<0):
        return render(request,"personalities/esfj/esfj.html")

    if(IE<0 and NS<0 and FT>0 and PJ>0):
        return render(request,"personalities/esfp/esfp.html")

    if(IE<0 and NS>0 and FT<0 and PJ<0):
        return render(request,"personalities/entj/entj.html")

    if(IE<0 and NS>0 and FT<0 and PJ>0):
        return render(request,"personalities/entp/entp.html")

    if(IE<0 and NS>0 and FT>0 and PJ<0):
        return render(request,"personalities/enfj/enfj.html")

    if(IE<0 and NS>0 and FT>0 and PJ>0):
        return render(request,"personalities/enfp/enfp.html")

    if(IE>0 and NS<0 and FT<0 and PJ<0):
        return render(request,"personalities/istj/istj.html")

    if(IE>0 and NS<0 and FT<0 and PJ>0):
        return render(request,"personalities/istp/istp.html")

    if(IE>0 and NS<0 and FT>0 and PJ<0):
        return render(request,"personalities/isfj/isfj.html")

    if( IE>0 and NS<0 and FT>0 and PJ>0):
        return render(request,"personalities/isfp/isfp.html")

    if(IE>0 and NS>0 and FT<0 and PJ<0):
        return render(request,"personalities/intj/intj.html")

    if(IE>0 and NS>0 and FT<0 and PJ>0):
        return render(request,"personalities/intp/intp.html")

    if(IE>0 and NS>0 and FT>0 and PJ<0):
        return render(request,"personalities/infj/infj.html")

    if(IE>0 and NS>0 and FT>0 and PJ>0):
        return render(request,"personalities/infp/infp.html")

    if(IE==0 or NS==0 or FT==0 or PJ==0):
        return render(request,"trial.html")


def adh(request):
    val10 = int(request.POST['nik'])
    val20 = int(request.POST['senora'])
    val30 = int(request.POST['sar'])
    val40 = int(request.POST['charu'])
    val50 = int(request.POST['dis'])
    val60 = int(request.POST['aunty'])
    val70 = int(request.POST['so'])
    val80 = int(request.POST['sasa'])
    val90 = int(request.POST['kom'])
    val100 = int(request.POST['que'])
    
    info = Users_Info.objects.earliest('user_name')


    report = val10 + val20 + val30 + val40 + val50 + val60 + val70 + val80 + val90 + val100
  
    return render(request,"result.html",{'report':report,'info':info}) 


def details1(request):
    return render(request,'details1.html')

def details2(request):
    return render(request,'details2.html')

def details3(request):
    return render(request,'details3.html')

def details4(request):
    return render(request,'details4.html')




def anxiety(request):
    return render(request,'test/anxiety.html')

def base(request):
    return render(request,'base.html')

def depression(request):
    return render(request,'test/depression.html')

def personalities(request):
    return render(request,'test/personalities.html')

def adhd(request):
    return render(request,'test/adhd.html')

def login(request):
    return render(request,'login.html')   

def quote(request):
    return render(request,'quote.html')   

def flip(request):
    return render(request,'flip.html') 

def xander(request):
    return render(request,'xander.html')

def trial(request):
    return render(request,'trial.html')

def elemental(request):
    return render(request,'elemental.html')

def trial2(request):
    return render(request,'triall2.html')

def dintro(request):
    return render(request,'dintro.html')
def aintro(request):
    return render(request,'aintro.html')
def adhdintro(request):
    return render(request,'adhdintro.html')

def mbtiintro(request):
    return render(request,'mbtiintro.html')

def amedication(request):
    return render(request,'amedication.html')
def dmedication(request):
    return render(request,'dmedication.html')
def adhdmedic(request):
    return render(request,'adhdmedic.html')




   

def enfjc(request):
    return render(request,'personalities/enfj/enfjc.html') 

def enfjf(request):
    return render(request,'personalities/enfj/enfjf.html') 

def enfji(request):
    return render(request,'personalities/enfj/enfji.html')     
   
def enfjp(request):
    return render(request,'personalities/enfj/enfjp.html') 

def enfjr(request):
    return render(request,'personalities/enfj/enfjr.html') 

def enfjs(request):
    return render(request,'personalities/enfj/enfjs.html') 

def enfjw(request):
    return render(request,'personalities/enfj/enfjw.html') 





def enfpc(request):
    return render(request,'personalities/enfp/enfpc.html') 

def enfpf(request):
    return render(request,'personalities/enfp/enfpf.html') 

def enfpi(request):
    return render(request,'personalities/enfp/enfpi.html')     
   
def enfpp(request):
    return render(request,'personalities/enfp/enfpp.html') 

def enfpr(request):
    return render(request,'personalities/enfp/enfpr.html') 

def enfps(request):
    return render(request,'personalities/enfp/enfps.html') 

def enfpw(request):
    return render(request,'personalities/enfp/enfpw.html') 




def entjc(request):
    return render(request,'personalities/entj/entjc.html') 

def entjf(request):
    return render(request,'personalities/entj/entjf.html') 

def entji(request):
    return render(request,'personalities/entj/entji.html')     
   
def entjp(request):
    return render(request,'personalities/entj/entjp.html') 

def entjr(request):
    return render(request,'personalities/entj/entjr.html') 

def entjs(request):
    return render(request,'personalities/entj/entjs.html') 

def entjw(request):
    return render(request,'personalities/entj/entjw.html') 




def entpc(request):
    return render(request,'personalities/entp/entpc.html') 

def entpf(request):
    return render(request,'personalities/entp/entpf.html') 

def entpi(request):
    return render(request,'personalities/entp/entpi.html')     
   
def entpp(request):
    return render(request,'personalities/entp/entpp.html') 

def entpr(request):
    return render(request,'personalities/entp/entpr.html') 

def entps(request):
    return render(request,'personalities/entp/entps.html') 

def entpw(request):
    return render(request,'personalities/entp/entpw.html') 





def esfjc(request):
    return render(request,'personalities/esfj/esfjc.html') 

def esfjf(request):
    return render(request,'personalities/esfj/esfjf.html') 

def esfji(request):
    return render(request,'personalities/esfj/esfji.html')     
   
def esfjp(request):
    return render(request,'personalities/esfj/esfjp.html') 

def esfjr(request):
    return render(request,'personalities/esfj/esfjr.html') 

def esfjs(request):
    return render(request,'personalities/esfj/esfjs.html') 

def esfjw(request):
    return render(request,'personalities/esfj/esfjw.html') 




def esfpc(request):
    return render(request,'personalities/esfp/esfpc.html') 

def esfpf(request):
    return render(request,'personalities/esfp/esfpf.html') 

def esfpi(request):
    return render(request,'personalities/esfp/esfpi.html')     
   
def esfpp(request):
    return render(request,'personalities/esfp/esfpp.html') 

def esfpr(request):
    return render(request,'personalities/esfp/esfpr.html') 

def esfps(request):
    return render(request,'personalities/esfp/esfps.html') 

def esfpw(request):
    return render(request,'personalities/esfp/esfpw.html') 


def estjc(request):
    return render(request,'personalities/estj/estjc.html') 

def estjf(request):
    return render(request,'personalities/estj/estjf.html') 

def estji(request):
    return render(request,'personalities/estj/estji.html')     
   
def estjp(request):
    return render(request,'personalities/estj/estjp.html') 

def estjr(request):
    return render(request,'personalities/estj/estjr.html') 

def estjs(request):
    return render(request,'personalities/estj/estjs.html') 

def estjw(request):
    return render(request,'personalities/estj/estjw.html') 


def estpc(request):
    return render(request,'personalities/estp/estpc.html') 

def estpf(request):
    return render(request,'personalities/estp/estpf.html') 

def estpi(request):
    return render(request,'personalities/estp/estpi.html')     
   
def estpp(request):
    return render(request,'personalities/estp/estpp.html') 

def estpr(request):
    return render(request,'personalities/estp/estpr.html') 

def estps(request):
    return render(request,'personalities/estp/estps.html') 

def estpw(request):
    return render(request,'personalities/estp/estpw.html') 


def infjc(request):
    return render(request,'personalities/infj/infjc.html') 

def infjf(request):
    return render(request,'personalities/infj/infjf.html') 

def infji(request):
    return render(request,'personalities/infj/infji.html')     
   
def infjp(request):
    return render(request,'personalities/infj/infjp.html') 

def infjr(request):
    return render(request,'personalities/infj/infjr.html') 

def infjs(request):
    return render(request,'personalities/infj/infjs.html') 

def infjw(request):
    return render(request,'personalities/infj/infjw.html') 


def infpc(request):
    return render(request,'personalities/infp/infpc.html') 

def infpf(request):
    return render(request,'personalities/infp/infpf.html') 

def infpi(request):
    return render(request,'personalities/infp/infpi.html')     
   
def infpp(request):
    return render(request,'personalities/infp/infpp.html') 

def infpr(request):
    return render(request,'personalities/infp/infpr.html') 

def infps(request):
    return render(request,'personalities/infp/infps.html') 

def infpw(request):
    return render(request,'personalities/infp/infpw.html') 


def intjc(request):
    return render(request,'personalities/intj/intjc.html') 

def intjf(request):
    return render(request,'personalities/intj/intjf.html') 

def intji(request):
    return render(request,'personalities/intj/intji.html')     
   
def intjp(request):
    return render(request,'personalities/intj/intjp.html') 

def intjr(request):
    return render(request,'personalities/intj/intjr.html') 

def intjs(request):
    return render(request,'personalities/intj/intjs.html') 

def intjw(request):
    return render(request,'personalities/intj/intjw.html') 


def intpc(request):
    return render(request,'personalities/intp/intpc.html') 

def intpf(request):
    return render(request,'personalities/intp/intpf.html') 

def intpi(request):
    return render(request,'personalities/intp/intpi.html')     
   
def intpp(request):
    return render(request,'personalities/intp/intpp.html') 

def intpr(request):
    return render(request,'personalities/intp/intpr.html') 

def intps(request):
    return render(request,'personalities/intp/intps.html') 

def intpw(request):
    return render(request,'personalities/intp/intpw.html') 


def isfjc(request):
    return render(request,'personalities/isfj/isfjc.html') 

def isfjf(request):
    return render(request,'personalities/isfj/isfjf.html') 

def isfji(request):
    return render(request,'personalities/isfj/isfji.html')     
   
def isfjp(request):
    return render(request,'personalities/isfj/isfjp.html') 

def isfjr(request):
    return render(request,'personalities/isfj/isfjr.html') 

def isfjs(request):
    return render(request,'personalities/isfj/isfjs.html') 

def isfjw(request):
    return render(request,'personalities/isfj/isfjw.html') 


def isfpc(request):
    return render(request,'personalities/isfp/isfpc.html') 

def isfpf(request):
    return render(request,'personalities/isfp/isfpf.html') 

def isfpi(request):
    return render(request,'personalities/isfp/isfpi.html')     
   
def isfpp(request):
    return render(request,'personalities/isfp/isfpp.html') 

def isfpr(request):
    return render(request,'personalities/isfp/isfpr.html') 

def isfps(request):
    return render(request,'personalities/isfp/isfps.html') 

def isfpw(request):
    return render(request,'personalities/isfp/isfpw.html') 


def istjc(request):
    return render(request,'personalities/istj/istjc.html') 

def istjf(request):
    return render(request,'personalities/istj/istjf.html') 

def istji(request):
    return render(request,'personalities/istj/istji.html')     
   
def istjp(request):
    return render(request,'personalities/istj/istjp.html') 

def istjr(request):
    return render(request,'personalities/istj/istjr.html') 

def istjs(request):
    return render(request,'personalities/istj/istjs.html') 

def istjw(request):
    return render(request,'personalities/istj/istjw.html') 


def istpc(request):
    return render(request,'personalities/istp/istpc.html') 

def istpf(request):
    return render(request,'personalities/istp/istpf.html') 

def istpi(request):
    return render(request,'personalities/istp/istpi.html')     
   
def istpp(request):
    return render(request,'personalities/istp/istpp.html') 

def istpr(request):
    return render(request,'personalities/istp/istpr.html') 

def istps(request):
    return render(request,'personalities/istp/istps.html') 

def istpw(request):
    return render(request,'personalities/istp/istpw.html') 



def enfj(request):
    return render(request,'personalities/enfj/enfj.html') 
def enfp(request):
    return render(request,'personalities/enfj/enfp.html') 
def entj(request):
    return render(request,'personalities/enfj/entj.html') 
def entp(request):
    return render(request,'personalities/enfj/entp.html') 
def esfj(request):
    return render(request,'personalities/enfj/esfj.html') 
def esfp(request):
    return render(request,'personalities/enfj/esfp.html') 
def estj(request):
    return render(request,'personalities/enfj/estj.html') 
def estp(request):
    return render(request,'personalities/enfj/estp.html') 
def infj(request):
    return render(request,'personalities/enfj/infj.html') 
def infp(request):
    return render(request,'personalities/enfj/infp.html') 
def intj(request):
    return render(request,'personalities/enfj/intj.html') 
def intp(request):
    return render(request,'personalities/enfj/intp.html') 
def isfj(request):
    return render(request,'personalities/enfj/isfj.html') 
def isfp(request):
    return render(request,'personalities/enfj/isfp.html') 
def istj(request):
    return render(request,'personalities/enfj/istj.html') 
def istp(request):
    return render(request,'personalities/enfj/istp.html') 



def setSession(request):
    request.session['session_data_1']="This is Session 1 Data"
    request.session['session_data_2']="This is Session 2 Data"
    return HttpResponse("Session Set")

def view_session(request):
    if request.session.has_key("session_data_1"):
        session_data_1=request.session['session_data_1']
    else:
        session_data_1="Data is Blank"

    if request.session.has_key("session_data_2"):
        session_data_2=request.session['session_data_2']
    else:
        session_data_2="Data is Blank"

    return render(request,"show_session_data.html",{"session_data_1":session_data_1,"session_data_2":session_data_2})

def del_session(request):
    del request.session['session_data_1']
    del request.session['session_data_2']
    return HttpResponse("Session Deleted")

def contact(request):
    if request.method =="POST":
   
        name = request.POST['w3lName'] 
        sender = request.POST['w3lSender']
        subject = request.POST['w3lSubject']
        message = request.POST['w3lMessage']

        send_mail(
            name + '-' + subject, #subject 
            message, #message 
            sender, #from_email 
            [' ',' '] #recipient_list
        )
       
        return render(request,"contactus.html",{'name':name})
    else:
        return render(request,"contactus.html")
  
def trial4(request):
    return render(request,'trial4.html')   
 
































































