import nbformat

def update_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    updates = {
        "q4_amount_desc": [
            "### Q4.2 Analysis: The Skew is Real!\n",
            "Data visualization often reveals surprises, and this dataset is a prime example. Plotting the foreign gift amounts immediately shows an **incredibly skewed distribution**. The vast majority of gifts are relatively small, but a few massive outliers stretch the x-axis so far that the histogram would look like a single bar without adjustment.\n",
            "\n",
            "To reveal any meaningful pattern, we had to use a **log scale** (`logy=True`). This transformation allows us to see the frequency of those rarer, high-value gifts that would otherwise be invisible. It's a classic hallmark of financial data—a 'heavy-tailed' distribution where the big players really stand out."
        ],
        "q6_proofs": [
            "### Answer to Q6: The Logic of Linear Transformations\n",
            "Let's break down how linear transformations ($Y = a + bX$) affect our summary statistics. This is crucial for understanding unit conversions (like Celsius to Fahrenheit).\n",
            "\n",
            "**1. Linearity of Mean:**\n",
            "The mean behaves very intuitively. Since we sum up all values, the constants $a$ and $b$ just factor out.\n",
            "$$\n",
            "m(a + bX) = \\frac{1}{N} \\sum_{i=1}^N (a + b x_i) = a + b \\times m(X)\n",
            "$$\n",
            "*In plain English:* If you double every value ($b=2$), the mean doubles. If you add 5 ($a=5$), the mean increases by 5.\n",
            "\n",
            "**2. Covariance Identity:**\n",
            "Covariance of a variable with itself is just a fancy name for **variance**.\n",
            "$$\n",
            "\\text{cov}(X,X) = s^2\n",
            "$$\n",
            "\n",
            "**3. Covariance Linearity:**\n",
            "When we scale one variable, the covariance scales by that same factor. The shift $a$ disappears because covariance measures *variability* around the mean, and shifting everything doesn't change relative variability.\n",
            "$$\n",
            "\\text{cov}(X, a+bY) = b \\times \\text{cov}(X,Y)\n",
            "$$\n",
            "\n",
            "**4. Bilinearity:**\n",
            "If we scale *both* variables, the scaling factors multiply.\n",
            "$$\n",
            "\\text{cov}(a+bX, a+bY) = b^2 \\text{cov}(X, Y)\n",
            "$$\n",
            "\n",
            "**5. Median and IQR:**\n",
            "**Yes.** Because our transformation ($b > 0$) is strictly increasing, it preserves the **order** of the data points. The middle value (median) stays in the middle, just scaled and shifted. Similarly, the spread between the 75th and 25th percentiles (IQR) scales by $b$, but the shift $a$ cancels out.\n",
            "\n",
            "**6. Non-linear Transformations:**\n",
            "This is where our intuition requires caution! Non-linear functions like $X^2$ or $\\sqrt{X}$ do **not** preserve these nice properties. As the code below demonstrates, the mean of the squares is generally *not* the square of the mean ($E[X^2] \\neq (E[X])^2$). We can't just plug in the means for non-linear functions."
        ]
    }

    count = 0
    for cell in nb.cells:
        if cell.get('id') in updates and cell.cell_type == 'markdown':
            cell.source = "\n".join(updates[cell.get('id')])
            print(f"Updated cell {cell.get('id')}")
            count += 1
            
    if count > 0:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"Successfully updated {count} cells.")
    else:
        print("No cells found to update.")

if __name__ == "__main__":
    update_notebook('/Users/wilsonfredbeck/DS/DS-3021-analytics/ml_container/programming-HW/assignment/01_assignment_wrangling_and_eda.ipynb')
