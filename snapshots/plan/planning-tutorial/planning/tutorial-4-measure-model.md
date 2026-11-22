---
title: "Fabric planning tutorial part 4: Build a P&L hierarchy using measure model builder"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-4-measure-model](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-4-measure-model) · Last updated on **2026-09-08**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Fabric planning tutorial part 4: Build a P&L hierarchy using measure model builder

Summarize this article for me

In this tutorial, you build and configure a *Measure Model* by organizing native and formula measures into a hierarchical P&L structure. Then, you create two scenarios in the Tree layout and compare them to see the real-time impact of revenue growth and cost restructuring on net profit.

## Prerequisites

Before you start this tutorial, ensure you complete the first tutorial: [Fabric planning tutorial part 0: Introduction and environment setup](tutorial-0-introduction)

## Configure a measure model

In this section, you set up the planning sheet and build a simple P&L model by using the Measure Model feature. Organize native measures into a parent-child hierarchy by using formula measures to turn a flat list of inputs into a structured P&L model.

1. In *Northwind\_FMCG\_Plan*, select **New Planning Sheet** in the **Home** ribbon. Enter *P&L â Measure model* and select **Create**.
2. Configure the field assignments from the P&L Measures table as follows:

   | Field | Value |
   | --- | --- |
   | Rows | Region hierarchyâ Region â Cities |
   | Columns | Date hierarchyâYear, Quarter, Month |
   | Values | All the measures from the P&L Measures table |
