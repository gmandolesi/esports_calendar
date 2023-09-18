from ics import Calendar, Event
c = Calendar()

e = Event()
e.name = "Quarter Final #1"
e.begin = '2023-10-20 05:00:00'
e.end = '2023-10-20 08:00:00'
c.events.add(e)

e = Event()
e.name = "Quarter Final #2"
e.begin = '2023-10-20 08:30:00'
e.end = '2023-10-20 11:30:00'
c.events.add(e)

e = Event()
e.name = "Semi Final #1"
e.begin = '2023-10-21 05:00:00'
e.end = '2023-10-21 08:00:00'
c.events.add(e)

e = Event()
e.name = "Quarter Final #2"
e.begin = '2023-10-21 08:30:00'
e.end = '2023-10-21 11:30:00'
c.events.add(e)

e = Event()
e.name = "Grand Final"
e.begin = '2023-10-22 08:30:00'
e.end = '2023-10-22 11:30:00'
c.events.add(e)

with open('../IntelExtremeMasters.ics', 'w') as my_file:
    my_file.writelines(c.serialize_iter())
