---
title: "Fabric planning tutorial part 10: Build a P&L intelligence sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence) · Last updated on **2026-09-11**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Fabric planning tutorial part 10: Build a P&L intelligence sheet

Summarize this article for me

In this tutorial, you build a P&L intelligence sheet by using the Enterprise Dataset semantic model. You create a financial matrix, add calculated and input rows, organize and format the report, add approval and stakeholder fields, and export the completed P&L.

## Prerequisites

Before you begin, ensure you have:

- Access to a Microsoft Fabric workspace with Fabric plan and permission to work with intelligence sheets.
- Access to the semantic model used in this tutorial.
- Completed [Introduction to intelligence sheets](tutorial-9-introduction-to-intelligence-sheets).

## Business context

You are a BI analyst at a SaaS company. Your team needs a P&L statement to analyze financial performance across products and business dimensions.

In this tutorial, you build the P&L statement in an intelligence sheet, add calculated and input rows, organize confidential information, add approval and stakeholder fields, and prepare the report for sharing and export.

In this tutorial, you:

1. Create a P&L intelligence sheet and configure a Matrix visual.
2. Add calculated and data input rows to the P&L.
3. Group, hide, reorder, and format rows and columns.
4. Add Approval Status and Stakeholder columns.
5. Add a report header and logo.
6. Export the completed P&L to Excel and PDF.

## Sample dataset

This tutorial uses the Enterprise Dataset semantic model to build the P&L statement.

If you didn't already import the dataset, follow the steps in [Introduction to intelligence sheets](tutorial-9-introduction-to-intelligence-sheets).

## Create the intelligence sheet and map data

Create an intelligence sheet, connect the Enterprise Dataset semantic model, add a Matrix visual, map the financial measures and account hierarchy, and apply the Financial template.

