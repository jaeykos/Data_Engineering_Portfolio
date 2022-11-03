## Project Description

   - Created [Tableau dashboard showing trading history of major Canadian Banks](https://public.tableau.com/views/StockTradingHistoryofMajorCanadianBanks/Dashboard1?:language=en-GB&publish=yes&:display_count=n&:origin=viz_share_link)
   - Written in Python with Pandas, and Pandassql 
   - Database: Google Sheets (Tableau Public only offers automatic data refresh on Google Sheets only)
   - Database is updated daily via with Task Scheduler, and Tableau Public autmatically retreives from database daily  
   - *1. Populate Stock Data (3yrs).ipynb* was ran initally to set up 3 years of trading history data into Google Sheet
   - *2. Update Stock Data (daily).py* is scheduled to run daily to append data and delete old data (keeps approxiamately 3 years of information)
