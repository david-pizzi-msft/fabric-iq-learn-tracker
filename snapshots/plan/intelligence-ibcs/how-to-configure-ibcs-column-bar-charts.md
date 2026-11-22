---
title: "Column and bar charts"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-ibcs/how-to-configure-ibcs-column-bar-charts](https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-ibcs/how-to-configure-ibcs-column-bar-charts) · Last updated on **2026-07-15**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Column and bar charts

Summarize this article for me

IBCS column and bar charts provide standardized visualizations for comparing business metrics across categories and time periods. Select the chart type that best fits your reporting scenario, such as comparing actual values, analyzing variances, or tracking performance over time.

## C01: Stacked column chart

Use this chart to analyze business metrics such as revenue, profit, and expenses across months, quarters, or business units and identify differences in magnitude between categories.

| Configuration option | Configuration value |
| --- | --- |
| Chart type | Stacked column |
| Category | Assign the dimension that defines the columns along the x-axis. The chart shows each unique value as a separate stacked column. *Example: Month*. |
| Actual(s) | Assign one or more measures to analyze. The values determine the height of each stacked column or segment. *Example: Revenue.* |
| Comparison 1-3 (vs Actuals) | Assign up to three additional measures to compare with the actual values. The chart shows each comparison measure as a separate stacked column or overlapped column for the same category.  This comparison is optional. *Example: Budget, Forecast, and Previous Year Revenue.* |
| Legend / Color by / Stacked | Assign the dimension that splits each column into stacked segments. The chart shows each unique value as a separate segment within the column. *Example: Product Category.* |

Tip

Assign a forecast measure to the Comparison 3 data well to plot hatched bars for future data. In this example, assign *Profit-Forecast.*

[![Screenshot of a stacked column chart with hatched bars to plot a forecast.](../media/intelligence-ibcs/how-to-configure-ibcs-column-bar-charts/ibcs-stacked-column-chart.jpg)](../media/intelligence-ibcs/how-to-configure-ibcs-column-bar-charts/ibcs-stacked-column-chart.jpg#lightbox)

## C02: Stacked bar

Use a bar chart to compare values across multiple categories, especially when category labels are long. Plot stacked bar charts to rank products, customers, regions, or departments by performance.

| Configuration option | Configuration value |
| --- | --- |
| Chart type | Stacked bar |
| Category | Assign the dimension that defines the columns along the y-axis. The chart shows each unique value as a separate stacked bar. *Example: Product.* |
| Actual(s) | Assign one or more measures to analyze. The values determine the height of each stacked bar or segment. *Example: Revenue.* |
| Legend / Color by / Stacked | Assign the dimension that splits each column into stacked segments. The chart shows each unique value as a separate segment within the column. *Example: Segment.* |

[![Screenshot of an IBCS stacked bar chart.](../media/intelligence-ibcs/how-to-configure-ibcs-column-bar-charts/ibcs-stacked-bar-chart.png)](../media/intelligence-ibcs/how-to-configure-ibcs-column-bar-charts/ibcs-stacked-bar-chart.png#lightbox)

## C03: Multi-tier column

Use a column chart with variance to compare actual values against a reference value, such as budget, forecast, or prior year. The variance highlights overperformance or underperformance for each category. Use this chart to monitor business performance against targets.

| Configuration option | Configuration value |
| --- | --- |
| Chart type | Overlapped column |
| Category | Assign the dimension that defines the columns along the x-axis. The chart shows each unique value as a separate column. *Example: Month*. |
| Actual(s) | Assign one or more measures to analyze. The values determine the height of each column. *Example: Profit Actual.* |
| Comparison 1-3 (vs Actuals) | Assign one or more measures to compare with the actual values. The chart shows each comparison measure as an overlapping or separate column for the same category and calculates the corresponding variance from the actual and comparison values. *Example: Profit Target, Profit Forecast.* |

Tip

- Assign a plan or target measure to the Comparison 2 data well to plot overlapped bars. In this example, assign *Profit-Target.*
- Assign a forecast measure to the Comparison 3 data well to plot hatched bars for future data. In this example, assign *Profit-Forecast.*

[![Screenshot of IBCS overlapped column chart with variances.](../media/intelligence-ibcs/how-to-configure-ibcs-column-bar-charts/ibcs-overlapped-column-chart.png)](../media/intelligence-ibcs/how-to-configure-ibcs-column-bar-charts/ibcs-overlapped-column-chart.png#lightbox)

## C04: Multi-tier bar

Use a bar chart with variance to compare actual and reference values across categories while emphasizing the variance. It's useful for analyzing performance across business units, products, or regions.

| Configuration option | Configuration value |
| --- | --- |
| Chart type | Waterfall + bar |
| Category | Assign the dimension that defines the columns along the y-axis. The chart shows each unique value as a separate stacked bar. *Example: Product.* |
| Actual(s) | Assign one or more measures to analyze. The values determine the height of each column. *Example: Profit-Actual.* |
| Comparison 1 (vs Actuals) | Assign the previous year's actuals measure for comparison. The chart shows the comparison measure as an overlapping or separate column for the same category *Example: Profit - Prior Year.* |

Tip

Assign a plan or target measure to the Comparison 1 data well to plot overlapped bars. In this example, assign *Profit-Prior Year.*

[![Screenshot of IBCS overlapped bar chart.](../media/intelligence-ibcs/how-to-configure-ibcs-column-bar-charts/ibcs-overlapped-bar-chart.png)](../media/intelligence-ibcs/how-to-configure-ibcs-column-bar-charts/ibcs-overlapped-bar-chart.png#lightbox)

---

## Feedback

Was this page helpful?

Yes

No

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

Ask Learn

Ask Learn

 Suggest a fix?

---

## Additional resources
