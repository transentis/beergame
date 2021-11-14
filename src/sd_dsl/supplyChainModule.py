from BPTK_Py import sd_functions as sd
from .module import Module

class SupplyChainModule(Module):
    def __init__(self, model, name):
        super().__init__(model, name)
        # Exports
        self.sending_orders = self.model.flow(self.module_element("sending_orders"))
        self.outgoing_deliveries = self.model.flow(self.module_element("outgoing_deliveries"))

    def initialize(self, supplier, customer, policy_settings):
        # Stocks

        self.open_orders = self.model.stock(self.module_element("open_orders"))
        self.inventory = self.model.stock(self.module_element("inventory"))
        self.deliveries_made = self.model.stock(self.module_element("deliveries_made"))
        self.orders_received = self.model.stock(self.module_element("orders_received"))
        self.order_line = self.model.stock(self.module_element("order_line"))

        # Flows

        self.incoming_orders = self.model.flow(self.module_element("incoming_orders"))
        self.outgoing_orders = self.model.flow(self.module_element("outgoing_orders"))
        self.incoming_deliveries = self.model.flow(self.module_element("incoming_deliveries"))
        self.making_orders = self.model.flow(self.module_element("making_orders"))

        # Converters

        self.incoming_delivery_rate = self.model.converter(self.module_element("incoming_delivery_rate"))
        self.outgoing_delivery_rate = self.model.converter(self.module_element("outgoing_delivery_rate"))
        self.incoming_order_rate = self.model.converter(self.module_element("incoming_order_rate"))
        self.total_stock = self.model.converter(self.module_element("total_stock"))
        self.surplus = self.model.converter(self.module_element("surplus"))
        self.backorder = self.model.converter(self.module_element("backorder"))
        self.order_decision = self.model.converter(self.module_element("order_decision"))
        self.naive_order_decision = self.model.converter(self.module_element("naive_order_decision"))
        self.sophisticated_order_decision = self.model.converter(self.module_element("sophisticated_order_decision"))
        self.target_supply_line = self.model.converter(self.module_element("target_supply_line"))

        # Initial Values

        self.open_orders.initial_value = 200.0
        self.inventory.initial_value = 400.0
        self.deliveries_made.initial_value = 0.0
        self.incoming_orders.initial_value = 0.0
        self.order_line.initial_value = 100.0


        # Equations

        ## Inflows and Outflows

        self.open_orders.equation = self.outgoing_orders-self.incoming_deliveries
        self.inventory.equation = self.incoming_deliveries-self.outgoing_deliveries
        self.deliveries_made.equation = self.outgoing_deliveries
        self.orders_received.equation = self.incoming_orders
        self.order_line.equation = self.making_orders-self.sending_orders

        ## Flows and Rates
        self.total_stock.equation = self.open_orders+self.inventory
        self.surplus.equation = self.inventory - self.backorder
        self.backorder.equation = sd.max(self.orders_received-self.deliveries_made,0)

        self.incoming_orders.equation = self.incoming_order_rate
        self.incoming_order_rate.equation = customer.sending_orders

        self.outgoing_orders.equation = self.making_orders

        self.incoming_deliveries.equation = self.incoming_delivery_rate

        self.incoming_delivery_rate.equation = sd.delay(self.model,supplier.outgoing_deliveries,policy_settings.delivery_delay,100.0) if supplier is not None else None

        self.outgoing_deliveries.equation = sd.min(self.inventory+self.incoming_deliveries,self.outgoing_delivery_rate)
        self.outgoing_delivery_rate.equation = sd.min(self.backorder+self.incoming_orders,self.inventory+self.incoming_deliveries)

        self.making_orders.equation = self.order_decision
        self.sending_orders.equation = sd.delay(self.model,self.making_orders,policy_settings.order_delay, 100.0)

        ## Decision Policies

        self.target_supply_line.equation = self.incoming_order_rate*policy_settings.target_supply_line_factor

        ### Order Decision

        self.order_decision.equation = sd.If(policy_settings.sophisticated_order_decision_on == 1.0, self.sophisticated_order_decision,self.naive_order_decision)

        ### Naive Order Decision

        self.naive_order_decision.equation = policy_settings.target_inventory - self.inventory + self.backorder + self.incoming_order_rate

        ### Sophisticated Order Decision

        self.sophisticated_order_decision.equation = 1.0*sd.round((sd.max(self.incoming_order_rate+(policy_settings.target_inventory-self.inventory + policy_settings.weighting_open_orders*(self.target_supply_line-self.open_orders))/policy_settings.stock_adjustment_time,0.0)),0)














