def crear_evento_google_calendar(service, titulo, fecha):
    evento = {
        'summary': titulo,
        'start': {'dateTime': fecha.isoformat(), 'timeZone': 'America/Bogota'},
        'end': {'dateTime': (fecha + timedelta(hours=1)).isoformat(), 'timeZone': 'America/Bogota'}
    }
    return service.events().insert(calendarId='primary', body=evento).execute()
