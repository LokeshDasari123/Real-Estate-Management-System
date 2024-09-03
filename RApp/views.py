from django.shortcuts import render,redirect
from .forms import AusForm,UsuserForm,UslistForm,UpForm,chgPwdForm,UdForm,SellForm,BuyForm,UspForm,PropForm,PropdelForm,PropsellForm,ApproveForm,Buymailtosell
from REMS import settings
from django.core.mail import send_mail,mail_admins,EmailMessage
from django.contrib import messages
from .models import User,seProfile,byProfile,Property
from django.db.models import Q
import mimetypes

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request): 
	return render(request,'html/about.html')     

def contact(request): 
	if request.method == "POST":
		sa = request.POST['sname']
		sndr = request.POST['sn']
		sbj = request.POST['sb']
		m = request.POST['msg']
		t = settings.EMAIL_HOST_USER
		a = "Message : "+m+"\n Mail : "+sndr+"\n Name : "+sa
		b = send_mail(sbj,a,t,[t])
		if b == 1:
			messages.success(request,"Mail has sent Successfully")
			return redirect('/cnt')
		else:
			messages.errors(request,"Mail not sent")
			return redirect('/cnt')
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		f = UsuserForm(request.POST)
		if f.is_valid():
			new_user = f.save()
			messages.success(request, "User Created Successfully")
			sbj = "Thanks for Signing Up to REMS"
			t1 = settings.EMAIL_HOST_USER
			if new_user.role_type_appl == 1:
				m1 = f"Dear {new_user.username},\nThank you for joining REMS!\nWe appreciate your support and look forward to enhancing your experience."
				b1 = send_mail(sbj, m1, t1, [new_user.email])
				new_user.eid = "REMS_" + str(new_user.id)
				new_user.role_type = 1
				new_user.save()
			else:
				m1 = f"Dear {new_user.username},\nThank you for joining REMS!\nYou have chosen for Seller Role. To acquire seller status, please stay in touch for further details and verification requirements."	
				b1 = send_mail(sbj, m1, t1, [new_user.email])
				new_user.eid = "REMS_" + str(new_user.id)
				new_user.save()
			return redirect('/lgn')
	f = UsuserForm()
	return render(request,'html/register.html',{'g':f})

def userlist(request): 
	c = User.objects.all()
	a = User.objects.all()
	for d in a:
		d.eid = "REMS_"+str(d.id)
		d.save()
	j = User.objects.filter(role_type_appl = 1)
	for i in j:
		i.role_type = 1
		i.save()
	n,m = {},{}
	if request.method == "POST":
		s = UslistForm(request.POST)
		if s.is_valid():
			user = s.save()
			messages.success(request,"User Created Successfully")
			sbj = "Thanks for Signing Up to REMS"
			t1 = settings.EMAIL_HOST_USER
			m1 = f"Dear {user.username},\nThank you for joining REMS!\nWe appreciate your support and look forward to enhancing your experience.\n Default Password : myproject@123 you can change it afterwards."
			b1 = send_mail(sbj, m1, t1, [user.email])
			return redirect('/usrlst')
		else:
			n[s] = s.errors
	for j in n.values():
		for v in j.items():
			m[v[0]] = v[1]
	s = UslistForm()
	return render(request,'html/userlist.html',{'w':s,'p':m.items(),'k':c})

def userupdate(request,h):
    t=User.objects.get(id=h)
    if request.method == "POST":
        z=UpForm(request.POST,instance=t)
        if z.is_valid():
            z.save()
            return redirect('/usrlst')
    z=UpForm(instance=t)
    return render(request,'html/userupd.html',{'s':z})

def userdelete(request,d):
    n=User.objects.get(id=d)
    if request.method == "POST":
        n1=UdForm(request.POST,instance=n) 
        n.delete()
        return redirect('/usrlst')
    n1=UdForm(instance=n)
    return render(request,'html/userdel.html',{'a':n1})

