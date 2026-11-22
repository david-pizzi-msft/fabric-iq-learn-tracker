---
title: "Create text parameters"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/parameters/how-to-create-text-parameters](https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/parameters/how-to-create-text-parameters) · Last updated on **2026-11-10**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create text parameters

Summarize this article for me

Use text parameters to inject dynamic text content directly into your reports. By binding text parameters to header or footer text boxes, you can easily modify report titles, add localized notes, or update print disclosures on the fly before generating final PDF or printed copies.

## Embed custom text in headers and footers

To enable dynamic header and footer updates, configure text parameters and embed them in the header component of your planning or intelligence sheets.

- [Use text parameters in planning sheets](#tabpanel_1_planning-sheets)
- [Use text parameters in intelligence sheets](#tabpanel_1_intelligence-sheets)

1. Create a new parameter and set the **Type** to **Text**. Enter the **Name**, **Description**, and **Parameter Id** for the parameter.

   [![Screenshot of configuring text parameter options for a planning sheet.](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/configure-text-parameter-planning-sheet.png)](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/configure-text-parameter-planning-sheet.png#lightbox)
2. Double-click the header of your planning sheet to edit it.
3. In the **Header & Footer** ribbon of your planning sheet, select **Parameters** and select the text parameter created in the first step. Close the header editor after inserting the parameter.

   [![Screenshot of inserting a text parameter into the planning sheet header from the Header & Footer ribbon.](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/insert-parameter-header.png)](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/insert-parameter-header.png#lightbox)
4. The header automatically updates to display the value entered in the parameter input box.

   [![Screenshot of a planning sheet header displaying the value entered in the text parameter input box.](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/text-entered-parameter-displayed-header.png)](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/text-entered-parameter-displayed-header.png#lightbox)

1. Create a new parameter and set the **Type** to **Text**. Enter the **Name**, **Description**, and **Parameter Id** for the parameter.

   [![Screenshot of creating a text parameter to capture the filter category.](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/text-parameter-configuration.png)](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/text-parameter-configuration.png#lightbox)
2. Create a second text parameter. The parameters display the filters applied.

   [![Screenshot of text parameters created to capture the category and time period.](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/create-second-text-parameter.png)](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/create-second-text-parameter.png#lightbox)
3. Select the chart visual and double-click the header area to open the text editor. Type `#` to view and select your parameter from the dropdown menu.

   [![Screenshot of selecting a parameter for the chart header.](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/insert-header-parameter.png)](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/insert-header-parameter.png#lightbox)
4. Repeat step 3 for other visuals in your dashboard as required.

   Note

   For matrix visuals, follow the same steps used to insert parameters in planning sheet headers.

   [![Screenshot of using the category parameter in the header of the treemap chart.](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/treemap-header-category-parameter.png)](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/treemap-header-category-parameter.png#lightbox)
5. As you enter values into the parameter inputs, the visual headers update dynamically. In this example, the headers provide clear context for the applied filters. The bar chart header updates to reflect the selected quarter. The treemap and matrix headers update to reflect the selected category.

   [![Animation showing visual headers updating dynamically: the bar chart shows the selected quarter, and the treemap and matrix show the category.](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/text-parameter-header-change.gif)](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/text-parameter-header-change.gif#lightbox)

## Use text parameters in formulas

Reference text parameters in custom formulas to drive logic based on text inputs and update calculated values on the fly.

1. Create a new parameter and set the **Type** to **Text**. Enter a relevant parameter ID; you reference this ID in the formula. Specify an optional default value.
2. In the **Planning** ribbon of your planning sheet, go to **Insert Column** > **Formula** to insert a new calculated measure.
3. Enter the formula. Press Ctrl + Spacebar to use IntelliSense to add references to the parameters in the formula.

   [![Screenshot of referencing the currency code parameter inside a formula.](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/text-parameter-formula-reference.png)](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/text-parameter-formula-reference.png#lightbox)
4. When you change the parameter, Fabric recalculates the values in real time - without making any changes to the underlying formula.

   [![Animation showing how the Normalized sales measure is recalculated when the currency code parameter is changed.](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/text-parameter-recalculation-animation.gif)](../../../media/resources/best-practices/parameters/how-to-create-text-parameters/text-parameter-recalculation-animation.gif#lightbox)

## Related content

- [Configure parameters](how-to-configure-parameters).
- [Create numeric input parameters](how-to-create-number-parameters).

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
