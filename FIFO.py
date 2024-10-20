import pandas as pd

## Constants: Update name to match input file
DATA_NAME = "Test Fifo.xlsx"
OUTPUT_NAME = "Test Fifo Updated.xlsx"

## Read Excel file
data=pd.read_excel(DATA_NAME)

date = data["Date"].tolist()
cur_inventory = data["Purchases"].tolist()
cur_cost = data["Cost"].tolist()
cur_units_sold = data["Sales"].tolist()

## Create a copy of the sales column to display
sales_global = []

## fifo(listOf Num, listOf Num, listOf Num) -> listOf Num
## Requirements: All Nums must be positive
def fifo(inv, cost, units_sold):
    ret = []
    inv_index = 0
    for i in range(len(units_sold)):       
        ret.append(0)
        sales_global.append(units_sold[i])
        if units_sold[i] == 0:
            continue
        while units_sold[i] > 0:           
            temp = inv[0] - units_sold[i]
            if temp > 0:
                ret[i] += units_sold[i]*cost[inv_index]
                inv[inv_index] -= units_sold[i]
                units_sold[i] = 0

            elif temp == 0:
                ret[i] += units_sold[i]*cost[inv_index]
                inv_index += 1
                units_sold[i] = 0

            else:
                temp2 = units_sold[i]
                while temp2 > 0:
                    ret[i] += min(inv[inv_index],temp2) * cost[inv_index]
                    if temp2 >= inv[inv_index]:
                        temp2 -= inv[inv_index]
                        inv_index += 1
                    else:
                        inv[inv_index] -= temp2
                        temp2 = 0
                units_sold[i] = temp2

    return ret

## real_cost(listOf Num, listOf Num) -> listOf Num
## Requirements: all Nums must be positive
def real_cost(disposition, spot):
    ret = []
    for i in range(len(disposition)):
        ret.append(disposition[i]*spot[i])
    return ret

## gain(listOf Num, listOf Num, listOf Num) -> listOf Num
## Requirements: all Nums must be positive
def gain(disposition, spot, cost_basis):
    ret = []
    for i in range(len(disposition)):
        ret.append(0)
        if disposition[i] == 0:
            continue
        else:
            ret[i] = disposition[i]*spot[i] - cost_basis[i]
    return ret

fifo_cost = fifo(cur_inventory, cur_cost, cur_units_sold)

## Create dataframes for output and write to an Excel file
excel = {"Date":date, "Purchases":cur_inventory, "Dispositions":sales_global, "Cost":cur_cost, "Disposal ($$)":real_cost(sales_global, cur_cost), "Cost Basis":fifo_cost, "FX Gain/(Loss)":gain(sales_global, cur_cost, fifo_cost)}
exceldf = pd.DataFrame(excel)
exceldf.to_excel(OUTPUT_NAME)

