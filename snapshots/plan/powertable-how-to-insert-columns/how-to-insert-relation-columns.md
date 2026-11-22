---
title: "Insert relation columns in PowerTable sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-columns/how-to-insert-relation-columns](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-columns/how-to-insert-relation-columns) · Last updated on **2026-08-07**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert relation columns in PowerTable sheet

Summarize this article for me

A relation column is a type of [visual column](how-to-insert-visual-columns) that creates a one-to-many relationship between records in two tables. It links a record in a parent (master) table to one or more related records in a child (details) table. You can use this column to organize and manage related data across tables. This relationship is called a **master-detail relationship**.

Use this feature to model a hierarchical relationship between two sets of records by connecting one record (the parent) to one or more related records (the children). This structure enables logical data grouping and represents a master record along with its associated details. For example, there could be a list of customers (parent records), each with several orders (child records).

![Diagram showing master-detail relationship where customer 1 with 3 orders points to three highlighted Orders rows.](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/relation-table-illustration.png)

Note

A single record in the master table can link to multiple records in the detail table, but each record in the detail table can only link to one record in the master table.

## **Benefits of adding a relation column**

Adding a relation column provides the following benefits:

- **Organized data structure:** Group related records to make complex datasets easier to navigate and understand.
- **Data integrity:** Maintain relationships between parent and child records to prevent incomplete or inconsistent data, such as an order item without an associated customer.
- **Streamlined data entry and updates:** Reduce data duplication by storing common information in parent records and allowing child records to inherit those values.
- **Simplified reporting and filtering:** Filter, summarize, and drill down into data by using parent-child relationships.
- **Improved user experience:** View and manage related parent and child records from a single interface.
- **Scaling and maintenance:** Scale your databases while maintaining data accuracy and integrity.

## Key components

A relation column uses the following components to establish a relationship between two tables:

- **Master table:** Contains the primary records. Each record represents a unique entity, such as a customer, project, or product.
- **Detail table:** Contains records that are related to a record in the master table. You can associate multiple detail records with a single master record.
- **Foreign key column:** Stores the reference to the primary key in the master table, establishing the relationship between the two tables. PowerTable uses this column to link each detail record to its corresponding master record.

## Add a relation column

This section explains the steps to add a relation column and create parent-child relationship linked tables by using an example.

### Prerequisite

If two or more tables in a dataset share a foreign key column, you can establish a primary-foreign relationship between them.

### Steps to add a relation column

In this example, you create a parent-child relationship between the **Product Subcategories** and **Products** tables. Both tables share the **ProductSubcategoryKey** column, which acts as a foreign key.

[![Screenshot of PowerTable master table ProductSubcategories and the shared key column outlined in red.](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/master-table.png)](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/master-table.png#lightbox)

[![Screenshot of PowerTable detail table Products with the shared ProductSubcategoryKey column outlined in red.](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/details-table.png)](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/details-table.png#lightbox)

Optionally, configure the foreign key column as a [lookup column](../powertable-how-to-configure-columns/how-to-configure-lookup-relation-columns) in the **Products** table to display the corresponding subcategory name from the **ProductSubcategories** table.

[![Screenshot of the PowerTable Products table with the SubcategoryName lookup column selected, showing colored subcategory tags.](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/lookup-column.png)](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/lookup-column.png#lightbox)

To create the relationship, add a **relation column** to the parent (subcategories) table.

1. Go to **Insert Column** > **Visual** **Column** > **Add Relation Column**. A side panel opens.

   [![Screenshot of the PowerTable Insert Column menu with Visual Column expanded and Add Relation Column highlighted.](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/add-relation-column.png)](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/add-relation-column.png#lightbox)
2. Configure the column properties:

   - **Column Name**: Enter a name for the relation column.
   - **Relation Table**: Select the child table to relate to, such as **Products**.
   - **Column from Current Table**: Select the column in the current (parent) table that establishes the relationship.
   - **Column from Relation Table**: Select the matching foreign key column in the related (child) table. *ProductSubcategoryKey* is the matching foreign key column in this example.
   - **Column To Display**: Select the column whose values are displayed as reference labels for related records when you expand a record. In this example, select **Product Subcategory Key**. The corresponding lookup labels are displayed as reference labels for related records in the details table.
   - **Display name for Relation Table**: Enter the text to display in the relation column. Users select this text to expand a record and view its related records.
3. **If Condition**: Optionally, select **Add Filter** to add one or more filter conditions. Combine multiple conditions by using **AND** or **OR**. PowerTable displays only related records that meet the specified conditions. For example, you can display child records only when the **Product Price** is more than a specific value.

   [![Screenshot of the Add Relation Column panel with column name, relation table, key columns, an If Condition filter, and Cascade delete toggle set to On.](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/configure-relation-column.png)](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/configure-relation-column.png#lightbox)
4. **Cascade delete to linked records**: Enable this option to delete related child records automatically when the parent record is deleted.
5. The display properties for the relation column can be configured in the panel's **Display** tab. To learn more, see [Display](../powertable-how-to-configure-columns/how-to-configure-display-column-properties).
6. Select **Save**.

The relation column is added to the subcategories table. The number of related child records for each parent record is displayed in parentheses.

![Screenshot of the ProductSubcategories table with a highlighted Related Products column showing Products counts in parentheses.](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/relation-column-added.png)

Expand a parent record to view its related child records. The related records open in a new table, identified by the selected subcategory label.

[![Screenshot of child records table showing Mountain Bikes products, with the SubcategoryName column and Display Value header highlighted.](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/expand-relation-column-record.png)](../media/powertable-how-to-insert-columns/how-to-insert-relation-columns/expand-relation-column-record.png#lightbox)

In the details table, you can:

- Select [**Insert Row**](../powertable-how-to-insert-rows-import-data#insert-rows) to add a new child record.
- Select [**Filter**](../powertable-how-to-filter-data) to filter the displayed records.
- Select [**Sort By**](../powertable-how-to-explore-organize-data#sort-records) to sort records by a specific column.
- Use the [**Search**](../powertable-how-to-explore-organize-data#search-records) box to find records by using keywords.

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
