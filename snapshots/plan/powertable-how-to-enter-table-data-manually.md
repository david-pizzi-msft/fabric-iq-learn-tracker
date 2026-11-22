---
title: "Create table app by entering data manually"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-enter-table-data-manually](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-enter-table-data-manually) · Last updated on **2026-10-01**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create table app by entering data manually

Summarize this article for me

This article explains how to create a table app using PowerTable by entering the data manually from scratch. You'll enter data to create a table in a database, then write back any subsequent changes to the same database using the PowerTable sheet.

Note

- You can also create a table by uploading data from an Excel or CSV file. For more information, see [Create a table app with PowerTable sheets](powertable-how-to-create-table-app).
- To connect an existing database table to a PowerTable sheet and create a table app, see [Connect to a database](powertable-how-to-connect-existing-database).
- To learn how to connect to a semantic model, see [Connect to a semantic model](powertable-how-to-connect-semantic-model).

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

To create a new table in the database and enter the data manually, follow these steps:

1. Select **New Table**.
2. Choose the database schema and enter a name for the table. Currently, table names support English characters only.
3. Select **Enter Data Manually** in the **Import Data** section.
4. Select **Next**.

   [![Screenshot of selecting the schema and entering the table name.](media/powertable-how-to-enter-table-data-manually/select-database.jpg)](media/powertable-how-to-enter-table-data-manually/select-database.jpg#lightbox)
5. Configure your table by adding the column name, primary key, and other relevant details like length, precision, scale, and so on, wherever applicable.

   [![Screenshot of entering the first column name.](media/powertable-how-to-enter-table-data-manually/enter-column-name.png)](media/powertable-how-to-enter-table-data-manually/enter-column-name.png#lightbox)

   Note

   - Currently, column names support English characters only. To display non-English column names, scroll to the right in the column configuration table and set the **Display Name** property to Japanese or another non-English label to display localized labels in PowerTable.
   - If your data contains Japanese or other non-English text, define those columns' input type as `NVARCHAR` so PowerTable supports and renders non-English characters correctly.
6. Select **Add Column** to add a new column. Use the bin icon to delete a column.
7. Select **Finish** after entering all the column details.

   [![Screenshot of selecting Finish after configuring all the column names for the new table.](media/powertable-how-to-enter-table-data-manually/finish-table.png)](media/powertable-how-to-enter-table-data-manually/finish-table.png#lightbox)
8. An empty table is successfully created using PowerTable, with the configured columns.

   [![Screenshot of the new empty table with configured columns.](media/powertable-how-to-enter-table-data-manually/empty-table.png)](media/powertable-how-to-enter-table-data-manually/empty-table.png#lightbox)
9. You can now insert rows into this table using the **Insert Row** option.

   [![Screenshot of inserting rows to the empty table.](media/powertable-how-to-enter-table-data-manually/insert-rows.png)](media/powertable-how-to-enter-table-data-manually/insert-rows.png#lightbox)
10. Select **Preview Changes** to preview the added rows and changes.

    [![Screenshot of preview with added rows and changes.](media/powertable-how-to-enter-table-data-manually/preview-changes.png)](media/powertable-how-to-enter-table-data-manually/preview-changes.png#lightbox)
11. To discard the changes, select **Discard Changes**.
12. After previewing, select **Save to Database** and **Proceed** to save the rows to the table in the database.
13. Finally, select **Save** at the top right corner to save the PowerTable sheet.

    [![Screenshot of saving the new table.](media/powertable-how-to-enter-table-data-manually/save-table.png)](media/powertable-how-to-enter-table-data-manually/save-table.png#lightbox)

## Related content

- [Create a table app with PowerTable by importing an Excel or a CSV file](powertable-how-to-create-table-app)
- [Connect PowerTable sheet to a semantic model](powertable-how-to-connect-semantic-model)
- [Connect to an existing database](powertable-how-to-connect-existing-database)

## Next steps

Configure [access control](powertable-how-to-set-up-access-control) and [automated workflows and approvals](powertable-how-to-configure-approval-workflow) for your new app.

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
