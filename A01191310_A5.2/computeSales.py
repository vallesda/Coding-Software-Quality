import time
import sys
import json

def generate_prices(products):
    """Generates map for prices"""
    prices = {}
    for product in products:
        title = product["title"]
        price = product["price"]
        if title and price:
            prices[title] = price
    return prices

def count_sales(sales, prices):
    """Counts all sales from records"""
    total_sales = 0.0
    for sale in sales:
        try:
            key = sale["Product"]
            quant = sale["Quantity"]
            if (key and quant) and key in prices:
                price = prices[key]
                total_sales += (price * quant)
        except ValueError:
            print(f"Error: Value for item not found: {ValueError}")
    return total_sales

def reads_json(filename):
    """Reads json in file provided by user"""
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"Error: File not found in path: {filename}")
    return None

def write_answers(total_sales, elapse_time):
    """Writes answer in file"""
    file_path = 'SalesResults.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Sales: {total_sales} \n")
        file.write(f"Elapsed-Time: {elapse_time}")

def main():
    """Computes Sales"""
    start_time = time.time()

    if len(sys.argv) != 3:
        print("Usage: python script.py <catalogue> <record>")
        sys.exit(1)

    price_catalogue = sys.argv[1]
    sales_record = sys.argv[2]

    catalogue_json = reads_json(price_catalogue)
    sales_json = reads_json(sales_record)
    total_sales = 0.0
    if catalogue_json and sales_json:
        prices = generate_prices(catalogue_json)
        total_sales = count_sales(sales_json, prices)
        print(f"Sales: {total_sales}\n")

    end_time = time.time()

    elapse_time = end_time - start_time
    write_answers(total_sales, elapse_time)
    print(f"Elapsed Time: {elapse_time}")


if __name__ == "__main__":
    main()
