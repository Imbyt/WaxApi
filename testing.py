import requests


class Spinney:
    def __init__(self, rarity, template_id, tickets, pap):
        self.rarity = rarity
        self.template_id = template_id
        self.cost = self.template_price()
        self.tickets = tickets
        self.pap = pap

    def template_price(self):
        response = requests.get(f'https://wax.api.atomicassets.io/atomicmarket/v2/sales?state=1&symbol=WAX&collection_name=spinniaworld&schema_name=spinney&template_id={self.template_id}&page=1&limit=100&order=asc&sort=price')
        lowest_listed_price = int(response.json()['data'][0]["listing_price"])
        lowest_listed = lowest_listed_price / 10 ** 8
        return lowest_listed

    def calc_tickets(self):
        avg_tickets = self.cost / self.tickets
        return avg_tickets

    def calc_pap(self):
        avg_pap = self.cost / self.pap
        return avg_pap


# ive pretty much built a dictionary here that I can call to with main using Spinney Class

common_spinney = Spinney("common", 716922, 20, 120)
uncommon_spinney = Spinney("common", 716922, 20, 120)
rare_spinney = Spinney("common", 716922, 20, 120)
epic_spinney = Spinney("common", 716922, 20, 120)
legendary_spinney = Spinney("common", 716922, 20, 120)

# in main I should have a label call to specific function defined within the class, also solves the problem of displaying the information correctly and where I would like
# when creating template_price I realized why we put self.rarity = rarity i.e.
