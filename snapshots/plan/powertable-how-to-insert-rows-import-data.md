---
title: "Insert, import, duplicate, and delete rows"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-rows-import-data](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-rows-import-data) · Last updated on **2026-08-02**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert, import, duplicate, and delete rows

Summarize this article for me

In a PowerTable sheet, you can add, import, copy, duplicate, and delete rows by using multiple methods. You can insert rows manually, import data from external files, duplicate existing records, or remove records as needed.

PowerTable provides the following row management capabilities:

- Add one or more rows directly to the table.
- Import large data sets from Excel or CSV files.
- Insert rows through user forms.
- Duplicate existing records to reduce manual data entry.
- Copy records between PowerTable and other applications.
- Delete one or more rows directly from the table.

## Insert rows

Use the **Insert Row** option to manually add new rows to a table.

Note

Use the [Import](#import-bulk-data) option to insert or update rows by using data from an external file.

### Insert a single row

To insert a single row:

1. Select **PowerTable** > **Insert Row**.

   ![Screenshot of the Insert Row option.](media/powertable-how-to-insert-import-rows/insert-row.png)
2. The table adds a new blank row as the last row.
3. Select each cell, enter a value, and press **Enter**.

   [![Screenshot of entering values in the inserted row.](media/powertable-how-to-insert-import-rows/enter-value.png)](media/powertable-how-to-insert-import-rows/enter-value.png#lightbox)
4. After inserting the required rows and entering the data, select **Save to Database** to save the changes.

To review the changes before saving, use **Preview Changes**. To remove the unsaved rows, use **Discard Changes**.

### Insert multiple rows

To insert multiple rows:

1. Select the dropdown next to **PowerTable** > **Insert Row**.
2. Select **Insert Multiple Rows**.

   ![Screenshot of the Insert Multiple Rows option.](media/powertable-how-to-insert-import-rows/insert-multiple-rows.png)
3. Enter the **Number of Rows** to insert.
4. Select **Insert**.

   [![Screenshot of the Insert Multiple Rows dialog box.](media/powertable-how-to-insert-import-rows/number-of-rows.png)](media/powertable-how-to-insert-import-rows/number-of-rows.png#lightbox)

   The specified number of rows is added to the table.

   [![Screenshot of the number of rows added to the table.](media/powertable-how-to-insert-import-rows/number-of-rows-added.png)](media/powertable-how-to-insert-import-rows/number-of-rows-added.png#lightbox)
5. Select each cell, enter a value, and press **Enter**.
6. Alternatively, you can [copy multiple rows from a spreadsheet application](#copy-and-paste-rows) such as Excel and paste them into the table.
7. Select **Save to Database** to save the changes.

To review the changes before saving, use **Preview Changes**. To remove the unsaved rows, use **Discard Changes**.

Note

- You can insert up to 1,000 rows at one time.
- You can configure access controls to determine who can add rows to a table. For more information, see [Access control](powertable-how-to-set-up-access-control).

### Insert using form interface

You can also configure the form interface as the default method for adding rows.

To set up the insert using a form interface:

1. Select the dropdown next to **PowerTable** > **Insert Row**.
2. Enable the **Insert Using Form By Default** toggle.

   ![Screenshot of the Insert Using Form By Default toggle.](media/powertable-how-to-insert-import-rows/insert-using-form-default.png)
3. When you select **Insert Row**, a new row is inserted, and the **Form Editor** opens automatically.

   [![Screenshot of the Form Editor.](media/powertable-how-to-insert-import-rows/form-editor.png)](media/powertable-how-to-insert-import-rows/form-editor.png#lightbox)
4. Enter the required values for the new row and select **Apply**.

   ![Screenshot of entering values in the Form Editor.](media/powertable-how-to-insert-import-rows/form-editor-enter-values.png)

   Note

   Use [Customize Form](powertable-how-to-generate-forms#customize-form) to change the form fields and structure. The form configuration interface lets you add, edit, delete, and format form fields.

   The new row is inserted into the table.

   [![Screenshot of the inserted row.](media/powertable-how-to-insert-import-rows/new-row-inserted.png)](media/powertable-how-to-insert-import-rows/new-row-inserted.png#lightbox)
5. After inserting the required rows, select **Save to Database** to save the changes.

## Insert rows by using forms

You can add new rows by using shareable PowerTable forms that you distribute through email or embed in websites. When users submit a form, the submitted values are inserted as new records in the table.

For information about creating and sharing forms, see [Create data entry forms](powertable-how-to-generate-forms).

PowerTable forms support only the creation of new records. They don't support updating existing records.

## Import bulk data

You can also import bulk data from Excel or CSV files to add new rows or update existing rows.

When you import data, PowerTable compares the primary key values in the imported file with the existing records in the table.

- Records with matching primary keys are updated.
- Records with new primary keys are inserted as new rows.
- Records with mismatched or invalid data are flagged as errors and can be reviewed through the import error logs.

To import data:

1. Select **PowerTable** > **Import**.

   ![Screenshot of the Import option.](media/powertable-how-to-insert-import-rows/import.png)
2. The **Import** dialog box appears. Select the **Excel** or **CSV option** to specify the format of the file and then select **Continue**.

   [![Screenshot of the Import dialog box.](media/powertable-how-to-insert-import-rows/excel-csv.png)](media/powertable-how-to-insert-import-rows/excel-csv.png#lightbox)
3. Browse to or drop the file in the selected format, and then select **Upload**.

   [![Screenshot of the excel file.](media/powertable-how-to-insert-import-rows/browse-file.png)](media/powertable-how-to-insert-import-rows/browse-file.png#lightbox)

   ![Screenshot of uploading the excel file.](media/powertable-how-to-insert-import-rows/import-file.png)
4. Review the uploaded data and the count of rows marked for insert and update operations, and then select **Import**. Any import errors, such as data type mismatches, appear on the **Error** tab.

   [![Screenshot of reviewing the imported data.](media/powertable-how-to-insert-import-rows/review-imported-data.png)](media/powertable-how-to-insert-import-rows/review-imported-data.png#lightbox)

The table is updated with the newly inserted rows and the modified values from the imported data.

[![Screenshot of the updated table with new rows.](media/powertable-how-to-insert-import-rows/inserted-rows.png)](media/powertable-how-to-insert-import-rows/inserted-rows.png#lightbox)

Note

- Ensure that the imported XLSX or CSV file contains the required primary key fields and any mandatory fields configured in the **Columns** section.
- You can import up to 20,000 new rows at one time.

## Copy and paste rows

### Excel to PowerTable sheet

You can populate a PowerTable sheet by copying rows from external applications, such as Microsoft Excel, and pasting them directly into the table. This approach is useful when you only have a few rows to insert and don't need a full import.

1. Copy the rows you want to add from the spreadsheet.

   [![Screenshot of copying rows from spreadsheet.](media/powertable-how-to-insert-import-rows/copy-rows-spreadsheet.png)](media/powertable-how-to-insert-import-rows/copy-rows-spreadsheet.png#lightbox)
2. Use [Insert Row](#insert-rows) to insert one or more rows.
3. Select the newly added rows, and then select the **Paste** option or press **Ctrl+V**.

   [![Screenshot of pasting the copied rows from spreadsheet.](media/powertable-how-to-insert-import-rows/paste.png)](media/powertable-how-to-insert-import-rows/paste.png#lightbox)

The data is imported from Excel to the PowerTable sheet.

### PowerTable sheet to other applications

You can also copy data from a PowerTable sheet and paste it into external applications such as Microsoft Excel, Word, or Notepad for further analysis, reporting, or sharing.

To copy rows:

1. Select one or more rows.
2. Select the **Copy to Clipboard** icon on the toolbar, or press **Ctrl+C**.
3. Paste the data in the required applications.

   [![Screenshot of the Copy to Clipboard option.](media/powertable-how-to-insert-import-rows/copy-to-clipboard.png)](media/powertable-how-to-insert-import-rows/copy-to-clipboard.png#lightbox)

## Duplicate rows

Duplicate existing records, and then modify only the required fields.

To duplicate rows:

1. Select one or more rows.
2. Select the **Duplicate** option on the toolbar.

   [![Screenshot of the Duplicate option.](media/powertable-how-to-insert-import-rows/duplicate.png)](media/powertable-how-to-insert-import-rows/duplicate.png#lightbox)

The selected rows are duplicated. You can now update the required fields.

[![Screenshot of the duplicated rows.](media/powertable-how-to-insert-import-rows/duplicated-rows.png)](media/powertable-how-to-insert-import-rows/duplicated-rows.png#lightbox)

Note

Update unique primary key values after duplication because the original primary key values are copied to the new records.

## Delete rows

Delete one or more rows from a table.

To delete rows:

1. Select one or more rows.
2. Select **Delete** on the toolbar.

   [![Screenshot of the Delete option.](media/powertable-how-to-insert-import-rows/delete.png)](media/powertable-how-to-insert-import-rows/delete.png#lightbox)
3. In the confirmation dialog box, select **Proceed**.

   [![Screenshot of the confirmation dialog box.](media/powertable-how-to-insert-import-rows/proceed.png)](media/powertable-how-to-insert-import-rows/proceed.png#lightbox)

   The selected rows are deleted.

   Note

   Depending on the delete-type configuration, rows are either soft-deleted or permanently deleted. To learn more, see **delete type** in the [delete](powertable-how-to-set-up-access-control#configure-the-delete-type) section.

   [![Screenshot of the deleted rows.](media/powertable-how-to-insert-import-rows/deleted-rows.png)](media/powertable-how-to-insert-import-rows/deleted-rows.png#lightbox)
4. After deleting the required rows, select **Save to Database** to save the changes, or **Discard Changes** to revert the deletion.

Note

You can configure access controls to determine who can delete rows from a table. For more information, see [access control](powertable-how-to-set-up-access-control#delete).

If you configure an approval workflow, update and deletion requests go through the workflow before the records are updated or deleted. To learn more, see [Approval workflow](powertable-how-to-configure-approval-workflow).

## FAQ

### What does **Insert Using Form By Default** change?

**Insert Using Form By Default** changes the default behavior of the **Insert Row** button.

- When you turn the option **off**, **Insert Row** adds a blank row directly to the grid.
- When you turn the option **on**, **Insert Row** opens the **Record Details** form instead.

### What does **Insert Multiple Rows** do?

**Insert Multiple Rows** lets you insert up to **1,000** blank rows into the table.

When you select this option, PowerTable prompts you to specify the number of rows to insert.

### In the insert form, do I have to fill in every field? Does selecting **Apply** save the record?

No. Selecting **Apply** doesn't save the record. It closes the form and stages the new row as a pending change.

When you add a new record:

- Complete all fields marked as **Mandatory** with an asterisk (\*).
- **Identity** columns are generated automatically.
- You can leave optional fields blank. Optional fields aren't marked with an asterisk (\*).

### Does selecting **Apply** in the Form Editor commit the changes?

No. Selecting **Apply** creates a pending change. You can combine it with other pending changes before you preview, discard, or save them.

The changes are committed only when you select **Save to Database**.

### Which rows does 'Bulk Edit' affect?

**Bulk Edit** is available only when you select multiple rows by using the row selectors (the checkboxes for each row). It applies changes only to the selected rows.

### What happens to existing rows during the import process?

Before importing data, PowerTable classifies each row by using the primary key field.

After you select the sheet and choose **Proceed**, PowerTable scans the file and categorizes the rows into the following tabs:

- **Insert**
- **Update**
- **Error**

Each tab displays the number of rows in that category. Selecting **Import** applies the actions accordingly.

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
