from ics import Calendar, Event
c = Calendar()

e = Event()
e.name = "Worlds Qualifying Series Best of 5"
e.begin = '2023-10-09 04:00:00'
e.end = '2023-10-09 07:00:00'
c.events.add(e)

e = Event()
e.name = "Worlds Best of 3"
e.end = '2023-10-10 13:00:00'
e.begin = '2023-10-10 07:00:00'
c.events.add(e)

e = Event()
e.name = "Worlds Best of 3"
e.end = '2023-10-11 13:00:00'
e.begin = '2023-10-11 07:00:00'
c.events.add(e)

e = Event()
e.name = "Worlds Best of 3"
e.end = '2023-10-12 13:00:00'
e.begin = '2023-10-12 07:00:00'
c.events.add(e)

e = Event()
e.name = "Worlds Best of 3"
e.end = '2023-10-13 13:00:00'
e.begin = '2023-10-13 07:00:00'
c.events.add(e)

e = Event()
e.name = "Worlds Best of 3"
e.end = '2023-10-14 13:00:00'
e.begin = '2023-10-14 07:00:00'
c.events.add(e)

with open('../LoL_WorldChampionship.ics', 'w') as my_file:
    my_file.writelines(c.serialize_iter())
