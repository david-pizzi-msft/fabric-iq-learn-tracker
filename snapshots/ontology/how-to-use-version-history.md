---
title: "Manage version history in ontology (preview)"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-version-history](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-version-history) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Manage version history in ontology (preview)

Summarize this article for me

With version history in ontology (preview), you capture named snapshots, called versions, of an ontology's definition, including its entity types and relationship types. Use version history to track who changed what and when, and to roll back to an earlier state. The version history pane lists every version with its date, time, and the user who created it, grouped by day.

Important

This feature is in [preview](../../fundamentals/preview).

## Prerequisites

Before you manage version history, make sure you have the following prerequisites:

- A [Fabric workspace](../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../enterprise/licenses#capacity).
- **Ontology item (preview)** enabled on your tenant.
- An ontology (preview) item that contains [entity types](how-to-create-entity-types) and [relationship types](how-to-create-relationship-types).
- **Read/Write** access to the ontology item. If you have read-only access, you can view versions but can't create, edit, restore, or delete them.

## Open the version history pane

To open the version history pane, follow these steps.

1. Open the ontology item and select **History** in the top-right corner.

   [![Screenshot of the History button in the ontology ribbon.](media/how-to-use-version-history/version-history-button.png)](media/how-to-use-version-history/version-history-button.png#lightbox)
2. The pane opens and loads the list of all versions. Each version shows the version name, date and time, and the user who created it.

   [![Screenshot of the Version history pane listing versions with date, time, and user.](media/how-to-use-version-history/version-history-pane.png)](media/how-to-use-version-history/version-history-pane.png#lightbox)

## Create a version

To capture the current state of the ontology as a version, follow these steps:

1. In the version history pane, select **+ New Version**. An inline **Create a version** box appears with a required version name and an optional description.

   [![Screenshot of the Create a version form with Version name and Description fields.](media/how-to-use-version-history/create-version.png)](media/how-to-use-version-history/create-version.png#lightbox)
2. Enter a **Version name**. The name is required.
3. Enter a **Description**. The description is optional.
4. Save the version. The version appears in the list.

## Browse and filter versions

In the version history pane, use the following options to find a specific version:

- Versions appear under a date header that shows the count in parentheses, for example `02/07/26 (6)`. Use the arrow next to a date header to expand or collapse that day's versions.
- Select the filter button next to **New Version** to filter versions by **Time**, **Last 7 Days**, or **Last 30 Days**, and by the user who created them.
- Select the version card to see its description.

## Edit, restore, or delete a version

Each version has an **Edit** (pencil) icon and a **More options** (three dots) menu with the following actions.

[![Screenshot of a version entry with edit, restore, and delete options.](media/how-to-use-version-history/version-entry-options.png)](media/how-to-use-version-history/version-entry-options.png#lightbox)

1. **Edit**: Change the version's name or description.
2. **Restore**: Replace the current ontology definition with the selected version. In the **Restore version** dialog, select the option to create a version of your current work first if you want to keep it. Restoring a version returns the entire ontology item definition that existed in that version, including its entity types and relationship types.
3. **Delete**: Permanently remove the version. You can't undo this action.

Note

Only users with **Read/Write** access can perform actions on versions. When you share an item with another user, they get read-only access by default (write actions are blocked).

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
