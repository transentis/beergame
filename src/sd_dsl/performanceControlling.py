from BPTK_Py import sd_functions as sd
from .module import Module


class PerformanceControlling(Module):

    def __init__(self, model,name):
        super().__init__(model,name)

    def initialize(self,brewery, distributor, wholesaler, retailer, policy_settings):
        # Stocks

        total_retailer_cost = self.model.stock(self.module_element("total_retailer_cost"))
        total_supply_chain_cost = self.model.stock(self.module_element("total_supply_chain_cost"))

        # Flows

        retailer_cost_in = self.model.flow(self.module_element("retailer_cost_in"))
        supply_chain_cost_in = self.model.flow(self.module_element("supply_chain_cost_in"))

        # Converters

        ## Brewery

        brewery_cost = self.model.converter(self.module_element("brewery_cost"))
        brewery_backorder_cost = self.model.converter(self.module_element("brewery_backorder_cost"))
        brewery_inventory_cost = self.model.converter(self.module_element("brewery_inventory_cost"))

        ## Distributor

        distributor_cost = self.model.converter(self.module_element("distributor_cost"))
        distributor_backorder_cost = self.model.converter(self.module_element("distributor_backorder_cost"))
        distributor_inventory_cost = self.model.converter(self.module_element("distributor_inventory_cost"))

        ## Wholesaler

        wholesaler_cost = self.model.converter(self.module_element("wholesaler_cost"))
        wholesaler_backorder_cost = self.model.converter(self.module_element("wholesaler_backorder_cost"))
        wholesaler_inventory_cost = self.model.converter(self.module_element("wholesaler_inventory_cost"))

        ## Retailer

        retailer_cost = self.model.converter(self.module_element("retailer_cost"))
        retailer_backorder_cost = self.model.converter(self.module_element("retailer_backorder_cost"))
        retailer_inventory_cost = self.model.converter(self.module_element("retailer_inventory_cost"))

        ## Supply Chain

        supply_chain_cost = self.model.converter(self.module_element("supply_chain_cost"))

        # Constants

        ## Supply Chain

        cost_per_item_in_backorder = self.model.constant(self.module_element("cost_per_item_in_backorder"))
        cost_per_item_in_inventory = self.model.constant(self.module_element("cost_per_item_in_inventory"))

        # Equations



        ## Supply Chain

        cost_per_item_in_inventory.equation = 0.5
        cost_per_item_in_backorder.equation = 1.0

        supply_chain_cost.equation = brewery_cost + retailer_cost + distributor_cost + wholesaler_cost
        supply_chain_cost_in.equation = supply_chain_cost

        total_supply_chain_cost.equation = supply_chain_cost_in
        ## Brewery*

        brewery_cost.equation = brewery_backorder_cost+brewery_inventory_cost
        brewery_backorder_cost.equation = cost_per_item_in_backorder*brewery.backorder
        brewery_inventory_cost.equation = cost_per_item_in_inventory*sd.max(brewery.inventory,policy_settings.target_inventory)

        ## Distributor

        distributor_cost.equation = distributor_backorder_cost+distributor_inventory_cost
        distributor_backorder_cost.equation = cost_per_item_in_backorder*distributor.backorder
        distributor_inventory_cost.equation = cost_per_item_in_inventory*sd.max(distributor.inventory,policy_settings.target_inventory)

        ## Wholesaler

        wholesaler_cost.equation = wholesaler_backorder_cost+wholesaler_inventory_cost
        wholesaler_backorder_cost.equation = cost_per_item_in_backorder*wholesaler.backorder
        wholesaler_inventory_cost.equation = cost_per_item_in_inventory*sd.max(wholesaler.inventory,policy_settings.target_inventory)

        ## Retailer

        retailer_cost.equation = retailer_backorder_cost+retailer_inventory_cost
        retailer_backorder_cost.equation = cost_per_item_in_backorder*retailer.backorder
        retailer_inventory_cost.equation = cost_per_item_in_inventory*sd.max(retailer.inventory,policy_settings.target_inventory)

        retailer_cost_in.equation = retailer_cost
        total_retailer_cost.equation = retailer_cost_in