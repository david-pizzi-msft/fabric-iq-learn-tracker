---
title: "Insert button columns in PowerTable"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-columns/how-to-insert-button-columns](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-insert-columns/how-to-insert-button-columns) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert button columns in PowerTable

Summarize this article for me

A button column is an interactive [visual column](how-to-insert-visual-columns) that you can add to your table and configure to open a URL or run an automation.

This article explains how to add a button column to your table.

## Insert the button column

1. Go to **PowerTable** > **Insert Column** > **Add Visual Column** > **Add Button Column**.

   ![Screenshot of PowerTable Insert Column menu with Visual Column and Add Button Column options highlighted.](../media/powertable-how-to-insert-columns/how-to-insert-button-columns/insert-button-column.png)
2. Configure the column details:

   - **Column Name:** Enter a name for the column.
   - **Label:** The default button label is *Click Here*. You can change the label if you want.
   - **Action:** Select the action to perform when you select the button. You can either open a URL or run an automation workflow.

   ![Screenshot of Button Column configuration displaying Label, Action dropdown, and URL fields.](../media/powertable-how-to-insert-columns/how-to-insert-button-columns/add-action.png)

## Add URL

1. To open a URL when users select the button, select **Open Url** in **Action**.
2. Select **Static** to enter a static URL, or **Formula** to enter a formula that generates a dynamic URL based on data.

   In the following image, a formula specifies a dynamic URL that changes depending on the product name. When you select a button, PowerTable opens the URL associated with the selected product.

   [![Screenshot of Button Column configuration showing Open Url action and dynamic URL formula field.](../media/powertable-how-to-insert-columns/how-to-insert-button-columns/add-url.png)](../media/powertable-how-to-insert-columns/how-to-insert-button-columns/add-url.png#lightbox)
3. Select **Save**. PowerTable adds the button column as shown in the following image:

   [![Screenshot of PowerTable sheet with a new Product Details column containing Know more buttons in each row that opens URL dynamically based on the product name.](../media/powertable-how-to-insert-columns/how-to-insert-button-columns/button-column-inserted.png)](../media/powertable-how-to-insert-columns/how-to-insert-button-columns/button-column-inserted.png#lightbox)

## Run an automation workflow

1. To trigger an automation workflow when you select the button, select **Execute an Automation** under **Action**.
2. Select an existing automation workflow from the list. If the required workflow doesn't exist, select **Create Automation** to open the automation window and create a new workflow.

   ![Screenshot of Add Button Column General tab with no automation available and Create Automation button highlighted.](../media/powertable-how-to-insert-columns/how-to-insert-button-columns/create-new-automation-for-button.png)
3. After selecting or creating the automation workflow, select **Save**.

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
