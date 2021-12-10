# NYISO-demand-pricing-tool
### Historical Data upload time is shown at the following links
Demand[^1]    
Demand Forecast[^2]  
   -  made at 9:30 for the next 5 days   

Price[^3]   
Price Forecast[^4]  
   -  made at 9:30 for next day 12am to 11pm   

### Clone into Repository
> git clone https://github.com/neviskevin/NYISO-demand-pricing-tool.git

### demand.py
```python
x = 'palIntegrated' # Gives realtime. Use 'isolf' for day ahead
y = '20201101' # this is the date string
demandZip(x, y) # demand(x, y) should be used for days of current month
```

[^1]: http://mis.nyiso.com/public/P-58Clist.htm
[^2]: http://mis.nyiso.com/public/P-7list.htm
[^3]: http://mis.nyiso.com/public/P-24Alist.htm
[^4]: http://mis.nyiso.com/public/P-2Alist.htm
