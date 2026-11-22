---
title: "PowerTable general FAQ"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/resources/powertable-general-faq](https://learn.microsoft.com/en-us/fabric/iq/plan/resources/powertable-general-faq) · Last updated on **2026-08-31**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# PowerTable general FAQ

Summarize this article for me

This FAQ addresses common questions and clarifications that arise while setting up PowerTable. It covers questions about creating plan items, workspace permissions, and SQL database setup.

- Feature-specific FAQs are covered in the relevant how-to sections.
- To see questions about creating and configuring PowerTable sheets, see [PowerTable Sheets Creation FAQ](powertable-sheets-creation-faq).

## What permissions do I need in the workspace to create the Fabric SQL database and the plan item?

You need at least the **Contributor** role in the Fabric workspace to create a plan item in Fabric and a Fabric SQL database.

## Why do I create a Fabric SQL database before creating the PowerTable sheet?

Unlike planning and intelligence sheets, PowerTable sheets connect directly to a Fabric SQL database instead of a semantic model. PowerTable reads data from and writes data back to the Fabric SQL database.

If you start with a CSV or Excel file, you must first import the data into a Fabric SQL database before you can use it in PowerTable. For this reason, you create the Fabric SQL database first.

## Why do I see two items with the same name in the workspace after creating the Fabric SQL database?

Creating a Fabric SQL database also creates a companion SQL analytics endpoint with the same name. This behavior is expected.

PowerTable connects *directly* to the Fabric SQL database, so you don't need to configure or use the SQL analytics endpoint when working with PowerTable.

## Do the names I choose for the Fabric SQL database and the plan item matter?

- The **Fabric SQL database** name matters because you select it in the **Select Fabric SQL Connection** dialog each time you create a PowerTable sheet.
- The **plan** item name is used only as a label. However, use a consistent name so that you can easily locate the item later and also work on it further, if needed.

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
