---
title: "Fabric planning tutorial part 2: Optimize data input measures to achieve a target result"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-2-optimizer](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-2-optimizer) · Last updated on **2026-09-21**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Fabric planning tutorial part 2: Optimize data input measures to achieve a target result

Summarize this article for me

The Optimizer feature is an automated, goal-seeking tool designed to eliminate manual trial and error when adjusting budget and planning numbers.

When you set a target for a calculated result (such as Gross Profit or Net Margin), the Optimizer automatically back-calculates and adjusts your editable data input measures (like Sales Growth % or COGS reduction) to reach that exact financial goal.

In this tutorial, you build a Gross Profit sheet, create a formula measure, and run the Optimizer to find the combination of revenue growth and cost reduction that achieves a $12.5M gross profit target.

## Prerequisites

Before you start this tutorial, ensure you complete the first tutorial: [Fabric planning tutorial part 0: Introduction and environment setup](tutorial-0-introduction)

## Set up the Gross Profit sheet

In this section, you create a Gross Profit sheet that pulls in the sales plan from another planning sheet and COGS from the semantic model. This sheet is the starting point for running the Optimizer.

1. In the **Home** ribbon, select **New Planning Sheet**. Enter *Gross Profit* and select **Create**.
2. Configure the field assignments:

   | Field | Value |
   | --- | --- |
   | Rows | Region Name â Category â Sub-category |
   | Columns | Date hierarchy |
   | Values | 2026 Sales Plan from **From Sheets** > Plan Intro; COGS 2025 from the measures table in the semantic model. |

   Tip

   Connect planning sheets by using columns from other planning sheets within the same plan item. This feature lets one planning sheet use data from another, making it possible to link related planning activities.
3. Double-click the **Sum of 2026 Sales Plan** label in the **Values** field and rename it to 2026 Sales Plan.

   [![Screenshot of mapping dimensions and measures from the semantic model and the intro planning sheet to the rows, columns, and values data wells.](../../media/planning-tutorial/planning/tutorial-2-optimizer/map-sales-plan-dimensions-data-wells.png)](../../media/planning-tutorial/planning/tutorial-2-optimizer/map-sales-plan-dimensions-data-wells.png#lightbox)

## Create editable input columns

In this section, you create editable copies of the Sales Plan and COGS columns.

Note

The Optimizer requires editable data input columns. You can't edit the original measures from other planning sheets or the semantic model measures. The source measures remain unchanged and can serve as a baseline for comparison after the Optimizer runs.

1. In the **Planning** ribbon, select **Number** > **Copy from another series** > **2026 Sales Plan**. Enter *Sales Plan* as the title and select **Create**.
2. In the **Planning** ribbon, select **Number** > **Copy from another series** > **2025 COGS**. Enter *COGS* as the title and select **Create**.
3. In the **Planning** ribbon, select **Show Columns** and hide the original *2026 Sales Plan* and *2025 COGS* columns. The editable Sales Plan and COGS input columns remain visible.

   [![Screenshot of creating data input measures from COGS and Sales Plan and using the Show Columns option to hide the original measures.](../../media/planning-tutorial/planning/tutorial-2-optimizer/hide-cogs-sales-plan-original-measures.png)](../../media/planning-tutorial/planning/tutorial-2-optimizer/hide-cogs-sales-plan-original-measures.png#lightbox)

## Calculate gross profit

In this section, you add a formula column that calculates Gross Profit from the Sales Plan and COGS input columns. This calculated value becomes the base on which the optimizer is applied.

1. In the **Planning** ribbon, select **Formula** and configure it as follows, and then select **Create**:

   | Setting | Value |
   | --- | --- |
   | Title | Gross Profit |
   | Formula | [Sales Plan] - [COGS] |
   | Column aggregation | Formula |
   | Row aggregation | Formula |
2. *Gross Profit* appears in the grid, calculated from the two input columns. Collapse the row hierarchy to the category level. In the **Planning** ribbon, select **Totals** and enable **Column Grand Total** on the left.

   [![Screenshot of creating the gross profit calculated measure.](../../media/planning-tutorial/planning/tutorial-2-optimizer/create-gross-profit-formula-enable-totals.png)](../../media/planning-tutorial/planning/tutorial-2-optimizer/create-gross-profit-formula-enable-totals.png#lightbox)

## Run and apply the optimizer

In this section, you run the optimizer to find the combination of *Sales Plan* and *COGS* values that achieves the $12.5M Gross Profit target. You then apply the optimized values to the sheet.

1. Select the *Gross Profit* grand total cell. In the **Planning** ribbon, select **Optimize**.
2. In **OptimizerâObjectives and Variables**, configure as follows and select **Next**:

   | Setting | Value |
   | --- | --- |
   | Objective | Target |
   | Target value | 12.5m |
   | Variables to update | Sales Plan, COGS |

   [![Screenshot of setting the objective to target and selecting the COGS and Sales Plan measures as optimizer variables.](../../media/planning-tutorial/planning/tutorial-2-optimizer/optimizer-set-objective-select-variables.png)](../../media/planning-tutorial/planning/tutorial-2-optimizer/optimizer-set-objective-select-variables.png#lightbox)
3. On the **Add Constraints** page, select **Run** without adding constraints.
4. On the **Output** screen, confirm **Target Value** shows 12.5M and **Achieved** shows 12.5M with a green check mark. Under **Variables**, observe that the optimizer calculated the optimal combination of *Sales Plan* and *COGS* to reach the gross profit target.

   [![Screenshot of the output screen with the achieved target value and optimized data inputs.](../../media/planning-tutorial/planning/tutorial-2-optimizer/optimized-variables-target-value-achieved.png)](../../media/planning-tutorial/planning/tutorial-2-optimizer/optimized-variables-target-value-achieved.png#lightbox)
5. Select **Apply**. The optimized values are written to the sheet.

   [![Screenshot of applying the optimized values to the planning sheet.](../../media/planning-tutorial/planning/tutorial-2-optimizer/planning-sheet-updated-optimized-values.png)](../../media/planning-tutorial/planning/tutorial-2-optimizer/planning-sheet-updated-optimized-values.png#lightbox)
6. In the **Planning** ribbon, select **Show Columns** and enable *2026 Sales Plan* and *2025 COGS*. The original and optimized columns appear side by side:

   - Sales Plan: $26.38m vs original $26.1mâan increase of $0.28m
   - COGS: $13.88m vs original $14.17mâa reduction of $0.29m

   Together, these two adjustments deliver the $12.5M gross profit target.

   [![Screenshot of comparing the optimized values with the baseline values for Sales Plan and COGS.](../../media/planning-tutorial/planning/tutorial-2-optimizer/compare-original-baseline-optimized-values.png)](../../media/planning-tutorial/planning/tutorial-2-optimizer/compare-original-baseline-optimized-values.png#lightbox)

## Next steps

In the next tutorial, [Forecasting and writeback](tutorial-3-forecasting-writeback), create a rolling forecast, use Predict to create a statistical forecast, and write the forecast values to a SQL database.

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