3. Double-click each measure label and remove the "Sum of" prefix to improve readability. Select the three dots (â®) next to *Avg Selling Price* in the **Values** field and select **Average** from the dropdown. This change populates the average selling price instead of the summed value.

   [![Screenshot of dimensions and measures assigned to rows, columns, and values to build a P&L hierarchy.](../../media/planning-tutorial/planning/tutorial-4-measure-model/assign-dimensions-measures-pnl-hierarchy.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/assign-dimensions-measures-pnl-hierarchy.png#lightbox)
4. Go to the **Model** ribbon and select **Measure Model**. The measure model canvas opens.
5. To create a formula measure for *Gross Revenue,* first drag *Sales Volume* and *Avg Selling Price* into the **Drop from measure list** section at the bottom of the canvas.
6. Select **Add Measure** > **Formula**. Name it *Gross Revenue* and enter the formula `[Sales Volume]*[Avg Selling Price]`. Select **Create**.

   Note

   Ensure the row and column aggregation type is set to Formula for all the formula measures you create.

   [![Screenshot of row and column aggregation set to Formula for the Gross Revenue measure.](../../media/planning-tutorial/planning/tutorial-4-measure-model/create-formula-measure-gross-revenue.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/create-formula-measure-gross-revenue.png#lightbox)

   *Gross Revenue* is added to the measure list.

   [![Screenshot of the Gross Revenue calculated measure added to the measure list.](../../media/planning-tutorial/planning/tutorial-4-measure-model/gross-revenue-added-measure-list.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/gross-revenue-added-measure-list.png#lightbox)
7. Drag the new *Gross Revenue* measure onto the canvas. Drag the *Sales Volume* and *Avg Selling Price* onto the *Gross Revenue* row â the measures snap into place as children. Observe that *Gross Revenue* becomes the parent of *Sales Volume* and *Avg Selling Price*.

   [![Animation showing how to add the Gross Revenue measure and create a hierarchy.](../../media/planning-tutorial/planning/tutorial-4-measure-model/create-measure-hierarchy-gross-revenue.gif)](../../media/planning-tutorial/planning/tutorial-4-measure-model/create-measure-hierarchy-gross-revenue.gif#lightbox)
8. Drag *Discounts and Returns* onto the canvas. Follow the same steps to create a *Net Revenue* measure by using the formula `[Gross Revenue] â [Discounts and Returns]`.
9. Drag *Net Revenue* onto the canvas. Then drag *Gross Revenue* and *Discounts and Returns* under the *Net Revenue* row. Observe that *Net Revenue* becomes the parent of *Gross Revenue* and *Discounts and Returns*.

   [![Screenshot of creating a hierarchy with Net Revenue as the parent.](../../media/planning-tutorial/planning/tutorial-4-measure-model/create-measure-hierarchy-net-revenue.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/create-measure-hierarchy-net-revenue.png#lightbox)
10. Create a formula measure for COGS by using the formula: `[Raw Material Cost]+[Labor Cost]+[Other Direct Exp]`. Drag the COGS measure onto the canvas.
11. Select *Raw Material Cost*, *Labor Cost*, and *Other Direct Exp*. From the **Insert Measure** dropdown, select **COGS**, and then select **Insert**.

    [![Screenshot of the insert measure option to create a hierarchy under the COGS measure.](../../media/planning-tutorial/planning/tutorial-4-measure-model/insert-measure-hierarchy-cogs.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/insert-measure-hierarchy-cogs.png#lightbox)

    The *COGS* measure becomes the parent of *Raw Material Cost*, *Labor Cost*, and *Other Direct Exp*.

    [![Screenshot of the measure hierarchy showing Raw Material Cost, Labor Cost, and Other Direct Exp nested under COGS.](../../media/planning-tutorial/planning/tutorial-4-measure-model/cogs-measure-hierarchy.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/cogs-measure-hierarchy.png#lightbox)
12. In the same way, create the following calculated measures:

    | Measure | Formula |
    | --- | --- |
    | Gross Profit | `[Net revenue] â [COGS]` |
    | Operating Expenses | `[Admin Expenses]+[Employee Expenses]+[R&D]+[Selling and Marketing Expenses]` |
    | Net Profit | `[Gross Profit] â [Operating Expenses]` |

    The final P&L hierarchy is shown in the following image:

    [![Screenshot of the final P&L hierarchy created in the measure model canvas.](../../media/planning-tutorial/planning/tutorial-4-measure-model/pnl-measure-hierarchy-model-canvas.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/pnl-measure-hierarchy-model-canvas.png#lightbox)

## View the P&L model

In this section, you view the P&L model in the **Measures in Rows** layout.

1. Select **Back to Home** at the top of the measure model canvas. In the **Planning** ribbon, select the **Layout** dropdown and select **Measures In Rows**.
2. Observe that the configured measure hierarchy is now displayed â a structured P&L view of the calculated measures and their underlying components, replacing the flat list from the setup step.

   [![Screenshot of the P&L model displayed in the Measures in Rows layout in a planning sheet.](../../media/planning-tutorial/planning/tutorial-4-measure-model/profit-loss-model-measures-rows-layout.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/profit-loss-model-measures-rows-layout.png#lightbox)

### Create best case and cost restructuring scenarios

In this section, you create two scenarios in the **Tree** layout â one to simulate revenue growth in *Sydney* and one to simulate restructuring costs in *London*.

### Create best-case scenario

In this section, you create a best-case scenario in the tree layout and simulate revenue growth for the *Sydney* node. The measure hierarchy updates in real time as you adjust each input.

1. In the **Planning** ribbon, select **Layout** and select **Tree**. The P&L model displays in tree view, breaking down from the grand total through regions and cities with the measure hierarchy.

   [![Screenshot of displaying the P&L hierarchy by using the tree view layout.](../../media/planning-tutorial/planning/tutorial-4-measure-model/pnl-hierarchy-tree-view.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/pnl-hierarchy-tree-view.png#lightbox)
2. Select **Display** in the **Tree View** ribbon. In the **Display Settings** side panel, turn off **Show Header KPI**.
3. Select **Create Scenario** and name it *Best Case.* Ensure that all measures from the semantic model are included in the series, and select **Create**.

   [![Screenshot of creating the best case scenario in Tree View.](../../media/planning-tutorial/planning/tutorial-4-measure-model/create-best-case-scenario-tree-view.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/create-best-case-scenario-tree-view.png#lightbox)
4. Under the *Asia Pacific* region, select the *Sydney* card. The simulation dialog box opens.
5. In the *Measure Simulation* dropdown, simulate the following under *Gross Revenue*:

   - Sales Volume: 5%
   - Avg Selling Price: 2%
   - Discounts and Returns: â5%

   [![Screenshot of the Measure Simulation dialog with Gross Revenue inputs simulated for the Asia Pacific Sydney card.](../../media/planning-tutorial/planning/tutorial-4-measure-model/scenario-simulations-sydney-region.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/scenario-simulations-sydney-region.png#lightbox)
6. Close the simulation dialog. Observe that the *Sydney* card updates in real time â *Net Profit*, *Gross Profit*, and *Net Revenue* show the upward variance indicators as each input is adjusted. The *Asia Pacific* and the *All* cards also update to reflect the change.

   [![Screenshot of the Sydney, Asia Pacific, and All cards updated with simulated values in the measure tree.](../../media/planning-tutorial/planning/tutorial-4-measure-model/sydney-asia-pacific-all-card-updated.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/sydney-asia-pacific-all-card-updated.png#lightbox)

### Cost restructuring scenario

In this section, you create a *Cost Restructuring* scenario and simulate reduced costs for the *London* node. This scenario lets you compare a cost-focused approach against the best case revenue-growth approach.

1. Select **Create Scenario** and name it *Cost Restructuring*. Ensure that the series includes all measures from the semantic model, and select **Create**.
2. Confirm you can see the new scenario in the bottom left. Under the *Europe* region, select the *London* card. The simulation dialog box opens. Select **Value**. Scroll down and simulate the following values under COGS and Operating Expenses:

   - Raw Material Cost: 400k
   - Labor Cost: 150k
   - Employee Expenses: 120k
   - Selling and Marketing Expenses: 160k

   [![Screenshot of the simulation dialog showing simulated COGS and operating expense values for the London card.](../../media/planning-tutorial/planning/tutorial-4-measure-model/cost-restructuring-simulation.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/cost-restructuring-simulation.png#lightbox)
3. Close the simulation dialog box. Select the down arrow on the *London* card and *Europe* cards. Observe that the cards update in real time. The full P&L cascade is visible on the card, showing how the restructured cost inputs flow through COGS, Operating Expenses, Gross Profit, and Net Profit.

   [![Screenshot of cost restructuring simulation changes applied to all related cards.](../../media/planning-tutorial/planning/tutorial-4-measure-model/cost-restructuring-simulation-updated-cards.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/cost-restructuring-simulation-updated-cards.png#lightbox)

## Compare scenarios

In this section, you compare the best case scenario with the cost restructuring scenario by using the **Compare Scenarios** feature.

1. In the **Tree View** ribbon, select **Compare Scenario**.
2. Configure the comparison with the following settings:

   - **Compare**: Best Case
   - **With**: Cost Restructuring
3. Observe the variance columns. The compare view places both scenarios side by side at every level of the hierarchy, making the difference immediately visible between a revenue growth approach and a cost restructuring approach.

   [![Screenshot of comparing the best case and cost restructuring scenarios with the variances calculated.](../../media/planning-tutorial/planning/tutorial-4-measure-model/compare-best-case-cost-restructuring-scenarios.png)](../../media/planning-tutorial/planning/tutorial-4-measure-model/compare-best-case-cost-restructuring-scenarios.png#lightbox)
4. Select **Exit Compare** to return to the tree view.

## Next steps

Build a P&L row model in the next tutorial, [Build a P&L hierarchy using row model builder](tutorial-5-row-model)

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
