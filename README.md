# End assignment python course .
## Supermarket tool

### Explanation of the supermarket tool:

By just using the command line, the inventory of the supermarket can be managed. Also, functions for buying product, selling products and making reports are included. 

* * *
The functions of this tool include:
* Buying products;
* Selling products;
* Have insight in the inventory;
* Have insight in the expiring dates of the products;
* Calculate the profit;
* Calculate the revenue;
* Exporting the above automatically in a .csv file;
* Exporting the above automatically in a .pdf file.
* * *

## Below, all the functions and how they work are explained
---
### Help in the command line:
---
For explanation of the tool and an helpful menu, use the following arguments:
>```
>Type in command line: py main.py -h 
> arguments -h or --help will show the following:

>arguments:
> for buying products, selling products and making reports:
>    buy    : Add the bought products to stock
>    report : Make a report 
>    sell   : Provide the sold item
>
>```

### The buying products function to fill the stock:
For explanation of the buying products function use the following arguments:
>```
> Type in command line: py main.py buy   , with the following possible sub-arguments:
> -h or --help               : Showing the following:
> -p or --product            : Fill in the name of the bought product
> -a or --amount             : How many items are bought?
> -bp or -- buy_price        : Fill in the price per bought item. e.g. 1.50 euro: 1.50
> -exp or -- expiration_date : Fill in the expiration date of the product as dd-mm-yyyy
> -d or --date               : Fill in the date of the transaction when it's on a different day than today.
>                              Type -d and the date as dd-mm-yyy. For example: py main.py buy -d 29-05-2021
>``` 
### The selling function to remove from stock:
For explanation of the selling products function use the following arguments:
>```
> Type in command line: py main.py sell -h  , with the following possible sub-arguments: 
> -h or --help               : Showing the following:
> -p or --product            : Fill in the name of the sold product
> -a or --amount             : How many products are sold?
> -sp or -sell_price         : Fill in the price the item is sold for. e.g. 2.75 euro: 2.75
> The selling function does not consider selling on a different day than today.
>```
### The 'make a report' function:
The report function is divided in certain steps. 
>```
> Type in command line: py main.py report
>```

After, the following sub-arguments are possible:
    * Inventory       : Shows the stock inventory of the supermarket
    * Revenue         : Calculates and shows the revenue, based on the bought and sold items
    * Profit          : Calculates and shows the profit, based on the sold items
    * Expiration dates: Shows the expiration dates of the products in stock, and shows when they are expired
    
The report of the the above mentioned sub-arguments can be given for:
    * Today
    * Yesterday
    * Last week
    * On a specific date

For example: To make a report about the profit made on 22-05-2021, the following input should be given in the command line:
>```
> py main.py report profit -d 22-05-2021
>```

To export the the reports to a .csv file (named 'report.csv') the input '-f true' should be given in the command line:
>```
> py main.py report profit -d 22-05-2021 -f true
>```

To export the reports into a .pdf file (named 'report.pdf') the inpit '-pdf true' should be given as last in the command line:
>```
> py main.py report profit -d 22-05-2021 -f true -pdf true
>```

## Following, some possible inputs and their results will be given:
To buy (and add to the stock of the supermarket) 500 beers, bought for 1.00 each which expire on 29-12-2021, you will need to type the following in the command line:
>```
> py main.py buy -p beer -bp 1.00 -exp 29-12-2021
>```

To sell (and remove from the stock of the supermarket) 200 beers, sold for 3.00 each, you will need to type the following in the command line:
>```
> py main.py sell -p beer -sp 3.00 -a 200
>```

To get a report about the inventory of the supermarket today, yesterday, lastweek or on a specific date,
exported to and .csv file and a .pdf file, you will need to type the following in the command line:
>```
> py main.py report inventory today -f true -pdf true
>```

>```
> py main.py report inventory yesterday -f true -pdf true
>```

>```
> py main.py report inventory lastweek -f true -pdf true
>```

>```
> py main.py report inventory date -d 22-05-2021 -f true -pdf true
>```

To make a report about the revenue of the supermarket, you will need to type the following in the command line:
>```
> py main.py report revenue today
>```
The above ofcourse is for today, but can be replaced with any of the date arguments as mentioned in the inventory report example.


To make a report about the profit of the supermarket, you will need to type the following in the command line:
>```
> py main.py report profit today
>```

To make a report about the expiration dates of the products in stock, the following needs to be typed in the command line:
>```
> py main.py report expdates today
>```

To see which products will be expired in the future, let's say 02-06-2021, the following needs to be typed in the command line:
>```
> py main.py report expdates date -d 02-06-2021
>```

***
## The following modules and versions are used in this tool:
### reportlab ,      version 3.5.59
### rich ,           version 9.8.2
### prettytable,     version 2.0.0
### python-dateutil, version 2.8.1
***
