---
title: "Fabric planning tutorial part 5: Build a P&L hierarchy using row model builder"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-5-row-model](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-5-row-model) · Last updated on **2026-11-05**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Fabric planning tutorial part 5: Build a P&L hierarchy using row model builder

Summarize this article for me

In this tutorial, you build and configure a row-based P&L model using the Row Model Builder by defining Net Profit as the root, organizing Gross Revenue, Net Revenue, COGS, and Operating Expenses into a connected hierarchy, and configuring formula and aggregate relationships to see how driver-level inputs roll up to Net Profit in real time.

## Prerequisites

Before you start this tutorial, ensure you complete the first tutorial: [Fabric planning tutorial part 0: Introduction and environment setup](tutorial-0-introduction)

## Configure a row model

In this section, you build a P&L hierarchy from scratch using Row Model Builder, starting from Net Profit and adding Gross Profit, Net Revenue, COGS, and Operating Expenses as connected nodes. Formula and data source rows define how each level calculates from the ones beneath it.

1. In *Northwind\_FMCG\_Plan*, select **New Planning Sheet** in the **Home** ribbon. Enter P&L â Row model and select **Create**.
2. Configure the field assignments from the P&L Rows as follows:

   | Field | Value |
   | --- | --- |
   | Rows | Account |
   | Columns | Date hierarchyâYear, Quarter, Month |
   | Values | Value |

   [![Screenshot of dimension and measure assignments from the P&L Rows table.](../../media/planning-tutorial/planning/tutorial-5-row-model/row-model-data-assignments.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/row-model-data-assignments.png#lightbox)
3. Go to the **Model** ribbon and select **Row Model**. The **Model Builder** dialog appears. Select **Enable**.
4. In the **Row Model** window, select the box corresponding to **Row Name**. Retain only the root node that is the *All* row, and delete the rest of the rows. Deselect the **All** row. Select **Delete**.

   [![Screenshot of the Row Model interface and selecting the rows to delete.](../../media/planning-tutorial/planning/tutorial-5-row-model/row-model-delete-rows-except-all-node.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/row-model-delete-rows-except-all-node.png#lightbox)

   A warning message appears asking for confirmation. Select **Delete**. The canvas is now ready to build a new row model.
5. Select the *All* row and select the edit icon. In the side pane, set the **Row Name** to *Net Profit*. In the **Configure as** dropdown, select **Formula**. Select **Apply**.

   Note

   You enter the formula for *Net Profit* after creating all the other nodes in the row model.

   [![Screenshot of configuring the root row as a formula row named Net Profit in the side pane.](../../media/planning-tutorial/planning/tutorial-5-row-model/add-net-profit-root-row-formula.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/add-net-profit-root-row-formula.png#lightbox)

   This action replaces the root node (*All* row) with *Net Profit*.
6. Select the *Net Profit* row. Select **Add Child** > **Formula**.

   [![Screenshot of selecting the Net Profit row and using the Add Child option.](../../media/planning-tutorial/planning/tutorial-5-row-model/select-net-profit-add-child.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/select-net-profit-add-child.png#lightbox)
7. Select the edit icon, name it *Gross Profit*, and select **Apply** to add *Gross Profit* as a child under *Net Profit*.

   [![Screenshot of Gross Profit added as a child row under Net Profit.](../../media/planning-tutorial/planning/tutorial-5-row-model/gross-profit-added-child-row.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/gross-profit-added-child-row.png#lightbox)
8. Select *Gross Profit*. Select **Add Child** > **Formula**. A new child row is added under *Gross Profit*. Select the edit icon, name it *Net Revenue*, and select **Apply**.
9. Select *Net Revenue*. Select **Add Child** > **Data Source**. Select the edit icon, name it *Gross Revenue*.
10. In **Choose Close Period Source Row**, select the corresponding source row from the semantic model. In this case, search for and select *Gross Revenue*. Select **Apply**.

    [![Screenshot of the configuration to create a Gross Revenue row by selecting the Choose Close Period Source Row.](../../media/planning-tutorial/planning/tutorial-5-row-model/side-pane-gross-revenue-data-source.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/side-pane-gross-revenue-data-source.png#lightbox)

    This action adds *Gross Revenue* as a child node under *Net Revenue.*

    [![Screenshot of the Gross Revenue data source row added as a child node under Net Revenue in the row model.](../../media/planning-tutorial/planning/tutorial-5-row-model/gross-revenue-child-node-net-revenue.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/gross-revenue-child-node-net-revenue.png#lightbox)
11. Select *Gross Revenue*. Select **Add Sibling** > **Data Source**. Select the edit icon, and name the row *Returns and Breakage.*
12. Select **Choose Close Period Source Row,** search for and select *Returns and Breakage* from the semantic model. Select **Apply**.
13. In the same way, add *Distribution Allowance & Rebates* and *Federal & State Excise Taxes* as siblings to *Gross Revenue* under *Net Revenue*.

    [![Screenshot of inserting sibling rows for the Gross Revenue row.](../../media/planning-tutorial/planning/tutorial-5-row-model/insert-sibling-rows-net-revenue.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/insert-sibling-rows-net-revenue.png#lightbox)
14. Select the **Configure Formula** box on the *Net Revenue* row. Enter the following formula in the formula box: `[Gross Revenue] -[Returns and Breakage] - [Distribution Allowance & Rebates] - [Federal & State Excise Taxes]` .
15. While typing the formula, you can select from the suggestions that appear as you start typing. To access help suggestions with examples, press **Ctrl + Space** with the cursor in the formula box. A suggestions pop-up opens with two tabs: **References** and **Functions**.

    - Select the **References** tab to reference and add the row names you want in the formula.
    - Select the **Functions** tab to view the list of supported functions. Select one to view its syntax and example and then insert it.
16. For hierarchical rows, typing a row reference in the formula box inserts the full path from the root node to the referenced row, as shown in the following image. Verify the row path to ensure that you reference the correct row.

    [![Screenshot of the Net Revenue formula pane where row references expand to full paths like [Gross Profit].[Net Revenue].[Gross Revenue].](../../media/planning-tutorial/planning/tutorial-5-row-model/hierarchical-row-formula.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/hierarchical-row-formula.png#lightbox)
17. Select **Apply**.

    [![Screenshot of entering the formula for net revenue.](../../media/planning-tutorial/planning/tutorial-5-row-model/enter-net-revenue-formula.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/enter-net-revenue-formula.png#lightbox)
18. Select *Net Revenue*. Select **Add Sibling** > **Aggregate**. Select the edit icon, name the row *COGS*, and select **Apply**.
19. In the same way you created Gross Revenue in step 10, to create children under the COGS row, select **Add Child** > **Data Source** and create rows for the following categories:

    - Brewing Materials
    - Packaging, Plant Overhead and Maintenance
    - Water & Utilities

    [![Screenshot of creating a hierarchy with child data source rows under the COGS row in the row model.](../../media/planning-tutorial/planning/tutorial-5-row-model/create-cogs-hierarchy.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/create-cogs-hierarchy.png#lightbox)
20. Enter the formula for *Gross Profit* as shown in the following image:

    [![Screenshot of entering the formula for Gross Profit.](../../media/planning-tutorial/planning/tutorial-5-row-model/gross-profit-formula.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/gross-profit-formula.png#lightbox)
21. Create a hierarchy for *Operating Expenses* by using the **Add Child** > **Data Source** option.

    [![Screenshot of creating a hierarchy for Operating Expenses using the Add Child data source option.](../../media/planning-tutorial/planning/tutorial-5-row-model/create-operating-expenses-hierarchy.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/create-operating-expenses-hierarchy.png#lightbox)
22. Finally, enter the formula for *Net Profit:* `[Gross Profit]-[Operating Expenses]`

    [![Screenshot of entering the formula for net profit.](../../media/planning-tutorial/planning/tutorial-5-row-model/enter-net-profit-formula.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/enter-net-profit-formula.png#lightbox)
23. Select **Back to Home**. Observe that the planning sheet now displays the full P&L hierarchy â *Net Profit* at the root, with *Gross Profit*, *Net Revenue*, *COGS*, and *Operating Expenses* as connected nodes. Expanding any node shows its contributing data source rows.

    [![Screenshot of the planning sheet showing the full profit and loss hierarchy with Net Profit at the root.](../../media/planning-tutorial/planning/tutorial-5-row-model/view-profit-loss-hierarchy-planning-sheet.png)](../../media/planning-tutorial/planning/tutorial-5-row-model/view-profit-loss-hierarchy-planning-sheet.png#lightbox)

## Next steps

In the next tutorial, [Consolidate plans across dimensions using cubes](tutorial-6-cube), allocate plans across multiple dimensions.

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
