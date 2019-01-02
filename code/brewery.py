from .supplyChainAgent import SupplyChainAgent


class Brewery(SupplyChainAgent):

    TYPE = "brewery"

    def setCustomerSupplier(self):
        self.customer = self.sim.next_agent(Distributor.TYPE, Distributor.STATES["ACTIVE"])

    def order(self):
        # because we are the brewery we don't actually place orders, we simply define the amount that is to be produced
        amount = self.incomingOrders
        self.inventory += amount


from .distributor import Distributor
