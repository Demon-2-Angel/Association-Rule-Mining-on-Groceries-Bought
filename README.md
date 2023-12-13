# Summary of Python Code for Association Rule Mining in Grocery Dataset
<p align=center>
<img src="https://github.com/Demon-2-Angel/Association-Rule-Mining-on-Groceries-Bought/blob/main/Images/shopping_cart_banner.jpg">
</p>

## 1. Data Loading and Exploration:
- Libraries such as NumPy, Pandas, and Plotly are imported for data manipulation and visualization.
- The 'apyori' library is imported for association rule mining.

## 2. Dataset Loading:
- The code loads a grocery dataset from a CSV file using Pandas, with the 'Date' column parsed as dates.

## 3. Data Cleaning:
- Null values in the dataset are checked.

## 4. Exploratory Data Analysis (EDA):
- The distribution of the top 10 products is calculated and displayed using Plotly.

## 5. One-Hot Encoding:
- The 'itemDescription' column is one-hot encoded, and the resulting columns are added to the DataFrame.

## 6. Data Transformation:
- The dataset is transformed to group records by 'Member_number' and 'Date', calculating the sum of each product purchased.

## 7. Association Rule Mining:
- The Apriori algorithm is used to discover association rules among purchased products.
- Transaction data is prepared, and association rules are mined with specified parameters like minimum support, confidence, lift, and minimum length.

## 8. Results Display:
- Discovered association rules are displayed, including antecedent, consequent, support, confidence, and lift for each rule.

## 9. Summary:
- The code provides insights into association rules in the grocery dataset, indicating which products are commonly bought together.

## 10. Note:
- There's a small typo in the code where 'min_confidance' should be corrected to 'min_confidence' in the apriori function.

## 11. Improvement:
- Consider making the code more modular by placing functionality into functions or classes for better organization and reusability.

**Note:** The effectiveness of association rules depends on dataset characteristics and parameter choices for the Apriori algorithm. Adjusting parameters may yield different results.
