#!/usr/bin/env python3

import json
import locale
import sys
import emails
import reports


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # handle max sales
    sales_by_model = {}

    for item in data:
      sales_by_model[item['total_sales']] = item['car']['car_make'] + " " + item['car']['car_model'] + " (" + str(item['car']['car_year']) + ")"

    most_sales = sorted(sales_by_model, reverse=True)[0]
    most_sales_model = sales_by_model[most_sales]

    # handle most popular car_year
    year_sales = {}

    for item in data:
      if item['car']['car_year'] in year_sales:
        year_sales[item['car']['car_year']]['count'] += 1
        year_sales[item['car']['car_year']]['sales'] += item['total_sales']
      else:
        year_sales[item['car']['car_year']] = {'count': 1, 'sales': item['total_sales']}

    most_popular_year = sorted(year_sales, key=lambda i : year_sales[i]['count'], reverse=True)[0]
    total_sales_year = year_sales[most_popular_year]['sales']

  summary = [
    "The {} generated the most revenue: ${} <br/>The {} had the most sales: {} <br/>The most popular year was {} with {} sales.".format(format_car(max_revenue["car"]), max_revenue["revenue"], most_sales_model, most_sales, most_popular_year, total_sales_year),
  ]

  return summary


def cars_dict_to_table(car_data):
  "Turns the data in car_data into a list of lists."
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = str(process_data(data)).replace("[", "").replace("]", "").replace("<br/>", "\n")
  print(summary)
  # turn this into a PDF report
  table_data = cars_dict_to_table(data)
  reports.generate("/tmp/cars.pdf", "Sales summary for last month", summary, table_data)

  # send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "student@example.com"
  subject = "Sales summary for last month"
  body = summary
  message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)
