---
title: "SETLAYOUT"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/setlayout](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/setlayout) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# SETLAYOUT

Summarize this article for me

Use SETLAYOUT to apply a layout to a planning sheet. The function supports hierarchy, table, tree, default, measures-on-rows, and measures-on-columns layouts.

## Syntax

```
SETLAYOUT(LAYOUT.layoutType)
```

## Parameters

The following table lists the layout references available for the layoutType parameter.

| Parameter | Description |
| --- | --- |
| LAYOUT.HIERARCHY | Applies the Hierarchy layout. |
| LAYOUT.TABLE | Applies the Table layout. |
| LAYOUT.TREE | Applies the Tree layout. |
| LAYOUT.DEFAULT\_LAYOUT | Applies the default layout. |
| LAYOUT.MoR | Displays measures on rows. |
| LAYOUT.MoC | Displays measures on columns. |

## Examples

Use the following formulas to apply the required layout to a planning sheet.

To apply the Hierarchy layout:

```
SETLAYOUT(LAYOUT.HIERARCHY)
```

To apply the Table layout:

```
SETLAYOUT(LAYOUT.TABLE)
```

To apply the Tree layout:

```
SETLAYOUT(LAYOUT.TREE)
```

To apply the default layout:

```
SETLAYOUT(LAYOUT.DEFAULT_LAYOUT)
```

To display measures on rows:

```
SETLAYOUT(LAYOUT.MoR)
```

To display measures on columns:

```
SETLAYOUT(LAYOUT.MoC)
```

## Configure the SETLAYOUT action

The following example configures a toggle parameter that switches between displaying measures on rows and columns.

1. In the planning sheet, create an action parameter.
2. In the **Edit Parameter** pane, configure the parameter as follows:

   - **Type**: Action
   - **Name**: Set Layout
   - **Parameter Id**: SetLayout
   - **Description**: Switch between displaying measures on rows and columns in the planning sheet.
   - **Interface Type**: Toggle
3. In **Interface Options**, enable **Enable Script** and **Include in read mode**. Set **Default State** to **Measures on Rows**.
4. Configure the **On State** with the label **Measures on Rows**. Set **Apply to** to **Planning**, and enter the following formula in **Formula Script**:

   ```
   SETLAYOUT(LAYOUT.MoR)
   ```

   [![Screenshot of the On State Configuration with the Measures on Rows label and the SETLAYOUT formula for the row layout.](../media/scripting-functions/setlayout/setlayout-configuration-mor.png)](../media/scripting-functions/setlayout/setlayout-configuration-mor.png#lightbox)
5. Configure the **Off State** with the label **Measures on Columns**. Set **Apply to** to **Planning**, and enter the following formula in **Formula Script**:

   ```
   SETLAYOUT(LAYOUT.MoC)
   ```

   [![Screenshot of the Off State Configuration with the Measures on Columns label and the SETLAYOUT formula for the column layout.](../media/scripting-functions/setlayout/setlayout-configuration-moc.png)](../media/scripting-functions/setlayout/setlayout-configuration-moc.png#lightbox)
6. Save the action parameter and update the planning sheet.

## Results

When the toggle is set to **Measures on Rows**, the planning sheet displays each measure as a row within the row hierarchy.

[![Screenshot of a planning sheet displaying the Actuals measure on rows within the row hierarchy.](../media/scripting-functions/setlayout/setlayout-result-mor.png)](../media/scripting-functions/setlayout/setlayout-result-mor.png#lightbox)

When the toggle is set to **Measures on Columns**, the planning sheet displays measure values across columns.

[![Screenshot of a planning sheet displaying Actuals values in columns.](../media/scripting-functions/setlayout/setlayout-result-moc.png)](../media/scripting-functions/setlayout/setlayout-result-moc.png#lightbox)

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
