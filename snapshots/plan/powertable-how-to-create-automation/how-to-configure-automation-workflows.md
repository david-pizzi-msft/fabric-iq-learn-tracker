---
title: "Configure automation workflows"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-create-automation/how-to-configure-automation-workflows](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-create-automation/how-to-configure-automation-workflows) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure automation workflows

Summarize this article for me

This article explains how to create an automation workflow. You learn how to configure workflow triggers and actions to automate tasks such as creating records, finding records, and cascading updates across related tables.

Use event triggers in automation to run downstream processes within Microsoft Fabric such as executing a dataflow, pipeline, notebook, or a semantic model refresh based on certain events. You can also integrate Microsoft Teams in your workflow so users get timely notifications.

Note

To learn about the concept of automation, see [Automation](../powertable-concept-automation).

## Create an automation flow

1. To create an automation for a table, go to **Setup** > **Automations**.

   ![Screenshot of the PowerTable ribbon with the Setup tab and Automations button highlighted.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/open-automations-from-setup-menu.png)
2. In the new window, select **Create Automation** to create a new automation flow.

   [![Screenshot of the Automations window with the Create Automation button highlighted.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/create-automation-button.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/create-automation-button.png#lightbox)
3. A new automation workflow is created for you to configure the trigger and actions. Name your automation flow by selecting the pencil icon.

## Add trigger

1. Select **Add Trigger** and choose a trigger. Alternatively, select one of the suggested triggers directly.

   [![Screenshot of the Automations editor with the Add Trigger button and pencil rename icon highlighted.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/add-trigger.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/add-trigger.png#lightbox)

   | Trigger | Description |
   | --- | --- |
   | When a record is created | Triggers an automation flow when a user creates a record in the PowerTable table. |
   | When a record is updated | Triggers an automation flow when a user updates an existing record. |
   | When a record is deleted | Triggers an automation flow when a user deletes a record. |
   | When a form is submitted | Triggers an automation flow when a user submits a form that creates a record. |
   | When a button is clicked | Triggers an automation flow when a user selects a button in a button column. |

   Note

   All triggers monitor events in the current table where you configure the automation.
2. After you select a trigger, the **Properties** pane opens.

   - Enter a description.
   - Select **+ Add** to add one or more rules that determine when the trigger starts.
   - Use **AND** or **OR** to combine multiple rules. The trigger runs only when the specified record or the data changes meet the configured conditions.
   - For **Update Record** trigger, you can specify which fields to monitor for data changes. If you specify all fields, the workflow includes any new fields that you add in the future.
   - The available operators depend on the selected field's data type. You can use operators such as **Equals**, **Less than**, **Greater than**, **Is**, **Is empty**, and **Contains**, and more.
   - The rules support using predefined built-in functions such as **Current date**, **Current user email**, and any field references that are available through forms or **Find Record(s)**.

   [![Screenshot of the Properties pane for a When a record is created trigger with the Rules section highlighted.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/automation-workflow-trigger-options.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/automation-workflow-trigger-options.png#lightbox)

## Add actions

Select **Add Action** to add one or more actions. You can trigger an action on related databases or Fabric items such as semantic models, notebooks, dataflows, or data pipelines. You can also integrate external applications such as Microsoft Teams to send notifications to users.

Each action type is explained in the following sections.

![Screenshot of the Add Action button highlighted with a menu listing Conditional Group, Repeating Group, Create Record, Update Record, Delete Record, Find Records, Bulk Create Record, and Execute Stored Procedure.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/automation-add-action-menu-options.png)

### Create Record

This action creates a new record in the specified table.

1. Enter the schema and table name.
2. Select **Add Fields** to specify the fields for the new record.
3. Enter the field values or use predefined functions to fill in their corresponding values.

   [![Screenshot of the Create Record action Properties pane with Add Fields highlighted and a menu listing trigger fields like OrderDateTime and OrderNumber.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/automation-create-record-add-fields-properties.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/automation-create-record-add-fields-properties.png#lightbox)

### Update record

This action updates one or more records that meet the specified conditions.

1. Enter the schema and table name to update.
2. Select **Update type**.

   - **Single Update**: Updates only the first record that matches the specified condition.
   - **Multiple Updates**: Updates all records that match the condition.
3. Configure the conditions for update.
4. Select **Add Fields** to add the fields that you want to update.

   [![Screenshot of automation editor showing Update Configuration, Single Update type, Conditions rules, and highlighted Add Fields button.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/automation-update-record-add-fields.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/automation-update-record-add-fields.png#lightbox)
5. Replace the existing values with static values or dynamically calculated values by using formulas, or clear the existing values.

   ![Screenshot of update field dropdown listing Replace Value, Clear Value, and arithmetic options in the Update Configuration pane.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/update-record-value-options.png)

### Delete record

This action deletes one or more records from the specified table that meet the configured conditions.

1. Enter the schema and the table name.
2. Configure the rules to pick the records to delete.

### Find records

Use **Find Record(s)** to retrieve one or more records from the specified table that meet the configured conditions.

1. After entering the schema and table name, select the **Fetch type**.

   - Select **Single Record** to retrieve a single record.
   - Select **Multiple Records** to retrieve multiple records in a single action. You can retrieve up to 1,000 records. Configure the **Retrieve Limit** to specify the maximum number of records to return.
2. Select the fields to retrieve.
3. Optionally, sort the retrieved records in ascending or descending order. The action returns the records in the specified order.
4. Configure the conditions used to find the records.

   [![Screenshot of the Find Record(s) action Properties pane showing Fetch type, record limit, selected columns, sorting, and condition rules.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/find-records-action-properties.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/find-records-action-properties.png#lightbox)

### Bulk create records

This creates multiple records in the specified table by using the records returned by the **Find Record(s)** action.

1. Include a [**Find Record(s)**](#find-records) action in your flow before adding records in bulk.
2. Select **Add Action** and select **Bulk Create Record**.
3. Specify the schema and table name where you want to create the records.
4. For **Input List**, select the records returned by the **Find Record(s)** action.
5. Select **Add Fields** to create the required destination fields.
6. Enter the field values or map each destination field to its corresponding field value from the records returned by the **Find Record(s)** action.

   [![Screenshot of the Bulk Create Record action Properties pane with Sales table selected and Record Mapping fields.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/bulk-create-record-input-list-map.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/bulk-create-record-input-list-map.png#lightbox)

Note

An automation flow can include multiple **Find Record(s)** actions. If you include multiple **Find Record(s)** actions, select the action that returns the records you want to use as the input list.

### Execute stored procedure

Use this action to run a stored procedure that you created in the database.

1. Enter the schema and the table name.
2. Configure the rules.
3. Select the stored procedure that you want to run.

### Clear semantic data cache

Use the **Clear semantic data cache** action to clear cached semantic data so that subsequent queries from the planning sheet retrieve the latest available values.

For example, a semantic model uses a database table as its source, and you update that table through a PowerTable sheet. If the semantic model is used in a planning sheet, clearing the semantic data cache can help the planning sheet retrieve updated values without requiring a manual refresh.

To automate cache clearing, add the **Clear semantic data cache** action to an automation workflow and configure a suitable trigger, such as **Record created**, **Record updated**, **Record deleted**, or **Form submitted**. When the trigger occurs, the action clears the cached semantic data, allowing subsequent queries from the planning sheet to retrieve the latest available values.

[![Screenshot of the automation editor with the Add Action menu open and the Clear Semantic Data Cache action highlighted under Miscellaneous.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/clear-semantic-data-cache.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/clear-semantic-data-cache.png#lightbox)

### Conditional Group

**Conditional Group** defines **If/Otherwise** branching logic. It evaluates one or more conditions and runs the corresponding actions based on the conditions that are met.

1. Select **Add Action**, and then select **Conditional Group**.
2. In the **Properties** pane, add one or more conditions for the **If** branch.

   [![Screenshot of the Properties pane Conditions section with a Rules row set to Quantity, less than, and 100.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/automation-if-condition.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/automation-if-condition.png#lightbox)
3. Select **Add Action** within the **If** branch to add an action to run when the conditions are met. Hover over to select **+** and add more actions if necessary.

   [![Screenshot of the automation flow with a Create Record action in the If branch highlighted and a plus button to add more actions.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/automation-if-branch-create-record-action.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/automation-if-branch-create-record-action.png#lightbox)
4. Select **Add Condition** to add an **Otherwise If** branch, and then configure its conditions.

   [![Screenshot of an automation with an Otherwise If branch added and the empty Rules row highlighted in the Properties pane.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/otherwise-if-branch.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/otherwise-if-branch.png#lightbox)
5. Select **Add Action** within the **Otherwise** **If** branch to add one or more actions when the conditions are met.
6. Repeat these steps to add additional **Otherwise If** branches and their corresponding actions.
7. To add a final **Otherwise** branch, select **If no other conditions are met** in the **Properties** pane. The actions in this branch run only when none of the preceding conditions are met.

   [![Screenshot of an automation with an Otherwise branch highlighted and the If no other conditions are met option selected in the Properties pane.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/otherwise-branch.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/otherwise-branch.png#lightbox)

### Repeating group

**Repeating group** repeats the same set of actions for each record that a **Find Record(s)** action returns.

1. Before adding a repeating group, include a [**Find Record(s)**](#find-records) action in your flow.
2. Select **Add Action**, and then select **Repeating Group**.
3. Enter an optional description.
4. For **Input List**, select the records that the **Find Record(s)** action returns.

   Note

   An automation flow can include multiple **Find Record(s)** actions. If you include multiple **Find Record(s)** actions, select the action that returns the records you want to use as the input list.
5. If an iteration fails, select **Continue** to continue processing the remaining records or select **Fail** to stop the workflow.

   [![Screenshot of the Repeating Group Properties panel with Input List set to Find Record(s) and Continue selected for failed iterations.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/repeating-group.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/repeating-group.png#lightbox)
6. Within the **Repeat for each** block, select **Add Action**, and then select an action that runs for each record in the input list. Use **+** to include more actions.

## Duplicate, delete, or rearrange actions

- Use the **More options** (**...**) menu on an action to duplicate or delete it.
- Use the **drag handle** (six-dot icon) to drag and drop the action and reorder the workflow.
- To insert an action between existing actions, select the **+** icon at the required location in the workflow.

  ![Screenshot of a workflow action with the highlighted More options button and a menu offering Duplicate Action and Delete Action.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/action-options-duplicate-delete-menu.png)

## Save the workflow

After you complete all configurations, the **Save** option is enabled. Select **Save** to save the workflow. Select **Back to Setup** to return to the previous page.

[![Screenshot of the Automations workflow editor with the Save button highlighted in the top-right corner.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/save-workflow.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/save-workflow.png#lightbox)

## Related content

- [Integrations in automation](how-to-configure-integrations).
- [Manage Automation](how-to-manage-automation).
- [Create a sample automation](how-to-create-sample-automation).

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
