---
title: "Build a dashboard in intelligence sheets"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-how-to-create-dashboards](https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-how-to-create-dashboards) · Last updated on **2026-07-12**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Build a dashboard in intelligence sheets

Summarize this article for me

Build interactive dashboards directly on your semantic models using more than 100 chart types, tables, matrices, KPI cards, and filters. The intelligence sheet offers a wide range of customization options to suit your reporting needs. In this article, you learn how to build a sample dashboard using the different components in an intelligence sheet.

## Prerequisites

Before you start designing a dashboard, make sure that you create an intelligence sheet and import the data you need.

## Create a dashboard

Combine charts, KPI cards, tables, matrices, and filters to create dashboards tailored to your business requirements.

1. Add a line chart to project the revenue, profit, and cost over five years. Select **Charts 100+** and select **Line**. Assign the axis dimensions and measures. Select the focus icon to customize the chart.

   [![Screenshot of assigning measures and dimensions to plot a line chart.](media/intelligence-how-to-create-dashboards/add-line-chart.png)](media/intelligence-how-to-create-dashboards/add-line-chart.png#lightbox)
2. In the **Line** ribbon, go to **Settings** > **Canvas**. Set the **Line type** to **Spline**. Customize the line and marker in the **Category format** section. Select **Back to Sheet** to return to the dashboard.

   [![Screenshot of customizing the color and type of the line chart.](media/intelligence-how-to-create-dashboards/customize-line-chart.png)](media/intelligence-how-to-create-dashboards/customize-line-chart.png#lightbox)
3. In the **Visualizations** tab, search for *Marimekko* and select **Vertical stacked marimekko** to compare revenue and margin proportions across product categories.
4. Assign the height and width measures, axis, and stacked dimensions to plot the marimekko.
5. Select a stack to use the on-object interaction menu. Apply basic customizations to the series color, font, data labels, and borders directly in the canvas without switching to focus mode.

   [![Screenshot of adding a marimekko chart and assigning the height and width measures.](media/intelligence-how-to-create-dashboards/add-marimekko-chart.png)](media/intelligence-how-to-create-dashboards/add-marimekko-chart.png#lightbox)
6. Plot an integrated variance chart to compare the revenue and prior year revenue over five years. Select **Integrated variance column** in the **Visualizations** pane and configure the measures and dimensions. The chart automatically shows the variance between the current and prior year revenue.
7. Select the x-axis title and choose the **Hide** option from the menu.

   [![Screenshot of adding an integrated variance chart.](media/intelligence-how-to-create-dashboards/add-integrated-variance-chart.png)](media/intelligence-how-to-create-dashboards/add-integrated-variance-chart.png#lightbox)
8. Select the **Filter** icon. Select the **Year** section to expand it and select the past five years in the **Basic** tab.

   [![Screenshot of filtering data for five years.](media/intelligence-how-to-create-dashboards/filter-years.png)](media/intelligence-how-to-create-dashboards/filter-years.png#lightbox)
9. Add matrices to show detailed data in rows and columns and to compare and analyze individual records. In the **Visualizations** pane, select **Matrix** and assign dimensions and measures.

   Note

   Assign actuals to the **Values (AC)** data well and prior year (PY), plan (PL), and forecast (FC) measures to the respective data wells to automatically calculate the variances.

   [![Screenshot of adding a matrix visual.](media/intelligence-how-to-create-dashboards/add-table.png)](media/intelligence-how-to-create-dashboards/add-table.png#lightbox)
10. Select the **Focus** icon to customize the table.

    [![Screenshot of focus mode for tables.](media/intelligence-how-to-create-dashboards/customize-table.png)](media/intelligence-how-to-create-dashboards/customize-table.png#lightbox)
11. Intelligence sheets automatically calculate variances based on the assigned measures. To show the variance columns, go to the **Matrix** tab, select **Show Columns**, and choose the required variance columns.

    [![Screenshot of showing variance columns.](media/intelligence-how-to-create-dashboards/show-columns.png)](media/intelligence-how-to-create-dashboards/show-columns.png#lightbox)
12. In the **Data** ribbon, go to **Insert Column** > **Formula**. Create a formula column to calculate the *implied price*.

    [![Screenshot of inserting a formula measure.](media/intelligence-how-to-create-dashboards/insert-formula.png)](media/intelligence-how-to-create-dashboards/insert-formula.png#lightbox)
13. Select a header, row dimension, or cell and go to the **Format** ribbon to customize the matrix.

    [![Screenshot of customizing matrix visuals and applying a header color.](media/intelligence-how-to-create-dashboards/edit-header.png)](media/intelligence-how-to-create-dashboards/edit-header.png#lightbox)
14. Select **KPIs** in the **Visualization** pane. To show a key metric in a KPI card, assign the measure to the **Actual(s)** field. Assign plan, previous year actuals, and forecast measures to the comparison data wells. The intelligence sheet automatically calculates and shows the corresponding variances in red and green.

    [![Screenshot of adding a KPI card to the dashboard.](media/intelligence-how-to-create-dashboards/add-kpi.jpg)](media/intelligence-how-to-create-dashboards/add-kpi.jpg#lightbox)
15. Select a card, hover over it, and then select the **Edit** icon to customize the KPI. Change the font style, add formulas, and insert charts.

    [![Screenshot of customizing KPI cards.](media/intelligence-how-to-create-dashboards/edit-kpi.png)](media/intelligence-how-to-create-dashboards/edit-kpi.png#lightbox)
16. Select the card, select **More options(...)**, and select **Duplicate** to create a copy of the card. Change the actuals and comparison assignments to a different metric. Repeat this process to create cards with uniform formatting for each metric.

    [![Screenshot of duplicating dashboard elements.](media/intelligence-how-to-create-dashboards/duplicate-card.png)](media/intelligence-how-to-create-dashboards/duplicate-card.png#lightbox)
17. Add text summaries to explain trends, results, and business outcomes shown in the dashboard. In the **Intelligence** ribbon, go to **Elements** > **Text** to insert a text box. Select the edit icon to format your text. Alternatively, select the text and use the floating toolbar.

    [![Screenshot of adding a textbox and using the rich text editor.](media/intelligence-how-to-create-dashboards/add-text-box.jpg)](media/intelligence-how-to-create-dashboards/add-text-box.jpg#lightbox)
18. Select an element and use the drag handle to reposition it on the dashboard.

    [![Screenshot of repositioning components in the dashboard.](media/intelligence-how-to-create-dashboards/move-components.jpg)](media/intelligence-how-to-create-dashboards/move-components.jpg#lightbox)
19. Select an element and go to the **Visual** tab in the corresponding ribbon to apply formatting such as borders and shadows.

    [![Screenshot of applying borders and shadows for each element in the dashboard.](media/intelligence-how-to-create-dashboards/add-border-shadow.jpg)](media/intelligence-how-to-create-dashboards/add-border-shadow.jpg#lightbox)
20. In the **Intelligence** ribbon, select **Elements**, and then insert shapes and text boxes to create a custom dashboard header.

    [![Screenshot of adding a custom dashboard header.](media/intelligence-how-to-create-dashboards/create-header.png)](media/intelligence-how-to-create-dashboards/create-header.png#lightbox)
21. Add comments to dashboards to provide context directly within the data. Select a cell, row, or column in a table or matrix, or select a data point in a chart. Select **Comment**, and then use the rich text editor to format the content. Assign comments to other users to collaborate on the dashboard.

    [![Screenshot of adding data point annotations to charts.](media/intelligence-how-to-create-dashboards/add-data-point-comments.png)](media/intelligence-how-to-create-dashboards/add-data-point-comments.png#lightbox)

    The following image shows the final dashboard:

    [![Screenshot of the dashboard with charts, KPI cards, matrices, and text elements.](media/intelligence-how-to-create-dashboards/final-dashboard.png)](media/intelligence-how-to-create-dashboards/final-dashboard.png#lightbox)

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
