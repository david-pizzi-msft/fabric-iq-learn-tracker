---
title: "Measure-based modeling"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-create-measure-model](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-create-measure-model) · Last updated on **2026-08-04**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Measure-based modeling

Summarize this article for me

Use measure-based modeling to organize the measures you define in a semantic model into a hierarchical structure that reflects business performance. This type of modeling enables you to analyze how changes in one measure affect related measures. For example, if material costs change, you can see how those changes cascade up to the net profit level.

Typically, when you place measures in the value field, they appear as column items. It's difficult to create a hierarchy for measures and analyze the performance. A measure model addresses this limitation by allowing you to build a measure hierarchy that you can apply across all row category items.

By using a measure model, you can:

- Organize measures according to business requirements.
- Perform planning and simulations at the measure level.
- Analyze the cascading impact of changes across the hierarchy in a single view.

## Configure measure-based model

1. Create a planning model by assigning dimensions and measures. Consider the revenue model in the following image.

   [![Screenshot of a planning sheet with the Fields pane highlighting Rows, Columns, and Values assignments.](media/planning-how-to-create-measure-model/planning-sheet-field-assignment-panel.png)](media/planning-how-to-create-measure-model/planning-sheet-field-assignment-panel.png#lightbox)
2. Go to the **Model** ribbon and select **Measure Model.**

   [![Screenshot of the Model ribbon with the measure model button highlighted.](media/planning-how-to-create-measure-model/model-ribbon-measure-model-button.png)](media/planning-how-to-create-measure-model/model-ribbon-measure-model-button.png#lightbox)

   This action opens the measure model canvas, that displays all the measures assigned to the planning sheet.

   [![Screenshot of the measure model canvas with the measures list highlighted.](media/planning-how-to-create-measure-model/measure-model-measures-list.png)](media/planning-how-to-create-measure-model/measure-model-measures-list.png#lightbox)
3. Create the required hierarchy using the measures list. Select **Add measure** > **Formula.**
4. In the side panel, enter the title and define the formula as shown in the following screenshot. Select **Create**.

   [![Screenshot of the Formula Measure panel with title *Gross Revenue*, formula [Sales Volume]*[Avg Selling Price], and Create button highlighted.](media/planning-how-to-create-measure-model/formula-measure-panel-gross-revenue.png)](media/planning-how-to-create-measure-model/formula-measure-panel-gross-revenue.png#lightbox)
5. The newly created measure is added to the measures list. Drag the measure, in this example, *Gross Revenue*, to the top section of the canvas to create a hierarchy.

   [![Screenshot of the measure model toolbar, Selected Measures panel, and arrow indicating dragging *Gross Revenue* onto the canvas.](media/planning-how-to-create-measure-model/drag-gross-revenue-measure-to-canvas.png)](media/planning-how-to-create-measure-model/drag-gross-revenue-measure-to-canvas.png#lightbox)
6. *Gross Revenue* is now available on the canvas screen. Select other measures such as *Sales Volume* and *Avg Selling Price* from the measure list. From the **Insert Measure** list, select the measure you created in the previous step, in this example, *Gross Revenue*, and select **Insert.**

   [![Screenshot of measure model with Sales Volume and Avg Selling Price selected, *Gross Revenue* chosen in Insert Measure, and Insert highlighted.](media/planning-how-to-create-measure-model/select-measures.png)](media/planning-how-to-create-measure-model/select-measures.png#lightbox)
7. The measures are now placed as child rows under *Gross Revenue*. This creates a **Gross Revenue** measure hierarchy.

   [![Screenshot of the measures grid showing *Gross Revenue* formula row with Sales Volume and Avg Selling Price as child rows.](media/planning-how-to-create-measure-model/measure-model-gross-revenue-hierarchy.png)](media/planning-how-to-create-measure-model/measure-model-gross-revenue-hierarchy.png#lightbox)
8. Drag another measure such as *Discount and Returns* to the **Drop from measure list** section. This measure is added outside the *Gross Revenue* hierarchy as a sibling of the *Gross Revenue* measure.

   [![Screenshot of dragging Discounts and Returns from the measure list into the Drop from measure list section on the canvas.](media/planning-how-to-create-measure-model/drag-discounts-returns-measure-drop-zone.png)](media/planning-how-to-create-measure-model/drag-discounts-returns-measure-drop-zone.png#lightbox)

   The following image shows all the measures added to the canvas.

   [![Screenshot of measures grid showing Name, Type, Configuration, and Aggregation columns with all four measures on the canvas.](media/planning-how-to-create-measure-model/measure-model-all-measures-added.png)](media/planning-how-to-create-measure-model/measure-model-all-measures-added.png#lightbox)

## Create measure hierarchy

1. Create a new calculated measure. Select **Add measure** and select **Formula**. Enter the title and define the formula. Select **Create**. In this example, the title is *Net Revenue* and the formula is **Gross Revenue* - Discount and Returns.*
2. Drag the *Net Revenue* measure onto the canvas. Drag the *Gross Revenue*\* measure below *Net Revenue* until it snaps into place as its child. Repeat this step for the *Discount and Returns* measure so that both measures appear as children of *Net Revenue*.

   [![Screenshot of measure model grid highlighting the *Net Revenue* hierarchy with *Gross Revenue*, Sales Volume, Avg Selling Price, and Discounts and Returns rows.](media/planning-how-to-create-measure-model/measure-model-net-revenue-hierarchy.png)](media/planning-how-to-create-measure-model/measure-model-net-revenue-hierarchy.png#lightbox)
3. After the measure hierarchy is created, select **Back to Home** in the toolbar.
4. To display the measures in rows, in the **Planning** ribbon, go to **Layout** > **Measures**. Select **In Rows**. This option displays the measures in a hierarchical structure under each row category.

   [![Screenshot of a measure model grid with Year, Quarter, and Month columns and the measure hierarchy highlighted.](media/planning-how-to-create-measure-model/measure-model-grid-measures-rows-layout.png)](media/planning-how-to-create-measure-model/measure-model-grid-measures-rows-layout.png#lightbox)

A measure model automatically cascades simulation impacts through both the measure hierarchy and the row hierarchy. This cascading effect enables users to understand how changes in business drivers affect overall performance. For example, suppose the sales volume of *Brazil* is increased through simulation; the impact is reflected in *Brazil*'s *Gross Revenue* and *Net Revenue*. The impact can also be seen on its parent *Latin America* up till the top level.

You can create multiple scenarios and perform simulations. You can compare these scenarios to understand which driver yields better performance for the business.

## Creating scenarios and performing simulations

This section explains how to create a scenario and perform simulations in a measure model to understand the impact on the overall business performance.

1. After you create the measure model, in the **Planning** ribbon, go to **Layout** and select **Tree**.
2. The model is displayed in a tree structure expanding from the grand total through regions and the measure hierarchy.

   [![Screenshot of Tree View tab displaying hierarchical measure cards and toolbar options like Create scenario and Compare scenario.](media/planning-how-to-create-measure-model/tree-view-measure-model-hierarchy.png)](media/planning-how-to-create-measure-model/tree-view-measure-model-hierarchy.png#lightbox)
3. In the **Tree View** ribbon, select **Display** and toggle off **Show Header KPI** for a cleaner view.

   [![Screenshot of Tree View ribbon with  Show Header KPI toggled off in Display Settings panel.](media/planning-how-to-create-measure-model/tree-view-toggle-header-kpi.png)](media/planning-how-to-create-measure-model/tree-view-toggle-header-kpi.png#lightbox)
4. Select **Create New Scenario** from the ribbon. Enter the **Scenario name**, in this example, *Best Case*.

   [![Screenshot of Create Scenario dialog with Scenario name field and series tags.](media/planning-how-to-create-measure-model/create-scenario-dialog-tree-view.png)](media/planning-how-to-create-measure-model/create-scenario-dialog-tree-view.png#lightbox)
5. Select any node in the tree. The simulation panel appears on the side. You can perform simulation by either entering a simulation percentage or using a slider.
   For example, for the *United States* node, apply the following changes:

   - Sales Volume: 5%
   - Avg Selling price: 3%
   - Discount and Returns: -2%

   Tip

   You can either enter a simulation percentage or simulation value by selecting the value.

   [![Screenshot of the United States node with Measure simulation panel showing sliders for Sales Volume +5%, Avg Selling Price +3%, and Discounts and Returns -2%.](media/planning-how-to-create-measure-model/measure-simulation-panel.png)](media/planning-how-to-create-measure-model/measure-simulation-panel.png#lightbox)
6. The simulation results automatically cascade through **Gross Revenue** and **Net Revenue** at the measure level and to *North America* at the parent level. Select the caret icon to expand and see all the measures listed for each node in a hierarchical format.

   [![Screenshot of simulation results cascading through *Gross Revenue* and *Net Revenue* nodes.](media/planning-how-to-create-measure-model/simulation-impact-cascade-measure.png)](media/planning-how-to-create-measure-model/simulation-impact-cascade-measure.png#lightbox)
7. Repeat the process to create multiple scenarios and compare them to determine which business drivers produce the best performance. For more information about comparing scenarios, see [Compare scenarios](planning-how-to-set-up-scenarios#compare-scenarios).

   [![Screenshot of the Scenario Comparison page comparing Base Scenario with Best Case across regions and measures.](media/planning-how-to-create-measure-model/scenario-comparison-base-versus-best-case.png)](media/planning-how-to-create-measure-model/scenario-comparison-base-versus-best-case.png#lightbox)

## FAQ

Frequently asked questions about measure-based modeling.

### What is the difference between a native/DAX measure and a formula measure?

Native/DAX measures come directly from the semantic model, such as Sales Volume or Raw Material Cost. A formula measure is calculated by combining other measures using an expression in the planning sheet, such as *Gross Revenue* being calculated as Sales Volume multiplied by Avg Selling Price. Formula measures can reference other formula measures too, which is how Net Profit ultimately rolls all the way down to native measures like Discounts and Returns.

### Why do I assign all the fact transaction measures to **Values** before I configure the measure model?

You must place every native/DAX measure used in the measure model in the **Values** field on the planning sheet. The measure model canvas only lists native/DAX measures that are already in the **Values** field, so you need to assign them upfront before you can build any hierarchy.

### What is the main purpose of the measure model?

When semantic model measures are the foundation of a planning model, the measure model provides a way to organize them into a meaningful hierarchy, such as a P&L structure, so teams can plan, simulate, and analyze the cascade of impacts across the full model in a single structured view.

### Does the order in which I drag measures onto the canvas affect whether the calculations are correct?

Canvas placement doesn't affect calculation accuracy, since the formulas themselves are independent of hierarchy positioning. What matters is the formula dependency order. COGS's formula must exist in the planning sheet before Gross Profit's formula can reference it, regardless of when either is dragged into the tree visually.

### If I nest a measure under the wrong parent by mistake, does that break its formula?

No. Nesting only controls where a measure displays in the hierarchy, not what it calculates. If Labor Cost were accidentally nested under Operating Expenses instead of COGS, its own value would stay correct, but COGS's total would be wrong since it would no longer include Labor Cost in its formula.

### If I place a measure under the wrong parent by mistake, how can I correct it?

You can unstage and reposition it rather than delete and rebuild it. In the Hierarchy Builder canvas, each measure has a small cross/remove icon available directly next to it. By selecting it, you unstage that measure from its current parent without deleting it. Once unstaged, you can drag it again into the correct position under the intended parent.

## What is the difference between nesting a measure under a parent in the canvas and adding a measure to the **Values** field on the planning sheet?

Nesting in the canvas defines the hierarchy structure - how measures roll up under Net Profit for display in Measures in Rows or Tree layout. Adding a measure to the **Values** data well on the planning sheet is what makes it appear as an editable or viewable column on that sheet. A measure can exist in the **Values** data well without being part of the hierarchy.

### Does every measure need to be dragged into the canvas individually?

Both approaches are used across the article - *Gross Revenue* and *Net Revenue* are dragged individually, while three children under *COGS* and four children under *Operating Expenses* are added using **Select All** and **Insert Measure**. The method you use depends on how many measures you're nesting under the same parent at once.

### Does switching to Measures in Rows change anything functionally, or is it purely visual?

It's a display change only. The same underlying measures, formulas, and data are shown, arranged so that each measure appears as a row rather than a column. It doesn't alter the measure model structure or its **Values** - it simply makes the P&L hierarchy easier to read.

### Is the measure model tied to the Simple P&L Model sheet specifically, or can the same structure be reused on other planning sheets?

You build and apply the measure model on the specific planning sheet on which you configure it. To reuse the same P&L logic on another sheet, you need to build or reference the structure on that sheet separately.

### Does switching to Tree layout change anything functionally?

It's a display change only - the same underlying nodes, formulas, and data are shown, rendered as connected branches instead of a flat hierarchy. It doesn't alter the **Measure Model** structure or its values.

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
