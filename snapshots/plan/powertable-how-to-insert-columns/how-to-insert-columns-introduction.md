---
title: "Introduction to inserting PowerTable columns"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-columns/how-to-insert-columns-introduction](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-columns/how-to-insert-columns-introduction) · Last updated on **2026-08-07**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Introduction to inserting PowerTable columns

Summarize this article for me

As your business requirements evolve, you might need to capture new types of information in your tables. In PowerTable, you can add columns to an existing table at any time. This feature lets you adjust your table structure as your needs change without rebuilding the table.

By using this feature, you can:

- Add and manage database columns directly from the PowerTable sheet, without writing any queries.
- Add columns only to the PowerTable sheet to manage extra data without affecting the source database.
- Choose from various column types such as data, formula, lookup, reference, attachment, roll up, button, and others to capture and manage information in the way that best suits your needs.

You can add a new column to a table during table creation, or after the table is created or connected.

## Add column during table creation

Use **Add column** during the initial table configuration to create and configure extra columns alongside the imported columns.

[![Screenshot of Configure Table step with column settings and Add Column button.](../media/powertable-how-to-insert-columns/add-columns-summary/add-during-table-creation.png)](../media/powertable-how-to-insert-columns/add-columns-summary/add-during-table-creation.png#lightbox)

## Add column after you create or connect a table

After you create or connect a table, add new columns at any time by using **Insert Column**.

[![Screenshot of PowerTable sheet showing Insert Column dropdown highlighted with column type choices.](../media/powertable-how-to-insert-columns/add-columns-summary/add-after-table-creation.png)](../media/powertable-how-to-insert-columns/add-columns-summary/add-after-table-creation.png#lightbox)

Alternatively, select **Setup** > **Columns** and use the **Add Visual Column**, **Add Formula Column**, and **Add Database Column** options during column configuration.

[![Screenshot of Columns setup page with Add Visual, Formula, and Database Columns dropdowns.](../media/powertable-how-to-insert-columns/add-columns-summary/add-columns-options.png)](../media/powertable-how-to-insert-columns/add-columns-summary/add-columns-options.png#lightbox)

- **Visual columns** exist only within the PowerTable sheet. PowerTable doesn't add these columns to the source database. This column type includes multi-select relationship columns, reference columns, relation columns, roll up, button, and attachment columns. For more information, see [Insert visual columns in PowerTable](how-to-insert-visual-columns).
- **Database columns** exist in the underlying database and become part of the table schema. For more information, see [Insert database columns in PowerTable](how-to-insert-database-column).
- **Formula columns** can be either visual or database columns. Use formula columns to calculate values based on formulas and display the results in the table. For more information, see [Insert formula columns in PowerTable](how-to-insert-formula-columns).

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
