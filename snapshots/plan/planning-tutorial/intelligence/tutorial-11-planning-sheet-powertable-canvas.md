---
title: "Fabric planning tutorial part 11: Create a planning sheet, PowerTable, and canvas integration"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas) · Last updated on **2026-09-15**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Fabric planning tutorial part 11: Create a planning sheet, PowerTable, and canvas integration

Summarize this article for me

In this tutorial, you create a planning sheet named `Financial Plan`, add a simulation based on the **Plan** measure, and embed the planning sheet in an intelligence sheet. You then create a PowerTable named `Sales Detail`, connect it to the Enterprise Dataset semantic model, and embed it alongside the planning sheet.

## Prerequisites

Before you begin, ensure that you have:

- Access to a Microsoft Fabric workspace with planning and permission to create planning sheets, intelligence sheets, and PowerTable sheets.
- Access to the Enterprise Dataset semantic model.
- Completed [Build a P&L intelligence sheet](tutorial-10-build-profit-and-loss-intelligence).
- The Enterprise Dataset sample. You can download the sample from the [Fabric samples GitHub repository](https://github.com/jagan0506/fabric-samples/blob/add-plan-enterprise-dataset/docs-samples/iq/plan/Enterprise%20Dataset.pbix).

## Create a planning sheet

Create a planning sheet named `Financial Plan`, connect the account hierarchy and measures, and configure the display.

1. On the **Home** tab, select **New Planning Sheet**.

   [![Screenshot of the Home tab with New Planning Sheet selected.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/create-planning-sheet.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/create-planning-sheet.png#lightbox)
2. When prompted, enter `Financial Plan` as the name, and then select **Create**.
3. On the right, select the **Fields** tab.
4. In the **Data** pane, expand **[Dim] Account**, and then select **Account Hierarchy**.
5. Add **Account Hierarchy** to **Rows**.
6. Under **Measures** > **Financial** > **Base Measures**, add **Actuals**, **Plan**, and **Forecast** to **Values**.

   [![Screenshot of the Fields and Data panes with Account Hierarchy and Actuals, Plan, and Forecast selected.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/configure-planning-sheet-fields.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/configure-planning-sheet-fields.png#lightbox)
7. On the **Format** tab, select **Appearance**. Search for `Ragged`, and turn on **Ragged Hierarchy**.

   [![Screenshot of the Appearance pane with Ragged Hierarchy search results and the toggle.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/enable-ragged-hierarchy.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/enable-ragged-hierarchy.png#lightbox)

   Ragged hierarchy formatting displays the account hierarchy without showing blank levels for accounts that don't use every hierarchy level.
8. Select **Auto Fit** > **Fit to Content** to widen the columns to fit their content.

   [![Screenshot of the Auto Fit menu with Fit to Content selected for the planning sheet columns.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/fit-column-to-content.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/fit-column-to-content.png#lightbox)

## Add a planning simulation

Insert a simulation column based on **Plan**, set its value range, and enter scenario adjustments.

1. Select the **Plan** column header.
2. On the **Planning** tab, select **Insert Column** > **Simulate**. If prompted to save the planning sheet, confirm the save and continue.

   [![Screenshot of the Planning tab with Insert Column and Simulate selected.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/insert-simulation-column.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/insert-simulation-column.png#lightbox)
3. In the **Simulation** pane, keep **Simulation based on** set to **Plan**.
4. Set **Value Range** to `10`, and then select **Create**.

   [![Screenshot of the Simulation pane with Plan selected as the simulation basis and Value Range set to 10.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/configure-simulation-column.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/configure-simulation-column.png#lightbox)

   The **Plan (Simulation)** column appears on the planning sheet. The simulation provides an editable scenario value that is based on the selected measure. You can adjust values by using the slider or by entering a value directly in a cell.
5. In the **Plan (Simulation)** column, apply these adjustments:

   | Account | Adjustment | How to enter |
   | --- | --- | --- |
   | *Hardware Revenue* | +5% | Select the cell and enter the percentage increase, or use the simulation slider. |
   | *Subscription Revenue* | â2% | Select the cell and enter the percentage decrease, or use the simulation slider. |
   | *Advertising & Promotion* | â6% | Select the cell and enter the percentage decrease, or use the simulation slider. |
   | *Digital Marketing* | $120M | Select the cell, enter `120m`, and press Enter. |

   [![Screenshot of Plan Simulation cells showing percentage adjustments and a 120m value entered for Digital Marketing.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/enter-simulation-adjustments.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/enter-simulation-adjustments.png#lightbox)
6. Verify that the **Plan (Simulation)** column reflects the updated scenario. You can adjust additional cells if needed.
7. Select **Save**.

   [![Screenshot of the planning sheet with Save selected after the simulation adjustments are entered.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/save-planning-sheet.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/save-planning-sheet.png#lightbox)

## Embed the planning sheet in an intelligence sheet

Embed `Financial Plan` in the intelligence sheet so that users can edit the planning data and view related visuals on the same canvas.

1. In the **Explorer** tab, select the intelligence sheet that you created in the previous tutorial.

   [![Screenshot of the Explorer tab showing the Intelligence sheet and Financial Plan sheet.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/switch-to-intelligence-sheet.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/switch-to-intelligence-sheet.png#lightbox)
2. On the **Visualization** tab, select **Planning**.

   [![Screenshot of the Visualizations pane with the Planning visual selected.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/select-planning-visual.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/select-planning-visual.png#lightbox)
3. In the sheet picker, select `Financial Plan`, and then select **Add**.

   [![Screenshot of the Select an Existing Planning Sheet window with Financial Plan selected and Add highlighted.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/select-planning-sheet-to-embed.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/select-planning-sheet-to-embed.png#lightbox)
4. Resize and reposition the embedded planning sheet alongside the existing visuals as needed.

## Add a KPI that uses the semantic model and planning sheet

Create a KPI that compares values from the semantic model with the simulated values from the embedded planning sheet.

1. On the **Visualization** tab, select **KPI Cards**, and then drag the visual onto the canvas.
2. In the KPI field well, add these fields from the semantic model:

   - **Comparison 1 (vs Actuals)**: **Measures** > **Financial** > **Base Measures** > **Plan**
   - **Comparison 2 (vs Actuals)**: **Measures** > **Financial** > **Base Measures** > **Actuals**
   - **Trellis Row**: **[Dim] Account** > **Account Level 3**
3. In the field well, expand **From Sheets** and select the embedded `Financial Plan` sheet.
4. Add **Plan (Simulation)** from **Financial Plan** to **Actuals**.

   [![Screenshot of the KPI field well with Actuals using Plan Simulation from Financial Plan, Plan and Actuals as comparisons, and Account Level 3 as the trellis row.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/configure-kpi-fields.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/configure-kpi-fields.png#lightbox)
5. Verify that the KPI displays **Plan (Simulation)** from the planning sheet alongside **Actuals** and **Plan**.
6. Change a value in the embedded planning sheet and verify that the **Plan (Simulation)** series updates in the KPI.

   [![Screenshot of the intelligence sheet showing the embedded planning sheet and KPI after a simulation value is changed.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/test-live-kpi-update.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/test-live-kpi-update.png#lightbox)

   Changes to the simulation values are reflected in the KPI without recreating the visual.

## Create a PowerTable sheet

Create a PowerTable sheet named `Sales Detail` and create an app that stores PowerTable metadata in a Fabric SQL database.

1. In the plan, select **New PowerTable Sheet**. You can also select the **PowerTable** icon on the landing page.

   [![Screenshot of the Home tab with New PowerTable Sheet selected.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/create-powertable-sheet.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/create-powertable-sheet.png#lightbox)
2. Enter `Sales Detail` as the name, and then select **Create**.
3. On the PowerTable welcome page, select **Create a New App**.

   [![Screenshot of the PowerTable welcome page with Create a New App selected.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/create-powertable-app.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/create-powertable-app.png#lightbox)

## Connect PowerTable to a Fabric SQL database

Connect the PowerTable app to a Fabric SQL database where app metadata is stored.

1. Under **Select a Connection**, select your Fabric SQL connection. If a suitable connection doesn't exist, create a new connection.
2. Under **Database Name**, select the Fabric SQL database where app metadata is stored, and then select **Add**.

   [![Screenshot of the OneLake catalog with Fabric SQL databases available for selection.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/select-fabric-sql-database.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/select-fabric-sql-database.png#lightbox)
3. Select **Connect**.

## Create the Sales Detail table

Create a new table and populate it from the Enterprise Dataset semantic model.

1. Select **New Table** > **New Table** (Import data and create a new table).
2. Select a **Schema**, and enter `Sales Detail` in **Table Name**.
3. Under **Import Data**, select **Connect To Semantic Model**.
4. Under **Select a Connection**, select your DMTS connection. Under **Semantic Model**, select **Enterprise Dataset**, and then select **Next**.

   [![Screenshot of the Select Table window configured to import data from the Enterprise Dataset semantic model.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/configure-semantic-model-connection.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/configure-semantic-model-connection.png#lightbox)

## Map fields and set the primary key

Map product and financial fields from the semantic model and use **Product Name** as the primary key.

1. In the **Configure Semantic Model** pane, use the semantic model tree to select fields.
2. Add these fields to **Fields**:

   - **[Dim] Product** > **Category**
   - **[Dim] Product** > **Product Name**
3. Add these measures to **Values**:

   - **Measures** > **Financial** > **Base Measures** > **Actuals**
   - **Measures** > **Financial** > **Base Measures** > **Plan**

   [![Screenshot of the Configure Semantic Model panel with Category, Product Name, Actuals, and Plan mapped.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/configure-powertable-semantic-model-fields.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/configure-powertable-semantic-model-fields.png#lightbox)
4. In the **Fields** list, select the three-dot menu next to **Product Name**, and then select **Set as Primary Key**.

   [![Screenshot of the Product Name field menu with Set as Primary Key selected.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/set-product-name-primary-key.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/set-product-name-primary-key.png#lightbox)
5. If needed, select the **Filter** tab to restrict the values that are imported.

   [![Screenshot of the Filter tab with Hardware, SaaS, and Services selected for the Category filter.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/filter-imported-values.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/filter-imported-values.png#lightbox)
6. Select **Next**.

## Configure PowerTable columns

Review the detected column settings before creating the table.

1. Review the automatically detected settings for each column. Confirm or update the **Data Type**, **Input Type**, and **Display Name** as needed.
2. Confirm the primary key selection and enter default values where required.

   [![Screenshot of the Configure Table page showing column data types, input types, primary key, and default value settings.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/configure-powertable-columns.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/configure-powertable-columns.png#lightbox)
3. Select **Finish** to create the table.
4. Select **Save** to save the PowerTable sheet.

## Embed the PowerTable in the intelligence sheet

Add the `Sales Detail` PowerTable to the intelligence sheet alongside the embedded planning sheet.

1. In the **Explorer** tab, select the intelligence sheet.
2. On the **Visualization** tab, select **PowerTable**.

   [![Screenshot of the Visualizations pane with PowerTable selected.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/select-powertable-visual.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/select-powertable-visual.png#lightbox)
3. In the PowerTable picker, select `Sales Detail`, and then select **Add**.

   [![Screenshot of the Select an Existing PowerTable window with Sales Detail selected.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/select-powertable-to-embed.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/select-powertable-to-embed.png#lightbox)
4. Resize and reposition the PowerTable alongside the embedded planning sheet so that users can view the simulation and product-level detail on the same canvas.

   [![Screenshot of the intelligence sheet canvas showing the embedded planning sheet, KPI visuals, and Sales Detail PowerTable together.](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/view-embedded-planning-and-powertable.png)](../../media/planning-tutorial/intelligence/tutorial-11-planning-sheet-powertable-canvas/view-embedded-planning-and-powertable.png#lightbox)

## Outcome

You now have an intelligence sheet that:

- Includes a `Financial Plan` planning sheet with **Actuals**, **Plan**, and **Forecast** mapped to the **Account Hierarchy**.
- Includes a **Plan (Simulation)** column with a value range of `10` and four scenario adjustments.
- Displays simulation results in a KPI that combines semantic model data with data from the embedded planning sheet.
- Includes a `Sales Detail` PowerTable connected to the Enterprise Dataset semantic model.
- Uses **Product Name** as the primary key and includes configured PowerTable columns.
- Displays the planning sheet and PowerTable together on the intelligence sheet canvas.

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
