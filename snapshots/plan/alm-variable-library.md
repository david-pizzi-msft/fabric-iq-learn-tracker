---
title: "ALM â Variable library"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/alm-variable-library](https://learn.microsoft.com/en-us/fabric/iq/plan/alm-variable-library) · Last updated on **2026-09-30**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# ALM â Variable library

Summarize this article for me

A variable library provides a reusable way to configure references that are used by Plan items. Instead of selecting the same semantic model, database, or connection each time, you can define the reference as a variable and reuse it where supported. This article shows how to use a variable library with a Plan item by creating the following variables:

- **SM\_Variable** â an item reference to the **Enterprise Dataset** semantic model.
- **DB\_Variable** â an item reference to the **My\_Planning\_DB** SQL database.
- **DMTS\_Variable** â a connection reference to the **My\_Fabric\_SQL\_Connection** connection, which uses the **FabricSql** connection type.

The example then uses these variables in the **Enterprise\_Plan** Plan item. The semantic model is configured from **SM\_Variable**, and the Writeback destination uses **DMTS\_Variable** for the connection and **DB\_Variable** for the database.

## Create a variable library

Create a variable library in the workspace where you are developing the

Plan item.

1. In your workspace, select **New item**.
2. Create a **Variable library** item.

[![Screenshot showing the workspace with the option to create a Variable library.](media/alm-variable-library/create-variable-library.png)](media/alm-variable-library/create-variable-library.png#lightbox)

3. Enter a name for the variable library.
4. Select **Create**.

In this example, the variable library is named **Variables\_1**.

[![Screenshot showing the New Variable library dialog with the variable library name entered.](media/alm-variable-library/name-variable-library.png)](media/alm-variable-library/name-variable-library.png#lightbox)

## Create an item reference for the semantic model

Create an item reference variable that points to the semantic model used by the Plan item.

1. In the variable library, select **New variable**.

[![Screenshot showing the New variable action in the variable library.](media/alm-variable-library/select-new-variable-semantic-model.png)](media/alm-variable-library/select-new-variable-semantic-model.png#lightbox)

2. Enter **SM\_Variable** as the variable name.
3. Select **Item reference** as the variable type.

[![Screenshot showing Item reference selected as the variable type.](media/alm-variable-library/select-item-reference.png)](media/alm-variable-library/select-item-reference.png#lightbox)

4. Select the item picker for the variable value.
5. Select the **Enterprise Dataset** semantic model.

[![Screenshot showing the Enterprise Dataset semantic model selected as the variable value.](media/alm-variable-library/select-enterprise-dataset.png)](media/alm-variable-library/select-enterprise-dataset.png#lightbox)

6. Select **Save**.

[![Screenshot showing the saved semantic model variable in the variable library.](media/alm-variable-library/save-semantic-model-variable.png)](media/alm-variable-library/save-semantic-model-variable.png#lightbox)

## Create a Plan item

Create the Plan item that uses the semantic model variable.

1. In the workspace, select **New item**.
2. Select **Plan**.

[![Screenshot showing New item with Plan selected.](media/alm-variable-library/create-plan-item.png)](media/alm-variable-library/create-plan-item.png#lightbox)

3. Enter **Enterprise\_Plan** as the Plan name.
4. Select **Create**.

[![Screenshot showing the New Plan dialog with Enterprise_Plan entered as the Plan name.](media/alm-variable-library/name-enterprise-plan.png)](media/alm-variable-library/name-enterprise-plan.png#lightbox)

## Use the semantic model variable in the Plan

Configure the Plan item to use **SM\_Variable** instead of selecting the semantic model directly.

1. In the Plan creation flow, select **Semantic Model**.

[![Screenshot showing the Semantic Model option for the new Plan item.](media/alm-variable-library/select-semantic-model.png)](media/alm-variable-library/select-semantic-model.png#lightbox)

2. In the **Select Semantic Model** pane, select **Variable Library**.
3. In **Semantic Model**, select **Select from variable**.

[![Screenshot showing Variable Library selected as the source for the semantic model.](media/alm-variable-library/select-variable-library-for-semantic-model.png)](media/alm-variable-library/select-variable-library-for-semantic-model.png#lightbox)

4. Select **SM\_Variable**.

[![Screenshot showing SM_Variable selected from the variable library.](media/alm-variable-library/select-semantic-model-variable.png)](media/alm-variable-library/select-semantic-model-variable.png#lightbox)

5. Select **Connect**.

[![Screenshot showing the Connect button after selecting the semantic model variable.](media/alm-variable-library/connect-semantic-model-variable.png)](media/alm-variable-library/connect-semantic-model-variable.png#lightbox)

The Plan is now configured to use the semantic model referenced by **SM\_Variable**.

[![Screenshot showing the semantic model added to the Plan item.](media/alm-variable-library/semantic-model-variable-added.png)](media/alm-variable-library/semantic-model-variable-added.png#lightbox)

## Create an item reference for the SQL database

Create an item reference variable for the SQL database that you use as the Writeback database.

1. In the variable library, select **New variable**.
2. Enter **DB\_Variable** as the variable name.
3. Select **Item reference** as the variable type.
4. Select the item picker for the variable value.

[![Screenshot showing the New variable action and Item reference selected for the database variable.](media/alm-variable-library/create-database-item-reference.png)](media/alm-variable-library/create-database-item-reference.png#lightbox)

5. Select **My\_Planning\_DB**.

[![Screenshot showing the SQL database item selected for DB_Variable.](media/alm-variable-library/select-sql-database.png)](media/alm-variable-library/select-sql-database.png#lightbox)

6. Select **Save**.

[![Screenshot showing DB_Variable saved in the variable library.](media/alm-variable-library/save-database-variable.png)](media/alm-variable-library/save-database-variable.png#lightbox)

## Create a connection reference for the App DB connection

Create a connection reference variable for the reusable App DB connection.

1. In the variable library, select **New variable**.
2. Enter **DMTS\_Variable** as the variable name.
3. Select **Connection reference** as the variable type.
4. Select the connection picker.

[![Screenshot showing the New variable action with Connection reference selected for DMTS_Variable.](media/alm-variable-library/create-connection-reference.png)](media/alm-variable-library/create-connection-reference.png#lightbox)

5. Select **My\_Fabric\_SQL\_Connection**.
6. Select **Save**.

[![Screenshot showing My_Fabric_SQL_Connection with the FabricSql connection type selected.](media/alm-variable-library/select-fabricsql-connection.png)](media/alm-variable-library/select-fabricsql-connection.png#lightbox)

[![Screenshot showing DMTS_Variable saved as a connection reference.](media/alm-variable-library/save-connection-variable.png)](media/alm-variable-library/save-connection-variable.png#lightbox)

The variable library now contains reusable references for the semantic model, SQL database, and App DB connection.

## Use the variables for a Writeback destination

Use **DMTS\_Variable** and **DB\_Variable** when you configure the Writeback destination in **Enterprise\_Plan**.

1. Open **Enterprise\_Plan**.
2. Select **Planning**.

[![Screenshot showing Enterprise_Plan opened with the Planning experience selected.](media/alm-variable-library/open-enterprise-plan-planning.png)](media/alm-variable-library/open-enterprise-plan-planning.png#lightbox)

3. Create a planning sheet.

[![Screenshot showing the New Planning Sheet dialog with the Create button.](media/alm-variable-library/create-planning-sheet.png)](media/alm-variable-library/create-planning-sheet.png#lightbox)

4. In the Writeback experience, select **Add destination**.

[![Screenshot showing the Add destination action for Writeback.](media/alm-variable-library/add-writeback-destination.png)](media/alm-variable-library/add-writeback-destination.png#lightbox)

5. In **Create Destination**, open the **Select a Connection** list.

[![Screenshot showing the Select a Connection list in the Create Destination pane.](media/alm-variable-library/open-connection-dropdown.png)](media/alm-variable-library/open-connection-dropdown.png#lightbox)

6. Select **Use Variable**.

[![Screenshot showing Use Variable selected for the connection.](media/alm-variable-library/select-use-variable.png)](media/alm-variable-library/select-use-variable.png#lightbox)

7. In the **Select variable** pane, select **DMTS\_Variable**.
8. Select **Select variable**.

[![Screenshot showing DMTS_Variable selected from the variable library.](media/alm-variable-library/select-dmts-variable.png)](media/alm-variable-library/select-dmts-variable.png#lightbox)

9. Under **Select Database From**, select **Variable Library**.
10. In **Database Name**, select **Select from variable**.

[![Screenshot showing Variable Library selected as the source for the database name.](media/alm-variable-library/select-database-from-variable.png)](media/alm-variable-library/select-database-from-variable.png#lightbox)

11. Select **DB\_Variable**.
12. Select **Select variable**.

[![Screenshot showing DB_Variable selected from the variable library.](media/alm-variable-library/select-db-variable.png)](media/alm-variable-library/select-db-variable.png#lightbox)

13. Complete the remaining required destination fields, such as **Schema** and **Table Name**.
14. Select **Add**.

[![Screenshot showing the completed Writeback destination configuration with variable-based connection and database values.](media/alm-variable-library/add-writeback-destination-configuration.png)](media/alm-variable-library/add-writeback-destination-configuration.png#lightbox)

The Writeback destination is added to the Plan using the reusable variables.

[![Screenshot showing the Writeback destination added to the Plan.](media/alm-variable-library/writeback-destination-added.png)](media/alm-variable-library/writeback-destination-added.png#lightbox)

## Summary

In this example, the variable library centralizes the references

required by the Plan item:

| Variable | Type | Reference |
| --- | --- | --- |
| **SM\_Variable** | Item reference | **Enterprise Dataset** semantic model |
| **DB\_Variable** | Item reference | **My\_Planning\_DB** SQL database |
| **DMTS\_Variable** | Connection reference | **My\_Fabric\_SQL\_Connection** connection |

The Plan uses **SM\_Variable** for its semantic model and uses **DMTS\_Variable** and **DB\_Variable** when configuring the Writeback destination. This approach avoids selecting the same references directly each time they are required and provides reusable configuration for ALM scenarios.

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
