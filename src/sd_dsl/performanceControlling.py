from BPTK_Py import sd_functions as sd
from .module import Module


class PerformanceControlling(Module):

    def __init__(self, model,name):
        super().__init__(model,name)

    def initialize(self,brewery, distributor, wholesaler, retailer, policy_settings):
        # Stocks

        self.total_retailer_cost = self.model.stock(self.module_element("total_retailer_cost"))
        self.total_supply_chain_cost = self.model.stock(self.module_element("total_supply_chain_cost"))

        # Flows

        self.retailer_cost_in = self.model.flow(self.module_element("retailer_cost_in"))
        self.supply_chain_cost_in = self.model.flow(self.module_element("supply_chain_cost_in"))

        # Converters

        ## Brewery

        self.brewery_cost = self.model.converter(self.module_element("brewery_cost"))
        self.brewery_backorder_cost = self.model.converter(self.module_element("brewery_backorder_cost"))
        self.brewery_inventory_cost = self.model.converter(self.module_element("brewery_inventory_cost"))

        ## Distributor

        self.distributor_cost = self.model.converter(self.module_element("distributor_cost"))
        self.distributor_backorder_cost = self.model.converter(self.module_element("distributor_backorder_cost"))
        self.distributor_inventory_cost = self.model.converter(self.module_element("distributor_inventory_cost"))

        ## Wholesaler

        self.wholesaler_cost = self.model.converter(self.module_element("wholesaler_cost"))
        self.wholesaler_backorder_cost = self.model.converter(self.module_element("wholesaler_backorder_cost"))
        self.wholesaler_inventory_cost = self.model.converter(self.module_element("wholesaler_inventory_cost"))

        ## Retailer

        self.retailer_cost = self.model.converter(self.module_element("retailer_cost"))
        self.retailer_backorder_cost = self.model.converter(self.module_element("retailer_backorder_cost"))
        self.retailer_inventory_cost = self.model.converter(self.module_element("retailer_inventory_cost"))

        ## Supply Chain

        self.supply_chain_cost = self.model.converter(self.module_element("supply_chain_cost"))

        # Constants

        ## Supply Chain

        self.cost_per_item_in_backorder = self.model.constant(self.module_element("cost_per_item_in_backorder"))
        self.cost_per_item_in_inventory = self.model.constant(self.module_element("cost_per_item_in_inventory"))

        # Equations



        ## Supply Chain

        self.cost_per_item_in_inventory.equation = 0.5
        self.cost_per_item_in_backorder.equation = 1.0

        self.supply_chain_cost.equation = self.brewery_cost + self.retailer_cost + self.distributor_cost + self.wholesaler_cost
        self.supply_chain_cost_in.equation = self.supply_chain_cost

        self.total_supply_chain_cost.equation = self.supply_chain_cost_in
        ## Brewery*

        self.brewery_cost.equation = self.brewery_backorder_cost+self.brewery_inventory_cost
        self.brewery_backorder_cost.equation = self.cost_per_item_in_backorder*brewery.backorder
        self.brewery_inventory_cost.equation = self.cost_per_item_in_inventory*sd.max(brewery.inventory,policy_settings.target_inventory)

        ## Distributor

        self.distributor_cost.equation = self.distributor_backorder_cost+self.distributor_inventory_cost
        self.distributor_backorder_cost.equation = self.cost_per_item_in_backorder*distributor.backorder
        self.distributor_inventory_cost.equation = self.cost_per_item_in_inventory*sd.max(distributor.inventory,policy_settings.target_inventory)

        ## Wholesaler

        self.wholesaler_cost.equation = self.wholesaler_backorder_cost+self.wholesaler_inventory_cost
        self.wholesaler_backorder_cost.equation = self.cost_per_item_in_backorder*wholesaler.backorder
        self.wholesaler_inventory_cost.equation=self.cost_per_item_in_inventory*sd.max(wholesaler.inventory,policy_settings.target_inventory)

        ## Retailer

        self.retailer_cost.equation = self.retailer_backorder_cost+self.retailer_inventory_cost
        self.retailer_backorder_cost.equation = self.cost_per_item_in_backorder*retailer.backorder
        self.retailer_inventory_cost.equation=self.cost_per_item_in_inventory*sd.max(retailer.inventory,policy_settings.target_inventory)

        self.retailer_cost_in.equation = self.retailer_cost
        self.total_retailer_cost.equation = self.retailer_cost_in