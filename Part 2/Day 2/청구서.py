invoice = """
0.....6.................................40....
1909  Pimoroni PiBrella                 $17.50
1910  Fimoroni FiCrella                 $20.50
"""

SKU = slice(0,6)
DESCRIPTION = slice(6,40)
UNIT_PRICE = slice(40, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[SKU],item[DESCRIPTION], item[UNIT_PRICE])