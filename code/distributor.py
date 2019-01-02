from .supplyChainAgent import SupplyChainAgent


class Distributor(SupplyChainAgent):
    TYPE = "distributor"

    def setCustomerSupplier(self):
        self.supplier = self.sim.next_agent(Brewery.TYPE, Brewery.STATES["ACTIVE"])
        self.customer = self.sim.next_agent(Wholesaler.TYPE, Wholesaler.STATES["ACTIVE"])

from .brewery import Brewery
from .wholesaler import Wholesaler

