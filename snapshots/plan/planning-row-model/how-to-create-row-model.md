---
title: "Create a row model"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-row-model/how-to-create-row-model](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-row-model/how-to-create-row-model) · Last updated on **2026-08-13**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create a row model

Summarize this article for me

Use row-based modeling to organize the rows in a planning sheet into a hierarchical structure that represents business drivers and outcomes. Each row can act as a driver, so you can define relationships between inputs and calculated results. This approach helps you analyze how changes in one row affect related rows. For example, if **Cost** changes, you can see how the change affects **Net Profit** through the defined row relationships.

By using a row model, you can:

- Organize rows into meaningful driver hierarchies according to business requirements.
- Build complex planning logic from simple data structures.
- Perform planning, forecasting, and simulations at the row level.
- Analyze the cascading impact of changes to a driver across the entire model in a single view.
- Give business users greater control over planning drivers and assumptions.

## Create row-based model

1. Create a planning sheet by assigning the required dimensions and measures from the semantic model.

   Consider the following planning sheet with the **Chart of Accounts** as the row dimension, **Year**, **Quarter**, and **Month** in the **Columns** field, and **Actuals** in the **Values** field.

   [![Screenshot of a planning sheet with Chart of Accounts rows and Year, Quarter, Month columns, and Actual in the Values field highlighted.](../media/planning-row-model/how-to-create-row-model/assign-measures.png)](../media/planning-row-model/how-to-create-row-model/assign-measures.png#lightbox)
2. Go to the **Model** ribbon and select **Row Model.** The **Model Builder** pop-up opens. Select **Enable**.

   [![Screenshot of the Model ribbon with Row Model highlighted and the Model Builder dialog showing the Enable button highlighted.](../media/planning-row-model/how-to-create-row-model/select-row-model.png)](../media/planning-row-model/how-to-create-row-model/select-row-model.png#lightbox)
3. This action enables **Model Builder**. You can select **Back to Home** to save the report and return to this screen by selecting **Row Model** again.

   [![Screenshot of the Row Model page with rows listed and Type, Configuration, and Aggregation columns after enabling Model Builder.](../media/planning-row-model/how-to-create-row-model/model-builder-enabled.png)](../media/planning-row-model/how-to-create-row-model/model-builder-enabled.png#lightbox)

   The model builder displays each row as a configurable driver for both open and closed periods, enabling you to build row-based models.
4. To build your model, delete all rows except the topmost *All* row. Select the row selection box in the column header, clear *All*, and then select **Delete**.

   [![Screenshot of the Row Model page with 12 rows selected, the All row unchecked, and Delete highlighted in the toolbar.](../media/planning-row-model/how-to-create-row-model/delete-all-except-top-row.png)](../media/planning-row-model/how-to-create-row-model/delete-all-except-top-row.png#lightbox)
5. To create the row hierarchy, select the top row and then select **Bulk Insert**.

   [![Screenshot of the Row Model page with the All row selected and Bulk Insert highlighted in the toolbar.](../media/planning-row-model/how-to-create-row-model/bulk-insert.png)](../media/planning-row-model/how-to-create-row-model/bulk-insert.png#lightbox)
6. In the side panel, enter the rows you want to add. Use **Tab** to add a row as a child at the next hierarchy level.

   [![Screenshot of the Insert Bulk Row panel with indented row names entered and the Add button highlighted.](../media/planning-row-model/how-to-create-row-model/enter-row-hierarchy.png)](../media/planning-row-model/how-to-create-row-model/enter-row-hierarchy.png#lightbox)
7. Select **Add**. The rows are added as shown in the following image.

   [![Screenshot of the Row Model page with Row Name, Type, Configuration, and Aggregation columns after bulk inserting rows.](../media/planning-row-model/how-to-create-row-model/created-row-model.png)](../media/planning-row-model/how-to-create-row-model/created-row-model.png#lightbox)

## Configure the row model

Configure each row to build a simple **Profit and Loss (P&L)** model.

1. Select the pencil icon on the topmost row (*All*) to configure its properties:

   - **Row Name:** Enter *Operating Profit*.
   - **Configure as:** Select **Formula**.
   - Enter the formula in the formula box as, `[Operating Income] â [Operating Expense]`. As you type, suggestions pop up, and you can choose the rows from the **References** tab.
2. Select **Apply**.

   [![Screenshot of Row Model editor with the All row panel showing Row Name Operating Profit, Configure as Formula, and Apply highlighted.](../media/planning-row-model/how-to-create-row-model/configure-top-node.png)](../media/planning-row-model/how-to-create-row-model/configure-top-node.png#lightbox)
3. Configure all leaf rows one by one. Select the pencil icon on *Revenue* or select its **Type** dropdown. Configure the type as **Data Source**.

   [![Screenshot of Row Model editor with Revenue row selected and its pencil icon highlighted, and the Revenue panel showing Configure as set to Data Source.](../media/planning-row-model/how-to-create-row-model/configure-leaf-node.png)](../media/planning-row-model/how-to-create-row-model/configure-leaf-node.png#lightbox)
4. In **Choose Close Period Source Row**, select the corresponding source row from the semantic model, and then select **Apply**. It is automatically applied for the **Open Period** as well.

   [![Screenshot of the Revenue panel listing source rows with Revenue selected and Apply highlighted.](../media/planning-row-model/how-to-create-row-model/select-source-row.png)](../media/planning-row-model/how-to-create-row-model/select-source-row.png#lightbox)
5. Ensure its **Desired Trend** is **Increase** (since it's revenue), and then select **Apply** again.
6. Now, configure the *Purchase* row:

   - **Configure as**: Select **Data Source**.
   - **Choose Close Period Source Row**: Select the source row from the semantic model using the list. It gets auto-applied to open period also.
   - **Desired Trend**: Set its desired trend as **Decrease** (since it's an expense).
7. Select **Apply**.

   [![Screenshot of Row Model with Purchase row selected and its panel showing Data Source, source row, and Decrease trend.](../media/planning-row-model/how-to-create-row-model/configure-purchase-row.png)](../media/planning-row-model/how-to-create-row-model/configure-purchase-row.png#lightbox)
8. Repeat the preceding step for the remaining child rows, *Transportation*, *Adv & Promotion*, and *Salaries*.
9. Configure the parent rows:

   - **Operating Income:** Configure as **Aggregate** to aggregate its child rows. Select **Sum** as the aggregation type. Set the desired trend to **Increase**.
   - **Operating Expense:** Configure as **Aggregate** to aggregate its child rows. Select **Sum** as the aggregation type. Set the desired trend to **Decrease**.

The row model is completely configured as shown in the following image.

[![Screenshot of the completed Row Model showing Operating Profit formula row with Operating Income and Operating Expense aggregate rows and their data source child rows.](../media/planning-row-model/how-to-create-row-model/complete-row-model.png)](../media/planning-row-model/how-to-create-row-model/complete-row-model.png#lightbox)

Select **Back to Home** to return to the planning sheet and view the created model.

[![Screenshot of the planning sheet with expandable Operating Profit, Operating Income, and Operating Expense hierarchy rows and child rows such as Revenue, Purchase, and Salaries.](../media/planning-row-model/how-to-create-row-model/planning-sheet-row-model.png)](../media/planning-row-model/how-to-create-row-model/planning-sheet-row-model.png#lightbox)

Note

- Select a row, and then select **Add Child** or **Add Sibling** to add a child row or a sibling row at the same hierarchy level.
- Configure a different setting for the **Open Period**, if required.
- Use the **Aggregation** dropdown to roll up the row's values across the selected time period (column dimension).

### How the row model helps you analyze business performance

A row model helps you analyze how changes to individual drivers affect related rows in the hierarchy. When you modify a driver, the resulting changes flow through the related calculations and parent rows.

For example, if you increase **Revenue**, the model calculates the corresponding impact on **Operating Profit** based on the relationships and formulas defined in the model.

You can also use a row model to forecast, create multiple scenarios, and perform simulations to compare different driver assumptions and evaluate their impact on business performance.

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
