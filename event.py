class Event:
    pass

class EventQueue:
    def __init__(self):
        self.events = []
        self.handlers = {}

    def push_event(self, event: Event):
       self.events.append(event) 

    def poll_event(self) -> Event | None:
        return self.events.pop(0) if len(self.events) > 0 else None
    
    def register_event(self, event_type, handler):
        if not event_type in self.handlers:
            self.handlers[event_type] = handler

    def handle_events(self):
        while (event := self.poll_event()) != None:
            if type(event) in self.handlers:
                self.handlers[type(event)](event)

