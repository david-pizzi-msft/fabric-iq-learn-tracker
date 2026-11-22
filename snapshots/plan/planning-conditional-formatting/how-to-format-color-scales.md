---
title: "Configure rules using format by color scale"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-conditional-formatting/how-to-format-color-scales](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-conditional-formatting/how-to-format-color-scales) · Last updated on **2026-05-18**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure rules using format by color scale

Summarize this article for me

When creating conditional formatting rules, you can choose from three **Format by** options that determine how formatting is applied. This article explains the **Color scale** format option in detail.

## Prerequisites

- You have access to a planning sheet.
- You have [created a rule in conditional formatting](how-to-create-rules).

## Enable format by color scale

Color scale applies gradient-based conditional formatting to values in a planning sheet. Color scales help visualize data distribution and identify high and low values using color intensity.

The **Color scale for** option lets you select the formatting target.

Available options include:

- **Background**: Applies gradient formatting to the cell background.
- **Font**: Applies gradient formatting to the text color.
- **Data Bars**: Displays bars inside cells to represent value magnitude.
- **Bubble Chart**: Applies color scaling to bubble chart visuals.
- **Action Dots**: Applies color-based indicators using action dots.
- **Action Color**: Applies color-based formatting to action or status indicators.

  ![Screenshot of color scale for options.](../media/planning-conditional-formatting/how-to-format-color-scales/color-scales.png)

## Define rule conditions

Further available conditional formatting options vary based on the selected **Color scale for** option.

## Background color scales

The **Background** color scale option applies conditional formatting by changing the background color of cells based on their values. Different colors are used to represent value ranges, making it easier to identify trends, patterns, highs, and lows within the data.

Background color scales are useful for heatmap-style analysis and visual comparison across rows, columns, or measures.

## Font color scales

The **Font** color scale option applies conditional formatting by changing the font color of cell values based on the underlying data. Colors are assigned according to the configured value ranges, helping highlight important values without modifying the cell background.

Font color scales are useful when you want to emphasize values while maintaining the existing cell background or layout formatting.

### Configure conditional formatting for background and font color scales

#### **Heat map type**

Use **Heat map type** to control how color scale formatting is evaluated across the planning sheet.

Select the appropriate heat map type based on how you want values to be compared and visualized.

Available options include:

- **Row wise**: Applies color scaling independently for each row based on the values within that row.
- **Column wise**: Applies color scaling independently for each column based on the values within that column.
- **Table wise**: Applies color scaling across the entire table using all visible values.

  ![Screenshot of heat map types.](../media/planning-conditional-formatting/how-to-format-color-scales/heat-map.png)

#### **Color scale type**

Use **Color scale type** to select the color distribution pattern used for conditional formatting.

Available options include:

- **Sequential**: Uses a gradual progression of colors to represent low-to-high values. This type is useful for displaying continuous numeric ranges.
- **Diverging**: Uses contrasting colors to highlight variation above and below a midpoint or baseline value. This type is useful for variance and performance analysis.
- **Diverging - color safe**: Uses accessibility-friendly diverging colors designed for improved readability and color differentiation.
- **Qualitative**: Uses distinct colors to represent categorical or non-sequential data values.
- **Qualitative - color safe**: Uses accessibility-friendly qualitative colors for categorical data visualization.
- **Continuous - Range**: Applies a continuous gradient across a defined value range.
- **Continuous - Diverging Range**: Applies diverging colors across a defined range with emphasis on midpoint variation.
- **Continuous**: Applies a smooth color transition between minimum and maximum values.
- **Continuous - Diverging**: Uses contrasting colors to highlight values above and below a midpoint or baseline value.
- **Custom**: Lets you define custom color ranges and thresholds for conditional formatting.

  ![Screenshot of color scale type.](../media/planning-conditional-formatting/how-to-format-color-scales/color-scale-type.png)

#### Color scheme

Use the **Color scheme** section to customize the appearance of the color scale conditional formatting.

You can configure the following settings:

