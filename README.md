# NYISO-demand-pricing-tool

Demand[^1]
Demand Forecast: http://mis.nyiso.com/public/P-7list.htm
Price: http://mis.nyiso.com/public/P-24Alist.htm
Price Forecast: http://mis.nyiso.com/public/P-2Alist.htm

navigate to directory where you can open ipynb files, clone into repository

> git clone https://github.com/neviskevin/NYISO-demand-pricing-tool.git

```python
x = 'palIntegrated' # or isolf
y = '20201101' # this is the date string
demandZip(x, y) # demand(x, y) should be used for days of current month
```
Here is a simple footnote.

A footnote can also have multiple lines[^2].  

You can also use words, to fit your writing style more closely[^note].

[^1]: http://mis.nyiso.com/public/P-58Clist.htm
[^2]: Every new line should be prefixed with 2 spaces.  
  This allows you to have a footnote with multiple lines.
[^note]:
    Named footnotes will still render with numbers instead of the text but allow easier identification and linking.  
    This footnote also has been made with a different syntax using 4 spaces for new lines.
