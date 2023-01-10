from BPTK_Py import Model
from BPTK_Py import sd_functions as sd

from policySettings import PolicySettings

class Beergame(Model):

        
    def __init__(self):
        super().__init__(starttime=1.0,stoptime=24.0, dt=1.0, name="Beergame Arrayed")

        policy_settings = PolicySettings(
            model=self,
            name="policy_settings"
        )
        self.points["delivery_delay"] = [(1.0, 1.0), (2.0, 1.0), (3.0, 1.0), (4.0, 1.0), (5.0, 1.0), (6.0, 1.0), (7.0, 1.0), (8.0, 1.0), (9.0, 1.0), (10.0, 1.0), (11.0, 1.0), (12.0, 1.0), (13.0, 1.0), (14.0, 1.0), (15.0, 1.0), (16.0, 1.0), (17.0, 1.0), (18.0, 1.0), (19.0, 1.0), (20.0, 1.0), (21.0, 1.0), (22.0, 1.0), (23.0, 1.0), (24.0, 1.0), (25.0, 1.0), (26.0, 1.0), (27.0, 1.0), (28.0, 1.0), (29.0, 1.0), (30.0, 1.0), (31.0, 1.0), (32.0, 1.0), (33.0, 1.0), (34.0, 1.0), (35.0, 1.0), (36.0, 1.0), (37.0, 1.0), (38.0, 1.0), (39.0, 1.0), (40.0, 1.0)]
        self.order = self.converter("order")
        self.actual_order = self.converter("actual_order")
        self.order_line = self.stock("order_line")
        self.brewery_actual_production = self.converter("brewery_actual_production")
        self.brewery_actual_production.equation = 100.0
        self.delivery_delay = self.converter("delivery_delay")
        self.delivery_delay = 100.0

        self.order.setup_named_vector({"brewery": 100.0, "distributor": 100.0, "wholesaler": 100.0, "retailer": 100.0})
        self.order_line.setup_named_vector({"brewery": 100.0, "distributor": 100.0, "wholesaler": 100.0, "retailer": 100.0})

        self.actual_order.equation = policy_settings.multiplayer_mode_on * self.order + (1.0 - policy_settings.multiplayer_mode_on)
        self.test = self.converter("test")
        self.test.equation = sd.delay(self, self.brewery_actual_production, self.delivery_delay, 100.0)
        #self.incoming_delivery.setup_named_vector({"brewery": sd.delay(self, self.brewery_actual_production, self.delivery_delay, 100), "distributor": self.outgoing_delivery_rate["brewery"], "wholesaler": self.outgoing_delivery_rate["distributor"], "retailer": self.outgoing_delivery_rate["wholesaler"]})

Beergame()