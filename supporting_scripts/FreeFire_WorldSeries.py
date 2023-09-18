from ics import Calendar, Event
c = Calendar()

e = Event()
e.name = "Free Fire World Series - Placeholder"
e.begin = '2023-11-10 00:00:00'
e.end = '2023-11-26 23:59:59'
c.events.add(e)

with open('../FreeFire_WorldSeries.ics', 'w') as my_file:
    my_file.writelines(c.serialize_iter())
