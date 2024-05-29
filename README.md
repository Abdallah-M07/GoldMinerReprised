Crypto Tracker

This Goldminer repository contains a Python script that fetches the latest cryptocurrency prices from the CoinMarketCap API and displays them both in the console and as a bar chart. This project is ideal for anyone looking to quickly get started with using APIs, handling JSON data, and creating basic visualizations in Python.

Features
Retrieves the latest prices of the top 7 cryptocurrencies.
Displays prices in GBP.
Handles API errors gracefully.
Provides a graphical representation of cryptocurrency prices using a bar chart.

Output:

The script will print the latest prices of the top 7 cryptocurrencies in GBP to the console.
A bar chart displaying the prices will be shown.
Code Overview
get_crypto_data(): Fetches the latest cryptocurrency data from the CoinMarketCap API.
display_crypto_prices(data): Parses and prints the cryptocurrency prices.
plot_crypto_prices(symbols, prices): Plots a bar chart of the cryptocurrency prices.
main(): Main function to run the script
