---
title: "Insert data input rows"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-rows-data-input](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-rows-data-input) · Last updated on **2026-08-20**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert data input rows

Summarize this article for me

Insert rows in planning sheets to add data that's missing from the source, and enter values manually. This method is useful when source data is incomplete or doesn't include newly introduced business entities or metrics. For example, a financial statement might include revenue and expense metrics but not shares outstanding, or a sales report might not yet contain data for a newly launched product category. By adding data input rows, you can capture missing values directly in the planning sheet and incorporate them into the planning process.

This article explains how to insert data input rows and enter values directly in the report.

## Insert a data input row

Insert a data input row using either of the following methods:

- [From the Planning tab](#from-the-planning-tab)
- [Using row gripper](#using-the-row-gripper)

### From the Planning tab

1. Select a row at the level where you want to insert the new row in the report.
2. Go to **Planning** > **Insert Row**. This option is disabled if no row is selected.
3. Navigate to **Data Input** and select **Number**.

![Screenshot of inserting data input rows using Planning tab.](media/planning-how-to-insert-rows-data-input/steps-insert-data-input-rows.png)

### Using the row gripper

1. Hover over a row to highlight the **row gripper** icon.
2. Select the gripper and choose **Insert** > **Data Input**.

   ![Screenshot of inserting data input rows using row gripper.](media/planning-how-to-insert-rows-data-input/steps-insert-row-row-gripper.png)

   A side pane opens where you can configure row properties.

   [![Screenshot of row properties side pane.](media/planning-how-to-insert-rows-data-input/side-pane-row-properties.png)](media/planning-how-to-insert-rows-data-input/side-pane-row-properties.png#lightbox)
3. Enter a name in the **Title** field, configure additional settings as needed (described in the following sections), and select **Create**. The system adds an empty row with default properties at the selected level.

Before you select **Create**, you can modify default row properties by configuring additional settings. The following sections describe these settings.

## Data input row properties

- **Row type**: Use the dropdown to select the type of row to insert:

  - **Calculated row (Formula)**
  - **Data input row (Number)**

  You can switch between row types at any time.

  [![Screenshot of configuring title and row type.](media/planning-how-to-insert-rows-data-input/title-row-type.png)](media/planning-how-to-insert-rows-data-input/title-row-type.png#lightbox)
- **Insert As**: Choose how the row is inserted:

  - **Single Row**: Inserts one row.
  - **Templated**: Inserts the row across all hierarchy levels. For example, you can create a product line and replicate it across all region levels.
- **Scaling factor**: Set the scale for values in the data input row to thousands, millions, billions, or trillions. By default, it's set to *Auto*.

  [![Screenshot of configuring insert as and scaling factor.](media/planning-how-to-insert-rows-data-input/insert-as-scaling-factor.jpg)](media/planning-how-to-insert-rows-data-input/insert-as-scaling-factor.jpg#lightbox)
- **Include in total**: When enabled, the row values are included in the parent total. It's enabled by default.
- **Distribute parent value to children**: When enabled, row values entered at the parent level are distributed to child levels.
- **Default value**: Set the initial value for the row, which can be either a static value or a value sourced from another row.

  Choose **Static** to enter a static row value. Choose **Row** to source values from another row in the report. Enter the required row name in the **Selected Row**.

  [![Screenshot of configuring include in total, distribute parent value to children and default value.](media/planning-how-to-insert-rows-data-input/include-in-total-default-value.jpg)](media/planning-how-to-insert-rows-data-input/include-in-total-default-value.jpg#lightbox)
- **Bind for cross filter/RLS**: Enable **Bind for Cross filter/RLS** to ensure that cross-filter selections and row-level security (RLS) rules are applied to formula rows and data input rows that reference other rows. For more information about binding rows, see [Configure formula row properties](planning-how-to-insert-rows-formula#configure-formula-row-properties).

  [![Screenshot of configuring bind for cross filter/RLS.](media/planning-how-to-insert-rows-data-input/bind-for-cross-filter.png)](media/planning-how-to-insert-rows-data-input/bind-for-cross-filter.png#lightbox)

  Note

  If the **Bind for cross filter/RLS option** is disabled, a manager responsible for *Canada* accounts might see a manually inserted row that references *US* data.
- **Delete a static row**: Hover over the row, select the row gripper, and then select **Delete Row**.
  Alternatively, delete rows from the [Manage Rows](planning-how-to-manage-inserted-rows) interface.

  ![Screenshot of deleting a row.](media/planning-how-to-insert-rows-data-input/delete-row.png)
- **Allow Input**: Choose when users are allowed to enter inputs into a data input row.

  - **Edit mode**: Users can enter values only in edit mode.
  - **Read mode**: Users can enter values even in read mode.

## Bulk insert data input rows

You can bulk insert leaf-level rows or row hierarchies by using the **Insert Row(s)** option from the Planning tab or row gripper.

### Insert rows

1. Select any child row or the parent row under which you want to create new rows. The new rows will be created below the selected row.
2. Use the row gripper and select **Insert** > **Insert Row(s)**, or go to **Planning** > **Insert Row** > **Data Input** > **Insert Row(s)**.

   ![Screenshot of bulk inserting rows using row gripper.](media/planning-how-to-insert-rows-data-input/steps-bulk-insert-row-gripper.png)

   [![Screenshot of bulk inserting rows using Planning tab.](media/planning-how-to-insert-rows-data-input/steps-bulk-insert-planning-tab.png)](media/planning-how-to-insert-rows-data-input/steps-bulk-insert-planning-tab.png#lightbox)
3. In the **Insert Row(s)** pop-up window, the parent row levels are already filled in. Enter the new row name.
4. To insert another row, select **Add New** or use the **+ icon** next to the parent category.
   [![Screenshot of bulk inserting rows.](media/planning-how-to-insert-rows-data-input/bulk-inserting-rows.png)](media/planning-how-to-insert-rows-data-input/bulk-inserting-rows.png#lightbox)
5. To insert multiple rows at once, use the dropdown next to **Add New** and choose whether you want to insert **1**, **5**, or **10 rows**.
6. Enter row names and select **Save**.

You can also specify row dimensions for the new rows by selecting the icon in the **Insert Row(s) window**.

![Screenshot of specifying row dimensions while bulk inserting.](media/planning-how-to-insert-rows-data-input/bulk-insert-specify-row-dimension.png)

## Insert a row hierarchy

To insert a hierarchy of rows:

1. Go to **Insert Row(s)** and select **Add New**.
2. In the Insert Row(s) window, the parent row hierarchy is pre-filled with existing values. Overwrite these values to define the new row hierarchy.
3. Select **Save**.

[![Screenshot of inserting row hierarchy.](media/planning-how-to-insert-rows-data-input/insert-row-hierarchy.png)](media/planning-how-to-insert-rows-data-input/insert-row-hierarchy.png#lightbox)

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
