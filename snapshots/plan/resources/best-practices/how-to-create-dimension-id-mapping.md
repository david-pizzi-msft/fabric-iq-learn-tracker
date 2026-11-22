---
title: "Maintain data integrity with dimension ID mapping"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/how-to-create-dimension-id-mapping](https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/how-to-create-dimension-id-mapping) · Last updated on **2026-10-05**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Maintain data integrity with dimension ID mapping

Summarize this article for me

In planning, forecasting, and enterprise reporting, report structures are rarely static. Category names evolve, product hierarchies get relabeled, and organizational units are frequently renamed (for example, updating a cost center name).

In dynamic reporting tools, visual annotations, custom formatting, cell comments, writeback, and manual data inputs (such as budget overrides or forecast updates) are attached to specific row dimensions. By using *Dimension ID Mapping,* you can link custom visual elements and planning inputs to a constant, non-changing identifier (such as a unique Product ID or Cost Center Code) rather than a volatile descriptive label (such as Product Name).

## Why do you need dimension ID mapping in Planning?

When row labels in your underlying data model change (for example, renaming a product), standard reporting visuals lose track of which row the custom notes, cell highlights, or data inputs belong to.

The following screenshot shows a note added, approval status set to completed, and custom formatting applied to the *Ergonomic Executive Backpacks* row.

