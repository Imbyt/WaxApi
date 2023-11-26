import requests


def getting_rarity(rarity):
    if rarity == "common":
        common = 716922
        return common
    elif rarity == "uncommon":
        uncommon = 750023
        return uncommon


def getting_ticket_cost(rarity, cost):
    if rarity == "common":
        ticket_cost = str(cost/20)
        return ticket_cost
    elif rarity == "uncommon":
        ticket_cost = str(cost/40)
        return ticket_cost


input_rarity = input("rarity")

# here I am calling getting_rarity to get the correct template id to pass into my api address
template_id = getting_rarity(input_rarity)
response = requests.get(f'https://wax.api.atomicassets.io/atomicmarket/v1/prices/templates?collection_name=spinniaworld&schema_name=spinney&template_id={template_id}&burned=false&symbol=WAX&page=1&limit=100&order=desc')
median = int(response.json()['data'][0]["suggested_median"])
# correcting the number
suggested_median = (median/10**8)
# here I am passing the initial rarity input and suggested medium after api call to get an avg ticket price
avg_ticket_cost = getting_ticket_cost(input_rarity, suggested_median)

print(f'{input_rarity} is currently on average {suggested_median} wax!')
print(f'{input_rarity} tickets cost on avg {avg_ticket_cost}!')
