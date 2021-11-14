from .module import Module


class PolicySettings(Module):
    
    def __init__(self, model, name):
        super().__init__(model, name)
        # constants

        self.target_supply_line_factor = self.model.constant(self.module_element("target_supply_line_factor"))
        self.target_inventory = self.model.constant(self.module_element("target_inventory"))
        self.target_retailer_cost = self.model.constant(self.module_element("target_retailer_cost"))
        self.target_supply_chain_cost = self.model.constant(self.module_element("target_supply_chain_cost"))
        self.target_surplus = self.model.constant(self.module_element("target_surplus"))

        self.weighting_backorder = self.model.constant(self.module_element("weighting_backorder"))
        self.weighting_inventory = self.model.constant(self.module_element("weighting_inventory"))
        self.weighting_open_orders = self.model.constant(self.module_element("weighting_open_orders"))
        self.stock_adjustment_time = self.model.constant(self.module_element("stock_adjustment_time"))

        self.steady_state_on = self.model.constant(self.module_element("steady_state_on"))
        self.sophisticated_order_decision_on = self.model.constant(self.module_element("sophisticated_order_decision_on"))

        self.order_delay = self.model.constant(self.module_element("order_delay"))
        self.delivery_delay = self.model.constant(self.module_element("delivery_delay"))
        self.rise_in_consumer_order = self.model.constant(self.module_element("rise_in_consumer_order"))

        # Equations

        self.target_supply_line_factor.equation = 2.0
        self.target_inventory.equation = 400.0
        self.target_retailer_cost.equation = 8300.0
        self.target_supply_chain_cost.equation = 29300.0
        self.target_surplus.equation = 250.0

        self.weighting_backorder.equation = 1.0
        self.weighting_inventory.equation = 1.0
        self.weighting_open_orders.equation = 1.0
        self.stock_adjustment_time.equation = 8.0

        self.steady_state_on.equation = 0.0
        self.sophisticated_order_decision_on.equation = 0.0

        self.order_delay.equation = 1.0
        self.delivery_delay.equation = 1.0
        self.rise_in_consumer_order.equation = 300.0





