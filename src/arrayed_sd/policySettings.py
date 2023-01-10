from BPTK_Py import Module


class PolicySettings(Module):
    
    def __init__(self, model, name):
        super().__init__(model, name)
        self.target_supply_line_factor = self.converter("target_supply_line_factor")
        self.target_supply_line_factor.equation = 1.0
        
        self.target_inventory = self.converter("target_inventory")
        self.target_inventory.equation = 400.0

        self.weighting_backorder = self.converter("weighting_backorder")
        self.weighting_backorder.equation = 1.0
        
        self.weighting_inventory = self.converter("weighting_inventory")
        self.weighting_inventory.equation = 1.0
        
        self.weighting_open_orders = self.converter("weighting_open_orders")
        self.weighting_open_orders.equation = 1.0
        
        self.stock_adjustment_time = self.converter("stock_adjustment_time")
        self.stock_adjustment_time.equation = 8.0
        

        self.target_retailer_cost = self.converter("target_retailer_cost")
        self.target_retailer_cost.equation = 7800.0

        self.target_supply_chain_cost = self.converter("target_supply_chain_cost")
        self.target_supply_chain_cost.equation = 29300.0

        self.target_surplus = self.converter("target_surplus")
        self.target_surplus.equation = 400.0


        self.sophisticated_order_decision_on = self.converter("sophisticated_order_decision_on")
        self.sophisticated_order_decision_on.equation = 0.0

        self.multiplayer_mode_on = self.converter("multiplayer_mode_on")
        self.multiplayer_mode_on.equation = 0.0

        self.game_mode_on = self.converter("game_mode_on")
        self.game_mode_on.equation = 0.0

        self.steady_state_on = self.converter("steady_state_on")
        self.steady_state_on.equation = 0.0
