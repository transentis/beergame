from BPTK_Py import Model
from BPTK_Py import sd_functions as sd
from policySettings import PolicySettings

class Beergame(Model):
    def __init__(self):
        super().__init__(starttime=1.0,stoptime=24.0, dt=1.0, name="Beergame Arrayed")
        print("Initializing!")
        policy_settings = PolicySettings(
            model=self,
            name="policy_settings"
        )

        # Policy Settings
        self.policy_settings = policy_settings    

        self.delivery_delay = self.converter("delivery_delay")
        self.customer_order = self.converter("customer_order")
        self.order = self.converter("order")
        self.actual_order = self.converter("actual_order")
        self.brewery_production = self.converter("brewery_production")
        self.brewery_actual_production = self.converter("brewery_actual_production")
        self.incoming_order = self.converter("incoming_order")
        self.total_incoming_orders = self.converter("total_incoming_orders")
        self.incoming_delivery = self.converter("incoming_delivery")
        self.supply_line = self.converter("supply_line")
        self.delivery_decision = self.converter("delivery_decision")
        self.outgoing_delivery = self.converter("outgoing_delivery")
        self.total_stock = self.converter("total_stock")
        self.inventory = self.converter("inventory")
        self.lagging_backorder = self.converter("lagging_backorder")
        self.lagging_surplus = self.converter("lagging_surplus")
        self.backorder = self.converter("backorder")
        self.surplus = self.converter("surplus")
        self.total_outgoing_orders = self.converter("total_outgoing_orders")
        self.naive_order_decision = self.converter("naive_order_decision")
        self.order_decision = self.converter("order_decision")
        self.target_supply_line = self.converter("target_supply_line") 
        self.target_total_stock = self.converter("target_total_stock")
        self.order_delay = self.converter("order_delay")
        self.sophisticated_order_decision = self.converter("sophisticated_order_decision")
        
        self.order_line = self.stock("order_line")
        self.lagging_supply_line = self.stock("lagging_supply_line")
        self.incoming_orders = self.stock("incoming_orders")
        self.lagging_supply_line = self.stock("lagging_supply_line")
        self.lagging_inventory = self.stock("lagging_inventory")
        self.deliveries = self.stock("deliveries")
        self.outgoing_orders = self.stock("outgoing_orders")
        self.order_line = self.stock("order_line")

        self.orders = self.flow("orders")
        self.incoming_order_rate = self.flow("incoming_order_rate")
        self.incoming_delivery_rate = self.flow("incoming_delivery_rate")
        self.outgoing_delivery_rate = self.flow("outgoing_delivery_rate")
        self.outgoing_delivery_rate.setup_named_vector({"brewery": 0.0, "distributor": 0.0, "wholesaler": 0.0, "retailer": 0.0})
        self.outgoing_orders_in = self.flow("outgoing_orders_in")
        self.making_orders = self.flow("making_orders")
        self.sending_orders = self.flow("sending_orders")
        
        self.delivery_delay.setup_named_vector({"brewery": 1.0, "distributor": 1.0, "wholesaler": 1.0, "retailer": 1.0})

        # Customer order
        self.points["dynamic_customer_order"] = [(1.0, 100.0), (2.0, 400.0), (3.0, 400.0), (4.0, 400.0), (5.0, 400.0), (6.0, 400.0), (7.0, 400.0), (8.0, 400.0), (9.0, 400.0), (10.0, 400.0), (11.0, 400.0), (12.0, 400.0), (13.0, 400.0), (14.0, 400.0), (15.0, 400.0), (16.0, 400.0), (17.0, 400.0), (18.0, 400.0), (19.0, 400.0), (20.0, 400.0), (21.0, 400.0), (22.0, 400.0), (23.0, 400.0), (24.0, 400.0), (25.0, 400.0), (26.0, 400.0), (27.0, 400.0), (28.0, 400.0), (29.0, 400.0), (30.0, 400.0), (31.0, 400.0), (32.0, 400.0), (33.0, 400.0), (34.0, 400.0), (35.0, 400.0), (36.0, 400.0), (37.0, 400.0), (38.0, 400.0), (39.0, 400.0), (40.0, 400.0)]
        #self.points["delivery_delay"] = [(1.0, 1.0), (2.0, 1.0), (3.0, 1.0), (4.0, 1.0), (5.0, 1.0), (6.0, 1.0), (7.0, 1.0), (8.0, 1.0), (9.0, 1.0), (10.0, 1.0), (11.0, 1.0), (12.0, 1.0), (13.0, 1.0), (14.0, 1.0), (15.0, 1.0), (16.0, 1.0), (17.0, 1.0), (18.0, 1.0), (19.0, 1.0), (20.0, 1.0), (21.0, 1.0), (22.0, 1.0), (23.0, 1.0), (24.0, 1.0), (25.0, 1.0), (26.0, 1.0), (27.0, 1.0), (28.0, 1.0), (29.0, 1.0), (30.0, 1.0), (31.0, 1.0), (32.0, 1.0), (33.0, 1.0), (34.0, 1.0), (35.0, 1.0), (36.0, 1.0), (37.0, 1.0), (38.0, 1.0), (39.0, 1.0), (40.0, 1.0)]

        
        self.customer_order.equation = policy_settings.steady_state_on*100.0+(1 - policy_settings.steady_state_on)*sd.lookup(sd.time(), self.points["dynamic_customer_order"])

        # orders
        
        self.order.setup_named_vector({"brewery": 100.0, "distributor": 100.0, "wholesaler": 100.0, "retailer": 100.0})

        
        self.order_line.setup_named_vector({"brewery": 100.0, "distributor": 100.0, "wholesaler": 100.0, "retailer": 100.0})

        
        self.actual_order.equation = policy_settings.game_mode_on * (policy_settings.multiplayer_mode_on * self.order + (1.0 - policy_settings.multiplayer_mode_on) * self.order) + (1.0 - policy_settings.multiplayer_mode_on) * self.order_line + (1.0 - policy_settings.game_mode_on) * self.order_line

        
        self.orders.equation = self.actual_order

        
        self.lagging_supply_line.setup_named_vector({"brewery": 100.0, "distributor": 100.0, "wholesaler": 100.0, "retailer": 100.0})
        
        
        self.brewery_production.equation = 100.0

        
        self.brewery_actual_production.equation = policy_settings.game_mode_on * (policy_settings.multiplayer_mode_on * self.brewery_production + (1.0 - policy_settings.multiplayer_mode_on) * self.order_line["brewery"]) + (1.0 - policy_settings.multiplayer_mode_on) * self.order_line["brewery"]

        # incoming orders
        
        self.incoming_order.setup_named_vector({"brewery": self.actual_order["distributor"], "distributor": self.actual_order["wholesaler"], "wholesaler": self.actual_order["retailer"], "retailer": self.customer_order})

        
        self.incoming_order_rate.equation = self.incoming_order

        
        self.incoming_orders.equation = self.incoming_order_rate

        
        self.total_incoming_orders.equation = self.incoming_order_rate + self.incoming_orders

        
        self.lagging_supply_line.setup_named_vector({"brewery": 0.0, "distributor": 0.0, "wholesaler": 0.0, "retailer": 0.0})
        self.lagging_supply_line.equation = self.orders - self.incoming_order_rate

        
        self.incoming_delivery.setup_named_vector({"brewery": sd.delay(self, self.brewery_actual_production, self.delivery_delay["brewery"], 100.0), "distributor": self.outgoing_delivery_rate["brewery"], "wholesaler": self.outgoing_delivery_rate["distributor"], "retailer": self.outgoing_delivery_rate["wholesaler"]})

        
        self.incoming_delivery_rate.equation = self.incoming_delivery

        
        self.supply_line.equation = self.orders + self.lagging_supply_line - self.incoming_delivery_rate

        
        self.lagging_inventory.setup_named_vector({"brewery": 400.0, "distributor": 400.0, "wholesaler": 400.0, "retailer": 400.0})
        self.lagging_inventory.equation = self.incoming_delivery_rate - self.outgoing_delivery_rate

        
        self.delivery_decision.setup_named_vector({"brewery": 0.0, "distributor": 0.0, "wholesaler": 0.0, "retailer": 0.0})

        
        self.outgoing_delivery.equation = self.delivery_decision

        
        self.outgoing_delivery_rate.equation = sd.min(self.lagging_inventory+self.incoming_delivery_rate, self.outgoing_delivery)

        
        self.deliveries.equation = self.outgoing_delivery_rate

        
        self.total_stock.equation = self.lagging_inventory + self.lagging_supply_line

        
        self.inventory.equation = sd.max(self.lagging_inventory + self.incoming_delivery_rate - self.outgoing_delivery_rate, 0.0)

        
        self.lagging_backorder.equation = sd.max(self.incoming_orders - self.deliveries, 0.0)

        
        self.lagging_surplus.equation = self.lagging_inventory - self.lagging_backorder

        
        self.backorder.equation = sd.max(self.lagging_backorder + self.incoming_order_rate - self.outgoing_delivery_rate, 0.0)

        
        self.surplus.equation = self.inventory - self.backorder

        self.delivery_decision.equation = sd.min(self.lagging_backorder+self.incoming_order,self.lagging_inventory+self.incoming_delivery_rate)
        # Outgoing orders
        
        self.outgoing_orders_in.equation = self.actual_order
        
        
        self.outgoing_orders.equation = self.outgoing_orders_in
        
        
        self.total_outgoing_orders.equation = self.outgoing_orders_in + self.outgoing_orders

        
        self.naive_order_decision.equation = sd.max(
            policy_settings.weighting_inventory * (policy_settings.target_inventory-self.lagging_inventory) +
            policy_settings.weighting_backorder * self.lagging_backorder + self.incoming_order, 0.0
        )

        
        self.order_decision.equation = self.sophisticated_order_decision*policy_settings.sophisticated_order_decision_on+(1-policy_settings.sophisticated_order_decision_on)*self.naive_order_decision

        
        self.target_supply_line.equation = policy_settings.target_supply_line_factor * self.incoming_order

        
        self.target_total_stock.equation = self.target_supply_line + policy_settings.target_inventory

        
        self.making_orders.equation = self.order_decision

        
        self.order_delay.equation = 1.0


        self.sending_orders.equation = sd.delay(self, self.making_orders, self.order_delay, 100.0)

        
        self.order_line.setup_named_vector({"brewery": 100.0, "distributor": 100.0, "wholesaler": 100.0, "retailer": 100.0})
        self.order_line.equation = self.making_orders - self.sending_orders

        # Should use floor
        self.sophisticated_order_decision.equation = sd.max(self.total_incoming_orders + sd.round((self.target_supply_line + self.total_incoming_orders + self.total_outgoing_orders) / policy_settings.stock_adjustment_time, 0.0), 0.0)

Beergame()