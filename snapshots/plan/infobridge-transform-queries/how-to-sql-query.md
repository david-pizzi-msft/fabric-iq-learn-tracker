---
title: "SQL queries in Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transform-queries/how-to-sql-query](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transform-queries/how-to-sql-query) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# SQL queries in Infobridge

Summarize this article for me

Use **SQL Query** to create a new query by writing SQL statements against an existing Infobridge query.

SQL queries let you retrieve specific columns, filter data, and reshape query results without modifying the original query.

Note

SQL queries create a new query. They don't modify the original Infobridge query.

## Example scenario

This example creates a new SQL query named **High Value Product Sales** from an existing planning sheet query.

The SQL query retrieves the product, category, country/region, units, unit price, and revenue columns from the source query.

## Create a SQL query

This example shows how to create a new SQL query from an existing Infobridge query.

1. On the **Home** ribbon, select **SQL Query**.

   [![Screenshot of the SQL Query command selected on the Home ribbon.](../media/infobridge-transform-queries/how-to-sql-query/select-sql-query.png)](../media/infobridge-transform-queries/how-to-sql-query/select-sql-query.png#lightbox)
2. In **Source Name**, enter **High Value Product Sales**.

   [![Screenshot of the Create SQL Query dialog displaying the Source Name and SQL Query fields.](../media/infobridge-transform-queries/how-to-sql-query/open-create-sql-query-dialog.png)](../media/infobridge-transform-queries/how-to-sql-query/open-create-sql-query-dialog.png#lightbox)
3. Under **Query References**, on the **Reference** tab, select **Query 1 - Planning 1**.

   Infobridge inserts the query reference into the SQL editor.

   [![Screenshot of the Create SQL Query dialog showing Query 1 - Planning 1 selected from the Reference tab.](../media/infobridge-transform-queries/how-to-sql-query/select-query-reference.png)](../media/infobridge-transform-queries/how-to-sql-query/select-query-reference.png#lightbox)
4. In **SQL Query**, enter the following SQL statement.

   ```
   SELECT
       ProductName,
       Category,
       Ctry,
       Units,
       "Unit Price",
       Revenue
   FROM {{query_id:1}}
   ```

   Note

   Add query references by using the **Query References** pane or by entering `{{query_id:1}}` directly in the SQL statement.
5. Select **Create**.

   Infobridge creates a new SQL query named **High Value Product Sales** under **Queries**.

   [![Screenshot of the Queries pane showing the newly created High Value Product Sales SQL query.](../media/infobridge-transform-queries/how-to-sql-query/sql-query-created.png)](../media/infobridge-transform-queries/how-to-sql-query/sql-query-created.png#lightbox)

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
