import requests


def get_spn_price():
    response = requests.get('https://wax.alcor.exchange/api/markets/792')
    last_price = response.json()['last_price']
    rounded_lp = round(last_price, 4)
    return rounded_lp


def spin_price_main():
    return get_spn_price()


if __name__ == '__main__':
    spin_price_main()