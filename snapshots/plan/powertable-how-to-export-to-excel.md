---
title: "Export PowerTable sheet to Excel"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-export-to-excel](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-export-to-excel) · Last updated on **2026-08-26**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Export PowerTable sheet to Excel

Summarize this article for me

Export PowerTable sheets to Excel so you can work with, share, and analyze your data outside of PowerTable.

This article explains common use cases for exporting PowerTable data to Excel and the steps to do it.

Exported Excel sheets include the PowerTable sheet data, inserted rows, and lookup labels. They preserve the data, sheet structure, and lookup labels, making it easy to perform offline analysis, share information, and create custom reports.

Note

Visual and formula columns that you add in the PowerTable sheet aren't included in the exported file. Also, export doesn't include the added comments and the comments column.

## Common use cases

- Share PowerTable data with stakeholders who don't have access to it.
- Make offline backups or snapshots of table data.
- Perform advanced data analysis by using Excel features such as PivotTables and advanced charts.

Note

Export to Excel is supported across all layouts except the crosstab layout.

## Export to Excel

1. To export the sheet in Excel format, select **PowerTable** > **Export**.

   [![Screenshot of PowerTable ribbon with Export button highlighted.](media/powertable-how-to-export-to-excel/export-option.png)](media/powertable-how-to-export-to-excel/export-option.png#lightbox)
2. Choose one of the two formats to export:

   - Select **Label** to include lookup labels in the exported data.
   - Select **Raw Data** to export the raw data in the same format you imported it into the PowerTable.
3. Select **Export**.

   ![Screenshot of Export dialog with Label and Raw Data options and Export button highlighted.](media/powertable-how-to-export-to-excel/select-export.png)
4. After the export completes, select **Download**. Then, right-click the generated file link and save the file to your local system.

   [![Screenshot of PowerTable Export Completed dialog with Download link highlighted.](media/powertable-how-to-export-to-excel/download-file.png)](media/powertable-how-to-export-to-excel/download-file.png#lightbox)
5. The exported file looks like the following image. The *ProductSubcategoryKey* field retains the lookup labels because you chose the **Label** option. The export also maintains the sheet layout structure.

   [![Screenshot of Excel showing exported Products sheet with lookup labels and all other columns.](media/powertable-how-to-export-to-excel/exported-file.png)](media/powertable-how-to-export-to-excel/exported-file.png#lightbox)
6. The **Raw Data** option generates the raw data in Excel as shown in the following image, without any lookup labels or structure.

   [![Screenshot of exported raw data in Excel with numeric ProductSubcategoryKey values.](media/powertable-how-to-export-to-excel/exported-raw-data.png)](media/powertable-how-to-export-to-excel/exported-raw-data.png#lightbox)

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
