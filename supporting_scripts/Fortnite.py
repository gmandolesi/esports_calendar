from ics import Calendar, Event
c = Calendar()

e = Event()
e.name = "Battle Royale Mix-Up Monday"
e.begin = '2023-09-18 15:00:00'
e.end = '2023-09-19 03:00:00'
c.events.add(e)

e = Event()
e.name = "Duos Cash Cup"
e.begin = '2023-09-22 08:00:00'
e.end = '2023-09-22 10:00:00'
c.events.add(e)

e = Event()
e.name = "Duos Cash Cup"
e.begin = '2023-09-22 15:00:00'
e.end = '2023-09-22 19:00:00'
c.events.add(e)

e = Event()
e.name = "Duos Cash Cup"
e.begin = '2023-09-22 21:00:00'
e.end = '2023-09-23 02:00:00'
c.events.add(e)

e = Event()
e.name = "Duos Cash Cup"
e.begin = '2023-09-23 08:00:00'
e.end = '2023-09-23 10:00:00'
c.events.add(e)

e = Event()
e.name = "Duos Cash Cup"
e.begin = '2023-09-23 15:00:00'
e.end = '2023-09-23 19:00:00'
c.events.add(e)

e = Event()
e.name = "Victory Cup"
e.begin = '2023-09-24 05:00:00'
e.end = '2023-09-25 02:00:00'
c.events.add(e)

e = Event()
e.name = "Battle Royale Mix-Up Monday"
e.begin = '2023-09-25 08:00:00'
e.end = '2023-09-25 10:00:00'
c.events.add(e)

e = Event()
e.name = "Battle Royale Mix-Up Monday"
e.begin = '2023-09-25 15:00:00'
e.end = '2023-09-26 02:00:00'
c.events.add(e)

e = Event()
e.name = "Fortnite Performance Evaluation"
e.begin = '2023-09-26 17:00:00'
e.end = '2023-09-26 20:00:00'
c.events.add(e)

e = Event()
e.name = "Duos Cash Cup"
e.begin = '2023-09-29 08:00:00'
e.end = '2023-09-29 10:00:00'
c.events.add(e)

e = Event()
e.name = "Duos Cash Cup"
e.begin = '2023-09-29 15:00:00'
e.end = '2023-09-30 02:00:00'
c.events.add(e)

e = Event()
e.name = "Duos Cash Cup"
e.begin = '2023-09-30 08:00:00'
e.end = '2023-09-30 10:00:00'
c.events.add(e)

e = Event()
e.name = "Duos Cash Cup"
e.begin = '2023-09-30 15:00:00'
e.end = '2023-09-30 23:00:00'
c.events.add(e)


with open('../Fortnite.ics', 'w') as my_file:
    my_file.writelines(c.serialize_iter())
