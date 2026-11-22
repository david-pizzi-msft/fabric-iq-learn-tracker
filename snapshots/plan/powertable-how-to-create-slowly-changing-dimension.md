---
title: "Create slowly changing dimensions"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-create-slowly-changing-dimension](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-create-slowly-changing-dimension) · Last updated on **2026-06-16**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create slowly changing dimensions

Summarize this article for me

Use Type 2 and Type 3 slowly changing dimensions (SCDs) to track changes to dimension data. In this article, you learn how to configure each SCD type and understand how they preserve historical and current attribute values. For more information about SCDs, see [Slowly Changing Dimensions](powertable-concept-slowly-changing-dimensions).

## Prerequisites

The source data used to populate a Type 2 slowly changing dimension must have the following columns:

- A natural key such as region ID, customer ID, or product ID.
- A unique sequence number that is used as the surrogate key.
- Two date columns that capture the start and end dates.
- A boolean column that indicates whether a record is active.

The source data used to populate a Type 3 SCD must include a corresponding history column for each column that maintains historical values.

Note

SCD configuration is available only during table creation. Tables can't be converted to slowly changing dimensions after they're created.

## Configure Type 2 SCD

Slowly changing dimensions are configured during table creation. In this example, you create an SCD table using data imported from an Excel file.

[![Screenshot of creating a table by importing data from an Excel file.](media/powertable-how-to-create-slowly-changing-dimension/import-table-data.png)](media/powertable-how-to-create-slowly-changing-dimension/import-table-data.png#lightbox)

1. In the table configuration, turn on **Enable support for Slowly Changing Dimensions (SCD)** and select **Type-2.**

   [![Screenshot of option to create a Type 2 SCD.](media/powertable-how-to-create-slowly-changing-dimension/type-two-option.png)](media/powertable-how-to-create-slowly-changing-dimension/type-two-option.png#lightbox)
2. Map the source columns to the surrogate key, natural key, active flag, and date range fields. Use **End Date Default Value** to define the default end date for active records. Choose either a null value or an infinite date.

   [![Screenshot of configuring Type 3 SCD by mapping the primary and history columns.](media/powertable-how-to-create-slowly-changing-dimension/configure-dimension-columns.png)](media/powertable-how-to-create-slowly-changing-dimension/configure-dimension-columns.png#lightbox)
3. In **SCD Columns**, select the columns whose changes you want to track in the slowly changing dimension and select **Finish**.

   The table is created.

   [![Screenshot of table created.](media/powertable-how-to-create-slowly-changing-dimension/table-created.png)](media/powertable-how-to-create-slowly-changing-dimension/table-created.png#lightbox)

### View change history

Slowly changing dimensions capture the changes made to each record.

1. Edit a cell value and select **Save to Database** to commit the change.

   ![Screenshot of editing values.](media/powertable-how-to-create-slowly-changing-dimension/edit-value.png)
2. The original record is marked as inactive and excluded from the grid. A new record containing the updated values is inserted at the end of the grid. To view the change history for a record, select the record and then select **History**.

   ![Screenshot of history option.](media/powertable-how-to-create-slowly-changing-dimension/history-option.png)
3. In the **History** pane, records with the **Active** flag enabled are the current active records. Their **End Date** is displayed as either null or an infinite date, based on the SCD configuration. After reviewing the change history, select the back icon to return to the grid.

   ![Screenshot of viewing older records.](media/powertable-how-to-create-slowly-changing-dimension/view-older-records.png)

## Configure Type 3 SCD

You can configure Type 3 SCDs when creating a table from a file, a semantic model, or by manually entering data.

1. In the table configuration, turn on **Enable support for Slowly Changing Dimensions (SCD)** and select **Type-3.**

   [![Screenshot of SCD Type 3 option.](media/powertable-how-to-create-slowly-changing-dimension/type-three-option.png)](media/powertable-how-to-create-slowly-changing-dimension/type-three-option.png#lightbox)
2. Select the current value column and its corresponding history column to track both the latest and previous values. Select **+ Add More** to maintain historical data for more than one column.

   [![Screenshot of configuring type three SCDs.](media/powertable-how-to-create-slowly-changing-dimension/configure-type-three-dimension-columns.png)](media/powertable-how-to-create-slowly-changing-dimension/configure-type-three-dimension-columns.png#lightbox)
3. Select **Finish** to create the table.

   [![Screenshot of table creation.](media/powertable-how-to-create-slowly-changing-dimension/create-table.png)](media/powertable-how-to-create-slowly-changing-dimension/create-table.png#lightbox)
4. When you edit a value, the older value is moved to the configured history column. Select **Preview Changes**.

   [![Screenshot of change preview.](media/powertable-how-to-create-slowly-changing-dimension/preview-changes.png)](media/powertable-how-to-create-slowly-changing-dimension/preview-changes.png#lightbox)
5. Verify the changes that were made.

   [![Screenshot of preview window.](media/powertable-how-to-create-slowly-changing-dimension/preview-window.png)](media/powertable-how-to-create-slowly-changing-dimension/preview-window.png#lightbox)
6. Select **Added**, **Updated**, or **Deleted** to preview records with specific changes. Select **Save to Database** to commit the changes.

   [![Screenshot of previewing specific changes.](media/powertable-how-to-create-slowly-changing-dimension/preview-specific-changes.png)](media/powertable-how-to-create-slowly-changing-dimension/preview-specific-changes.png#lightbox)

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
