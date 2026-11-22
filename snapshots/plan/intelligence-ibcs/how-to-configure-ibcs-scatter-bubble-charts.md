---
title: "Scatter and bubble charts"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-ibcs/how-to-configure-ibcs-scatter-bubble-charts](https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-ibcs/how-to-configure-ibcs-scatter-bubble-charts) · Last updated on **2026-09-15**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Scatter and bubble charts

Summarize this article for me

IBCS scatter and bubble charts help you visualize relationships between business measures using standardized layouts and semantic formatting. Use these charts to identify correlations, clusters, trends, and outliers while comparing data across categories.

## C09: Scattergrams

Use an IBCS scatter chart to analyze the relationship between two measures. It's useful for identifying correlations, trends, clusters, and outliers in business data, such as sales versus profit or revenue versus quantity. Use this chart to compare the distribution of data points across two numeric measures.

| Configuration option | Configuration value |
| --- | --- |
| **Chart type** | Scatter Chart |
| **Category** | Assign a dimension to define each bubble. Each category is displayed as a separate bubble. *Example: Product Subcategory.* |
| **X-Axis** | Assign a measure to plot on the x-axis. The values determine the horizontal position of each bubble. *Example: Sales, Profit, or Cost.* |
| **Y-Axis** | Assign a measure to plot on the y-axis. The values determine the vertical position of each bubble. *Example: Quantity.* |
| **Legend / Color by / Stacked** | Assign a dimension to categorize the bubbles. Each category is displayed in a different color. *Example: Segment.* |

[![Screenshot of the category, x-axis, y-axis, and legend assignments used to configure an IBCS bubble chart.](../media/intelligence-ibcs/how-to-configure-ibcs-scatter-bubble-charts/axis-values-assignments-scatter-chart-ibcs.png)](../media/intelligence-ibcs/how-to-configure-ibcs-scatter-bubble-charts/axis-values-assignments-scatter-chart-ibcs.png#lightbox)

## C10: Bubble charts

Use an IBCS bubble chart to compare the relationship between two measures while using bubble size to represent a third measure. It's useful for analyzing metrics such as revenue, profit, and market share across products, customers, or regions. Use this chart to visualize multiple business measures in a single view.

| Configuration option | Configuration value |
| --- | --- |
| **Chart type** | Bubble Chart |
| **Category** | Assign a dimension to define each bubble. Each category is displayed as a separate bubble. *Example: Product.* |
| **X-Axis** | Assign a measure to plot on the x-axis. The values determine the horizontal position of each bubble. *Example: Profit - Actual.* |
| **Y-Axis** | Assign a measure to plot on the y-axis. The values determine the vertical position of each bubble. *Example: Profit - Target.* |
| **Size** | Assign the measure that determines the size of each bubble. *Example: Quantity sold.* |
| **Legend / Color by / Stacked** | Assign a dimension to define the bubble legend. Each category is represented by a different colored bubble. *Example: Segment.* |

[![Screenshot of axis, category, legend and values parameters required to create an IBCS bubble chart.](../media/intelligence-ibcs/how-to-configure-ibcs-scatter-bubble-charts/axis-values-assignments-bubble-chart-ibcs.png)](../media/intelligence-ibcs/how-to-configure-ibcs-scatter-bubble-charts/axis-values-assignments-bubble-chart-ibcs.png#lightbox)

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
