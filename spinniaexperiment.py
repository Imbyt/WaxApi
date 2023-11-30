import requests
from tkinter import *



def main():
    def getting_rarity(rarity):
        if rarity == "common":
            common = 716922
            return common
        elif rarity == "uncommon":
            uncommon = 750023
            return uncommon
        elif rarity == "rare":
            rare = 716924
            return rare
        elif rarity == "epic":
            epic = 716925
            return epic
        elif rarity == "legendary":
            legendary = 716926
            return legendary


    def getting_ticket_cost(rarity, cost):
        if rarity == "common":
            ticket_cost = str(cost / 20)
            return ticket_cost
        elif rarity == "uncommon":
            ticket_cost = str(cost / 40)
            return ticket_cost
        elif rarity == "rare":
            ticket_cost = str(cost / 80)
            return ticket_cost
        elif rarity == "epic":
            ticket_cost = str(cost / 160)
            return ticket_cost
        elif rarity == "legendary":
            ticket_cost = str(cost / 160)
            return ticket_cost


    def getting_pip_value(rarity, cost):
        if rarity == "common":
            pip_cost = str(cost / 120)
            return pip_cost
        elif rarity == "uncommon":
            pip_cost = str(cost / 240)
            return pip_cost
        elif rarity == "rare":
            pip_cost = str(cost / 480)
            return pip_cost
        elif rarity == "epic":
            pip_cost = str(cost / 960)
            return pip_cost
        elif rarity == "legendary":
            pip_cost = str(cost / 1920)
            return pip_cost


    rarities = ("common", "uncommon", "rare", "epic", "legendary")
    for rarities in rarities:
        # here I am calling getting_rarity to get the correct template id to pass into my api address
        template_id = getting_rarity(rarities)
        response = requests.get(f'https://wax.api.atomicassets.io/atomicmarket/v1/prices/templates?collection_name=spinniaworld&schema_name=spinney&template_id={template_id}&burned=false&symbol=WAX&page=1&limit=100&order=desc')
        median = int(response.json()['data'][0]["suggested_median"])
        # correcting the number
        suggested_median = (median / 10 ** 8)
        # here I am passing the initial rarity input and suggested medium after api call to get an avg ticket price
        avg_ticket_cost = getting_ticket_cost(rarities, suggested_median)
        avg_pip_cost = getting_pip_value(rarities, suggested_median)
        values = [rarities.capitalize(), suggested_median, avg_ticket_cost, avg_pip_cost]
        return values


#       print(f'{x.capitalize()} is currently on average {suggested_median} WAX.')
#       print(f'{x.capitalize()} have a ticket cost on avg {avg_ticket_cost} WAX.')
#       print(f'{x.capitalize()} have a pip cost on avg of {avg_pip_cost} WAX.')


if __name__ == '__main__':
    main()