| Setting | Description |
| --- | --- |
| Color scheme | Select the color palette used for the color scale. |
| Reverse color | Reverses the selected color sequence. |
| Number of bands | Defines the number of color intervals used in the scale. |
| Hide value | Hides cell values and displays only the color formatting. |
| Auto font color | Automatically adjusts the font color for improved readability against the background color. |
| Include null | Includes null or blank values in the color scale evaluation. |

Note

**Hide value, Auto font color** and **Include null** are only available for **Background** color scales.

Here's how the conditional formatting rule looks when applied for **Background** color scales.

[![Screenshot of background color scales.](../media/planning-conditional-formatting/how-to-format-color-scales/background-color-scales.png)](../media/planning-conditional-formatting/how-to-format-color-scales/background-color-scales.png#lightbox)

## Data bars

The **Data bars** color scale option applies conditional formatting by displaying horizontal bars within cells based on the underlying values. The length of each bar represents the relative value compared to other values in the selected range.

Use data bars to quickly identify trends, compare values, and highlight high or low-performing data points visually.

### Configure conditional formatting for data bar color scales

You can configure the following options for data bar color scales:

- **Minimum and maximum values**: Define the range used to calculate bar lengths.
- **Bar color**: Select the color used for the data bars.
- **Hide value**: Choose whether to display the cell value along with the data bar.
- **Alignment -** Configure the position of the data bars within the cell, such as left or right.

After configuring the settings, save the rule to apply the data bar formatting to the selected cells.

Here's how the conditional formatting rule looks when applied for **Data Bars** color scales.

[![Screenshot of data bars.](../media/planning-conditional-formatting/how-to-format-color-scales/data-bars.png)](../media/planning-conditional-formatting/how-to-format-color-scales/data-bars.png#lightbox)

## Bubble chart color scales

The **Bubble chart** color scale option applies conditional formatting by displaying values as bubbles within cells. The size of each bubble represents the relative magnitude of the value, enabling quick visual comparison across the selected range.

Bubble charts help identify trends, outliers, and value distribution in a compact visual format.

### Configure conditional formatting for bubble chart color scales

You can configure the following options for bubble chart color scales:

- **Hide value**: Choose whether to display the cell value along with the bubble.
- **Bubble overlay**: Enable this option to allow the bubble chart to overlap the cell value.
- **Bubble color**: Select the color used for the bubbles.
- **Apply color to text**: Enable this option to apply the selected bubble color to the cell text.
- **Heat map type**: Select the heat map style to determine how colors are applied to the selected values. For more information, see [Heat map type](#heat-map-type).
- **Measure based color**: The bubble gradient and color intensity are determined based on the minimum and maximum values of the measure selected from the dropdown.

After configuring the settings, save the rule to apply the bubble chart formatting to the selected cells.

[![Screenshot of bubble charts.](../media/planning-conditional-formatting/how-to-format-color-scales/bubble-charts.png)](../media/planning-conditional-formatting/how-to-format-color-scales/bubble-charts.png#lightbox)

## Action dots and Action colors

The **Action dots** and **Action colors** options apply conditional formatting to action indicators in the planning sheet based on the configured rules and selected values.

- **Action dots** indicate the extent to which cell values deviate from the target or desired range in the measure. These indicators help you compare values against the midpoint or a specified target value within the measure. They display visual indicators as colored dots within cells to highlight status, trends, or important changes. The number of dots represents the magnitude of the difference
- **Action colors** apply color formatting to action indicators, making it easier to identify different states or conditions at a glance. Action colors are a variation of action dots where the deviation of cell values from the target value is represented using color gradients. The color scale indicates positive or negative deviation, while the gradient intensity represents the magnitude of the deviation.

These options help improve visibility and enable quick analysis of planning data.

### Configure conditional formatting for Action Dots and Action Colors color scales

- **Custom color ranges -** Use **Custom color ranges** to define color ranges based on **values** or **percentages**. You can add or remove ranges as needed.
- **Hide Values -** Enabling **Hide Values** hides the values of the cells.
- **Middle percentage -** The **Middle percentage** setting defines the midpoint used in a gradient scale. This is applicable only for Action Dots.

[![Screenshot of action dots.](../media/planning-conditional-formatting/how-to-format-color-scales/action-dots.png)](../media/planning-conditional-formatting/how-to-format-color-scales/action-dots.png#lightbox)

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
