"""
Задача 5:

Напишите программу, которая моделирует бронирование билетов на
мероприятия. Пользователь может добавлять событие, бронировать и отменять
билеты, а также узнавать актуальную информацию по событиям и
забронированным билетам. Должны быть реализованы классы и методы:
• Event — хранит информацию о мероприятии, такую как название, цена
одного билета, место проведения и количество доступных билетов:
    o Методы:
        o get_event_info – возвращает информацию о событии
• Ticket — хранит информацию о том, на какое событие билет, о стоимости
билета, его владельце и идентификационный номер билета:
    o Методы:
        o get_ticket_info – возвращает информацию о билете
• BookingSystem — класс для управления процессом бронирования:
    o Методы:
        o add_event – добавляет событие в систему
        o get_available_events – возвращает информацию о доступных
            событиях
        o check_availability – возращает доступное количество билетов на
            переданное событие
        o book_ticket – бронирует указанное количество билетов на нужное
            мероприятие на имя определенного человека
        o cancel_booking – отменяет бронь билета по его идентификационному
            номеру
        o get_booked_tickets – возвращает информацию о забронированных билетах

Пример:
booking_system = BookingSystem()

event = Event("Концерт", 500, "Городской парк", 100) # Добавили новое событие
booking_system.book_ticket("Концерт", 2, "Иван Иванов") # Забронировали 2 билета на концерт

print(booking_system. check_availability("Концерт")) # Оставшиеся билеты = 98
print(booking_system.get_ booked_tickets())
# {
# "Event Name": "Концерт",
# "Owner": "Иван Иванов",
# "Price": 500,
# "ID": 0,
# },
# {
# "Event Name": "Концерт",
# "Owner": "Иван Иванов",
# "Price": 500,
# "ID": 1,
# }
"""

class Event:
    def __init__(self, name, price, location, available_tickets):
        self.name = name
        self.price = price
        self.location = location
        self.available_tickets = available_tickets

    def get_event_info(self):
        return {
            "Event Name": self.name,
            "Price": self.price,
            "Location": self.location,
            "Available Tickets": self.available_tickets
        }


class Ticket:
    def __init__(self, event_name, price, owner, ticket_id):
        self.event_name = event_name
        self.price = price
        self.owner = owner
        self.ticket_id = ticket_id

    def get_ticket_info(self):
        return {
            "Event Name": self.event_name,
            "Owner": self.owner,
            "Price": self.price,
            "ID": self.ticket_id
        }


class BookingSystem:
    def __init__(self):
        self.events = []
        self.tickets = []
        self.next_ticket_id = 0

    def add_event(self, name, price, location, available_tickets):
        event = Event(name, price, location, available_tickets)
        self.events.append(event)
        return event

    def get_available_events(self):
        return [event.get_event_info() for event in self.events]

    def check_availability(self, event_name):
        for event in self.events:
            if event.name == event_name:
                return event.available_tickets
        return 0

    def book_ticket(self, event_name, quantity, owner):
        for event in self.events:
            if event.name == event_name:
                if event.available_tickets >= quantity:
                    booked_tickets = []
                    for _ in range(quantity):
                        ticket = Ticket(event_name, event.price, owner, self.next_ticket_id)
                        self.tickets.append(ticket)
                        booked_tickets.append(ticket.get_ticket_info())
                        self.next_ticket_id += 1
                    event.available_tickets -= quantity
                    return booked_tickets
                else:
                    return None
        return None

    def cancel_booking(self, ticket_id):
        for i, ticket in enumerate(self.tickets):
            if ticket.ticket_id == ticket_id:
                event_name = ticket.event_name
                for event in self.events:
                    if event.name == event_name:
                        event.available_tickets += 1
                        break
                del self.tickets[i]
                return True
        return False

    def get_booked_tickets(self):
        return [ticket.get_ticket_info() for ticket in self.tickets]


# Пример использования
booking_system = BookingSystem()

event = Event("Концерт", 500, "Городской парк", 100)
booking_system.events.append(event)

booked = booking_system.book_ticket("Концерт", 2, "Иван Иванов")

print(booking_system.check_availability("Концерт"))
print(booking_system.get_booked_tickets())
