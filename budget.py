import pandas as pd
import argparse
import matplotlib.pyplot as plt

class BudgetManager:
    """
    Class that tracks your finances, provides analytics based on monthly spending
    and spending based on location, and gives suggestions on spending habits.
    """
    def __init__(self, filename, delimiter=','):
        """
        Creates new instance for the BudgetManager class 

        Args:
            filename (str): Path to the CSV file
            delimiter (str): Character separating values
        """
        self.filename = filename
        self.data = pd.read_csv(filename, delimiter=delimiter)

    def parse_currency(self, value):
        """
        Parses and converts a currency that is a string into a float

        Args:
            value (str or float): The currency value

        Returns:
            float: The value of the currency as a float
        """
        if isinstance(value, str):
            return float(value.replace('$', '').replace(',', ''))
        return value

    def total_expenses(self):
        """
        Calculates total expenses across all categories

        Returns:
            dict: keys as categories and values as corresponding total spendings
        """
        expenses_by_category = {}
        for _, row in self.data.iterrows():
            category = row['category']
            spending = self.parse_currency(row['spending'])
            if category not in expenses_by_category:
                expenses_by_category[category] = 0
            expenses_by_category[category] += spending
        return expenses_by_category


    def spending_by_category(self, category):
        """
        Calculate the total spending for a specified category
        
        Args:
        category (str): The category for which the total spending needs to be 
        calculated.
        """
        total_spending = 0
        for _, row in self.data.iterrows():
            if row['category'] == category:
                total_spending += self.parse_currency(row['spending'])
        return total_spending

    def analytics_by_month(self, month):
        """
        Provides a summary of expenses grouped by category for a specified month
    
        Args:
        month (str): The month for which we want expenses to be calculated
    
        Returns:
        dict: A dictionary where keys are categories and values are the summed 
        spending amounts for the specified month.
        """
        month_data = self.data[self.data['month'] == month]
        month_data.loc[:, 'spending'] = month_data['spending'].apply(self.parse_currency)
        expenses_by_category = month_data.groupby('category')['spending'].sum().to_dict()
        return expenses_by_category

   
    def analytics_by_location(self, location):
        """
        Tracks spending by location

        Parameters:
            location (str): location of individual
        
        Returns: dictionary 
        """
        location_data = self.data[self.data['location'] == location]
        location_data['spending'] = location_data['spending'].apply(self.parse_currency)
        expenses_by_location = location_data.groupby('category')['spending'].sum().to_dict()
        return expenses_by_location


    def recommendations(self):
        """
        Gives recommendations based on total expenses and total income

        Returns:
            str: statement that instructs user based on if they are 
            overspending or not
        """
        total_income = self.parse_currency(self.data['income'].sum())
        total_expenses = self.parse_currency(self.data['spending'].sum())
        return "Consider reducing your expenses." if total_expenses > total_income else "Your spending is within your income. Good job!"



class Visualization:
    "A class for visualizing your total expenses."
    def __init__(self, data):
        self.data = data

    def plot_expenses_by_category(self):
        """
        Plot total expenses by category as a bar chart

        """
        expenses_data = self.data.total_expenses()
        categories = list(expenses_data.keys())
        values = list(expenses_data.values())
        plt.bar(categories, values)
        plt.xlabel('Category')
        plt.ylabel('Spending ($)')
        plt.title('Expenses by Category')
        plt.xticks(rotation=90)
        plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    budget_manager = BudgetManager(args.filename)
    print("Expenses by category:", budget_manager.total_expenses())
    print("Analytics for January:", budget_manager.analytics_by_month('January'))
    print("Analytics for New York:", budget_manager.analytics_by_location('New York'))
    print("Spending in Home & Utilities category:", budget_manager.spending_by_category('Home & Utilities'))
    print("Key recommendations:", budget_manager.recommendations())

    visualizer = Visualization(budget_manager)
    visualizer.plot_expenses_by_category()
