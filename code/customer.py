from BPTK_Py import Agent
from BPTK_Py import Event
from .events import Events
from .retailer import Retailer


class Customer(Agent):
    TYPE = "customer"
    STATES = {"ACTIVE": "active"}

    def __init__(self, agent_id, sim):
        super().__init__(agent_id, sim)
        self.outgoingOrders = 0

        self.supplier = None

    def initialize(self):
        self.supplier = self.sim.next_agent(Retailer.TYPE, Retailer.STATES["ACTIVE"])
        self.register_event_handler(self.STATES["ACTIVE"], Events.DELIVERY, self.handle_delivery_event)

    def handle_delivery_event(self, event):
        self.outgoingOrders -= event.data["delivery"]

    def order(self, time, sim_round, step):
        amount = 100 if time < 2 else 400
        self.supplier.receive_instantaneous_event(Event(Events.ORDER, self.id, self.supplier.id, {"order": amount}))
        self.outgoingOrders += amount

    def act(self, time, sim_round, step):
        super().act(time, sim_round, step)
        self.order(time, sim_round, step)
