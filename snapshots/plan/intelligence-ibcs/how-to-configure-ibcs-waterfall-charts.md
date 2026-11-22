---
title: "Waterfall charts"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts](https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts) · Last updated on **2026-11-18**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Waterfall charts

Summarize this article for me

IBCS waterfall charts help explain how positive and negative values contribute to a net change between a starting and ending value. Use these charts to visualize business drivers such as revenue, costs, profit, and variances by using standardized IBCS layouts and semantic formatting.

## C05: Columns with waterfall

Use an IBCS columns with waterfall chart to show how incremental increases and decreases contribute to a final value by using vertical columns. It's best suited for financial statements, profit and loss analysis, and budget-to-actual reconciliations.

| Configuration option | Configuration value |
| --- | --- |
| **Chart type** | Waterfall + column |
| **Category** | Assign the dimension that defines the categories on the x-axis. The waterfall shows each category as a unique column. *Example: Month.* |
| **Actual(s)** | Assign one measure to analyze. The values determine the height of each column. *Example: Profit - Actual.* |
| **Comparison 1â3 (vs Actuals)** | Assign prior-year, plan, and forecast measures to compare with actual values. The chart shows each comparison measure as an overlapping or separate column for the same category and calculates the corresponding variance from the actual and comparison values. *Example: Profit - Prior Year, Profit - Target, Profit - Forecast.* |

[![Screenshot of an IBCS waterfall chart with columns to show actuals, plan, and forecast values.](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-columns-waterfall.jpg)](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-columns-waterfall.jpg#lightbox)

## C06: Bars with vertical waterfall

Use an IBCS bars with vertical waterfall chart to visualize cumulative changes by using horizontal bars. It's useful for comparing contributions across categories with long labels, such as departments, products, or cost centers.

| Configuration option | Configuration value |
| --- | --- |
| **Chart type** | Waterfall + bar |
| **Category** | Assign the dimension that defines the categories on the y-axis. The chart shows each category as a unique bar in the waterfall. *Example: Country/Region.* |
| **Actual(s)** | Assign one measure to analyze. The values determine the length of each bar. *Example: Profit - Actual.* |
| **Comparison 1â3 (vs Actuals)** | Assign prior-year, plan, and forecast measures to compare with actual values. The chart shows each comparison measure as an overlapping or separate bar for the same category and calculates the corresponding variance from the actual and comparison values. *Example: Profit - Prior Year, Profit - Target, Profit - Forecast.* |

[![Screenshot of assigning measures and dimensions to render an IBCS waterfall chart.](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-bar-waterfall-assign-dimensions-measures.png)](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-bar-waterfall-assign-dimensions-measures.png#lightbox)

Follow these steps to customize the chart as per IBCS specifications:

1. In the **Waterfall + bar** ribbon, go to **Themes** (paintbrush icon) and select IBCS.
2. Go to **Series** and deselect **Delta PY** and **Delta PY%**. This action removes the pin charts for prior-year absolute and relative variances.

   [![Screenshot of selecting the variance measure for plan.](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-bar-waterfall-series-select-plan-variance.png)](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-bar-waterfall-series-select-plan-variance.png#lightbox)
3. Select the y-axis title and select the hide icon.
4. Double-click the title to edit it and add a relevant title as per IBCS.
5. In the **Waterfall + bar** ribbon, select **Deviation** > **Customize.**
6. Turn on the **Enable Deviation** switch to render deviation lines between actuals and comparison measures.
7. In the **Deviation** pane, set **Label Display** to **Value.** In the **Text & Appearance** section, set **Shape** to **Ellipses**. Select **Apply**.

   The following screenshot shows the C06 waterfall:

   [![Screenshot of ibcs waterfall chart with variances.](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-bar-waterfall-set-deviation-final.png)](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-bar-waterfall-set-deviation-final.png#lightbox)

## C12: Vertical waterfall

Use a vertical IBCS waterfall chart to emphasize the progression from a starting value to an ending value across sequential business events or reporting periods. This chart commonly explains changes in cash flow, operating profit, or revenue. Use this chart when the order of contributions is an important part of the analysis.

| Configuration option | Configuration value |
| --- | --- |
| **Chart type** | Side by side waterfall |
| **Category** | Assign the dimension that defines the categories on the x-axis. The chart shows each category as a separate waterfall column. *Example: Income statement line items.* |
| **Actual(s)** | Assign one measure to analyze. The values determine the height of each bar in the first waterfall. *Example: AC.* |
| **Comparison 1 (vs Actuals)** | Assign a measure to compare against actuals. The values determine the height of each bar in the second waterfall. The lollipop and bar charts show the absolute and relative variance between the actual and comparison measures. *Example: PY.* |

![Screenshot of a side-by-side waterfall chart with IBCS formatting applied and variances plotted as bar and pin charts.](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-vertical-waterfall.png)

Additional configuration steps for the C12 vertical waterfall chart:

1. In the chart ribbon (in this example, **Side by side waterfall**), go to **Sort**, then set the sorting method to **Native** and **By** to **Axis**.
2. Select a bar to use the on-object interaction menu. Convert the bars to result bars.

   [![Screenshot of using the on-object interaction menu to plot result bars in an IBCS waterfall chart.](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-vertical-waterfall-result-bar.png)](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-vertical-waterfall-result-bar.png#lightbox)
3. Select bars that represent expenses or costs and use the on-object interaction menu to invert them.

   [![Screenshot of using the on-object interaction menu to invert bars for costs and expenses in an IBCS waterfall chart.](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-verticall-waterfall-invert.png)](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-verticall-waterfall-invert.png#lightbox)
4. In the **Side by side waterfall** ribbon, go to **Settings** > **Others** and enable **Category sign** to show plus, minus, and equal to symbols against each category.

   [![Screenshot of showing positive and negative signs for each bar in an IBCS waterfall chart.](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-waterfall-show-sign.png)](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-waterfall-show-sign.png#lightbox)

The following screenshot shows the C12 vertical waterfall:

[![Screenshot of an IBCS vertical waterfall chart.](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-waterfall-final.png)](../media/intelligence-ibcs/how-to-configure-ibcs-waterfall-charts/ibcs-waterfall-final.png#lightbox)

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
