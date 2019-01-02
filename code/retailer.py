from .supplyChainAgent import SupplyChainAgent


class Retailer(SupplyChainAgent):

    TYPE = "retailer"

    def setCustomerSupplier(self):
        self.supplier = self.sim.next_agent(Wholesaler.TYPE, Wholesaler.STATES["ACTIVE"])
        self.customer = self.sim.next_agent(Customer.TYPE, Customer.STATES["ACTIVE"])

from .wholesaler import Wholesaler
from .customer import Customer