def chgepwd(request):
    if request.method == "POST":
        n=chgPwdForm(user=request.user,data=request.POST)
        if n.is_valid():
            n.save()
            return redirect('/lgn')
    n=chgPwdForm(user=request)
    return render(request,'html/changepaswd.html',{'h':n})

def profile(request):
    return render(request, "html/profile.html")

def updprofile(request):
	k = User.objects.get(id=request.user.id)
	if request.user.role_type == "2":
		t = seProfile.objects.all()
		m = []
		for i in t:
			m.append(i.sc_id)
		if request.user.id not in m:
			if request.method == "POST":
				h = UspForm(request.POST,request.FILES,instance=k)
				y = SellForm(request.POST,request.FILES)
				if h.is_valid() and y.is_valid():
					h.save()
					b = y.save(commit=False)
					b.sc_id = request.user.id
					b.sstatus = 1
					b.save()
					return redirect('/pfle')
			y = SellForm()
			h = UspForm(instance=k)
			return render(request,'html/updateprofile.html',{'e':h,'t':y})
		else:
			p = seProfile.objects.get(sc_id=request.user.id)
			if request.method == "POST":
				h = UspForm(request.POST,request.FILES,instance=k)
				y = SellForm(request.POST,request.FILES,instance=p)
				if h.is_valid() and y.is_valid():
					h.save()
					y.save()
					return redirect('/pfle')
			y = SellForm(instance=p)
			h = UspForm(instance=k)
			return render(request,'html/updateprofile.html',{'e':h,'t':y})
	elif request.user.role_type == "1":
		j = byProfile.objects.all()
		s = []
		for i in j:
			s.append(i.bc_id)
		if request.user.id not in s:
			if request.method == "POST":
				h = UspForm(request.POST,request.FILES,instance=k)
				n = BuyForm(request.POST)
				if h.is_valid() and n.is_valid():
					h.save()
					z = n.save(commit=False)
					z.bc_id = request.user.id
					z.bstatus = 1
					z.save()
					return redirect('/pfle')
			h = UspForm(instance=k)
			n = BuyForm()
			return render(request,'html/updateprofile.html',{'e':h,'a':n})
		else:
			v = byProfile.objects.get(bc_id=request.user.id)
			if request.method == "POST":
				h = UspForm(request.POST,request.FILES,instance=k)
				n = BuyForm(request.POST,instance=v)
				if h.is_valid() and n.is_valid():
					h.save()
					n.save()
					return redirect('/pfle')
			h = UspForm(instance=k)
			n = BuyForm(instance=v)
			return render(request,'html/updateprofile.html',{'e':h,'a':n})
	else:
		if request.method == "POST":
			h = UspForm(request.POST,request.FILES,instance=k)
			if h.is_valid():
				h.save()
				return redirect('/pfle')
		h = UspForm(instance=k)
		return render(request,'html/updateprofile.html',{'e':h})

def addprop(request):
	p = Property.objects.filter(pown_id = request.user.id)
	a = User.objects.get(id = request.user.id)
	if request.method == "POST":
		d = PropForm(request.POST,request.FILES)
		if d.is_valid():
			w = d.save(commit=False)
			w.pown_id = request.user.id
			if a:
				w.propown = a.eid 
				w.propprevown = a.eid
			w.save()
			return redirect('/propadd')
	d = PropForm()
	return render(request,'html/addproperty.html',{'z':d,'h':p})

def updprop(request,w):
	z=Property.objects.get(id=w)
	if request.method == "POST":
		x=PropForm(request.POST,request.FILES,instance=z)
		if x.is_valid():
			x.save()
			if request.user.is_superuser:
				return redirect('/proplista')
			else:
				return redirect('/propadd')
	x=PropForm(instance=z)
	return render(request,'html/updateproperty.html',{'c':x})

