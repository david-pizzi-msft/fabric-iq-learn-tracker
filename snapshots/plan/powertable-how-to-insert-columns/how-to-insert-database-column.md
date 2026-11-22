---
title: "Insert database columns"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-columns/how-to-insert-database-column](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-columns/how-to-insert-database-column) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert database columns

Summarize this article for me

Add new columns to the source database directly through the PowerTable app. This feature removes the need to work with the database directly, enhancing security and efficiency.

Note

Ensure you have the required permissions to the database you connect to, as you're adding a column directly to the source database.

## Add a database column

Consider the following example where you add the *Status* column to the **Products** table.

1. Select **PowerTable** > **Insert Column** > **Database Column** to add a new column to the source table.

   ![Screenshot of PowerTable Insert Column menu with Database Column option highlighted.](../media/powertable-how-to-insert-columns/how-to-add-database-columns/insert-database-column.png)
2. In the side panel, enter the column name and its data type. For this example, add a text column by selecting the `VARCHAR` data type.

   [![Screenshot of Add Database Column panel with Column Name and Data type fields highlighted.](../media/powertable-how-to-insert-columns/how-to-add-database-columns/column-name-type.png)](../media/powertable-how-to-insert-columns/how-to-add-database-columns/column-name-type.png#lightbox)
3. Select **Not null** to prevent null values in the column. When you enable this option, you must specify a default value to use when no value is available.

   ![Screenshot of Add Database Column panel with Not null checkbox enabled and Default Value set to OPEN.](../media/powertable-how-to-insert-columns/how-to-add-database-columns/null-default-value.png)
4. Even if you don't select **Not null**, you can specify a default value for the column. Default values can be either **manual** or **formula-based**:

   - Select **Manual** to specify a static default value.
   - Select **Formula** to derive the default value by using a configurable formula instead of a static value.

   ![Screenshot of Add Database Column panel with Default Value section highlighted showing Manual and Formula options.](../media/powertable-how-to-insert-columns/how-to-add-database-columns/set-default-value.png)

   Note

   You can specify a default value for the column, regardless of whether you configure the column as nullable or non-nullable. For more information about configuring default values, see [Default value](../powertable-how-to-configure-columns/how-to-configure-general-column-properties#default-value).
5. Use **Length** to set the character limit for this column.
6. Select **Save** to create the database column.

## Null setting scenarios

### When you select Not null

When you select Not null, the default value automatically fills the new column and any future rows you add. This setup ensures a valid value is always available when you don't provide one explicitly. You can update these values later.

[![Screenshot of PowerTable showing Status column with OPEN default value applied to existing and new rows.](../media/powertable-how-to-insert-columns/how-to-add-database-columns/default-value-added.png)](../media/powertable-how-to-insert-columns/how-to-add-database-columns/default-value-added.png#lightbox)

### When you clear Not null

When you clear Not null, the column accepts null values. When you create the column, the existing rows are blank, even if you set a default value. However, when you add new rows, the configured default value automatically fills the column. You can modify the default value if needed.

![Screenshot of PowerTable with Status column blank for existing rows and OPEN default value in new row.](../media/powertable-how-to-insert-columns/how-to-add-database-columns/default-value-applied-new-row-only.png)

## Configure extra properties

Configure extra properties for the new column by using these steps:

1. Open the column header menu for the new column, and then select **Edit**.

   ![Screenshot of PowerTable column header menu with Edit option highlighted.](../media/powertable-how-to-insert-columns/how-to-add-database-columns/edit-column-properties.png)
2. Configure the column properties, and then select **Save**. To learn about configuring columns, see [Configure general properties](../powertable-how-to-configure-columns/how-to-configure-general-column-properties#configure-general-properties) and [Configure display properties](../powertable-how-to-configure-columns/how-to-configure-display-column-properties).

   ![Screenshot of Status column properties panel showing General tab with Input Type, Data Type, Constraints, and Default Value settings.](../media/powertable-how-to-insert-columns/how-to-add-database-columns/configure-columns-panel.png)

Now you can enter data in the column. The new column and the changes sync with the source database.

[![Screenshot of PowerTable showing the newly added Status column with user-added values ready for syncing.](../media/powertable-how-to-insert-columns/how-to-add-database-columns/database-column-added.png)](../media/powertable-how-to-insert-columns/how-to-add-database-columns/database-column-added.png#lightbox)

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
