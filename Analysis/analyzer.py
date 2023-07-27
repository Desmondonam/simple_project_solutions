import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    return pd.read_csv(file_path)


def analyze_data(data):
    # Basic summary statistics
    print("Summary Statistics:")
    print(data.describe())

    # Total revenue and total quantity sold
    total_revenue = data["Revenue"].sum()
    total_quantity_sold = data["Quantity Sold"].sum()
    print(f"\nTotal Revenue: ${total_revenue:.2f}")
    print(f"Total Quantity Sold: {total_quantity_sold}")

    # Top selling products
    top_selling_products = data.groupby(
        "Product")["Quantity Sold"].sum().nlargest(5)
    print("\nTop Selling Products:")
    print(top_selling_products)


def visualize_data(data):
    # Visualize total revenue per month
    data["Date"] = pd.to_datetime(data["Date"])
    data["Month"] = data["Date"].dt.month
    monthly_revenue = data.groupby("Month")["Revenue"].sum()

    plt.figure(figsize=(8, 6))
    plt.bar(monthly_revenue.index, monthly_revenue.values,
            tick_label=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    plt.xlabel("Month")
    plt.ylabel("Total Revenue ($)")
    plt.title("Total Revenue per Month")
    plt.show()


if __name__ == "__main__":
    file_path = "sales_data.csv"

    # Load data
    sales_data = load_data(file_path)

    # Analyze data
    analyze_data(sales_data)

    # Visualize data
    visualize_data(sales_data)
