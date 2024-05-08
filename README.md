Files in Repository
- budget.py: This file contains the main classes for managing expenses data. It includes the BudgetManager class for tracking finances, providing analytics,
  and giving recommendations. It also contains the Visualization class for visualizing total expenses.
- budgetfile.csv: This CSV file contains sample budget data used by the budget.py program. It includes columns such as date, category, month, spending, location, and income.

Running the Program
- You can run this program in the command line. Navigate to the directory/folder where budget.py and budgetfile.csv are located. The program takes one command line
  argument, the csv file. Enter the following in the command line to run the program: python budget.py budgetfile.csv

Interpreting the Output
-You will see results such as Expenses by category, Analytics for {month}, and Analytics for {location} in a dictionary, where the key is the category of spending, and the 
value is the aggregate amount spent in that category. You will also see a recommendation statement based on your spending habit (if income is greater than expenses and vice
versa).
- You will also see a bar chart visualizing your expenses across all different categories

Attribution



| Method/function | Primary author | Techniques demonstrated  |
| ------------- |:-------------:| -----:|
| parse_currency     | Deborah Alain | conditional statement |
| total_expenses   | Deborah      |  conditional statement  |
| spending_by_category | Cullen Kweti      | key function |
| analytics_by_month | Cullen |  groupby() operation in Pandas |
| analytics_by_location | Dagem Legesse |  groupby() operation in Pandas |
| recommendations | Dagem | conditional expression |
| plot_expenses_by_category | Robert Dang | data visualization with pyplot |
| __name__ == "main" | Robert | ArgumentParser class, f-strings containing expressions |




