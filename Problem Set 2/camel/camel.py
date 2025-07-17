import requests
import sys

def main():
    try:
        value = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        result = response.json()
        price = result["bpi"]["USD"]["rate_float"]
        amount = price*value
        print(f"${amount :,.4f}")

    except IndexError:
        sys.exit("Missing command-line argument")

    except ValueError:
        sys.exit("Command-line argument is not a number")

    except requests.RequestException:
        sys.exit()


main()