[![Screenshot of custom formatting, completed approval status, and a note applied to the Ergonomic Executive Backpacks row.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/formatting-status-note-applied-to-row.png)](../../media/resources/best-practices/how-to-create-dimension-id-mapping/formatting-status-note-applied-to-row.png#lightbox)

If you change the row label, in this example, change *Ergonomic Executive Backpack* to *Standard Laptop Backpack*, you lose the custom formatting, data inputs, and annotations tied to the label.

[![Screenshot of formatting, data inputs, and notes removed on changing the row label.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/formatting-lost-label-change.png)](../../media/resources/best-practices/how-to-create-dimension-id-mapping/formatting-lost-label-change.png#lightbox)

Planning and forecasting workflows also require writing data back to database tables or data warehouses. If writeback relies on descriptive labels that change over time, it creates orphan records or breaks audit trails.

## Configure dimension ID mapping

By default, notes, comments, and formatting tie directly to volatile dimension labels. Configure dimension ID mapping to link these inputs to persistent, unique identifiers, such as a product ID or cost center code.

Important

Set up dimension ID mapping before making changes such as creating data input fields, adding notes, or applying formatting to the planning sheet.

1. Open the **Data** side pane and select the settings icon. Open the **Dimension ID Mapping** tab.

   [![Screenshot of the Dimension ID Mapping tab in the Data pane settings showing dimensions mapped to labels by default.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/default-label-dimension-id-mapping.png)](../../media/resources/best-practices/how-to-create-dimension-id-mapping/default-label-dimension-id-mapping.png#lightbox)
2. Select the **ID Column** option to assign an ID column instead of using the dimension category value. Choose the column from **Select Mapping Field** and select **Apply**. The following screenshot shows how to change the dimension ID mapping for the *SalesRepName* dimension to *SalesRepID*.

   [![Screenshot of the Dimension ID Mapping tab with the ID Column option mapping the SalesRepName dimension to SalesRepID.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/change-dimension-id-mapping.png)](../../media/resources/best-practices/how-to-create-dimension-id-mapping/change-dimension-id-mapping.png#lightbox)
3. When you update the sales rep in the *Central* region from *Nicole Wagner* to *Andzelika Juskaite*, the entered budget values, approval status, notes, and formatting are retained.

   [![Animation showing that updating the sales representative name retains budget values, approval status, notes, and formatting.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/update-sales-rep-name-preserve-formatting.gif)](../../media/resources/best-practices/how-to-create-dimension-id-mapping/update-sales-rep-name-preserve-formatting.gif#lightbox)

## Configure dimension ID mapping for writeback

Mapping a dimension label to a unique column ID prevents unnecessary row creation during writeback. When you enable this feature, updating a dimension label updates the existing record rather than creating a new row in the writeback table. Without dimension ID mapping, label changes are treated as new entries, generating duplicate rows.

1. In the **Data** pane, open **Dimension ID Mapping** settings. Use the steps in the [Configure Dimension ID Mapping](#configure-dimension-id-mapping) section to select the IDs corresponding to the dimension labels.

   [![Screenshot of setting the dimension ID mapping for region and sales representative.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/dimension-id-mapping-region-sales-representative.png)](../../media/resources/best-practices/how-to-create-dimension-id-mapping/dimension-id-mapping-region-sales-representative.png#lightbox)
2. In the **Writeback** ribbon, go to **Writeback Settings** > **Data**. Under **Exclude Dimensions for Writeback**, select the dimension labels mapped in the previous step (for example, *RegionName* and *SalesRepName*). Since these fields are already linked to dimension IDs, they don't need to be written back.

   Note

   - The **Exclude Dimensions for Writeback** option is enabled only if dimension ID mapping is configured.
   - If your source data includes housekeeping fields (such as *LastUpdatedAt*) assigned to rows or columns in a planning sheet, writeback might create unwanted duplicate records. To prevent this problem, disable the **In Key** toggle for that dimension under **Dimension ID Mapping** and add it to **Exclude Dimensions for Writeback**. Writeback automatically captures the timestamp and username, so housekeeping columns from the source aren't required.

   [![Screenshot of writeback settings with the sales representative and region fields excluded.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/exclude-dimensions-writeback-option.png)](../../media/resources/best-practices/how-to-create-dimension-id-mapping/exclude-dimensions-writeback-option.png#lightbox)
3. Trigger writeback. For demonstration purposes, consider the sales rep highlighted in the planning sheet:

   [![Screenshot of a planning sheet with a sales representative record highlighted.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/sample-data-highlighted-planning-sheet.png)](../../media/resources/best-practices/how-to-create-dimension-id-mapping/sample-data-highlighted-planning-sheet.png#lightbox)

   Open the destination SQL database. Notice how the RegionID and SalesRepID are written back to the destination table even though you didn't add them to the planning sheet.

   ![Screenshot of RegionID and SalesRepID fields written back to the SQL destination table.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/sales-representative-id-written-back.png)

   The following screenshot shows the writeback table data if you don't exclude the label columns in writeback settings (Step 2).

   [![Screenshot of the SQL writeback table showing sales representative name label columns written back when not excluded.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/sales-representative-label-written-back-sql-table.png)](../../media/resources/best-practices/how-to-create-dimension-id-mapping/sales-representative-label-written-back-sql-table.png#lightbox)
4. Update the dimension label in the semantic model. In this example, the sales representative name changed from *Andzelika Juskaite* to *Nicole Wagner*. Refresh your planning sheet to see the updated data.

   [![Screenshot of the sales representative name updated to Nicole Wagner in the planning sheet.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/sales-representative-name-updated-planning-sheet.png)](../../media/resources/best-practices/how-to-create-dimension-id-mapping/sales-representative-name-updated-planning-sheet.png#lightbox)
5. Change a data input entry and trigger writeback again. In this example, we changed the **Approval Status** to *Completed* for the *Enterprise Multifunction Printers* row.

   [![Screenshot of updating the approval status to completed.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/approval-status-changed-completed.png)](../../media/resources/best-practices/how-to-create-dimension-id-mapping/approval-status-changed-completed.png#lightbox)
6. Verify the data in the destination SQL table. Even though the sales representative's name changed, the writeback updated the existing record rather than inserting a duplicate row.

   [![Screenshot of the destination SQL table showing the existing record updated with Completed approval status and no duplicate row.](../../media/resources/best-practices/how-to-create-dimension-id-mapping/writeback-sql-table-record-updated-no-duplicate.png)](../../media/resources/best-practices/how-to-create-dimension-id-mapping/writeback-sql-table-record-updated-no-duplicate.png#lightbox)

## Related content

- [Use Writeback to save planning data to a Fabric SQL database](/en-us/fabric/iq/plan/planning-writeback/planning-how-to-persist-data.md).

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
