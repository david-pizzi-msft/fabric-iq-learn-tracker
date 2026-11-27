---
title: "Set up writeback to persist data"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-persist-data](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-persist-data) · Last updated on **2026-11-26**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Set up writeback to persist data

Summarize this article for me

Planning supports exporting planning data to Fabric SQL databases. Write back budgets, forecasts, adjustments, and scenarios to keep planning data synchronized with enterprise systems. Unlike conventional BI and planning tools that require predefined database schemas and IT-managed writeback infrastructure, planning supports dynamic database configuration and runtime table creation.

## Writeback use cases

Maintain planning and analytics data in a single governed environment instead of exporting data manually. Common scenarios include:

- Save budget and forecast inputs directly to the data platform.
- Store scenario planning results for further analysis.
- Capture manual adjustments made in planning sheets.
- Synchronize planning data with enterprise data warehouses.

## Prerequisites

Before you begin, make sure you have the following prerequisites in place:

- The planning sheet contains at least one row or column dimension.
- Required permissions are assigned to users who perform writeback.
- To use OneLake as the writeback destination, enable the corresponding tenant and workspace settings. To learn more about the settings, see [OneLake enablement tenant setting](../onelake-enablement-tenant-setting#enable-onelake-storage-for-new-plan-items). These settings apply to new plan items. For existing plan items, also [migrate the item to OneLake](../onelake-enablement-tenant-setting#migrate-existing-plan-items-to-onelake).

## Create a writeback destination

Before writing back your planning data, configure a writeback destination, either OneLake or a Fabric SQL database. Hybrid configurations aren't supported.

1. In the **Writeback** ribbon, select **Add Destination**.
2. Select the **Storage Type** - based on this selection, your data is saved to a Fabric SQL database or directly in OneLake.

   Note

   - This setting is a one-time setting for a planning sheet. When you create subsequent destinations, you don't select the storage type.
   - To switch to OneLake (or vice versa), delete all existing destinations before adding a destination of the new type.
3. Configure the Fabric SQL or OneLake destination table and schema.

### Fabric SQL destination

To add a Fabric SQL destination, follow these steps:

1. Select an existing Fabric SQL database connection or select **+ Create Connection** to create a new one.
2. Configure the database name:

   - Direct Selection: Choose **Database Item** to select a specific database.
   - Environment-Based: Reference a variable library to automatically adapt database names across different environments (for example, Dev, Test, Prod). To learn more about using variable libraries in writeback, see [Use variables for writeback destinations and connections](../resources/cicd-planning#use-variables-for-writeback-destinations-and-connections).
3. Select the database from the OneLake catalog or select the configured variable. Specify the schema name and table name.

### OneLake

To add a OneLake destination, enter the schema name and writeback table name.

For either type of destination, finish the remaining settings:

1. Enter the **Decimal Precision** to specify the number of digits after the decimal point for numeric columns.
2. Use **Text Length** to define the maximum length for string columns (for example, length of all string columns = 512) or choose **Custom**.
3. Select **Add** to create the writeback destination.

![Screenshot of creating a writeback destination.](../media/planning-writeback/planning-how-to-persist-data/create-writeback-destination.png)

## Manage destinations

To view, update, or reuse configured destinations, go to **Writeback** > **Manage**.

[![Screenshot of writeback destinations configured in the planning sheet.](../media/planning-writeback/planning-how-to-persist-data/manage-destination.png)](../media/planning-writeback/planning-how-to-persist-data/manage-destination.png#lightbox)

## Configure writeback settings

Use writeback settings to configure how data entered in a planning sheet is saved back to the underlying data source. Writeback settings help ensure that planning data entered by users is stored correctly, consistently, and in a format that aligns with the organization's data model. Define the structure, filtering behavior, and data format used when writing planning values to the destination.

Configure settings from **Writeback > Settings**.

- **General**: Defines the core settings for the writeback operation. For detailed information about general settings for writeback, see [Configure general settings for writeback](planning-how-to-configure-general-settings).
- **Data**: Used to select and configure the measures and dimensions that participate in the writeback process.
- **Destinations**: Defines where the planning data is written back, such as a database table or storage location.
- **Advanced**: Provides more configuration options for controlling writeback behavior and system-level settings.

[![Screenshot of writeback settings.](../media/planning-writeback/planning-how-to-persist-data/writeback-settings.jpg)](../media/planning-writeback/planning-how-to-persist-data/writeback-settings.jpg#lightbox)

### Set the writeback type

Control how data is structured in the writeback table. Go to **Writeback > Settings > Writeback Type**, and select one of the following types:

- Select **Long** to store measures as key-value pairs in a row-based format.
- Select **Wide** to store measures in a column-based format.
- Select **Long with Changes**. This format is the same as long format, but tracks only the changed values written back from the planning sheet.
- Select **Wide with Changes**. This format is the same as wide format, but tracks only the changed values written back from the planning sheet.

[![Screenshot of selecting the writeback type.](../media/planning-writeback/planning-how-to-persist-data/select-writeback-type.jpg)](../media/planning-writeback/planning-how-to-persist-data/select-writeback-type.jpg#lightbox)

## Perform writeback

Follow the steps in this section to write back data from your planning sheet to the configured destination and view the writeback log.

1. Write back scenarios, forecasts, data inputs, and comments to the designated data platform. Select **Writeback** > **Writeback** to trigger a writeback. After completion, a confirmation message is displayed.

   [![Screenshot of writeback completion notification.](../media/planning-writeback/planning-how-to-persist-data/writeback-status.jpg)](../media/planning-writeback/planning-how-to-persist-data/writeback-status.jpg#lightbox)
2. Open the destination database to view the writeback data.

   Important

   Authorized database access only

   Always query your writeback data by using your configured destination database. Don't access or query the internal \_\_fabric\_plan\_sys\_db database, as it's reserved strictly for system operations and app storage.

   [![Screenshot of data written back to a Fabric SQL destination.](../media/planning-writeback/planning-how-to-persist-data/writeback-destination-data.png)](../media/planning-writeback/planning-how-to-persist-data/writeback-destination-data.png#lightbox)
3. After the initial writeback, you might need to add or remove row or column dimensions as you build your planning sheet. If the destination structure must change because of these updates, drop and re-create the table with the updated structure before the next writeback.

   [![Screenshot of destination structure mismatch.](../media/planning-writeback/planning-how-to-persist-data/writeback-table-mismatch.png)](../media/planning-writeback/planning-how-to-persist-data/writeback-table-mismatch.png#lightbox)
4. Writeback logs include milestones, payload size, and writeback duration. Select **Writeback** > **Logs** to view the writeback logs.

   [![Screenshot of writeback logs.](../media/planning-writeback/planning-how-to-persist-data/writeback-logs.jpg)](../media/planning-writeback/planning-how-to-persist-data/writeback-logs.jpg#lightbox)
5. Select a writeback ID to view detailed information about a specific writeback instance.

   [![Screenshot of writeback logs with payload size, milestones, and duration.](../media/planning-writeback/planning-how-to-persist-data/writeback-detailed-logs.png)](../media/planning-writeback/planning-how-to-persist-data/writeback-detailed-logs.png#lightbox)

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
