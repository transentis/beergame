from .supplyChainAgent import SupplyChainAgent


class Wholesaler(SupplyChainAgent):
    TYPE = "wholesaler"

    def setCustomerSupplier(self):
        self.supplier = self.sim.next_agent(Distributor.TYPE, Distributor.STATES["ACTIVE"])
        self.customer = self.sim.next_agent(Retailer.TYPE, Retailer.STATES["ACTIVE"])

from .distributor import Distributor
from .retailer import Retailer

