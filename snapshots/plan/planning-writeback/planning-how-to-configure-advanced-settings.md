---
title: "Configure advanced settings"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-configure-advanced-settings](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-configure-advanced-settings) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure advanced settings

Summarize this article for me

In **Writeback Settings**, the **Advanced** tab lets you configure validation rules and rename writeback columns. These settings control which data is written back and how the destination stores it.

## Validate writeback columns

In **Advanced**, enforce validation rules before writeback. Use a null check or a formula-based condition.

[![Screenshot of the writeback column validation.](../media/planning-writeback/planning-how-to-configure-advanced-settings/writeback-column-validation.png)](../media/planning-writeback/planning-how-to-configure-advanced-settings/writeback-column-validation.png#lightbox)

Validation options include:

- **Cannot be empty**: Use to write back only non-null cells for the selected field.

  [![Screenshot of the writeback column validation type cannot be empty.](../media/planning-writeback/planning-how-to-configure-advanced-settings/writeback-column-validation-types.png)](../media/planning-writeback/planning-how-to-configure-advanced-settings/writeback-column-validation-types.png#lightbox)
- **Enter formula**: Use to define a formula that must evaluate to true for cells to be written back. Cells that don't meet the validation rule are excluded during writeback.

  - Apply cross-filters during validation. During writeback, the system shows a preview of excluded cells.

  [![Screenshot of the writeback column validation type enter formula.](../media/planning-writeback/planning-how-to-configure-advanced-settings/writeback-validation-expression.jpg)](../media/planning-writeback/planning-how-to-configure-advanced-settings/writeback-validation-expression.jpg#lightbox)

### Prevent writeback when validation fails

Turn on **Prevent writeback when validation fails** to stop writeback when empty fields are detected. When validation fails, the system generates an exception notification with details about the empty measures, columns, or rows that don't meet the validation condition.

[![Screenshot of the writeback settings prevent writeback when validation fails.](../media/planning-writeback/planning-how-to-configure-advanced-settings/writeback-prevent-writeback-when-validation-fails.png)](../media/planning-writeback/planning-how-to-configure-advanced-settings/writeback-prevent-writeback-when-validation-fails.png#lightbox)

## Rename writeback columns

Specify custom column names for the writeback table.

To rename columns, go to **Writeback settings > Advanced** and select **Writeback column rename**.

[![Screenshot of the writeback setting to rename column name.](../media/planning-writeback/planning-how-to-configure-advanced-settings/writeback-column-rename.jpg)](../media/planning-writeback/planning-how-to-configure-advanced-settings/writeback-column-rename.jpg#lightbox)

Tip

Use standard database naming conventions, such as `snake_case` or `PascalCase`, to ensure compatibility with your destination database.

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
