import requests

RARITIES = ['common', 'uncommon', 'rare', 'epic', 'legendary']


def getting_template_id(rarity):
    template_id_dict = {
        'common': 716922,
        'uncommon': 750023,
        'rare': 716924,
        'epic': 716925,
        'legendary': 716926
    }
    template_id = template_id_dict[rarity]
    response = requests.get(f'https://wax.api.atomicassets.io/atomicmarket/v2/sales?state=1&symbol=WAX&collection_name=spinniaworld&schema_name=spinney&template_id={template_id}&page=1&limit=100&order=asc&sort=price')
    null_check = []
    if null_check == response.json()['data']:
        lowest_listed = 'null'
        avg_ticket_cost = 'null'
        avg_pip_cost = 'null'
        return [lowest_listed, avg_ticket_cost, avg_pip_cost]
    lowest_listed_price = int(response.json()['data'][0]["listing_price"])
    lowest_listed = lowest_listed_price / 10 ** 8

    def getting_ticket_cost(cost):
        rarity_tickets_dict = {
            'common': 20,
            'uncommon': 40,
            'rare': 80,
            'epic': 160,
            'legendary': 320
        }
        ticket_amount = rarity_tickets_dict[rarity]
        final_cost = round((cost / ticket_amount), 2)
        return final_cost

    def getting_pip_value(cost):
        rarity_pip_dict = {
            'common': 120,
            'uncommon': 240,
            'rare': 480,
            'epic': 960,
            'legendary': 1920
        }
        pip_amount = rarity_pip_dict[rarity]
        final_cost = round((cost / pip_amount), 2)
        return final_cost
    return [lowest_listed, getting_ticket_cost(lowest_listed), getting_pip_value(lowest_listed)]


def creating_spinney_dictionary():
    spinney_dict = {}
    for rarity in RARITIES:
        values = [getting_template_id(rarity)]
        spinney_dict[rarity] = values
    return spinney_dict


def get_lowest_listed_rune_price(rarity):
    template_id_dict = {
        'common': 749979,
        'uncommon': 749981,
        'rare': 749982,
        'epic': 749983,
        'legendary': 749984
    }
    template_id = template_id_dict[rarity]
    response = requests.get(f'https://wax.api.atomicassets.io/atomicmarket/v2/sales?state=1&symbol=WAX&collection_name=spinniaworld&schema_name=runes&template_id={template_id}&page=1&limit=100&order=asc&sort=price')
    null_check = []
    if null_check == response.json()['data']:
        lowest_listed = 'null'
    else:
        lowest_listed_price = int(response.json()['data'][0]["listing_price"])
        lowest_listed = (lowest_listed_price / 10 ** 8)
    return lowest_listed


def creating_rune_dictionary():
    rune_dict = {}
    for rarity in RARITIES:
        values = [get_lowest_listed_rune_price(rarity)]
        rune_dict[rarity] = values
    return rune_dict


def main(command):
    commmand_dict = {
        "spinney": creating_spinney_dictionary(),
        "rune": creating_rune_dictionary()
    }
    what_do = commmand_dict[command]
    return what_do


if __name__ == '__main__':
    main()
# Script will not run unless activated with a main w/argument passed








