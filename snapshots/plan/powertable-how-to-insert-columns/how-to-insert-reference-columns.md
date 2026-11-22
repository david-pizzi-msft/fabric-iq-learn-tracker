---
title: "Insert reference columns in PowerTable"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-columns/how-to-insert-reference-columns](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-columns/how-to-insert-reference-columns) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert reference columns in PowerTable

Summarize this article for me

A reference column is a type of [visual column](how-to-insert-visual-columns) that joins tables through matching columns and shows related data from another table directly within the current table. You can access information from related tables without duplicating the data.

This article explains the steps to insert a reference column that references data from another table by using a sample scenario.

## Insert the reference columns with a sample scenario

Consider the following example: You add a reference column to the *Products* table that references and shows order dates from the *Sales* table.

1. To add a reference column, go to **PowerTable** > **Insert Column** > **Visual Column** > **Add Reference Column**.

   ![Screenshot of PowerTable menu with Insert Column, Visual Column, and Add Reference Column highlighted.](../media/powertable-how-to-insert-columns/how-to-insert-reference-columns/insert-reference-column.png)
2. In the side panel, enter a name for the column.
3. Use **Input Type** to select the column's input type based on what you want to reference. Depending on the chosen type, the reference columns are available for selection. For example, if you choose **Date**, all date columns are available for selection.

   [![Screenshot of Add Reference Column panel with Input Type set to Date and Column Name Order Date highlighted.](../media/powertable-how-to-insert-columns/how-to-insert-reference-columns/input-type-name.png)](../media/powertable-how-to-insert-columns/how-to-insert-reference-columns/input-type-name.png#lightbox)
4. Select the schema, reference table name, and the reference column to show.
   In this example, *Sales* is the reference table and *Order Date* is the reference column.

   ![Screenshot of Add Reference Column panel with schema, reference table, and matching columns configured, Save button highlighted.](../media/powertable-how-to-insert-columns/how-to-insert-reference-columns/configure-reference-column.png)
5. Enable [Match multiple](#match-multiple-records) to retrieve multiple values from all matching records in the reference table.
6. Select the matching column between the current table and the reference table.

   Note

   - PowerTable uses the matching column to map the records and retrieve values from the reference table.
   - When tables have multiple matching columns and you choose a different matching column, PowerTable uses the new column mappings to match records and retrieve reference values.
7. Select **Save**. PowerTable adds the reference column.

   [![Screenshot of PowerTable displaying product records with the new reference column added.](../media/powertable-how-to-insert-columns/how-to-insert-reference-columns/reference-column-added.png)](../media/powertable-how-to-insert-columns/how-to-insert-reference-columns/reference-column-added.png#lightbox)

Note

Reference columns are non-editable, and their values only change when the underlying column values change.

Tip

Use the **Display** tab in the **Add Reference Column** side panel to specify how PowerTable shows the values. To learn more, see [Display](../powertable-how-to-configure-columns/how-to-configure-display-column-properties).

## Match multiple records

When you turn on **Match multiple**, the reference column retrieves values from multiple matching records in the reference table. The values appear in the reference column.

When you turn off this feature, the matching columns identify a single latest record in the reference table. Turn on this option when a record in the current table can associate with multiple matching records in the reference table.

[![Screenshot of PowerTable reference column popup showing multiple matching Order Date values 02/28/2023 and 12/03/2023.](../media/powertable-how-to-insert-columns/how-to-insert-reference-columns/matching-multiple-records.png)](../media/powertable-how-to-insert-columns/how-to-insert-reference-columns/matching-multiple-records.png#lightbox)

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
