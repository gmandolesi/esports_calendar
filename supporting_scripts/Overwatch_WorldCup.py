from ics import Calendar, Event
c = Calendar()

e = Event()
e.name = "Overwatch World Cup - Placeholder"
e.begin = '2023-10-29 00:00:00'
e.end = '2023-11-01 23:59:59'
c.events.add(e)

with open('../Overwatch_WorldCup.ics', 'w') as my_file:
    my_file.writelines(c.serialize_iter())
