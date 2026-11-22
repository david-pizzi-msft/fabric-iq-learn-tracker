---
title: "Build a table app using PowerTable by importing an Excel file"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-create-table-app](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-create-table-app) · Last updated on **2026-09-18**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Build a table app using PowerTable by importing an Excel file

Summarize this article for me

PowerTable lets you build no-code table apps in Fabric Plan. It has an Excel-like interface for structured data entry and reference data management.

In this article, you learn how to create a table app with PowerTable sheets.

To create a table app using PowerTable, use one of these four approaches:

- Upload Excel or CSV file to import data
- [Connect to an existing database table](powertable-how-to-connect-existing-database)
- [Enter data directly into the table app](powertable-how-to-enter-table-data-manually)
- [Connect to a semantic model](powertable-how-to-connect-semantic-model)

In this article, you use the first method: how to upload an Excel or a CSV file to create a PowerTable sheet.

Note

- In the first three methods, the app uses the same underlying database table as both the source and destination. You create a database table and import or enter data into it, or connect to an existing database table. Any changes made through the app are written back to the same table.
- In the last method, where you connect to a semantic model, the semantic model is the input source and the database table is the destination for writeback data.

## Prerequisites

Before you begin, make sure that you have the following prerequisites in place:

- Connection established to the [Fabric SQL database](planning-how-to-create-database-connection) that stores the data for your PowerTable app.
- [A plan item](planning-how-to-get-started#create-plan-item) created in your Fabric workspace.

## Create a PowerTable sheet

1. In your plan, select **New PowerTable Sheet** or select the **PowerTable** icon on the landing page. Enter a name for the sheet and select **Create**.

   [![Screenshot of a new PowerTable sheet.](media/includes/new-powertable.png)](media/includes/new-powertable.png#lightbox)
2. Select **Create a New App** to create your app. You can also select **Explore PowerTable** to experience a sample PowerTable app.

   [![Screenshot of the Create a New App button.](media/includes/create-new-app.png)](media/includes/create-new-app.png#lightbox)
3. **Select a Connection:** Choose a Fabric SQL connection if available. If there are no connections, create one by selecting [Create Connection](planning-how-to-create-database-connection).

   [![Screenshot of selecting a Fabric SQL connection in the PowerTable connection dropdown.](media/includes/connect.png)](media/includes/connect.png#lightbox)
4. **Database Name:** Select the **Database Name** field to open the list of databases available.

   [![Screenshot of the Database Name field highlighted in the Select Fabric SQL Connection dialog, ready to open the database list.](media/includes/select-field-choose-database.png)](media/includes/select-field-choose-database.png#lightbox)
5. Select the destination Fabric SQL database to store the table data and then select **Add**.

   [![Screenshot of selecting the database.](media/includes/select-database.png)](media/includes/select-database.png#lightbox)
6. Select **Connect**.

   ![Screenshot of selecting connect to connect to the database.](media/includes/connect-database.png)

## Create a table

Select a table for the data to be stored in. There are two options:

- Select **Existing Table** to connect to an existing table in the Fabric SQL database, OR
- Select **New Table** to create a new table in the database. This option is shown in the next steps.

To create a new table and import the Excel or CSV data, follow these steps:

1. Select **New Table**.
2. Choose the database schema.
3. Enter a **Table Name**. Currently, table names support English characters only.
4. Select **Upload File** in the **Import Data** section.
5. Select the space to upload the CSV or Excel file from your local system.

   [![Screenshot of uploading an Excel or CSV  file to PowerTable.](media/powertable-how-to-create-table-app/upload-file.png)](media/powertable-how-to-create-table-app/upload-file.png#lightbox)
6. Select the sheet that contains the data you want to import.

   - Enter a name for the table.
   - Review and, if necessary, modify the start and end cell ranges that contain the data to import.
   - Preview the imported data, and then select **Next**.

   [![Screenshot of previewing data.](media/powertable-how-to-create-table-app/preview-data.png)](media/powertable-how-to-create-table-app/preview-data.png#lightbox)

   Note

   To import only the headers, toggle on **Import header only**.

### Configure table

PowerTable sheets automatically detect column properties and rename any unsupported column names to match the supported format. You can review and modify them as needed.

Currently, column names support English characters only. To display non-English column names, scroll to the right in the column configuration table and set the **Display Name** property to Japanese or another non-English label to display localized labels in PowerTable.

If your data contains Japanese or other non-English text, define those columns' input type as `NVARCHAR` so PowerTable supports and renders non-English characters correctly.

[![Screenshot of the table configuration window with field names to configure their properties.](media/powertable-how-to-create-table-app/table-configuration.png)](media/powertable-how-to-create-table-app/table-configuration.png#lightbox)

1. Review the detected column settings. Modify them if required.
2. If the primary key isn't selected, select the appropriate column as the primary key.
3. Configure columns as required:
   - Mark fields as **Mandatory** if they must contain values.
   - Set fields with distinct values as **Unique Key** to allow unique values.
   - Set a column as an **Identity Column** when you need PowerTable to generate unique, sequential values automatically. Only numeric columns and primary key columns can be configured as identity columns.
4. Modify column properties, including:
   - Length
   - Data type
   - Input type
   - Display name
5. Enter default values for columns, if required.
6. Optionally, select **Add Column** to create additional columns.
7. To create a composite primary key, select **Unique Combination**, and then select two or more columns to define a unique combination key.

[![Screenshot of selecting unique combination and choosing two fields.](media/powertable-how-to-create-table-app/unique-combination.png)](media/powertable-how-to-create-table-app/unique-combination.png#lightbox)

Note

In this step, you can **enable Slowly Changing Dimensions (SCDs)** by turning the toggle.
For a table, this setting is a one-time configuration that you can't change later.

Select **Finish**.

[![Screenshot of selecting Finish to save table configuration.](media/powertable-how-to-create-table-app/finish-table.png)](media/powertable-how-to-create-table-app/finish-table.png#lightbox)

The table app is created successfully in PowerTable with the configured columns and values. Select **Save** to save your table.

[![Screenshot of saving the new table app.](media/powertable-how-to-create-table-app/save-table.png)](media/powertable-how-to-create-table-app/save-table.png#lightbox)

### Write back changes to source

You can update your data table and sync changes with the source database.

1. To edit a cell in the table, double-click it, enter the value, and select **Enter**.
2. With **Preview Changes**, you can preview the changes.
3. Select **Save to Database**, then **Proceed** to save the changes instantly (unless an [approval workflow](powertable-how-to-configure-approval-workflow) is enabled).

   [![Screenshot of saving the table to database.](media/powertable-how-to-create-table-app/save-to-database.png)](media/powertable-how-to-create-table-app/save-to-database.png#lightbox)

   The source database is updated.
4. Select **PowerTable > Audit**. The audit trail records all changes in detail, including the Row ID, action type, modified columns, previous values, new values, user name, and timestamp.

   [![Screenshot of audit log.](media/powertable-how-to-create-table-app/audit.png)](media/powertable-how-to-create-table-app/audit.png#lightbox)

## Next steps

After creating your first PowerTable application, explore these other features:

- **Reference data management**: Manage master and reference data centrally while maintaining synchronization with enterprise data platforms. PowerTable sheets provide support for bulk insert/update, lookups, formulas, cascading updates, audit tracking, CRUD permissions, SCD support, and native Microsoft Fabric SQL DB integration.
- **Project management**: PowerTable sheets provide Gantt layouts and timeline views to manage project schedules, track progress, and monitor dependencies.
- **Workflow management**: Approval workflows enable governance over sensitive data updates by routing change requests through designated approvers.
- **Operational automation**: Eventâdriven automation enables teams to automate repetitive processes such as record updates and notify them via email/Teams notifications.
- **Collaborative data management**: Comments, threaded discussions, mentions, and notifications allow teams to collaborate directly within the data application.
- **Productivity**: Use forms for structured data collection and insertion without coding. Use the master-detail view, cross-tab view, and resource layout for time management, task management, tracking, and resource planning.
- **Connected planning**: Link PowerTable tables to plans so updates in PowerTable sheets become inputs for a plan. This process allows a change in your revenue forecast to automatically flow into headcount, cash flow, and operational plans.

## Related content

Other ways to create a table:

- [Connect to a semantic model](powertable-how-to-connect-semantic-model)
- [Connect to a database table](powertable-how-to-connect-existing-database)
- [Enter data manually](powertable-how-to-enter-table-data-manually)

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
