---
title: "Insert rollup columns in PowerTable sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-columns/how-to-insert-rollup-columns](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-columns/how-to-insert-rollup-columns) · Last updated on **2026-08-07**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert rollup columns in PowerTable sheet

Summarize this article for me

A rollup column aggregates values from related records in a linked table and displays the aggregated result in the current table. Use rollup columns to calculate values such as **sum**, **count**, **average**, **minimum**, **maximum**, **median**, **earliest date**, **latest date**, **countA**, **empty**, and more.

## Use cases of rollup column

Use a rollup column to:

- Display the total hours logged for a project.
- Show the number of open tasks assigned to an employee.
- Calculate the total value or quantity of orders for a product or customer.
- Display the latest or earliest order date for a product.

A rollup column is similar to a [reference column](how-to-insert-reference-columns) but also automatically calculates aggregated values from related records. This feature eliminates the need to manually maintain summary values across multiple tables. When data in the linked table changes, the rollup value recalculates automatically.

This article explains how to create and configure a rollup column by using a sample **Products** table.

In this example, you create:

- A rollup column that displays the **total order quantity** for each product.
- A rollup column that displays the **latest order date** for each product.

## Add a rollup column

1. Go to **PowerTable** > **Insert Column** > **Visual Column** > **Add Roll Up Column**. A side panel opens.

   [![Screenshot of the Insert Column menu expanded to Visual Column showing the Add Roll Up Column option highlighted.](../media/powertable-how-to-insert-columns/how-to-insert-rollup-columns/add-rollup-column.png)](../media/powertable-how-to-insert-columns/how-to-insert-rollup-columns/add-rollup-column.png#lightbox)
2. Configure the following details:

   - **Column Name**: Enter an appropriate name for the rollup column, such as *Total Orders*.
   - **Schema**: Select the schema that contains the linked table.
   - **Linking Table**: Select the table that contains the records to aggregate.
   - **Column from Current Table**: Select the column in the current table used to match records.
   - **Column from Linking Table**: Select the matching column in the linked table. In this example, *ProductKey* is the matching column.
   - **Column To Rollup**: Select the column to aggregate. Here, choose *OrderQuantity* as the column to roll up.
   - **Aggregation**: Select an aggregation function, such as **Sum**, **Average**, or **Count**. Use **Sum** to add and aggregate the order quantities for each product.

   [![Screenshot of the Add Roll Up Column panel with Column Name, Schema, Linking Table, Column To Rollup, and Aggregation fields filled in.](../media/powertable-how-to-insert-columns/how-to-insert-rollup-columns/configure-rollup-column.png)](../media/powertable-how-to-insert-columns/how-to-insert-rollup-columns/configure-rollup-column.png#lightbox)
3. **If Condition**: Optionally, add one or more filter conditions by using **Add Filter** to aggregate only the records that meet specific criteria. Combine multiple conditions by using **AND** or **OR**. For example, you can aggregate only the orders placed after a specific date by filtering on the **OrderDate** column.
4. The display properties for the rollup column can be configured in the panel's **Display** tab. To learn more, see [Display](../powertable-how-to-configure-columns/how-to-configure-display-column-properties).
5. Select **Save**.

PowerTable adds a rollup column that displays the aggregated order quantity for each product based on the matching product key.

[![Screenshot of a product table showing aggregated order quantities in the highlighted Total Orders column, with blank values for some rows.](../media/powertable-how-to-insert-columns/how-to-insert-rollup-columns/rollup-column-added.png)](../media/powertable-how-to-insert-columns/how-to-insert-rollup-columns/rollup-column-added.png#lightbox)

Note

Products with no related records or no values to aggregate display a blank value in the rollup column.

## Another example

To create another rollup column that displays the latest order date, repeat the same steps. Select **Order Date** as the column to roll up, and select **Latest Date** as the **Aggregation** type. Select **Save**.

![Screenshot of the Add Roll Up Column dialog with Column To Rollup set to OrderDate and Aggregation set to Latest Date, and Save highlighted.](../media/powertable-how-to-insert-columns/how-to-insert-rollup-columns/another-example.png)

The latest order date rollup column is added, as shown in the following image.

[![Screenshot of the product table grid with the new Latest rollup column highlighted, showing latest order dates or blanks.](../media/powertable-how-to-insert-columns/how-to-insert-rollup-columns/another-example-result.png)](../media/powertable-how-to-insert-columns/how-to-insert-rollup-columns/another-example-result.png#lightbox)

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
