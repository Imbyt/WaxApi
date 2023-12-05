import requests


class Spinney:
    def __init__(self, template_id, tickets, pap):
        self.template_id = template_id
        self.tickets = tickets
        self.pap = pap
        self.cost = self.template_price()

    def template_price(self):
        response = requests.get(f'https://wax.api.atomicassets.io/atomicmarket/v2/sales?state=1&symbol=WAX&collection_name=spinniaworld&schema_name=spinney&template_id={self.template_id}&page=1&limit=100&order=asc&sort=price')
        lowest_listed_price = int(response.json()['data'][0]["listing_price"])
        lowest_listed = lowest_listed_price / 10 ** 8
        return lowest_listed

    def calc_tickets(self):
        avg_tickets = round((self.cost / self.tickets), 2)
        return avg_tickets

    def calc_pap(self):
        avg_pap = round((self.cost / self.pap), 2)
        return avg_pap


class Rune:
    def __init__(self, template_id):
        self.template_id = template_id

    def template_price(self):
        response = requests.get(f'https://wax.api.atomicassets.io/atomicmarket/v2/sales?state=1&symbol=WAX&collection_name=spinniaworld&schema_name=runes&template_id={self.template_id}&page=1&limit=100&order=asc&sort=price')
        lowest_listed_price = int(response.json()['data'][0]["listing_price"])
        lowest_listed = lowest_listed_price / 10 ** 8
        return lowest_listed


spinney_dict = {
    "common": Spinney(716922, 20, 120),
    "uncommon": Spinney(750023, 40, 240),
    "rare": Spinney(716924, 80, 480),
    "epic": Spinney(716925, 160, 960),
    "legendary": Spinney(716926, 320, 1920)
}

rune_dict = {
    "common": Rune(749979),
    "uncommon": Rune(749981),
    "rare": Rune(749982),
    "epic": Rune(749983),
    "legendary": Rune(749984)
}


def get_rune(rarity):
    return Rune.template_price(rune_dict[rarity])


def price(rarity):
    spinney = spinney_dict[rarity]
    return spinney.template_price()


def tickets(rarity):
    spinney = spinney_dict[rarity]
    return spinney.calc_tickets()


def pap(rarity):
    spinney = spinney_dict[rarity]
    return spinney.calc_pap()


# in main I should have a label call to specific function defined within the class, also solves the problem of displaying the information correctly and where I would like
# when creating template_price I realized why we put self.rarity = rarity i.e.
