import requests
from tkinter import *


def getting_template_id(rarity):
    template_id_dict = {
        'common': 716922,
        'uncommon': 750023,
        'rare': 716924,
        'epic': 716925,
        'legendary': 716926
    }
    template_id = template_id_dict[rarity]
    return template_id

def getting_ticket_cost(rarity, cost):
    rarity_tickets_dict = {
        'common': 20,
        'uncommon': 40,
        'rare': 80,
        'epic': 160,
        'legendary': 320
    }
    ticket_amount = rarity_tickets_dict[rarity]
    final_cost = (cost/ticket_amount)
    return final_cost


def getting_pip_value(rarity, cost):
    rarity_pip_dict = {
        'common': 120,
        'uncommon': 240,
        'rare': 480,
        'epic': 960,
        'legendary': 1920
    }
    pip_amount = rarity_pip_dict[rarity]
    final_cost = (cost / pip_amount)
    return final_cost

def main():
    rarities = ("common", "uncommon", "rare", "epic", "legendary")
    for rarity in rarities:
        template_id = getting_template_id(rarity)
        response = requests.get(f'https://wax.api.atomicassets.io/atomicmarket/v1/prices/templates?collection_name=spinniaworld&schema_name=spinney&template_id={template_id}&burned=false&symbol=WAX&page=1&limit=100&order=desc')
        median = int(response.json()['data'][0]["suggested_median"])
        suggested_median = (median / 10 ** 8)
        avg_ticket_cost = getting_ticket_cost(rarity, suggested_median)
        avg_pip_cost = getting_pip_value(rarity, suggested_median)
        value_set = []
        values = [rarity.capitalize(), suggested_median, avg_ticket_cost, avg_pip_cost]
    for rarity in rarities:
        value_set.extend(values)
    return value_set


#       print(f'{x.capitalize()} is currently on average {suggested_median} WAX.')
#       print(f'{x.capitalize()} have a ticket cost on avg {avg_ticket_cost} WAX.')
#       print(f'{x.capitalize()} have a pip cost on avg of {avg_pip_cost} WAX.')


if __name__ == '__main__':
    main()









