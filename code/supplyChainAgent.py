from BPTK_Py import Agent
from BPTK_Py import Event
from BPTK_Py import log
from .events import Events


class SupplyChainAgent(Agent):
    STATES = {"ACTIVE": "active"}

    def __init__(self, agent_id, sim):
        super().__init__(agent_id, sim)
        self.outgoingOrders = 0
        self.incomingOrders = 0
        self.inventory = 400
        self.supplier = None
        self.customer = None

    def handle_delivery_event(self, event):
        self.outgoingOrders -= event.data["delivery"]
        self.inventory += event.data["delivery"]

    def handle_order_event(self, event):
        self.incomingOrders += event.data["delivery"]

    def initialize(self):
        self.register_event_handler(self.STATES["ACTIVE"], Events.DELIVERY, self.handle_delivery_event)
        self.register_event_handler(self.STATES["ACTIVE"], Events.ORDER, self.handle_order_event)
        self.setCustomerSupplier()

    def deliver(self):
        amount = min(self.inventory, self.incomingOrders)
        self.customer.receive_instantaneous_event(
            Event(Events.DELIVERY, self.id, self.customer.id, {"delivery": amount}))
        self.inventory -= amount
        self.incomingOrders -= amount

    def order(self):
        amount = self.incomingOrders
        self.supplier.receive_instantaneous_event(Event(Events.ORDER, self.id, self.supplier.id, {"order": amount}))
        self.outgoingOrders += amount

    def setCustomerSupplier(self):
        log("[ERROR] SupplyChainAgent.setCustomerSupplier should be called on a subclass")

    def act(self, time, sim_round, step):
        super().act(time, sim_round, step)
        self.order(time, sim_round, step)
        self.deliver(time, sim_round, step)