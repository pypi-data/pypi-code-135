"""
    starfish.provenance contract

"""
import json

from convex_api.contract import Contract

from convex_api.utils import (
    add_0x_prefix,
    to_address
)

from starfish.network.convex.convex_account import ConvexAccount
from starfish.types import AccountAddress


class ProvenanceContract(Contract):

    def register_provenance(self, asset_id: str, data: str, account: ConvexAccount):
        quote_data = Contract.escape_string(data)
        command = f'(register {add_0x_prefix(asset_id)} "{quote_data}")'
        result = self.send(command, account)
        if result and 'value' in result:
            return {
                'timestamp': result['value']['timestamp'],
                'owner': to_address(result['value']['owner']),
            }
        return result

    def event_list(self, asset_id: str, query_address: AccountAddress = None):
        command = f'(event-list {add_0x_prefix(asset_id)})'
        address = self.address
        if query_address:
            address = to_address(query_address)
        result = self.query(command, address)
        if result and 'value' in result:
            return ProvenanceContract.convert_event_list(result['value'])
        return result

    def owner_asset_list(self, owner_address: AccountAddress, query_address: AccountAddress = None):
        query_address_value = self.address
        if query_address:
            query_address_value = to_address(query_address)

        owner_address_value = to_address(owner_address)
        command = f'(owner-list {owner_address_value})'
        result = self.query(command, query_address_value)
        if result and 'value' in result:
            return result['value']
        return result

    def asset_list(self, query_address: AccountAddress = None):
        address = self.address
        if query_address:
            address = to_address(query_address)
        command = '(asset-list)'
        result = self.query(command, address)
        if result and 'value' in result:
            return result['value']
        return result

    @staticmethod
    def convert_event_list(items):
        event_list = []
        for item in items:
            json_data = item['data']
            try:
                json_data = json.loads(item['data'])
            except Exception as e:
                assert e
                pass
            event_list.append({
                'timestamp': item['timestamp'],
                'owner': to_address(item['owner']),
                'data': json_data,
            })
        return event_list
