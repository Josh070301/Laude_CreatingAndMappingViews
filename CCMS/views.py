from django.shortcuts import render
from django.http import HttpResponse

def Mission(request):
    msg = '<h1>CCMS Mission</h1> \
    <p>The College of Computer Studies shall produce \
    technically competent Information Technology professionals adequately \
    prepared in the practice of their profession supportive of \
        national development goals and standards of global excellence.</p>'
    return HttpResponse(msg);

def Vision(request):
    msg = '<h1>CCMS Vision</h1> \
    <p>The College of Computer Studies shall be a center of excellence in Information \
    Technology education.</p>'
    return HttpResponse(msg);

def Objectives(request):
    msg = '<h1>CCMS Objectives</h1> \
    <p>After graduation, alumni of MSEUF-CCS programs shall:<br><br> \
    1. Be employed and demonstrate professionalism, competence and passion in solving \
    contemporary computing problems by developing or utilizing innovative IT solutions.<br><br> \
    2. Embark in lifelong learning or research to attune to the continuous innovation in the IT \
    industry in order to adapt to the changing demands of the global market; and <br><br> \
    3. Exhibit leadership and teamwork, and commitment to their respective local or global organizations.</p>'
    return HttpResponse(msg);

def home(request):
    msg = 'check urls.py <Br>\
    http://127.0.0.1:8000/Objectives/ <br> \
    http://127.0.0.1:8000/Mission/ <br>\
    http://127.0.0.1:8000/Vision/ <Br>\
    '
    return HttpResponse(msg);