---
title: "Edit and bulk edit data"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-bulk-edit-data](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-bulk-edit-data) · Last updated on **2026-09-18**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Edit and bulk edit data

Summarize this article for me

Use the PowerTable sheet to edit and update data directly in the database without writing code. Before saving, preview your changes to verify them. When you save the changes, they sync with the source in real time to keep the data up to date.

PowerTable provides the following editing capabilities:

- Update records directly from the table or through the form interface.
- Bulk edit or delete multiple records to maintain data consistency and save time.
- Preview all changes in a separate window before saving them to the database.
- View, search, filter, and export the history of saved changes.

In this article, you learn how to edit individual records and perform bulk edits in PowerTable sheets.

## Edit data in a table

To edit data directly in a table:

1. Double-click the cell that you want to modify, edit the existing value, and then press **Enter**.

   ![Screenshot of editing data directly in a cell.](media/powertable-how-to-bulk-edit-data/edit-data-cell.png)
2. PowerTable highlights changed cells and makes the **Save to Database**, **Preview Changes**, and **Discard Changes** options available.

   [![Screenshot of the options available after editing the data.](media/powertable-how-to-bulk-edit-data/save-to-database-options-available.png)](media/powertable-how-to-bulk-edit-data/save-to-database-options-available.png#lightbox)
3. Choose how you want to proceed with the edited value:

   - Select **Save to Database** to save the changes to the source database.
   - Select **Discard Changes** to revert any unsaved changes.
   - Select **Preview Changes** to review the modified records and compare the old and new values before saving.

The [Preview Changes](#preview-changes-before-saving) window displays all pending changes, including added, updated, and deleted records.

[![Screenshot of the preview changes window.](media/powertable-how-to-bulk-edit-data/preview-changes-opened.png)](media/powertable-how-to-bulk-edit-data/preview-changes-opened.png#lightbox)

## Edit by using a form interface

You can also edit a row by using the form interface.

1. Select the row to edit, and then go to **Manage Record**.

   [![Screenshot of the available manage record option after selecting one or more rows.](media/powertable-how-to-bulk-edit-data/manage-record.png)](media/powertable-how-to-bulk-edit-data/manage-record.png#lightbox)
2. A side panel opens with the **Form Editor**, where you can modify the required fields for the selected row.

   [![Screenshot of the Record Details side panel with Form Editor.](media/powertable-how-to-bulk-edit-data/form-editor-side-panel.png)](media/powertable-how-to-bulk-edit-data/form-editor-side-panel.png#lightbox)
3. Optionally, select **Customize Form** to [customize](powertable-how-to-generate-forms#customize-form) the form as needed.
4. After making the changes, select **Apply** to save them.
5. PowerTable highlights changed cells. Select **Save to Database** to save the changes, **Preview Changes** to review the modified records, or **Discard Changes** to revert them.

   ![Screenshot of the options available after editing the data by using a form.](media/powertable-how-to-bulk-edit-data/save-options-using-form.png)

## Bulk edit data

Use the bulk edit feature in PowerTable sheet to edit or delete common attributes across multiple records at the same time.

To edit multiple cells:

1. Select the rows you want to edit. To select all rows in the table or clear the selection, select the row selector in the table header.
2. Select the **Bulk Edit** option that appears after you select more than one row.

   ![Screenshot of the Bulk Edit option on the toolbar.](media/powertable-how-to-bulk-edit-data/bulk-edit.png)
3. In the **Bulk Edit** side panel, select the field you want to edit and the type of action to perform.

   Under **Action**,

   - Select **Clear cell contents** to remove the existing value.
   - Select **Set cell value** to update the existing value or enter a new value.

     [![Screenshot of the Actions in the Bulk Edit side panel.](media/powertable-how-to-bulk-edit-data/actions.png)](media/powertable-how-to-bulk-edit-data/actions.png#lightbox)
   - For text fields, select **Append Value** to add text before or after the existing value by using **Prefix** or **Suffix**.

     ![Screenshot of the Actions with Append Value action.](media/powertable-how-to-bulk-edit-data/action-append-value.png)

   The following example appends the specified suffix to the *ProductSKU* field.

   [![Screenshot of the appended field with suffix.](media/powertable-how-to-bulk-edit-data/appended-field.png)](media/powertable-how-to-bulk-edit-data/appended-field.png#lightbox)

   - For number fields, select **Offset Value** to increase, decrease, multiply, or divide the existing numeric value by a specified offset.

     ![Screenshot of the Actions with Offset Value action.](media/powertable-how-to-bulk-edit-data/action-offset-value.png)

   This example multiplies the *ProductPrice* field by two for the selected rows.

   [![Screenshot of the field multiplied by the offset value 2.](media/powertable-how-to-bulk-edit-data/offset-value-output.png)](media/powertable-how-to-bulk-edit-data/offset-value-output.png#lightbox)
4. Select **Add Action** to configure additional field updates, and then select **Apply** after configuring all required actions.

   ![Screenshot of the Bulk Edit side panel with Add Action option.](media/powertable-how-to-bulk-edit-data/add-action.png)
5. Select **Save to Database** to save the changes.

   [![Screenshot of the options available after editing the data by using the Bulk Edit side panel.](media/powertable-how-to-bulk-edit-data/save-options-bulk-edit.png)](media/powertable-how-to-bulk-edit-data/save-options-bulk-edit.png#lightbox)

## Bulk edit by using the form interface

You can also bulk edit data by using the form interface, which updates multiple fields across the selected rows at the same time.

Tip

Forms let you quickly edit multiple field attributes at once. In [Bulk Edit](#bulk-edit-data), you must select **Add Action** for each field to change.

To perform a bulk edit by using the form interface:

1. Select the required rows, and then select **Manage Record**.
2. In the **Form Editor** side panel that opens, modify the required fields.
3. Select **Apply** to update the selected rows.

   [![Screenshot of bulk editing by using a form.](media/powertable-how-to-bulk-edit-data/bulk-edit-form.png)](media/powertable-how-to-bulk-edit-data/bulk-edit-form.png#lightbox)

The *ModelName* field now shows *Racing Socks*, and the *ProductColor* field now shows *Yellow*.

[![Screenshot of the bulk edited values by using a form.](media/powertable-how-to-bulk-edit-data/bulk-edited-form.png)](media/powertable-how-to-bulk-edit-data/bulk-edited-form.png#lightbox)

## Find and replace data

Use **Find and Replace** to locate specific values in a table and replace them with new values. This feature helps you update recurring values across multiple records.

To find and replace values:

1. Select the **Find and Replace** option above the table.

   [![Screenshot of the Find and Replace option.](media/powertable-how-to-bulk-edit-data/find-and-replace.png)](media/powertable-how-to-bulk-edit-data/find-and-replace.png#lightbox)

   The **Find and Replace** window opens, as shown in the following image.

   [![Screenshot of the Find and Replace window.](media/powertable-how-to-bulk-edit-data/find-and-replace-window.png)](media/powertable-how-to-bulk-edit-data/find-and-replace-window.png#lightbox)
2. In the **Find** box, enter the value to search for.
3. Optionally, select a specific column from the **Column** dropdown. To search across all columns, keep the default selection, **All**.

   [![Screenshot of the Find text box and Column dropdown in the Find and Replace window.](media/powertable-how-to-bulk-edit-data/find-column-options.png)](media/powertable-how-to-bulk-edit-data/find-column-options.png#lightbox)
4. Select a match type:

   - **Match Case** to perform a case-sensitive search.
   - **Match entire cell contents** to match only cells whose contents exactly match the search value.

   [![Screenshot of the Match Case and Match entire cell contents options.](media/powertable-how-to-bulk-edit-data/match-case-entire-cell.png)](media/powertable-how-to-bulk-edit-data/match-case-entire-cell.png#lightbox)
5. In the **Replace With** box, enter the replacement value.

   [![Screenshot of the Replace With text box in Find and Replace window.](media/powertable-how-to-bulk-edit-data/replace-with.png)](media/powertable-how-to-bulk-edit-data/replace-with.png#lightbox)
6. Select **Find All** to view all matching results.

   [![Screenshot of the Find All option in the Find and Replace window.](media/powertable-how-to-bulk-edit-data/find-all.png)](media/powertable-how-to-bulk-edit-data/find-all.png#lightbox)
7. Use **Find Next** or **Find Previous** to navigate through the matching records.

   [![Screenshot of the Find Next and Find Previous options.](media/powertable-how-to-bulk-edit-data/find-next-previous.png)](media/powertable-how-to-bulk-edit-data/find-next-previous.png#lightbox)
8. Select **Replace** to replace the currently selected match, or **Replace All** to replace all matching values.

   [![Screenshot of the Replace and Replace All options.](media/powertable-how-to-bulk-edit-data/replace-replace-all.png)](media/powertable-how-to-bulk-edit-data/replace-replace-all.png#lightbox)

After the replacement completes, the modified cells appear highlighted. Select **Save to Database** to save the changes, **Preview Changes** to review them, or **Discard Changes** to revert them.

[![Screenshot of bulk editing by using find and replace.](media/powertable-how-to-bulk-edit-data/save-preview-discard.png)](media/powertable-how-to-bulk-edit-data/save-preview-discard.png#lightbox)

Tip

Use the **Column** dropdown to limit the search to a specific column and reduce the number of matching results.

## Preview changes before saving

When a table contains multiple modifications, it can be difficult to review and verify all changes before saving them to the database. PowerTable sheet lets you preview all pending changes in one place, and then save or discard them as needed.

Note

**Preview Changes** displays only pending changes that you didn't save to the database yet. To view the history of saved changes, use [**Audit Log**](powertable-how-to-view-audit-logs).

1. After you perform insert, update, or delete operations, the **Preview Changes** option becomes available along with the count of rows containing pending changes in the table.

   [![Screenshot of the Preview Changes option.](media/powertable-how-to-bulk-edit-data/preview-changes.png)](media/powertable-how-to-bulk-edit-data/preview-changes.png#lightbox)
2. Select **Preview Changes** to view all pending changes along with their change types. Select **All** to view every change, or select the appropriate tab to view records for a specific change type.

   [![Screenshot of the Preview Changes window.](media/powertable-how-to-bulk-edit-data/preview-changes-window.png)](media/powertable-how-to-bulk-edit-data/preview-changes-window.png#lightbox)
3. Select **Save to Database** to save the pending changes to the database.

   [![Screenshot of the Save to Database option in the preview changes window.](media/powertable-how-to-bulk-edit-data/save-to-database.png)](media/powertable-how-to-bulk-edit-data/save-to-database.png#lightbox)
4. To discard specific changes, select the row that you want to revert and then select **Reset**.

   [![Screenshot of the Reset option in the preview changes window.](media/powertable-how-to-bulk-edit-data/reset.png)](media/powertable-how-to-bulk-edit-data/reset.png#lightbox)

## View change history

Select the **History** tab in the form editor panel to view the history of changes to the selected records. The history includes the type of change, the row and column names that changed, who made the change, when they made it, and which values they modified.

[![Screenshot of the Record Details side panel with History option.](media/powertable-how-to-bulk-edit-data/history.png)](media/powertable-how-to-bulk-edit-data/history.png#lightbox)

- Use **Search** to search for a specific log.
- Use **Filter** to filter the log history by action type (Insert, Update, or Delete), who made the change, when the change occurred, or who approved the change (if approvals are enabled).

You can also find this information in **Audit Logs**, which provide more detailed tracking information for all changes.
Select [**Audit Logs**](powertable-how-to-view-audit-logs) to view more history details.

[![Screenshot of the key features available in the Audit Logs window.](media/powertable-how-to-bulk-edit-data/audit-log-features.png)](media/powertable-how-to-bulk-edit-data/audit-log-features.png#lightbox)

## Export history

In addition to viewing and tracking the history of changes, you can export the history by using the **Export** option. The export process creates an Excel (.xlsx) file with the audit logs.

To export the change history for the selected rows:

1. Select **History** > **Export**.

   [![Screenshot of the Record Details side panel with Export option.](media/powertable-how-to-bulk-edit-data/export.png)](media/powertable-how-to-bulk-edit-data/export.png#lightbox)
2. The **Export Audit Logs** panel opens, where you can configure the export settings.

   [![Screenshot of the Export Audit Logs panel.](media/powertable-how-to-bulk-edit-data/export-audit-logs.png)](media/powertable-how-to-bulk-edit-data/export-audit-logs.png#lightbox)
3. Choose the log time period to export. **Last 30 Days** is the default. You can also select **Custom Date Range** from the dropdown list and specify the required start and end dates.

   ![Screenshot of the Include data for option in Export Audit Logs panel.](media/powertable-how-to-bulk-edit-data/include-data-for.png)
4. **Download File** is the default option. Select **Export** to generate the audit log file.
5. After the link appears, right-click it and save it to your local system.

   [![Screenshot of the generated file link to save.](media/powertable-how-to-bulk-edit-data/file-generated.png)](media/powertable-how-to-bulk-edit-data/file-generated.png#lightbox)

## FAQ

### Why don't my edits reach the database as soon as I make them?

PowerTable stores your edits as pending changes until you commit them.

When you modify a cell:

- **Save to Database**, **Preview Changes**, and **Discard Changes** become available.
- **Preview Changes** displays the current number of pending changes.

Your changes aren't written to the Fabric SQL database until you select **Save to Database**. This behavior allows you to batch multiple edits into a single commit.

### What does the **Save Changes** prompt do? What happens if I select **Don't show this again**?

The **Save Changes?** prompt asks you to confirm that you want to commit all pending changes to the database.

If you select **Don't show this again**, PowerTable suppresses the confirmation dialog for future saves. Selecting **Save to Database** then commits the changes without prompting for confirmation.

After a successful commit:

- A **Data saved successfully** notification appears.
- The page refreshes.
- **Save to Database**, **Preview Changes**, and **Discard Changes** are disabled until you make additional changes.

### How do I clear a cell instead of replacing its value?

Right-click the cell and select **Clear Contents**.

### Non-English text in my tables is displayed as `????`. What should I do?

PowerTable supports non-English text, such as Japanese, when the column's input type is `NVARCHAR`.

For new tables, select `NVARCHAR` as the input type when you configure the column. For existing tables, check the column's input type. If the column is already configured as `NVARCHAR`, manually replace all the `????` values with the original non-English text. Alternatively, create a new table and configure the column with the `NVARCHAR` input type.

For non-English column names, use the **Display Name** property to display the column name in PowerTable.

### Why does the Form Editor behave differently when I select multiple rows?

When you edit a single row, the **Form Editor** displays the existing values so that you can view and update the record.

When you edit multiple rows, the **Form Editor** updates only the fields that you modify. It leaves all other fields in each selected row unchanged. Multiple-row mode doesn't display existing values or allow you to clear a field.

### What does the Offset Value action do? How is it different from setting a value?

The **Offset Value** action changes each row's existing value instead of replacing it with the same value.

You can use it to:

- Increase a value.
- Decrease a value.
- Multiply a value.
- Divide a value.

Because the action modifies each row's current value, the resulting value can differ from one row to another.

### Can I run more than one Bulk Edit action at the same time?

Yes. After you configure an action, select **Add Action** to add another one.

PowerTable applies all configured actions together when you select **Apply**.

### Can I undo part of a batch before committing it?

Yes. Select **Preview Changes** to review pending changes across the following tabs:

- **All**
- **Added**
- **Updated**
- **Deleted**

You can then select one or more rows and choose **Reset** to revert only those pending changes.

### Does 'Find and Replace' search the entire sheet?

No. **Find and Replace** searches only the column that you select in the **Column** dropdown.

If you don't select **Match entire cell contents**, PowerTable replaces the matching text wherever it appears within a cell value instead of replacing only cells whose entire value matches the search text.

### Does 'Replace All' write changes directly to the database?

No. **Replace All** creates pending changes, just like other editing operations.

After you close the **Find and Replace** dialog, select **Save to Database** to commit the changes.

### There are five editing methods. How do I know which one to use?

Choose the editing method based on the type of change that you want to make.

For example:

- Use the **Row Editor** to copy and paste values across rows or fill down values.
- Use the **Form Editor** to view and edit the existing values of a single record.
- Use **Bulk Edit** to increase, decrease, multiply, or divide values across multiple selected rows.
- Use **Find and Replace** to replace values across multiple rows within a selected column.

All five editing methods support **Preview Changes** and **Discard Changes**.

### What is the difference between the Data and Access audit tabs?

The **Data** tab records data changes, including insert, update, and delete operations. It also displays details such as:

- Row ID.
- Action.
- Transaction ID.
- Source type.
- Modified column.
- Previous value.
- New value.

The **Access** tab records changes to row-level and column-level access security settings.

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
