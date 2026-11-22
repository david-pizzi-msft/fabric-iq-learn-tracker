---
title: "Get started with intelligence sheets"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-how-to-get-started](https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-how-to-get-started) · Last updated on **2026-07-08**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Get started with intelligence sheets

Summarize this article for me

Intelligence sheets provide a no-code, end-to-end reporting experience that brings all your data visualization needs together on a single platform. Use intelligence sheets to build reports, create dashboards, and run ad hoc analysis directly on top of your semantic models or planning sheets. Intelligence sheets include a visualization library of more than 100 chart types, including advanced visualizations such as marimekko, boxplot, waterfalls, and radar/polar charts. This article guides you through creating your first intelligence sheet.

## Import data to visualize

Intelligence sheets let you transform data from planning sheets, semantic models, and file-based sources such as Excel and Parquet files into interactive reports and dashboards. Create visualizations such as charts, tables, matrices, KPI cards, and filters to analyze performance, monitor key metrics, and share insights across your organization.

### Import data from a semantic model

Import an existing semantic model to create reports based on curated business data. By connecting to a semantic model, you can use predefined measures, relationships, and calculations. You can build reports and visualizations without modeling the data yourself.

Tip

You can also import a semantic model after creating an intelligence sheet. In the **Data** pane, select **+ Add** and import the semantic model.

