---
title: "OPEN SHEET"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/open-sheet](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/open-sheet) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# OPEN SHEET

Summarize this article for me

Use the OPEN\_SHEET function to open planning sheet when a user runs a script. For example, add a button that lets users navigate from one planning sheet to another.

## Syntax

The following syntax opens a planning sheet.

```
OPEN_SHEET(sheets.sheetLabel1)
```

Replace sheetLabel1 with the reference to the sheet you want to open.

## Example

The following example opens the planning sheet named Planning 2.

```
OPEN_SHEET(sheets."Planning 2@3")
```

## Configure a button to open a planning sheet

1. Open the planning item and create or edit an action parameter.
2. Set **Type** to **Action**.
3. Enter a name, such as Open Planning Sheet.
4. In **Description**, explain what the action does. For example, enter: Opens Planning Sheet 2 when the user selects the button.
5. Under **Interface Options**, set **Interface Type** to **Button**.
6. Select **Enable Script**.
7. Under **Button Configuration**, set **Label** to Open Planning Sheet 2.
8. Add an action, select the root scope, and enter the following formula script:

   ```
   OPEN_SHEET(sheets."Planning 2@3")
   ```
9. Save the button configuration, and then select **Update**.

   [![Screenshot of the button configuration for the OPEN_SHEET function.](../media/scripting-functions/open-sheet/open-sheet-configuration.png)](../media/scripting-functions/open-sheet/open-sheet-configuration.png#lightbox)

   When a user selects **Open Planning Sheet 2**, the planning item opens the specified planning sheet.

   [![Screenshot of the planning item after the OPEN_SHEET function opens the target planning sheet.](../media/scripting-functions/open-sheet/open-sheet-result.png)](../media/scripting-functions/open-sheet/open-sheet-result.png#lightbox)

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