def sellprop(request,k):
	a=Property.objects.get(id=k)
	m2 = User.objects.get(id = request.user.id)  
	if request.method == "POST":
		x1=PropsellForm(request.POST,instance=a)
		if x1.is_valid():
			user1 = x1.save()
			a2 = User.objects.get(eid = user1.propsoldto)
			name = a2.username
			sndr = a2.email 
			doc = a.propdoc
			t = settings.EMAIL_HOST_USER
			sbj = "Regarding Property"
			msg1 ="Congratulations on your new property May it be filled with happiness and new beginnings. Enjoy every moment!"
			k1 = f"Dear {name},\n {msg1} \n Seller Details : \n Username : {m2.username}\n Email : {m2.email}\n Mobile No : {m2.mble}"
			email = EmailMessage(sbj, k1, t, [sndr])
			if doc:
				file_name = doc.name
				file_content = doc.read()
				content_type, _ = mimetypes.guess_type(file_name)
				email.attach(file_name,file_content,content_type)
			if email.send() == 1:
				messages.success(request,"Mail has sent Successfully")
				if request.user.is_superuser:
					return redirect('/proplista')
				else:
					return redirect('/propadd')
			else:
				messages.errors(request,"Mail not sent") 
	x1=PropsellForm(instance=a)
	return render(request,'html/sellpropto.html',{'c1':x1})

def deleprop(request,p): 
    k = Property.objects.get(id=p)
    if request.method == "POST":
        k1 = PropdelForm(request.POST, instance=k)
        k.delete()
        return redirect('/propadd')
    k1 = PropdelForm(instance=k)
    return render(request, 'html/deleteproperty.html', {'a': k1})

def proplist(request):
	p = Property.objects.all()
	a = User.objects.get(id = request.user.id)
	if request.method == "POST":
		d = PropForm(request.POST,request.FILES)
		if d.is_valid():
			w = d.save(commit=False)
			w.pown_id = request.user.id
			if a:
				w.propown = a.eid 
				w.propprevown = a.eid
			w.save()
			return redirect('/proplista')
	d = PropForm()
	return render(request,'html/addproperty_admin.html',{'z':d,'h':p})

def allprops(request):
	p1 = Property.objects.all()
	return render(request,'html/all_properties.html',{'z1':p1})

def allpropsadet(request,a):
	p2 = Property.objects.get(id = a)
	s2 = User.objects.get(id = p2.pown_id)
	if s2.is_superuser:
		return render(request,'html/all_properties_details.html',{'z2':p2,'z4':s2})
	else:
		p2 = Property.objects.get(id = a)
		s1 = seProfile.objects.get(sc_id = p2.pown_id)
		s2 = User.objects.get(id = p2.pown_id)
		return render(request,'html/all_properties_details.html',{'z2':p2,'z3':s1,'z4':s2})

def propmy(request):
	m = Property.objects.filter(Q(pown_id=request.user.id) | Q(propsoldto=request.user.eid))
	return render(request,'html/userproperties.html',{'z1':m})

def propbuy(request):
	m = Property.objects.exclude(Q(pown_id=request.user.id) | Q(propstatus = 'g'))
	return render(request,'html/buyproperties.html',{'z1':m})

def detbuyprop(request,q):   
	p2 = Property.objects.get(id = q)
	s2 = User.objects.get(id = p2.pown_id)
	if s2.is_superuser:
		return render(request,'html/buyproperties_details.html',{'z2':p2,'z4':s2})
	else:
		p2 = Property.objects.get(id = q)
		s1 = seProfile.objects.get(sc_id = p2.pown_id)
		s2 = User.objects.get(id = p2.pown_id)
		return render(request,'html/buyproperties_details.html',{'z2':p2,'z3':s1,'z4':s2}) 

def mypropbuy(request):
	m =Property.objects.filter(propsoldto = request.user.eid)
	return render(request,'html/buypropertiesforbuyer.html',{'z1':m})

def adapprov(request):
	m2 = User.objects.filter(role_type_appl=2) 
	return render(request,'html/adminapproval.html',{'z2':m2})