1. To connect to a semantic model, select **Semantic Model** from the **Get data** section of the landing page.
2. Select **Semantic Model Item** and select the search field.

   [![Screenshot of selecting the semantic model search field.](media/intelligence-how-to-get-started/select-semantic-model-connection.jpg)](media/intelligence-how-to-get-started/select-semantic-model-connection.jpg#lightbox)
3. Select the semantic model you want from the list.

   [![Screenshot of selecting the semantic model from the list.](media/intelligence-how-to-get-started/select-semantic-model.png)](media/intelligence-how-to-get-started/select-semantic-model.png#lightbox)
4. The semantic model appears in the intelligence sheet.

   [![Screenshot of semantic model imported into the intelligence sheet.](media/intelligence-how-to-get-started/semantic-model-imported.png)](media/intelligence-how-to-get-started/semantic-model-imported.png#lightbox)

### Import data from Excel and CSV files

Import Excel and CSV files to create interactive reports and visualizations from existing business data. You can analyze trends, monitor key metrics, and share insights through charts, tables, matrices, and dashboards without a direct connection to a database or semantic model. Business users can create reports and dashboards directly from familiar file formats, reducing dependency on IT teams.

In the landing page, select **Excel/CSV** and upload the file.

[![Screenshot of Excel/CSV import option in the landing page.](media/intelligence-how-to-get-started/landing-page-excel-option.png)](media/intelligence-how-to-get-started/landing-page-excel-option.png#lightbox)

Alternatively, after creating an intelligence sheet, follow these steps.

1. Expand the **Queries** section in the **Data** pane.
2. Select **Add**, and then select the upload format (**Excel** or **CSV**).

   [![Screenshot of options to import Excel or CSV files after creating an intelligence sheet.](media/intelligence-how-to-get-started/infobridge-add-excel-csv.png)](media/intelligence-how-to-get-started/infobridge-add-excel-csv.png#lightbox)
3. Select the file for upload. For Excel sources, select the sheet to import. Select **Create**.

   [![Screenshot of uploading an Excel or CSV sheet.](media/intelligence-how-to-get-started/upload-excel-csv-file.png)](media/intelligence-how-to-get-started/upload-excel-csv-file.png#lightbox)
4. After you add the source, select **Close** in the top-right corner to exit Infobridge. To learn more about Infobridge and its applications, see [data integration with bridges](infobridge-how-to-create-bridge).

   [![Screenshot of the data  preview displayed after importing a file.](media/intelligence-how-to-get-started/preview-file-data.png)](media/intelligence-how-to-get-started/preview-file-data.png#lightbox)
5. The dimensions and measures appear in the **Queries** section of the **Data** pane. Map them to an intelligence sheet component such as a chart or matrix for visualization and reporting.

## Create an intelligence sheet

Create an intelligence sheet to visualize and analyze your data by using a variety of report elements, including charts, KPI cards, tables, matrices, and filters.

1. Select **New Intelligence Sheet** or select the intelligence sheet icon from the landing page.

   [![Screenshot of adding a new intelligence sheet.](media/intelligence-how-to-get-started/add-new-intelligence-sheet.png)](media/intelligence-how-to-get-started/add-new-intelligence-sheet.png#lightbox)
2. Select the icons on the right side of the canvas to open the **Data** and **Visualizations** panes.

   [![Screenshot of data and visualization panes.](media/intelligence-how-to-get-started/show-data-visualization-panes.png)](media/intelligence-how-to-get-started/show-data-visualization-panes.png#lightbox)
3. Select a data presentation format (such as **Gantt**, **Matrix**, **KPI**, or **Chart**) from the **Visualizations** pane.
4. Each type of visualization has specific data wells. Drag and drop measures and dimensions into the data wells to display them on the canvas.

   [![Screenshot of assigning measures and dimensions to the data wells for a matrix visual.](media/intelligence-how-to-get-started/assign-dimension-measures-data-wells.png)](media/intelligence-how-to-get-started/assign-dimension-measures-data-wells.png#lightbox)
5. Use the intelligence toolbar for canvas-level customizations such as setting backgrounds, changing themes, and configuring element interactions.

   [![Screenshot of using the intelligence toolbar.](media/intelligence-how-to-get-started/intelligence-toolbar.png)](media/intelligence-how-to-get-started/intelligence-toolbar.png#lightbox)

## Add charts to visualize data

The intelligence sheet includes a library of more than 100 visualization types to support a wide range of reporting scenarios. Choose from standard charts and advanced visualizations, such as marimekko, box plot, waterfall, radar, and polar charts. Storytelling visuals include slope graphs, lollipop charts, dumbbell charts, and dot plots.

Some chart types require specific field mappings to render. For example, marimekko charts require measures for both height and width; hierarchical charts such as treemap and sunburst require one or more hierarchical dimensions; and gauge charts require actual and target measures.

1. Select the **Charts 100+** visual to add a chart.
2. Choose the chart type from the **Visualizations** pane based on your requirement.

   [![Screenshot of the visualization library in intelligence sheets.](media/intelligence-how-to-get-started/visualization-library.png)](media/intelligence-how-to-get-started/visualization-library.png#lightbox)

   - When you know the chart type, enter its name in the search box. For example, type line, waterfall, boxplot, or mekko to view all available variations of that chart type.

     [![Screenshot of searching for a specific chat family.](media/intelligence-how-to-get-started/search-chart-type.png)](media/intelligence-how-to-get-started/search-chart-type.png#lightbox)
   - Prebuilt International Business Communication Standards (IBCS) charts reduce design effort while ensuring visual consistency and adherence to IBCS reporting standards. Select **IBCS** and choose a chart type such as waterfall, integrated variance, stacked bar, bullet, line/area, and more.

     [![Screenshot of selecting IBCS charts from the visualization library.](media/intelligence-how-to-get-started/ibcs-charts.png)](media/intelligence-how-to-get-started/ibcs-charts.png#lightbox)
   - Storytelling charts make complex data more engaging and easier to understand. Select **Special** to plot storytelling charts like range plots, tornado, sankey, ribbon, and slope graphs.

     [![Screenshot of storytelling charts.](media/intelligence-how-to-get-started/storytelling-charts.png)](media/intelligence-how-to-get-started/storytelling-charts.png#lightbox)
3. Drag and drop dimensions and measures from the **Data** pane to the appropriate data well in the **Visualizations** pane. The chart appears on the canvas.
4. Each chart type has a dedicated toolbar for advanced customization, sorting, ranking, and deviation.

   [![Screenshot of the toolbar for each chart type.](media/intelligence-how-to-get-started/chart-dedicated-toolbar.png)](media/intelligence-how-to-get-started/chart-dedicated-toolbar.png#lightbox)
5. Select the caret icon to expand and collapse the toolbar.

   [![Screenshot of option to expand and collapse the toolbar.](media/intelligence-how-to-get-started/expand-collapse-toolbar.png)](media/intelligence-how-to-get-started/expand-collapse-toolbar.png#lightbox)

## Highlight metrics with KPI cards

Add KPI cards to highlight critical metrics and trends in your dashboard. Use cards to quickly monitor performance and track business goals.

1. Select **KPIs** from the **Visualizations** pane.
2. Assign the metric to display to the **Actual(s)** data well.
3. To display the variance between different metrics, assign other measures to the **Comparison** data well.

   [![Screenshot of displaying variances in KPI cards.](media/intelligence-how-to-get-started/kpi-display-variance.png)](media/intelligence-how-to-get-started/kpi-display-variance.png#lightbox)
4. Assign **Trellis Row** dimensions to split a metric based on specific dimension categories. This example shows the overall cost distribution across different regions.

   [![Screenshot of adding row dimensions to create a trellis.](media/intelligence-how-to-get-started/trellis-configuration.png)](media/intelligence-how-to-get-started/trellis-configuration.png#lightbox)
5. Assign a dimension to the **Trellis Column** data well to split a metric based on another set of dimension categories.
6. Hover over a card and drag the blue line to resize it.

   [![Screenshot of using the drag handle to resize cards.](media/intelligence-how-to-get-started/change-panel-height.png)](media/intelligence-how-to-get-started/change-panel-height.png#lightbox)
7. Insert inline charts to visualize KPI metrics. Before inserting a chart, assign the axis dimension to the **Category** data well.
8. In the **KPI** ribbon, select **Sparkline** and choose the chart type.

   [![Screenshot of inserting charts in KPI cards.](media/intelligence-how-to-get-started/kpi-sparkline.png)](media/intelligence-how-to-get-started/kpi-sparkline.png#lightbox)

## Apply filters for interactive analysis

Use filters to narrow data and focus on the information that matters most. Intelligence sheets offer a range of filter types to meet your data exploration needs. When you apply a filter, it applies to all the components in your dashboard.

1. To add a dashboard filter, select **Filter** from the **Visualizations** pane.
2. Assign the filtering dimension to the **Category** data well.
3. The intelligence sheet automatically creates the filter type best suited to the dimensional data. In this example, the intelligence sheet inserts a date slider.

   [![Screenshot of adding a date filter to a dashboard.](media/intelligence-how-to-get-started/super-filter.png)](media/intelligence-how-to-get-started/super-filter.png#lightbox)
4. Apply filters to refine dashboard results and gain targeted insights. Dashboard elements such as charts, KPI cards, and tables respond to filter changes.

   [![Screenshot of applying a filter across dashboard elements.](media/intelligence-how-to-get-started/apply-filter-dashboard-elements.png)](media/intelligence-how-to-get-started/apply-filter-dashboard-elements.png#lightbox)

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
