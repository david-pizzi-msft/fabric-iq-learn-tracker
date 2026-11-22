---
title: "Configure rules using IF conditions"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-conditional-formatting/how-to-format-if](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-conditional-formatting/how-to-format-if) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure rules using IF conditions

Summarize this article for me

When creating conditional formatting rules, you can choose from three **Format by** options that determine how formatting is applied. This article explains the configuration of rules in conditional formatting using IF conditions in detail.

## Prerequisites

- You have access to a planning sheet.
- You have [created a rule in conditional formatting](how-to-create-rules).

## Enable format by rules (IF conditions)

In the **Format by** dropdown, select **Rules (If conditions)** to configure rule-based conditional formatting based on one or more logical conditions. Format cells using font styles, colors, borders, icons, or background highlights when specified conditions are met.

## Configure formatting styles

In the **Style** section, define how data should appear when conditions are met:

- **Font style**: Apply bold, italic, or underline
- **Font color**: Change text color
- **Cell background**: Highlight cells with color
- **Borders**: Add custom borders
- **Icons or text**: Display indicators or symbols
- **Hide values**: Mask sensitive data when conditions are met

You can also:

- Align icons within cells
- Display only icons or text (hide values)
- Apply formatting to charts or labels where applicable.

  ![Screenshot of formatting style.](../media/planning-conditional-formatting/how-to-format-if/formatting-style.png)

## Define rule conditions

Use the **Conditions** section to specify when formatting is applied. You can combine multiple conditions using AND/OR logic.

Each condition contains the following components:

| Setting | Description |
| --- | --- |
| Measure or field | Select the measure or column to evaluate. |
| Operator | Define the comparison logic, such as *Greater than*, *Less than*, or *Equal to*. |
| Condition type | Specify the comparison source, such as **Number**, **Data selection**, **Value**, or **Formula**. |
| Value | Enter the comparison value or select a reference. |

Supported condition types include:

- **Number**: Apply formatting based on numeric thresholds.
- **Data selection**: Reference another cell value dynamically.
- **Value**: Compare against another measure or column.
- **Formula**: Use expressions combining measures and values.
- **User selection**: Apply formatting dynamically based on runtime user interaction.

  ![Screenshot of configuring conditions.](../media/planning-conditional-formatting/how-to-format-if/configure-conditions.png)

## Nested conditions

You can configure advanced conditional formatting by selecting **Add Condition**.

- Add multiple conditions and combine them using AND/OR logic.
- Apply complex business rules across dimensions.

  [![Screenshot of configuring nested conditions.](../media/planning-conditional-formatting/how-to-format-if/nested-conditions.png)](../media/planning-conditional-formatting/how-to-format-if/nested-conditions.png#lightbox)

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