def detaofapp(request,k):
	m3 = User.objects.get(id = k)
	m5 = seProfile.objects.get(sc_id= k)
	
	return render(request,'html/adminapprovaldetails.html',{'z4':m3,'z5':m5})

def updatesell(request,h):
	m3 = User.objects.get(id =h) 
	if request.method == "POST":
		m4 = ApproveForm(request.POST,instance=m3)
		if m4.is_valid():
			m4.save()
			sa = m3.username
			sndr = m3.email
			sbj = "Application Status for Seller Role"
			m = request.POST['msg']
			tm="If you have any questions, feel free to reach out."
			k1 = f"Dear {sa},\n {m} \n {tm}"
			t = settings.EMAIL_HOST_USER
			b = send_mail(sbj,k1,t,[sndr])
			if b== 1:
				messages.success(request,"Mail has sent Successfully")
				return redirect('/approval')
			else:
				messages.errors(request,"Mail not sent") 
				return redirect('/approval')
	m4 = ApproveForm(instance=m3)
	return render(request,'html/adminapprov_deny.html',{'z4':m4})

def mailtosell(request,h1,h2):
	a = User.objects.get(id = h1)
	b = Property.objects.get(id = h2)
	c = User.objects.get(id = request.user.id)
	if request.method =="POST":
		a1 = Buymailtosell(request.POST,instance=a)
		sa = a.username
		sndr = a.email
		sbj = "Potential Buyer Interest in Your Property"
		m = request.POST['msg']
		type_1 = "default"
		if b.proptype == 1:
			type_1 = "Residential"
		elif b.proptype == 2:
			type_1 = "Commercial"
		elif b.proptype == 3:
			type_1 = "Agriculturial"
		else:
			type_1 = "Industrial"
		tm=f"I am pleased to inform you that we have a potential buyer interested in your {b.proptitle} id is {b.id} property at {b.propcity} and type is {type_1}. They'd like to learn more."
		tm1=f"Buyer Details are\n UserName : {c.username}\n Email : {c.email}\n Mobile No : {c.mble}\n Try to contact him"
		msg1 = f"Dear {sa},\n {m} \n {tm}\n {tm1}"
		t = settings.EMAIL_HOST_USER
		b = send_mail(sbj,msg1,t,[sndr])
		if b== 1:
			messages.success(request,"Mail has sent Successfully")
			return redirect('/buyprop')
		else:
			messages.errors(request,"Mail not sent") 
			return redirect('/buyprop')
	a1 = Buymailtosell(instance=a)
	return render(request,'html/mail_to_seller.html',{'z1':a1,'z2':b})

def solddetails(request,k1):
	b1 = Property.objects.get(id = k1)
	b2 = User.objects.get(eid = b1.propown)
	b3 = User.objects.get(eid = b1.propsoldto)
	return render(request,'html/sold_details.html',{'y1':b2,'y2':b3,'y3':b1})

def mailsendtoa(request,a1):
	n1 = User.objects.get(id = a1)
	if request.method == "POST":
		b1 = Buymailtosell(request.POST,instance=n1)
		sa = n1.username
		sndr = n1.email
		uid = n1.eid
		m = request.POST['msg']
		sbj = request.POST['sb']
		m = request.POST['msg']
		t = settings.EMAIL_HOST_USER
		msg2 = f"ID : {uid} \n Username : {sa} \n Email : {sndr} \n Message : {m}"
		b = send_mail(sbj,msg2,t,[t])
		if b == 1:
			messages.success(request,"Mail has sent Successfully")
			return redirect(f'/mailtoadmin/{str(a1)}')
		else:
			messages.errors(request,"Mail not sent")
			return redirect(f'/mailtoadmin/{str(a1)}')
	b1 = Buymailtosell(instance=n1)
	return render(request,'html/mail_admin_doubts.html',{'g':b1})
