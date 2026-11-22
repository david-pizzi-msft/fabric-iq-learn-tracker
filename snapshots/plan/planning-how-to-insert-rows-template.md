---
title: "Insert template rows"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-rows-template](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-rows-template) · Last updated on **2026-05-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert template rows

Summarize this article for me

Planning enables efficient hierarchy handling with template rows, letting you insert custom rows across all levels of a hierarchy at once instead of adding them individually.

This article explains how to insert template rows and use them across hierarchy levels.

## Create a template row

1. Select the row underneath the space where you want to insert the template row. The template row will be inserted above the selected row.
2. Go to **Planning** > **Insert Row** > **Data Input** and select **Number**, or select the **row gripper**, then choose **Insert** > **Data Input**.
3. In the **Static Row** pane, select **Templated**, enter a title, and configure values as needed:

   [![Screenshot of inserting a template row.](media/planning-how-to-insert-rows-template/insert-template-row.jpg)](media/planning-how-to-insert-rows-template/insert-template-row.jpg#lightbox)
4. Configure a default value for the template row.

   - Choose **Row** in **Default Value** to source values from another row.
   - Choose **Static** to enter a fixed value.
   - Or enter values directly in the rows after creation.
5. Finally, select **Create** to insert the row across all hierarchy levels.

Note

You can also create formula (calculated) rows as template rows, by selecting **Planning** > **Insert Row** > **Formula**. Alternatively, set the **Row Type** to *Formula* in the side pane shown in the images.

## Configure template row properties

Configure other properties for template rows, such as **Scaling Factor**, **Include in total**, **Distribute parent value to children**, and **Allow input**. For more information, see [Row properties](planning-how-to-insert-rows-data-input#data-input-row-properties).

You can also configure the following settings for template rows:

- **Row position**: Defines where the row appears at each category level. By default, it's set to *Auto*.

  - **Auto**: Creates the template row above the selected row.
  - **First**: Creates the template row at the top of each category level.
  - **Last**: Creates the template row at the bottom of each category level.

  [![Screenshot of row position in template row properties.](media/planning-how-to-insert-rows-template/template-row-properties.png)](media/planning-how-to-insert-rows-template/template-row-properties.png#lightbox)

## Edit or delete a template row

- Use the row gripper and select the **Edit** or **Delete Row** options.
- Or go to **Insert Row** > **Manage Rows** > **Template Rows**, hover over the created row, and choose the appropriate action through the icons.

  [![Screenshot of editing or deleting a template row.](media/planning-how-to-insert-rows-template/edit-delete-template-row.png)](media/planning-how-to-insert-rows-template/edit-delete-template-row.png#lightbox)

## Conditional template rows

Template conditions can be configured to control which parent categories and levels receive template rows. Template rows are created only for row categories that meet these conditions.

1. In the **Static Row** window > **Template conditions** section, select **Configure**.
2. In the **Set Template Conditions** window, specify where the template rows should be applied by choosing the required categories, and select **Apply**.

   [![Screenshot of setting a template condition.](media/planning-how-to-insert-rows-template/set-template-conditions.png)](media/planning-how-to-insert-rows-template/set-template-conditions.png#lightbox)
3. Use this to restrict or allow specific hierarchy levels to get the template rows.

   The following image shows the *Energy Drinks* template row inserted only for the selected category, *Beverages*, across the hierarchy.

   [![Screenshot of a template row inserted only for selected category.](media/planning-how-to-insert-rows-template/energy-drinks-template-row.png)](media/planning-how-to-insert-rows-template/energy-drinks-template-row.png#lightbox)

## Dynamic referencing in template rows

Planning provides a dynamic referencing feature that lets you reference a siblingâs child row while inserting calculated template rows. This lets values be automatically populated based on the corresponding parent category.

### Create a dynamic reference in template rows

1. Select the row underneath the space where you want to insert the template row. The template row will be inserted above the selected row.
2. Go to **Planning** > **Insert Row** and select **Formula**, or use the **row gripper** > **Insert > Formula**.
3. In the **Calculated Row** window, select **Templated** and enter a title.
4. Define a formula by using **References** to source values from a sibling row.

   In the following example, a template row named *Cocktails* references the value of *Soda* under the *Beverages* category.

   [![Screenshot of configuring dynamic reference row.](media/planning-how-to-insert-rows-template/dynamic-reference-row.png)](media/planning-how-to-insert-rows-template/dynamic-reference-row.png#lightbox)

   The referenced value is applied across all sibling categories within the same *Sub Region*. For sub-regions such as *APAC* and *EMEA*, the *Cocktails* row dynamically retrieves the value of the *Soda* subcategory within each respective sub-region.

   [![Screenshot of inserting a dynamically referenced row.](media/planning-how-to-insert-rows-template/cocktails-dynamic-row.png)](media/planning-how-to-insert-rows-template/cocktails-dynamic-row.png#lightbox)

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
