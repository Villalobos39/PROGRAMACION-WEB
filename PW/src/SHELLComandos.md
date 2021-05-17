(VENV)demo002> python manage.py shell

******************************************************************
>>> 
    from home.models import Lead
>>> 
    Lead.objects.all()

            <QuerySet [<Lead: kevin>, <Lead: Junior Paul>, <Lead: Brayan Yahir>, <Lead: Alejo Benjamin>, <Lead: Dulce Jasmin>]>

******************************************************************
>>> 
    Lead.objects.filter(marketing_strategy="FACEBOOK")
<QuerySet [<Lead: Alejo Benjamin>, <Lead: Dulce Jasmin>]>
>>> 
    for lead in Lead.objects.all:

******************************************************************
>>> 
    for lead in Lead.objects.all():
...     print(lead)
...
Kevin
Junior Paul
Brayan Yahir
Alejo Benjamin
Dulce Jasmin


>>> 
    for lead in Lead.objects.all():
...     print(lead.register_timestamp)
...
2021-03-24 21:45:27.593057+00:00
2021-03-18 22:30:58.472362+00:00
2021-03-17 10:20:32.315784+00:00
2021-03-24 21:06:35.066573+00:00
2021-03-17 08:09:26.233668+00:00

******************************************************************
>>> 
    p=Lead.objects.all()
>>> 
    p[0].last_name
'Carrillo'
>>> 
    p.first()
<Lead: Kevin>

******************************************************************
>>> 
    p=Lead.objects.filter(contacted=True).order_by("-register_timestamp")
>>> 
    p
<QuerySet [<Lead: Junior Paul>, <Lead: Brayan Yahir>, <Lead: Dulce Jasmin>]>
>>>
    p=Lead.objects.filter(contacted=True, marketing_strategy="FACEBOOK" ).order_by("-register_timestamp")
>>> 
    P
<QuerySet [<Lead: Dulce Jasmin>]>

******************************************************************
>>> 
    p=Lead.objects.filter(contacted=True, marketing_strategy="FACEBOOK" ).order_by("-register_timestamp").count()
>>>
    p
1
>>>

******************************************************************
>>> 
    p=Lead.objects.filter(contacted=True, marketing_strategy="FACEBOOK" ).order_by("-register_timestamp")
>>> 
    if p.exists:
...     print("No esta vacio")
...
No esta vacio
>>>

******************************************************************


******************************************************************


******************************************************************

