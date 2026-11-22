---
title: "Bulk edit data"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-bulk-edit](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-bulk-edit) · Last updated on **2026-05-14**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Bulk edit data

Summarize this article for me

Use *bulk edit* to update multiple values in a planning sheet at the same time. Apply the same value across categories, dimensions, hierarchy levels, or data input types.

Use bulk edit operations to:

- Allocate costs or revenue across multiple fields.
- Distribute forecast or budget values across categories.
- Assign the same expiry date to multiple products.
- Assign the same manager to multiple locations.

## Open bulk edit

1. Go to the **Planning** tab.
2. In the **Tools** section, select **Bulk Edit**.

## Select a measure

In **Measure**, select the data input measure to update.

[![Screenshot of selecting a measure in Bulk Edit.](media/planning-how-to-bulk-edit/bulk-edit-select-measure.png)](media/planning-how-to-bulk-edit/bulk-edit-select-measure.png#lightbox)

## Select categories and dimensions

1. In **Select Filter**, choose the categories and dimensions to update.
2. Select multiple values for each dimension as required.
3. Add filters for another dimensions.

The planning sheet updates dynamically based on the selected filters.

[![Screenshot of filters used to select categories and dimensions in Bulk Edit.](media/planning-how-to-bulk-edit/bulk-edit-select-filter.png)](media/planning-how-to-bulk-edit/bulk-edit-select-filter.png#lightbox)

## Select a row hierarchy level

In **Apply to Row Level**, select the hierarchy level to update.

[![Screenshot of the Apply to Row Level option in Bulk Edit.](media/planning-how-to-bulk-edit/bulk-edit-select-apply-to-row-level.png)](media/planning-how-to-bulk-edit/bulk-edit-select-apply-to-row-level.png#lightbox)

## Select a column hierarchy level

1. In **Apply to Column Level**, select the column hierarchy level to update.
2. If the planning sheet doesn't contain a column hierarchy, apply updates at the grand total or quarter level.

[![Screenshot of the Apply to Column Level option in Bulk Edit.](media/planning-how-to-bulk-edit/bulk-edit-select-apply-to-column-level.png)](media/planning-how-to-bulk-edit/bulk-edit-select-apply-to-column-level.png#lightbox)

## Configure the update type

1. In **Type**, select the update type.
2. Enter the value to apply.

Supported update types include:

- **Append By**: Adds the entered value to the existing value.
- **Set Value**: Replaces the existing value.
- **Reset Value**: Removes the existing value.

[![Screenshot of update type options in Bulk Edit.](media/planning-how-to-bulk-edit/bulk-edit-select-type.png)](media/planning-how-to-bulk-edit/bulk-edit-select-type.png#lightbox)

## Distribute values

1. Select a **Distribution** method for child rows. Distribute updated values equally or based on another measure's weights.

   [![Screenshot of distribution options for child rows in Bulk Edit.](media/planning-how-to-bulk-edit/bulk-edit-select-distribution.png)](media/planning-how-to-bulk-edit/bulk-edit-select-distribution.png#lightbox)
2. Child rows inherit values based on the selected distribution method.

   [![Screenshot of updated cells highlighted in a planning sheet.](media/planning-how-to-bulk-edit/bulk-edit-result.png)](media/planning-how-to-bulk-edit/bulk-edit-result.png#lightbox)

## Supported data input types

Bulk edit supports multiple data input types, including:

- Text
- Date
- Person
- Single-select dropdown
- Multi-select dropdown

Apply values across selected categories, subcategories, and dimensions.

### Bulk edit text inputs

Use **Bulk Edit** to apply text values across selected categories and subcategories.

[![Screenshot of applying text values with Bulk Edit.](media/planning-how-to-bulk-edit/bulk-edit-text-inputs.png)](media/planning-how-to-bulk-edit/bulk-edit-text-inputs.png#lightbox)

The text column is updated with the selected value.

[![Screenshot of text values updated across selected rows.](media/planning-how-to-bulk-edit/bulk-edit-text-inputs-result.png)](media/planning-how-to-bulk-edit/bulk-edit-text-inputs-result.png#lightbox)

### Bulk edit date inputs

Use **Bulk Edit** to apply date values across selected categories and subcategories.

[![Screenshot of applying date values with Bulk Edit.](media/planning-how-to-bulk-edit/bulk-edit-date.png)](media/planning-how-to-bulk-edit/bulk-edit-date.png#lightbox)

The date column is updated with the selected date.

[![Screenshot of updated date values across selected rows.](media/planning-how-to-bulk-edit/bulk-edit-date-result.png)](media/planning-how-to-bulk-edit/bulk-edit-date-result.png#lightbox)

### Add duration to existing dates

Use **Bulk Edit** to add a duration to existing date values.

Supported duration types:

- Years
- Quarters
- Months
- Weeks
- Days

[![Screenshot of the Add Duration option for date values in Bulk Edit.](media/planning-how-to-bulk-edit/bulk-edit-add-duration.png)](media/planning-how-to-bulk-edit/bulk-edit-add-duration.png#lightbox)

Date values are recalculated based on the selected duration.

[![Screenshot of date values updated after applying a duration.](media/planning-how-to-bulk-edit/bulk-edit-add-duration-result.png)](media/planning-how-to-bulk-edit/bulk-edit-add-duration-result.png#lightbox)

### Bulk edit person inputs

Use **Bulk Edit** to assign person values across selected categories and subcategories.

[![Screenshot of assigning person values with Bulk Edit.](media/planning-how-to-bulk-edit/bulk-edit-person.png)](media/planning-how-to-bulk-edit/bulk-edit-person.png#lightbox)

The person column is updated with the selected user value.

[![Screenshot of assigned person values across selected rows.](media/planning-how-to-bulk-edit/bulk-edit-person-result.png)](media/planning-how-to-bulk-edit/bulk-edit-person-result.png#lightbox)

### Bulk edit single-select dropdown inputs

Use **Bulk Edit** to apply a single dropdown value across selected categories and subcategories.

[![Screenshot of applying a single-select dropdown value with Bulk Edit.](media/planning-how-to-bulk-edit/bulk-edit-single-select.png)](media/planning-how-to-bulk-edit/bulk-edit-single-select.png#lightbox)

The single-select column is updated with the selected dropdown value.

[![Screenshot of updated single-select values across selected rows.](media/planning-how-to-bulk-edit/bulk-edit-single-select-result.png)](media/planning-how-to-bulk-edit/bulk-edit-single-select-result.png#lightbox)

### Bulk edit multi-select dropdown inputs

Use **Bulk Edit** to apply multiple dropdown values across selected categories and subcategories.

[![Screenshot of applying multi-select dropdown values with Bulk Edit.](media/planning-how-to-bulk-edit/bulk-edit-multi-select.png)](media/planning-how-to-bulk-edit/bulk-edit-multi-select.png#lightbox)

The multi-select column is updated with the selected dropdown values.

[![Screenshot of updated multi-select values across selected rows.](media/planning-how-to-bulk-edit/bulk-edit-multi-select-result.png)](media/planning-how-to-bulk-edit/bulk-edit-multi-select-result.png#lightbox)

## Usage notes

When editing data in bulk:

- Numerical data inputs support append and distribution operations.
- Date input types support duration-based updates and date selection.
- Apply changes to specific column hierarchy levels, such as region or date hierarchies.

Bulk editing is supported for simulation measures and scenarios. Apply simulations to selected categories and dimensions in a single operation.

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
