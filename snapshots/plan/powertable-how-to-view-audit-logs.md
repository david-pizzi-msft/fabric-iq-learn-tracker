---
title: "Audit logs in PowerTable"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-view-audit-logs](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-view-audit-logs) · Last updated on **2026-07-14**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Audit logs in PowerTable

Summarize this article for me

Audit logs provide a comprehensive record of changes to a table. In PowerTable, the audit log helps you track changes to data, user access activities, and configuration settings.

By using the audit log, you can:

- Track data, access, and configuration changes.
- Review who made a change and when they made it.
- Search and filter logs to locate specific records.
- Export audit logs for auditing, reporting, and compliance purposes.

In this article, you learn how to view, search, filter, and export audit logs.

## View audit logs and track changes

To view audit logs:

1. Select **PowerTable** > **Audit**. The audit log window opens and shows recent changes to the table.

   ![Screenshot of the Audit option on the toolbar.](media/powertable-how-to-view-audit-logs/audit.png)
2. Select the appropriate tab to review a specific type of change:

   - **Data**: Shows data modifications to records.
   - **Access**: Shows changes to row and column access permissions.
   - **Table**: Shows changes to table settings and configurations.

   [![Screenshot of the Data, Access and Table options.](media/powertable-how-to-view-audit-logs/data-access-table.png)](media/powertable-how-to-view-audit-logs/data-access-table.png#lightbox)

### Data

The **Data** tab provides a chronological record of transactions and actions on the source table.

The audit log includes the following information:

- Row ID of the modified record.
- Type of modification.
- Transaction ID for the change.
- Source type.
- Modified columns.
- Previous and new values.
- User who made the change.
- Date and time of the change.
- Approver details, such as approver names and date and time of approval: if approval flow is enabled.

[![Screenshot of the Data tab.](media/powertable-how-to-view-audit-logs/data.png)](media/powertable-how-to-view-audit-logs/data.png#lightbox)

The audit log captures significant actions such as **Insert**, **Update**, **Delete**, and **Soft Delete**.

### Access

The **Access** tab tracks changes to row and column access permissions, including who made each change and when.

[![Screenshot of the Access tab.](media/powertable-how-to-view-audit-logs/access.png)](media/powertable-how-to-view-audit-logs/access.png#lightbox)

### Table

The **Table** tab records changes to table settings and column configurations, including the addition of new columns and updates to existing column settings.

[![Screenshot of the Table tab.](media/powertable-how-to-view-audit-logs/table.png)](media/powertable-how-to-view-audit-logs/table.png#lightbox)

Important

PowerTable sheet doesn't support audit log when type 2 SCDs are enabled.

## Search and filter audit logs

Use the **Search** and **Filter** options to locate specific changes and records.

### Search log

Enter a **Row ID**, **Modified Column**, **Action**, or **Source Type** to search for specific audit log entries. The logs update dynamically to show the entries that match your search criteria.

[![Screenshot of searching a log..](media/powertable-how-to-view-audit-logs/search-log.png)](media/powertable-how-to-view-audit-logs/search-log.png#lightbox)

### Filter by user

To view the changes a specific user made, select the user from the **All Users** dropdown.

![Screenshot of filtering the logs by user.](media/powertable-how-to-view-audit-logs/all-users.png)

### Filter by time period

Filter logs by a predefined time period or a custom date range. The default is **Last 24 Hours**.

[![Screenshot of filtering the logs by time period.](media/powertable-how-to-view-audit-logs/last-24-hours.png)](media/powertable-how-to-view-audit-logs/last-24-hours.png#lightbox)

### Advanced filters

Select **Filter** to filter the logs based on the following options:

- **Action**: Filter logs by action type, such as Insert, Update, Delete, or Soft Delete.
- **Approved By**: Filter logs by the user who approved the changes.
- **Modified Column**: Filter logs by the modified columns.
- **Transaction ID**: Filter logs by specific transaction IDs.
- **Reset All**: Clear all applied filters.

[![Screenshot of the filtering options in Filter pane.](media/powertable-how-to-view-audit-logs/filter.png)](media/powertable-how-to-view-audit-logs/filter.png#lightbox)

## Export audit logs

You can export audit logs in Excel (.xlsx) format for offline analysis and reporting.

1. To export, select **Download Logs**.

   [![Screenshot of the Download Logs option.](media/powertable-how-to-view-audit-logs/download-logs.png)](media/powertable-how-to-view-audit-logs/download-logs.png#lightbox)
2. Specify the time period for the exported logs by using the **Include Data For** dropdown.

   [![Screenshot of the Export Audit Logs window.](media/powertable-how-to-view-audit-logs/include-data-for.png)](media/powertable-how-to-view-audit-logs/include-data-for.png#lightbox)
3. By default, *Last 30 Days* is selected. To export logs for a certain time period, select **Custom Date Range** and enter the relevant dates.
4. Select **Export**.
5. After the file link appears, select and hold (or right-click) the link and save the file to your local system.

## Refresh logs

Use **Refresh** to retrieve the latest logs.

## Revert changes

Use **Revert Changes** to revert previously written-back updates, so you can safely restore records to an earlier state. If you make incorrect changes, you can undo them by using this option.

You can only revert **UPDATE** actions.

1. Select one or more records from the audit log that contain updated values.
2. Select **Revert Changes**.

   [![Screenshot of the Revert Changes option.](media/powertable-how-to-view-audit-logs/revert-changes.png)](media/powertable-how-to-view-audit-logs/revert-changes.png#lightbox)
3. Confirm the changes and select **Revert**.

   [![Screenshot of the Revert Changes dialog box.](media/powertable-how-to-view-audit-logs/revert.png)](media/powertable-how-to-view-audit-logs/revert.png#lightbox)

PowerTable rolls back the updates to their previous state.

[![Screenshot of the rolled back updates.](media/powertable-how-to-view-audit-logs/rolled-back-updates.png)](media/powertable-how-to-view-audit-logs/rolled-back-updates.png#lightbox)

PowerTable logs the revert actions, as shown in the following screenshot, along with the action type, user information, and reverted timestamp. PowerTable also keeps the old entries intact for complete traceability.

[![Screenshot of the logged revert actions.](media/powertable-how-to-view-audit-logs/logged-revert-actions.png)](media/powertable-how-to-view-audit-logs/logged-revert-actions.png#lightbox)

PowerTable doesn't support **Revert Changes** for Type 3 SCD records.

[![Screenshot of the revert changes not supported for Type 3 SCD records notification.](media/powertable-how-to-view-audit-logs/revert-not-supported-type3-scd.png)](media/powertable-how-to-view-audit-logs/revert-not-supported-type3-scd.png#lightbox)

### Reversion in case of multiple updates in a row

If you update a record multiple times, PowerTable uses the earliest modification before the selected items for reversion.

For example, in the following image, the product color changes three times. *NA* > *Pink* > *Red* > *Black*.

You select the change from *Pink* to *Red* for reversion.

[![Screenshot of the Revert Changes for multiple updates.](media/powertable-how-to-view-audit-logs/reversion-multiple-updates.png)](media/powertable-how-to-view-audit-logs/reversion-multiple-updates.png#lightbox)

PowerTable performs the reversion in the following way:

1. PowerTable undoes any changes made after the selected modification. PowerTable undoes both changesâfrom *Pink* to *Red* and the subsequent change from *Red* to *Black*.
2. The record reverts to the last modification made (*NA* > ***Pink***) before the chosen change.

   [![Screenshot of reverting multiple updates.](media/powertable-how-to-view-audit-logs/revert-multiple-updates.png)](media/powertable-how-to-view-audit-logs/revert-multiple-updates.png#lightbox)
3. When you select **Revert**, the reverted state becomes the current version.

### Error log

If you delete a record after an update, you can't revert that update because the record no longer exists. PowerTable displays these records on the **Error** tab in the confirmation preview so that you can review them before proceeding.

Consider the following example, where you select all changes for reversion. The confirmation preview shows the old and new values for records that you can revert. For row ID *611*, PowerTable displays an error because you deleted the record after updating it.

[![Screenshot of the Error tab in Revert Changes dialog box.](media/powertable-how-to-view-audit-logs/error.png)](media/powertable-how-to-view-audit-logs/error.png#lightbox)

To exclude the deleted rows and proceed with reverting the remaining records, select **Exclude errors and Revert**.

## View writeback logs

Writeback logs provide a high-level view of writeback operations performed on a table. Use writeback logs to monitor the status of transactions, track import and update activities, and review execution details for each writeback operation.

To view writeback logs, select **PowerTable**, select the dropdown arrow next to **Audit**, and then select **Writeback Logs**.

![Screenshot of Writeback logs option on the toolbar.](media/powertable-how-to-view-audit-logs/writeback-logs.png)

The **Writeback Logs** page opens and shows all writeback transactions for the selected table.

[![Screenshot of the Writeback Logs page.](media/powertable-how-to-view-audit-logs/writeback-logs-page.png)](media/powertable-how-to-view-audit-logs/writeback-logs-page.png#lightbox)

The writeback logs page includes the following information:

- **ID**: Unique identifier for the writeback transaction.
- **Database**: Name of the database associated with the transaction.
- **Source**: Source system where the transaction ran.
- **Transaction**: Type of writeback operation performed.
- **Row Count**: Number of rows affected by the transaction.
- **Duration**: Time to complete the transaction.
- **Status**: Current status of the transaction.
- **Started At**: Date and time when the transaction started.
- **Started By**: User who performed the transaction.

### Search and filter writeback logs

Use the search and filter options to find specific writeback transactions.

The following filters are available:

- **ID**: Search for a specific writeback transaction by its ID.

  [![Screenshot of the ID search box.](media/powertable-how-to-view-audit-logs/id.png)](media/powertable-how-to-view-audit-logs/id.png#lightbox)
- **Transaction**: Filter transactions by operation type, such as **Insert**, **Update**, **Delete**, **SCD Update**, or **Bulk Import**.

  [![Screenshot of the Transaction dropdown.](media/powertable-how-to-view-audit-logs/transaction.png)](media/powertable-how-to-view-audit-logs/transaction.png#lightbox)
- **Started By**: Filter transactions by the user who initiated the writeback operation.

  [![Screenshot of the Started By dropdown.](media/powertable-how-to-view-audit-logs/started-by.png)](media/powertable-how-to-view-audit-logs/started-by.png#lightbox)
- **Status**: Filter transactions by status, such as **Success**, **Partial Success**, **Failed**, **Running**, or **Queued**.

  [![Screenshot of the Status dropdown.](media/powertable-how-to-view-audit-logs/status.png)](media/powertable-how-to-view-audit-logs/status.png#lightbox)
- **Job Type**: Filter transactions by execution type, such as **Direct** or **Approvals**.

  [![Screenshot of the Job Type dropdown.](media/powertable-how-to-view-audit-logs/job-type.png)](media/powertable-how-to-view-audit-logs/job-type.png#lightbox)
- **Started At**: Filter transactions by time period, including **Within the Last 24 Hours**, **Last 7 Days**, **Last 30 Days**, or a custom date range by using **Between**.

  [![Screenshot of the Started At dropdown.](media/powertable-how-to-view-audit-logs/started-at.png)](media/powertable-how-to-view-audit-logs/started-at.png#lightbox)
- **Reset Filter**: Clear all applied filters and restore the default view. This option becomes available when you apply one or more filters.

  [![Screenshot of the Reset Filter option.](media/powertable-how-to-view-audit-logs/reset-filter.png)](media/powertable-how-to-view-audit-logs/reset-filter.png#lightbox)

## View last updated details

Use the **Last Updated Details** columns to view the most recent update information for each record directly in the PowerTable sheet.

To insert these columns:

1. Select **PowerTable**, and then select the dropdown arrow next to **Audit**.
2. Turn on the **Last Updated Details** toggle.

   ![Screenshot of the Last Updated Details toggle.](media/powertable-how-to-view-audit-logs/last-updated-details.png)

The table includes two extra columns:

- **Last Edited At**: Shows the date and time when the record was last modified.
- **Last Edited By**: Shows the user who last modified the record.

  [![Screenshot of the Last Edited At and Last Edited By columns.](media/powertable-how-to-view-audit-logs/last-edited-at-by.png)](media/powertable-how-to-view-audit-logs/last-edited-at-by.png#lightbox)

Disable the **Last Updated Details** toggle to hide these columns from the table.

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
