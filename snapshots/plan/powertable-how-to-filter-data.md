---
title: "Filter data in PowerTable"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-filter-data](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-filter-data) · Last updated on **2026-07-19**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Filter data in PowerTable

Summarize this article for me

Use filters to focus on specific records and analyze only the data that meets your criteria. PowerTable provides basic filters, advanced filters, and Top N filtering options to help you quickly narrow down large datasets.

## Apply basic filters

Use basic filters to directly select the values or categories you want to filter.

1. In the PowerTable sheet, select the **Filter** icon to open the **Super Filter** pane.

   [![Screenshot of the filter icon and Super Filter pane.](media/powertable-how-to-filter-data/filter-icon.png)](media/powertable-how-to-filter-data/filter-icon.png#lightbox)
2. Select a column.
3. Select one or more values to filter the records. The table automatically filters based on the selected values.

   [![Screenshot of selecting the filter values from the dropdown.](media/powertable-how-to-filter-data/select-values.png)](media/powertable-how-to-filter-data/select-values.png#lightbox)

### Search within filter values

Use the search box in the filter pane to locate specific filter values when a column contains many options.

[![Screenshot of the search box in the filter pane.](media/powertable-how-to-filter-data/search.png)](media/powertable-how-to-filter-data/search.png#lightbox)

## Apply advanced filters

Use the advanced filtering option to filter records based on specific criteria.

To apply an advanced filter:

1. Select the **Advanced** tab in the filter pane.
2. Choose the condition you want from the dropdown list, based on the column's data type.

   [![Screenshot of the Advanced tab in the filter pane.](media/powertable-how-to-filter-data/advanced.png)](media/powertable-how-to-filter-data/search.png#lightbox)
3. Enter the filter criteria and apply the filter.

   [![Screenshot of configuring an advanced filter in the filter pane.](media/powertable-how-to-filter-data/filter-criteria.png)](media/powertable-how-to-filter-data/filter-criteria.png#lightbox)

### Number filters

The following number filter conditions are available:

- Equals
- Does not equal
- Greater than
- Greater than or equal to
- Less than
- Less than or equal to
- Between
- Blank

In the following example, a filter on the *ProductPrice* column displays values between 1,000 and 3,000. A filter icon in the column header indicates an applied filter.

[![Screenshot of the filter applied in a numeric column.](media/powertable-how-to-filter-data/number-filter.png)](media/powertable-how-to-filter-data/number-filter.png#lightbox)

You can also use the slider or value range controls to filter numeric data.

[![Screenshot of the slider while configuring advanced filter.](media/powertable-how-to-filter-data/slider.png)](media/powertable-how-to-filter-data/slider.png#lightbox)

### Text filters

The following text filter conditions are available:

- Contains
- Does not contain
- Starts with
- Does not start with
- Isblank
- Is not blank

In the following example, a filter displays only products whose *ProductName* contains *frame*.

[![Screenshot of the filter applied to a text column.](media/powertable-how-to-filter-data/text-filter.png)](media/powertable-how-to-filter-data/text-filter.png#lightbox)

PowerTable provides suggestions while you enter filter values.

[![Screenshot of the provided suggestions when a filter value is entered.](media/powertable-how-to-filter-data/suggestion.png)](media/powertable-how-to-filter-data/suggestion.png#lightbox)

## Apply multiple filters

Apply filters to multiple columns simultaneously to further refine the displayed results.

In the following example, the filters display records where *ProductColor* is *Black* or *Blue*, and *ProductPrice* is greater than 2000.

[![Screenshot of applying multiple filters.](media/powertable-how-to-filter-data/multiple-filters.png)](media/powertable-how-to-filter-data/multiple-filters.png#lightbox)

## Apply a Top N filter

Use the **Top N** filter to display the top, bottom, or both top and bottom records based on the values in a numeric column. The **Top N** filter is available only for text columns, so you can filter text values based on a related numeric field.

To apply a Top N filter:

1. Select the **Top N** tab in the filter pane.
2. From the **Show items** dropdown, select **Top**, **Bottom**, or **Both**.
3. In the **Values** field, enter or select the number of records to display.
4. From the **Based On** dropdown, select the numeric column to rank the records.

   [![Screenshot of applying Top N filter.](media/powertable-how-to-filter-data/top-n-filter.png)](media/powertable-how-to-filter-data/top-n-filter.png#lightbox)

The following example filters the top five products based on their *ProductPrice* values.

[![Screenshot of the top 5 products based on product price.](media/powertable-how-to-filter-data/top-five-products.png)](media/powertable-how-to-filter-data/top-five-products.png#lightbox)

## Advanced filter

Use **Advanced Filter** to create complex filtering conditions by combining multiple filters and filter groups with **AND** or **OR** logic.

To apply the advanced filter:

1. Select **Advanced Filter** from the **More options** (**...**) menu in the filter pane.

   [![Screenshot of the Advanced Filter option.](media/powertable-how-to-filter-data/advanced-filter.png)](media/powertable-how-to-filter-data/advanced-filter.png#lightbox)
2. Select **Add Filter** to include one or more filter conditions.

   [![Screenshot of the Advanced Filter dialog with Add Filter button highlighted.](media/powertable-how-to-filter-data/add-filter.png)](media/powertable-how-to-filter-data/add-filter.png#lightbox)
3. Choose to combine the filter conditions by using AND or OR logic. The following image combines the filter conditions using **OR**. Select products if the product subcategory is *Socks* or if the product size is *M*.

   [![Screenshot of the Advanced Filter dialog with OR selected to combine ProductSubcategory is Socks and ProductSize is M conditions.](media/powertable-how-to-filter-data/combine-filter-conditions.png)](media/powertable-how-to-filter-data/combine-filter-conditions.png#lightbox)
4. Select **Add Group** to create a filter group.

   [![Screenshot of the Advanced Filter dialog with Add Group button highlighted.](media/powertable-how-to-filter-data/add-filter-group.png)](media/powertable-how-to-filter-data/add-filter-group.png#lightbox)
5. Use the **Add Filter** option to add one or more filter conditions within the group. Combine them using **AND** or **OR**.

   ![Screenshot of the Advanced Filter dialog with a nested group using AND logic and the Add Filter button highlighted.](media/powertable-how-to-filter-data/add-filter-inside-group.png)

   In this case, PowerTable evaluates the inner filter group first with AND, then combines it with the two outer filter conditions using OR.
6. Select **Update** to apply the filters. PowerTable displays products that meet *any* of the following conditions:

   - The product subcategory is *Socks*.
   - The product size is *M*.
   - The product is *Shorts*, the color is *Black*, and the size is *M*.

   [![Screenshot of PowerTable showing filtered products with Socks rows, size M rows, and Black Shorts of size M rows highlighted.](media/powertable-how-to-filter-data/apply-filter.png)](media/powertable-how-to-filter-data/apply-filter.png#lightbox)

The following image shows another example that combines two filter groups using OR.

![Screenshot of Advanced Filter panel with two And groups for subcategory, size, and color.](media/powertable-how-to-filter-data/example-two-groups.png)

- The first group filters products where *ProductSubcategoryKey* **is** *Socks* **AND** *ProductSize* **is** *M*.
- The second group filters products where *ProductSubcategoryKey* **is** *Shorts* **AND** *ProductColor* **is** *Black* **AND** *ProductSize* **is** *M*.
- The advanced filter combines the two groups using **OR**, so PowerTable displays records that satisfy either group.

[![Screenshot of PowerTable results with Socks rows and Black Shorts of size M highlighted.](media/powertable-how-to-filter-data/result-example.png)](media/powertable-how-to-filter-data/result-example.png#lightbox)

### Other options

- Use **Reset All** to reset all the filter and filter group configurations and add a new set of filters.
- Select **Delete Group** to delete a filter group.

  [![Screenshot of Advanced Filter dialog with Reset All and Delete Group buttons highlighted.](media/powertable-how-to-filter-data/delete-group.png)](media/powertable-how-to-filter-data/delete-group.png#lightbox)
- You can rearrange filters and filter groups by using the drag handle next to each item.

  [![Screenshot of Advanced Filter dialog with drag handles highlighted next to filters and filter groups.](media/powertable-how-to-filter-data/drag-handle.png)](media/powertable-how-to-filter-data/drag-handle.png#lightbox)

## Apply filters at the global level

By default, the **Filter** pane displays **Page level** filters, which apply only to the current PowerTable sheet. Use **Global level** filters to apply the same filter criteria across multiple PowerTable sheets that share one or more common columns.

To apply a global-level filter:

1. In the **Filter** pane, scroll to the **Global level** section and select the **+** icon.
2. Select the dimensions that you want to use for filtering across tables.
3. In **Add data fields here**, select the PowerTable sheets and the corresponding columns to map them by using common columns.
4. Apply the required filter. The filtered results appear across all configured PowerTable sheets.

For example, consider **Products** as the current table and **Subcategory** as a related table. The **ProductKey** column links both tables. If you configure **ProductSubcategoryKey**, **ProductName**, and **ModelName** as filter dimensions and map the tables by using **ProductKey**, a filter that you apply to **ModelName** in the **Products** table also applies to the **Subcategory** table.

## Clear filters

Select the clear icon next to a filter to remove it.

[![Screenshot of the clear filter icon.](media/powertable-how-to-filter-data/clear-filter.png)](media/powertable-how-to-filter-data/clear-filter.png#lightbox)

To remove all applied filters, select **Reset All** from the **More options** (**...**) menu in the Filter pane.

[![Screenshot of the Reset All option.](media/powertable-how-to-filter-data/reset-all.png)](media/powertable-how-to-filter-data/reset-all.png#lightbox)

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