1. On the **Home** tab, select **New Intelligence Sheet**.

   [![Screenshot of the Home tab with New Intelligence Sheet selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-semantic-model.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-semantic-model.png#lightbox)
2. Name the intelligent sheet and select **Create**.
3. Select the **Data** pane icon on the right to expand it, and then select **Add** under **Semantic Model**.

   [![Screenshot of an intelligence sheet with the Data pane icon and the Add button under Semantic Model highlighted.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/open-data-pane.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/open-data-pane.png#lightbox)
4. In **Select Semantic Model**, select **Semantic Model Item** and select the search field to choose a semantic model.

   [![Screenshot of the Select Semantic Model dialog with Semantic Model Item selected and the Semantic Model search field highlighted.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-search-field.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-search-field.png#lightbox)
5. In **OneLake catalog**, select **Enterprise Dataset**, and then select **Add**.

   [![Screenshot of Enterprise Dataset selected in the OneLake catalog semantic model list.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-enterprise-dataset.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-enterprise-dataset.png#lightbox)
6. Verify that **Semantic Model** is selected and that **Enterprise Dataset** is selected, and then select **Connect**.

   [![Screenshot of the Select Semantic Model window with Enterprise Dataset and Connect.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/connect-semantic-model.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/connect-semantic-model.png#lightbox)
7. After the semantic model is connected, select **New Intelligence Sheet**.

   [![Screenshot of the Home tab with New Intelligence Sheet selected after the semantic model is connected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/create-intelligence-sheet.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/create-intelligence-sheet.png#lightbox)
8. In **New Intelligence Sheet**, enter `P&L Statement` as the name, and then select **Create**.

   [![Screenshot of the New Intelligence Sheet window with P&L Statement as the name.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/name-intelligence-sheet.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/name-intelligence-sheet.png#lightbox)
9. In the **Visualizations** pane, select **Matrix**.

   [![Screenshot of the Visualizations pane with Matrix selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-matrix-visual.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-matrix-visual.png#lightbox)
10. Map the data to the Matrix visual:

    - In the **Data** pane, expand **Semantic Model** > **Measure** > **Financial** > **Base Measures**. Add **Actuals** to **Values (AC)** and **Plan** to **Compare to Plan (PL)**.
    - Under **[Dim] Account**, expand **Account Hierarchy** and add the hierarchy to **Rows**. The hierarchy includes the account levels used by the matrix.
    - Under the date dimension, add **Time** to **Columns**.

    [![Screenshot of the Data pane showing Actuals, Plan, and Account Hierarchy mapped to the Matrix visual.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/map-matrix-fields.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/map-matrix-fields.png#lightbox)
11. On the **Matrix** tab, select **Templates**, and then select **Financial**.

    [![Screenshot of the Matrix tab with the Financial template selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/apply-financial-template.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/apply-financial-template.png#lightbox)

    The Financial template applies indentation, subtotals, and bold formatting to parent rows.

## Add calculated and input rows

Add rows that aren't part of the semantic model: Gross Margin %, Shares Outstanding, and Earnings Per Share.

### Insert a calculated row: Gross Margin %

Create a calculated row to show gross margin as a percentage of revenue.

1. On the **Data** tab, select **Insert Row** > **Formula**.

   [![Screenshot of the Data tab with Formula selected and the Calculated Row pane open.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/create-gross-margin-formula.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/create-gross-margin-formula.png#lightbox)
2. In the **Calculated Row** pane, enter `Gross Margin %` in **Title**.
3. In **Formula**, enter `([Revenue] - [Cost of Revenue / COGS]) / [Revenue]` using row references.
4. Set **Scaling Factor** to **None**, and then select **Create**.
5. Select the **Gross Margin %** row. On the **Matrix** tab, select the **%** button to format the row as a percentage.

   [![Screenshot of the Gross Margin % row selected with the percentage formatting button highlighted.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/format-gross-margin-percentage.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/format-gross-margin-percentage.png#lightbox)

### Insert a static row: Shares Outstanding

Add a data input row for the number of shares used in the report.

1. Select the row gripper for **Revenue**, select **Insert**, and then select **Data Input**.

   [![Screenshot of the row context menu with Insert and Data Input selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/insert-data-input-row.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/insert-data-input-row.png#lightbox)
2. In the **Data Input** pane, enter `Shares Outstanding` in **Title**, and then select **Create**.

   [![Screenshot of the Data Input pane with Shares Outstanding entered as the title.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/create-shares-outstanding-row.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/create-shares-outstanding-row.png#lightbox)
3. Enter `100m` for **Actuals** and `150m` for **Plan**, pressing Enter after each value.

   [![Screenshot of Shares Outstanding values entered for Actuals and Plan.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/enter-shares-outstanding-values.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/enter-shares-outstanding-values.png#lightbox)

### Insert a calculated row: Earnings Per Share

Create a calculated row that divides revenue by the number of shares outstanding.

1. On the **Data** tab, select **Insert Row** > **Formula**.

   [![Screenshot of the Data tab with Formula selected for a new calculated row.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/insert-calculated-row.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/insert-calculated-row.png#lightbox)
2. In the **Calculated Row** pane, enter `Earnings Per Share` in **Title**.
3. In **Formula**, enter `[Revenue] / [Shares Outstanding]`, and then select **Create**.

   [![Screenshot of the Earnings Per Share formula using Revenue divided by Shares Outstanding.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/enter-eps-formula.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/enter-eps-formula.png#lightbox)
4. Select the **Earnings Per Share** row. On the **Matrix** tab, select the **$â¬** button.

   [![Screenshot of the Prefix / Suffix window with a dollar value prefix.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/apply-currency-format.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/apply-currency-format.png#lightbox)
5. In **Value prefix**, enter `$`, and then select **Apply**.

## Format and organize the report

Group related rows and columns, hide confidential rows, reorder the new rows, apply highlighting, and add gridlines.

### Group and hide confidential rows

Group sensitive rows together and hide them from the report view.

1. Select **Engineering Salaries** and **Product Management**. Use Ctrl-click to select both rows.
2. On the **Matrix** tab, select **Layout** > **Group** > **Create Group**.

   [![Screenshot of the Matrix Layout menu with Group and Create Group selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/create-confidential-group.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/create-confidential-group.png#lightbox)
3. In the group window, enter `Confidential` as the group name, and then create the group.

   [![Screenshot of the Create Group window for the Confidential group.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/name-confidential-group.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/name-confidential-group.png#lightbox)
4. Select the gripper for the **Confidential** group, select **Actions**, and then select **Hide icon & children**.

   [![Screenshot of the row context menu with Actions and Hide icon & children selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/hide-confidential-group-rows.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/hide-confidential-group-rows.png#lightbox)
5. Select the **Confidential** row. On the **Format** tab, select **Font Color**, enter `#9467BD`, and then select **Save**.

   [![Screenshot of the matrix after the confidential rows are hidden.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/view-hidden-rows.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/view-hidden-rows.png#lightbox)

   [![Screenshot of the Format tab with Font Color selected for the Confidential row.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/apply-font-color.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/apply-font-color.png#lightbox)

### Group the metrics columns

Group the **Actuals** and **Plan** columns to organize the report metrics.

1. Ctrl+click the **Actuals** and **Plan** column headers.
2. On the **Matrix** tab, select **Layout** > **Group** > **Create Group**.

   [![Screenshot of the Matrix Layout menu with Group and Create Group selected for the metric columns.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/create-metrics-group.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/create-metrics-group.png#lightbox)
3. Enter `Metrics` as the group name, and then create the group.

   [![Screenshot of the Create Group window for the Metrics group.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/name-metrics-group.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/name-metrics-group.png#lightbox)

   [![Screenshot of the matrix after the Metrics group is created.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/view-metrics-group.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/view-metrics-group.png#lightbox)

### Reorder and highlight rows

Reorder the added rows and highlight Earnings Per Share for easier identification.

1. Select **Shares Outstanding**, **Earnings Per Share**, and **Gross Margin %**, and drag them above **Revenue**.

   [![Screenshot of the rows selected for reordering above Revenue.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-rows-to-reorder.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-rows-to-reorder.png#lightbox)
2. Verify that the new rows appear above **Revenue**.

   [![Screenshot of the reordered P&L rows above Revenue.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/view-reordered-rows.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/view-reordered-rows.png#lightbox)
3. Select **Earnings Per Share**. On the **Format** tab, select **Fill Color**, enter `#9467BD`, and then select **Save**.

   [![Screenshot of the Format tab with the Fill Color control set to #9467BD.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-fill-color.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-fill-color.png#lightbox)

   [![Screenshot of the Earnings Per Share row highlighted with the fill color.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/apply-fill-color.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/apply-fill-color.png#lightbox)

### Add gridlines and apply report colors

Apply gridlines and report theme colors to improve the matrix layout.

1. On the **Format** tab, select **Major Gridlines**, and then select **Single**.

   [![Screenshot of the Major Gridlines menu with Single selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/set-major-gridlines.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/set-major-gridlines.png#lightbox)
2. Use the **Theme Colors** options on the **Format** tab to apply the organizationâs report colors to the matrix.

## Add custom columns, report header, and export

Add **Approval Status** and **Stakeholder** columns, add a report header and logo, and export the completed P&L.

### Add Approval Status

Add a column to track the approval state of the report.

1. On the **Data** tab, select **List**, and then select **Single Select**.

   [![Screenshot of the Data tab with List and Single Select selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/insert-approval-status-column.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/insert-approval-status-column.png#lightbox)
2. In the **Data Input** pane, enter `Approval Status` in **Title**.
3. Select **Presets**, select **Approval Status**, and then select **Apply**.

   [![Screenshot of the Approval Status data input pane with the Approval Status preset selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/configure-approval-status-column.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/configure-approval-status-column.png#lightbox)
4. Select **Create**.

   [![Screenshot of the Data Input pane with Create selected for Approval Status.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/create-approval-status-column.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/create-approval-status-column.png#lightbox)

### Add stakeholder

Add a column to assign report ownership to a stakeholder.

1. On the **Data** tab, select **Person**.

   [![Screenshot of the Data tab while adding the Stakeholder column.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/insert-stakeholder-column.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/insert-stakeholder-column.png#lightbox)
2. In the **Data Input** pane, enter `Stakeholder` in **Title** and select **Person** for **Input type**.

   [![Screenshot of the Data Input pane with Stakeholder as the title and Person selected as the input type.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/configure-stakeholder-person-column.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/configure-stakeholder-person-column.png#lightbox)
3. Select **Create**.

   [![Screenshot of the matrix with Approval Status and Stakeholder columns added.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/view-custom-columns.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/view-custom-columns.png#lightbox)
4. In a stakeholder cell, enter `@` followed by a user's name to search the organization directory and assign ownership.

### Add a report header

Add a report header with a title and logo to identify the finished report.

1. On the **Format** tab, select **Header & Footer**.

   [![Screenshot of the Format tab with Header & Footer selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/open-header-footer-formatting.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/open-header-footer-formatting.png#lightbox)
2. The **Header & Footer** tab opens. Select **Presets**, and then select **Header**.

   [![Screenshot of the Header & Footer tab with the Header preset selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-header-preset.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-header-preset.png#lightbox)
3. Select the report title container and change the title to `Profit and Loss Statement`.

   [![Screenshot of the report header with Profit and Loss Statement entered as the title.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/set-report-title.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/set-report-title.png#lightbox)
4. Select the **Your Logo** container and select **Replace Image**.

   [![Screenshot of the report header with the Your Logo container selected for replacement.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/replace-report-logo.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/replace-report-logo.png#lightbox)
5. Upload the `Contoso` logo image and select **Save**.

   [![Screenshot of the report header with the Contoso logo applied.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/upload-contoso-logo.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/upload-contoso-logo.png#lightbox)

### Export the report

Export the completed report to Excel and PDF for sharing and offline use.

1. On the **Matrix** tab, select **Export**.

   [![Screenshot of the Matrix tab with Export selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-excel-export.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/select-excel-export.png#lightbox)
2. In the **Export** window, select **Excel**.
3. To preserve the matrix hierarchy for interactive expansion and collapse, select **With Expand/Collapse**. Select **Entire Matrix**, and then select **Export**.

   [![Screenshot of the Export window with Excel and With Expand/Collapse selected.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/configure-excel-export.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/configure-excel-export.png#lightbox)
4. When the download is ready, open or save the Excel file from your browser's Downloads notification.

   [![Screenshot of the browser Downloads notification for the exported Excel file.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/download-excel-export.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/download-excel-export.png#lightbox)
5. Repeat the export and select **PDF** in the **Export** window. Select **Entire Matrix**, and then select **Export**.

   [![Screenshot of the Export window with PDF selected and the browser Downloads notification.](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/download-pdf-export.png)](../../media/planning-tutorial/intelligence/tutorial-10-build-profit-and-loss-intelligence/download-pdf-export.png#lightbox)

## Outcome

You now have a P&L intelligence sheet that:

- Uses the Enterprise Dataset semantic model with a Matrix visual and Financial template.
- Includes calculated and input rows for Gross Margin %, Shares Outstanding, and Earnings Per Share.
- Groups, hides, reorders, and formats P&L rows and columns.
- Includes Approval Status and Stakeholder fields.
- Includes a report header and logo.
- Can be exported to Excel and PDF.

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
