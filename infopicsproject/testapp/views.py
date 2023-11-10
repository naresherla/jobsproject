from django.shortcuts import render

# Create your views here.
def index_info(request):
    return render(request,'testapp/index.html')
def sports_info(request):
    head_msg='Sports information'
    msg1='india`s national game hockey'
    msg2='cricket '
    msg3='most played game in india'
    type = 'sports'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,'type':type}
    return render(request,'testapp/info.html',context=my_dict)
def politics_info(request):
    head_msg = 'politics information'
    msg1 = 'Pm Modi ji'
    msg2 = 'KCR ts cm'
    msg3 = 'politics are dirty'
    type = 'politics'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3, 'type': type}
    return render(request,'testapp/info.html',context=my_dict)
def systems_info(request):
    head_msg = 'systems information'
    msg1 = 'hp laptop'
    msg2 = 'dell laptop'
    msg3 = 'asus lap'
    type = 'systems'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3, 'type': type}
    return render(request,'testapp/info.html',context=my_dict)