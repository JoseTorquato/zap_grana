import json

from django.shortcuts import render

from agenda.models import WeddingRegistration


def calendar_view(request):
    registros_reservados = WeddingRegistration.objects.all()
    print(registros_reservados)
    reservados =  []
    ocupados =  []
    for reservado in registros_reservados:
        if reservado.status == 'pré reserva':
            reservados.append({ "id": reservado.id, "start": reservado.event_date.strftime('%Y-%m-%d'), "title": reservado.bride_and_groom_names, "display": "background", "backgroundColor": "orange", "textColor": "black"  })
        elif reservado.status == 'ocupado':
            ocupados.append({ "id": reservado.id, "start": reservado.event_date.strftime('%Y-%m-%d'), "allDay": True, "title": reservado.bride_and_groom_names, "display": "background", "backgroundColor": "red", "textColor": "black"  })

    return render(request, 'pages/calendar/calendar.html', context={
        "reservados": json.dumps(reservados),
        "ocupados": json.dumps(ocupados)
    })
