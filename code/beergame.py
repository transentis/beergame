from BPTK_Py import Model


class Beergame(Model):

    def instantiate_model(self):
        self.register_agent_factory(Brewery.TYPE, lambda agent_id, scenario: Brewery(agent_id, scenario))
        self.register_agent_factory(Distributor.TYPE, lambda agent_id, scenario: Distributor(agent_id, scenario))
        self.register_agent_factory(Wholesaler.TYPE, lambda agent_id, scenario: Wholesaler(agent_id, scenario))
        self.register_agent_factory(Retailer.TYPE, lambda agent_id, scenario: Retailer(agent_id, scenario))
        self.register_agent_factory(Customer.TYPE, lambda agent_id, scenario: Customer(agent_id, scenario))


from .brewery import Brewery
from .distributor import Distributor
from .wholesaler import Wholesaler
from .retailer import Retailer
from .customer import Customer


