---
title: "Create table app by connecting to a database table"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-connect-existing-database](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-connect-existing-database) · Last updated on **2026-10-01**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create table app by connecting to a database table

Summarize this article for me

Connect your existing database tables to PowerTable to manage both transactional and master data in one place. After establishing the connection, you can edit data, insert rows and columns, set up workflows, and write back changes directly to the connected database.

The following steps explain the process.

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

1. Select **Existing Table** to connect to an existing Fabric SQL database.

   Note

   - Currently, table names that contain only English characters display correctly. Tables with non-English characters aren't supported.
2. Choose the database schema and the table name to connect to.
3. Select **Next**.

   [![Screenshot of selecting an existing database.](media/powertable-how-to-connect-existing-database/select-existing-database.png)](media/powertable-how-to-connect-existing-database/select-existing-database.png#lightbox)
4. PowerTable sheets automatically detect column properties. Review the table configuration.
5. Modify the input type and the primary key if needed.

   If your data contains Japanese or other non-English text, define those columns' input type as `NVARCHAR` so PowerTable supports and renders non-English characters correctly.

   Similarly, column names support English characters only. To display non-English column names, scroll to the right in the column configuration table and set the **Display Name** property to Japanese or another non-English label to display localized labels in PowerTable.
6. Select **Finish**.

   [![Screenshot of selecting Finish after configuring the table.](media/powertable-how-to-connect-existing-database/finish-table.png)](media/powertable-how-to-connect-existing-database/finish-table.png#lightbox)

You have now successfully connected to a database and created a table app using PowerTable. Select **Save** to save your table.

[![Screenshot of saving the new table.](media/powertable-how-to-connect-existing-database/save-table.png)](media/powertable-how-to-connect-existing-database/save-table.png#lightbox)

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
