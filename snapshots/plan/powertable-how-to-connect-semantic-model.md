---
title: "Create table app by connecting to a semantic model"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-connect-semantic-model](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-connect-semantic-model) · Last updated on **2026-10-26**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create table app by connecting to a semantic model

Summarize this article for me

This article describes how to create a table app by connecting the PowerTable sheet to a semantic model. You can save the data table, along with any changes or updates, to your preferred destination database. You can also write back subsequent changes to the same database table.

In this method, the semantic model is the initial input source, and the created database is the destination that stores the data and changes written back from the app.

Note

You can also create a table by uploading data from an Excel or CSV file. For more information, see [Create a table app with PowerTable sheets](powertable-how-to-create-table-app).
To connect an existing database table to a PowerTable sheet and create a table app, see [Connect to a database](powertable-how-to-connect-existing-database).

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

1. Select **New Table**.
2. Choose the database schema.
3. Enter a **Table Name**. Currently, table names support English characters only.
4. Choose **Connect To Semantic Model** in **Import Data**.
5. Select **Semantic Model Item** and then select the search field to choose a semantic model.

   [![Screenshot of the Select Table dialog with New Table, Connect To Semantic Model, and Semantic Model Item selected and the Semantic Model search field highlighted.](media/powertable-how-to-connect-semantic-model/select-semantic-model-field.png)](media/powertable-how-to-connect-semantic-model/select-semantic-model-field.png#lightbox)

   Note

   The connection-based flow for semantic models is deprecated. You can connect to a semantic model directly by using your signed-in identity without configuring a shared cloud connection.
6. Select a semantic model from the list and select **Add**.

   [![Screenshot of the OneLake catalog Choose a semantic model dialog with Employee Details selected and the Add button highlighted.](media/powertable-how-to-connect-semantic-model/choose-semantic-model.png)](media/powertable-how-to-connect-semantic-model/choose-semantic-model.png#lightbox)
7. Select **Next**.

   [![Screenshot of connecting to semantic model.](media/powertable-how-to-connect-semantic-model/new-table.png)](media/powertable-how-to-connect-semantic-model/new-table.png#lightbox)

   Note

   Capacity workspaces with Pro licenses are not supported. Make sure to select a workspace of premium capacity.

### Map data

1. Map and assign your data to the table by selecting the required fields and corresponding values.

   [![Screenshot of assigning fields and values.](media/powertable-how-to-connect-semantic-model/assign-fields.png)](media/powertable-how-to-connect-semantic-model/assign-fields.png#lightbox)

   Note

   Currently, column names support English characters only. To display non-English column names in the table app, configure the display name as mentioned in [the following section](#configure-table).
2. Set the primary key fields by selecting the three dots and selecting primary keys.

   [![Screenshot of setting primary keys.](media/powertable-how-to-connect-semantic-model/set-primary-key.png)](media/powertable-how-to-connect-semantic-model/set-primary-key.png#lightbox)
3. If needed, you can use filters to include only specific field values from the table.

   [![Screenshot of using filters.](media/powertable-how-to-connect-semantic-model/using-filters.png)](media/powertable-how-to-connect-semantic-model/using-filters.png#lightbox)
4. Select **Next**.

   [![Screenshot of configured semantic model for the new table.](media/powertable-how-to-connect-semantic-model/configured-semantic-model.png)](media/powertable-how-to-connect-semantic-model/configured-semantic-model.png#lightbox)

### Configure table

PowerTable sheets automatically detect column properties and rename any unsupported column names to match the supported format. You can review and modify them as needed.

Note

- Currently, column names support English characters only. To display non-English column names, scroll to the right in the column configuration table and set the **Display Name** property to Japanese or another non-English label to display localized labels in PowerTable.
- If your data contains Japanese or other non-English text, define those columns' input type as `NVARCHAR` so PowerTable supports and renders non-English characters correctly.

[![Screenshot of table configuration window after configuring the fields.](media/powertable-how-to-connect-semantic-model/finish-table-from-model.jpg)](media/powertable-how-to-connect-semantic-model/finish-table-from-model.jpg#lightbox)

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

Note

In this step, you can **enable Slowly Changing Dimensions (SCDs)** by turning the toggle.
For a table, this is a one-time configuration that you can't modify later.

### Finish

Select **Finish**.

The table app is created successfully in PowerTable with the configured columns and values. Select **Save** to save your table.

[![Screenshot of saving the new table app.](media/powertable-how-to-connect-semantic-model/save-table-from-model.png)](media/powertable-how-to-connect-semantic-model/save-table-from-model.png#lightbox)

### Refresh semantic model

Select **Refresh** > **Semantic Model** in the status bar to refresh and retrieve the latest data from the semantic model. Use this option when the source data changes and you want to update the data displayed in the PowerTable sheet before saving it to the destination database.

Refreshing the semantic model updates the data available in the PowerTable sheet, including newly added or updated records. This action lets you work with the latest source data before saving the table to the database.

[![Screenshot of the PowerTable status bar with the Refresh dropdown expanded to show the Semantic Model option.](media/powertable-how-to-connect-semantic-model/refresh-semantic-model.png)](media/powertable-how-to-connect-semantic-model/refresh-semantic-model.png#lightbox)

## FAQ

### Do changes made in PowerTable update the semantic model or its underlying data source?

No. PowerTable uses the semantic model only to **seed** the destination table. It doesn't update the semantic model or its underlying data source.

When you create a PowerTable app from a semantic model, PowerTable reads the semantic model and copies its data into the selected **Fabric SQL database** destination table.

After the initial load:

- PowerTable writes all changes directly to the **Fabric SQL database destination table**.
- Changes made in PowerTable don't update the semantic model or its underlying data source.

### Are there any exceptions to this behavior based on the underlying data source (Lakehouse, Warehouse, or external database) or on the semantic model storage mode?

No. The **Save to Database** option always writes data to the configured **Fabric SQL database destination table**, regardless of the semantic model's underlying data source or storage mode.

When you create a PowerTable app from a semantic model:

- The semantic model only seeds the PowerTable with initial data. The underlying data source, whether a **Lakehouse, Warehouse, or external database**, doesn't receive any data.
- The semantic model's storage mode, whether **Import, DirectQuery, or Direct Lake**, doesn't affect the write path. It only determines how PowerTable reads the seed data.
- After the initial load, PowerTable writes all changes directly to the configured **Fabric SQL database destination table**.

### When do newly added members in PowerTable appear on a planning sheet? Is this scenario supported?

Yes. PowerTable supports this scenario. Newly added members appear in the planning sheet in two ways:

- **Direct connection:** When PowerTable writes to a Fabric SQL database table, the table appears in the planning sheet's data pane under **Data > From Sheets**, where you can assign its columns directly as dimensions and measures. There's no replication or intermediate semantic model. Newly added members are available in the planning sheet as soon as you commit the changes.
- **Direct Lake connection:** When the planning sheet uses a **Direct Lake semantic model**, PowerTable writes the data to the Fabric SQL database table, which is automatically replicated to **OneLake**. The Direct Lake semantic model reads the replicated data from OneLake. When automatic updates are enabled, newly added members automatically appear in the planning sheet after the changes reach OneLake, although a short delay might occur because replication has near-real-time latency.

Note

Schema changes, such as adding or modifying columns, might require a semantic model refresh.

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
