---
title: "Build a sample automation"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-create-automation/how-to-create-sample-automation](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-create-automation/how-to-create-sample-automation) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Build a sample automation

Summarize this article for me

This article extends the [Configure automation workflows](how-to-configure-automation-workflows) how-to guide by showing how to create an automation workflow by using a sample customer order processing scenario.

Note

To learn more about the concept of automation and how to set up the different triggers and actions, see [Automation](../powertable-concept-automation) and [Configure automation workflows](how-to-configure-automation-workflows).

## Sample scenario

For this example, consider the following tables in PowerTable:

1. An **Order Requests** table to store customer order requests submitted through a form.

   [![Screenshot of PowerTable showing the Order Requests table with two rows of customer name, product, quantity, and stock data.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/powertable-order-requests-table.png)](../media/powertable-how-to-create-automation/how-to-create-sample-automation/powertable-order-requests-table.png#lightbox)
2. An **Orders** table to store processed orders.

   [![Screenshot of PowerTable showing the Orders table with 10 rows of order date, order number, customer, product key, quantity, status, stock, and product name.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/powertable-order-table.png)](../media/powertable-how-to-create-automation/how-to-create-sample-automation/powertable-order-table.png#lightbox)
3. An **Inventory** table that contains product information and available stock quantities.

   [![Screenshot of PowerTable showing the Inventory table with 10 rows of ProductKey, Stock, Warehouse, LastUpdated, Restock, and Product Name columns.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/powertable-inventory-table.png)](../media/powertable-how-to-create-automation/how-to-create-sample-automation/powertable-inventory-table.png#lightbox)
4. A [form](../powertable-how-to-generate-forms) that stores customer order requests in the **Order Requests** table.

   ![Screenshot of Form collecting customer name, phone, product name, and quantity for order requests.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/order-request-form.png)

## Workflow overview

When a customer submits an order request through the form, the workflow verifies inventory for the requested product and then performs the appropriate actions based on stock availability.

The workflow retrieves the product details from the **Inventory** table, checks whether sufficient stock is available, and either creates an order and updates inventory or marks the product for restocking.

The workflow performs the following tasks:

1. A customer submits an order request through the form.
2. The **When a form is submitted** trigger starts the workflow.
3. The **Find Record(s)** action retrieves the requested product details from the **Inventory** table.
4. The workflow compares the requested quantity with the available stock quantity.
5. If sufficient stock is available, the workflow:
   - Creates an order record in the **Orders** table.
   - Sets the order status to **Processing**.
   - Updates the inventory by subtracting the requested quantity from the available stock.
6. Otherwise, the workflow updates the **Restock** status in the **Inventory** table to indicate that additional stock is required.

## Create the workflow and add trigger

1. Open the **Order Requests** table.
2. Create a new automation workflow by using **Setup** > **Automations**.
3. Select **When a form is submitted** as the trigger.
4. In the **Properties** pane, [configure the trigger](how-to-configure-automation-workflows#add-trigger) to run only when the required customer details are present. The trigger starts only when the *Customer Phone*, *Product Name*, and *Quantity* **aren't empty**.

   [![Screenshot of the Automations Properties pane with trigger conditions requiring Customer Phone, Product Name, and Quantity to be not empty.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/configure-trigger-sample.png)](../media/powertable-how-to-create-automation/how-to-create-sample-automation/configure-trigger-sample.png#lightbox)

## Retrieve the product details

1. Select **Add Action** > **Find Record(s)**.
2. Select the schema. In **Table**, select **Inventory**.
3. Select **Single Record** to fetch the single matching product record.
4. [Configure the action](how-to-configure-automation-workflows#find-records) to find the product that matches the product requested in the submitted form. Use *ProductName* to find the matching product since the form has only the product name.
5. Return the **Product Key**, **Product Name**, and **Stock Quantity** fields by selecting them in **Select columns**.

   [![Screenshot of the Find Record(s) action Properties pane with Inventory table, Single Record fetch type, selected columns, and a Product Name rule.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/configure-find-records-action-inventory.png)](../media/powertable-how-to-create-automation/how-to-create-sample-automation/configure-find-records-action-inventory.png#lightbox)

The workflow uses the retrieved product details to validate stock inventory and populate the order record.

## Add a condition

1. Add a **Conditional Group**.
2. Configure the **If** condition to check if the requested quantity is less than the available stock quantity.

   [![Screenshot of Properties pane Conditions section with Rules field set to Quantity < Stock next to the workflow trigger and actions.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/configure-condition-quantity-less-than-stock.png)](../media/powertable-how-to-create-automation/how-to-create-sample-automation/configure-condition-quantity-less-than-stock.png#lightbox)

## Configure the If branch

If sufficient stock is available, create a record in the **orders** table.

1. Add a [**Create Record**](how-to-configure-automation-workflows#create-record) action.
2. Select the schema and select the orders table (*Orders1*) under **Table**.
3. Select **Add Field** to add the fields for the record.
4. For field values, select **+** and map the customer details from the **Order Requests** table, sourced from the form.
5. For product-related fields, map the product details from the **Find Record(s)** action. For example, retrieve the *Product Key* from **Inventory** table fetched by using **Find Record(s)**.
6. Set the **Status** field to *Processing*.

   [![Screenshot of Properties pane for Create Record in Orders1, mapping ProductKey, Quantity, Status, and CustomerName fields.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/create-record-orders-field-mapped.png)](../media/powertable-how-to-create-automation/how-to-create-sample-automation/create-record-orders-field-mapped.png#lightbox)

Next, update the stock in inventory:

1. Add an [**Update Record**](how-to-configure-automation-workflows#update-record) action.
2. Select the schema and select **Inventory** table.
3. Select **Single Update** to update a single record.
4. Use the *ProductKey* in **Rules** to identify the corresponding product.
5. **Select** **Replace Value** and **Subtract**. Then, select the *Stock* and *Quantity* fields to update the inventory record by subtracting the requested quantity from the available stock.

   [![Screenshot of Properties pane for Update Record in Inventory, subtracting Quantity from Stock using a ProductKey rule.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/update-record-inventory-stock-subtract.png)](../media/powertable-how-to-create-automation/how-to-create-sample-automation/update-record-inventory-stock-subtract.png#lightbox)

## Add Otherwise branch

1. Select **Add Condition** to add another condition branch.
2. In the **Properties** pane, select **If no other condition are met** to make it the final branch.

   [![Screenshot of Properties pane Configuration Details with If no other conditions are met selected for the new condition branch.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/otherwise-branch-no-other-conditions-met.png)](../media/powertable-how-to-create-automation/how-to-create-sample-automation/otherwise-branch-no-other-conditions-met.png#lightbox)

## Configure the Otherwise branch

If sufficient stock isn't available, update the restock field in the **Inventory** table to *Yes*.

1. Add an **Update Record** action.
2. Select the schema and select **Inventory** table.
3. Select **Single Update** to update a single record.
4. Use the *ProductKey* in **Rules** to identify the corresponding product.
5. Update the corresponding inventory record.
6. Set the **Restock** field to **Yes** and update the last updated date.

   [![Screenshot of the Update Record action Properties panel with Single Update selected, ProductKey rule, and Restock set to Yes.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/update-record-inventory-restock-yes.png)](../media/powertable-how-to-create-automation/how-to-create-sample-automation/update-record-inventory-restock-yes.png#lightbox)

The flow is complete.

![Screenshot of the Get Order automation flow with form trigger, Find Records, and an If Quantity < Stock condition with Create Record and Update Record actions.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/get-order-automation-complete-flow-overview.png)

Consider a user submits the form as shown in the following image.

![Screenshot of a submitted form showing Quinn Anderson, phone number, Water Bottle, and quantity 20, with Submit highlighted.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/order-form-submission-filled-customer-details.png)

The orders table is updated. The stock inventory is also updated from 60 to 40 as seen in the *Stock* reference column.

[![Screenshot of the orders table with a highlighted new row for Quinn Anderson, Water Bottle, quantity 20, Processing status, and Stock 40.](../media/powertable-how-to-create-automation/how-to-create-sample-automation/orders-table-new-row.png)](../media/powertable-how-to-create-automation/how-to-create-sample-automation/orders-table-new-row.png#lightbox)

If the requested quantity is more than the stock, the *Restock* field is updated in the **Inventory** table.

This example is a sample workflow that demonstrates a simple use case. Use more actions and their combinations for your workflows as needed.

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
