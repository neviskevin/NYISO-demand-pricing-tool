# NYISO-demand-pricing-tool
## historical Data upload time is shown at the following links
## forecast is made at 9:30, pricing is next day 12am to 11pm and demand is the next 5 days
Demand[^1]    
Demand Forecast[^2]  
Price[^3]   
Price Forecast[^4]

navigate to directory where you can open ipynb files, clone into repository

> git clone https://github.com/neviskevin/NYISO-demand-pricing-tool.git

#demand.py
```python
x = 'palIntegrated' # or isolf
y = '20201101' # this is the date string
demandZip(x, y) # demand(x, y) should be used for days of current month
```

[^1]: http://mis.nyiso.com/public/P-58Clist.htm
[^2]: http://mis.nyiso.com/public/P-7list.htm
[^3]: http://mis.nyiso.com/public/P-24Alist.htm
[^4]: http://mis.nyiso.com/public/P-2Alist.htm
