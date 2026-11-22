---
title: "Area and line charts"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-ibcs/how-to-configure-ibcs-line-area-charts](https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-ibcs/how-to-configure-ibcs-line-area-charts) · Last updated on **2026-07-21**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Area and line charts

Summarize this article for me

IBCS area and line charts help you visualize trends, patterns, and changes over time by using standardized layouts and semantic formatting. Use these charts to track business performance, compare actual and reference values, and communicate trends consistently across reports.

## C07: Line chart

An IBCS line chart visualizes trends and changes across sequential time periods. It works best for tracking KPIs such as revenue, profit, expenses, or inventory over time. Use it to analyze growth patterns, seasonal trends, and changes in performance.

| Configuration option | Configuration value |
| --- | --- |
| Chart type | Line |
| Category | Assign the dimension that defines the columns along the x-axis. *Example: Month*. |
| Actual(s) | Assign one or more measures to analyze. The values determine the position of each data point on the y-axis, and the connected points form the trend line. *Example: Profit - Actual*. |
| Comparison 1 (vs Actuals) | Assign the previous year's actuals measure for comparison. The chart shows the comparison measure as a second line. This comparison is optional. *Example: Profit - Prior Year*. |
| Comparison 3 (vs Actuals) | Assign a forecast measure for comparison. The chart shows the comparison measure as a dotted line for the forecast period. This comparison is optional. *Example: Profit - Forecast*. |

[![Screenshot of measure and dimension assignments for an IBCS line chart.](../media/intelligence-ibcs/how-to-configure-ibcs-line-area-charts/ibcs-line-assign-data.png)](../media/intelligence-ibcs/how-to-configure-ibcs-line-area-charts/ibcs-line-assign-data.png#lightbox)

1. In the **Line** ribbon, select **Series**. Deselect the variance series (the column and lollipop charts) to show only the line chart.

   [![Screenshot of removing the variance series to show in the chart.](../media/intelligence-ibcs/how-to-configure-ibcs-line-area-charts/ibcs-line-select-series.jpg)](../media/intelligence-ibcs/how-to-configure-ibcs-line-area-charts/ibcs-line-select-series.jpg#lightbox)
2. Select **Deviation** > **Customize** > **Display** and select **Create your own**. Select **Apply**, and then select the points to plot the deviation.

   [![Screenshot of adding a deviation line between selected points in the chart.](../media/intelligence-ibcs/how-to-configure-ibcs-line-area-charts/show-deviation.jpg)](../media/intelligence-ibcs/how-to-configure-ibcs-line-area-charts/show-deviation.jpg#lightbox)
3. To customize the series colors, in the chart ribbon (in this example, **Line**), go to **Settings** > **Canvas** > **Category format** and select the colors to apply.

   [![Screenshot of setting custom line colors from canvas settings.](../media/intelligence-ibcs/how-to-configure-ibcs-line-area-charts/customize-line-series-colors.png)](../media/intelligence-ibcs/how-to-configure-ibcs-line-area-charts/customize-line-series-colors.png#lightbox)

## C08: Area chart

IBCS area charts emphasize the magnitude of values while showing trends over time. The shaded area highlights cumulative values, making it easier to compare the overall volume of business metrics such as sales, cash flow, or production. Use this chart when both trend and magnitude are important to the analysis.

| Configuration option | Configuration value |
| --- | --- |
| Chart type | Stacked area |
| Category | Assign the dimension that defines the columns along the x-axis. *Example: Month*. |
| Actual(s) | Assign one or more measures to analyze. The values determine the position of each data point on the y-axis, and the connected points form the trend line. *Example: Profit - Actual*. |
| Legend / Color by / Stacked | Assign a dimension to split the measure into separate series. The chart plots each unique value as a distinct area and stacks the areas to show the cumulative total. *Example: Region*. |

[![Screenshot of the dimension and measure assignment for an IBCS area chart.](../media/intelligence-ibcs/how-to-configure-ibcs-line-area-charts/ibcs-area-chart-data-assignment.png)](../media/intelligence-ibcs/how-to-configure-ibcs-line-area-charts/ibcs-area-chart-data-assignment.png#lightbox)

To customize the series colors, in the chart ribbon (in this example, **Stacked area**), go to **Settings** > **Canvas** > **Stack groups** and select the colors to apply.

[![Screenshot of an IBCS area chart with custom colors.](../media/intelligence-ibcs/how-to-configure-ibcs-line-area-charts/ibcs-area-customize-colors.jpg)](../media/intelligence-ibcs/how-to-configure-ibcs-line-area-charts/ibcs-area-customize-colors.jpg#lightbox)

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
