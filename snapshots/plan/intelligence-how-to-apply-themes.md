---
title: "Apply and customize themes for standardization"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-how-to-apply-themes](https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-how-to-apply-themes) · Last updated on **2026-06-24**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Apply and customize themes for standardization

Summarize this article for me

Use built-in themes or create custom themes to ensure consistent color schemes across all the elements in your intelligence dashboards. Themes reduce the time and effort you spend on dashboard design. Applying themes eliminates manual styling of each element and promotes better readability with pretested color contrasts.

In this article, you learn to apply ready-to-use themes in your dashboards, charts, and KPI cards. You also learn how to customize, import, and export themes.

## Apply dashboard themes

Dashboard themes provide a faster way to apply colors, fonts, and styling across KPIs, tables, charts, and visual elements. By using single-click themes, instantly apply a color scheme without configuring each element separately.

In the **Intelligence** ribbon, go to **Canvas** > **Themes** to select a different color palette.

[![Screenshot of panel showing built-in themes like dark, color blind dark, color blind light.](media/intelligence-how-to-apply-themes/theme-interface.png)](media/intelligence-how-to-apply-themes/theme-interface.png#lightbox)

Intelligence sheets support multiple predefined themes:

- **Light**: A clean, bright theme designed for general business reporting and everyday dashboard use.
- **Dark**: A dark-background theme that reduces screen glare and improves visibility in low-light environments.
- **Color blind Light**: A light theme that uses a color palette optimized for users with color vision deficiencies, improving accessibility and readability.
- **Color blind Dark**: A dark theme with colorblind-friendly colors, combining accessibility with a low-glare viewing experience.
- **IBCS**: A theme that follows the International Business Communication Standards (IBCS) and uses standardized colors, visual conventions, and formatting to improve report consistency and data comprehension.

Select a theme to apply it across all the elements in the dashboard.

[![Screenshot of applying a different theme.](media/intelligence-how-to-apply-themes/change-dashboard-theme.png)](media/intelligence-how-to-apply-themes/change-dashboard-theme.png#lightbox)

## Create and edit dashboard themes

Themes support extensive customizations. Tailor themes to match your organization's branding, reporting standards, or accessibility requirements. Modify colors, canvas backgrounds, text formatting, borders, and headers to create a standardized dashboard design.

1. Select **Add Theme**.
2. In the **Color Palette** section, specify the chart and variance colors.
3. In the **Page** section, set the canvas and wallpaper backgrounds. Import images or select a color for the background. Optionally, enable gridlines and set page dimensions.
4. Customize the font family, font size, and color in the **Text** section. For automatic adjustments:

   - Enable **Responsive Size** to adjust the font size based on the canvas area.
   - Turn on **Enable Auto Font** to change the font color for maximum visibility based on the background.
5. Set the border, shadow, and header colors in the **Layout** section.

[![Screenshot of theme customization options for the canvas background, font, border, and page dimensions.](media/intelligence-how-to-apply-themes/customize-theme.png)](media/intelligence-how-to-apply-themes/customize-theme.png#lightbox)

Tip

Hover over a theme and select **More options** (...) > **Edit** to personalize a prebuilt theme.

## Import and export dashboard themes

Import custom themes in JSON format into an intelligence sheet to apply formatting standards across dashboards and reports. Select **Import JSON**. Upload a JSON file or paste the content.

[![Screenshot of importing a custom theme.](media/intelligence-how-to-apply-themes/import-dashboard-theme.png)](media/intelligence-how-to-apply-themes/import-dashboard-theme.png#lightbox)

Export themes that you configure in an intelligence sheet and reuse them in other intelligence sheets. Hover over a theme and select **More options** (...) > **Export**. Copy the configuration and save it in a `.json` file.

[![Screenshot of exporting a theme in JSON format.](media/intelligence-how-to-apply-themes/export-dashboard-theme.png)](media/intelligence-how-to-apply-themes/export-dashboard-theme.png#lightbox)

## Apply built-in themes for charts

Each chart type uses a default color scheme. Select a different theme to change the colors.

1. To view available themes, select the paintbrush icon in the chart ribbon (in this example, **Treemap**).

   [![Screenshot of built-in chart themes like dark, midnight, and color blind themes.](media/intelligence-how-to-apply-themes/chart-theme.png)](media/intelligence-how-to-apply-themes/chart-theme.png#lightbox)
2. Select color palettes like the dark theme or color blind dark/white from the **Classic** theme section.

   [![Screenshot of applying a different chart theme.](media/intelligence-how-to-apply-themes/change-chart-theme.png)](media/intelligence-how-to-apply-themes/change-chart-theme.png#lightbox)
3. Apply themes that conform to specific standards like IBCS. Create dashboards that follow established reporting conventions by applying a prebuilt IBCS-aligned theme.

   [![Screenshot of IBCS chart theme.](media/intelligence-how-to-apply-themes/ibcs-chart-theme.png)](media/intelligence-how-to-apply-themes/ibcs-chart-theme.png#lightbox)

## Change the theme for KPI cards

Change the theme to use a predefined set of colors and formatting options in KPI dashboards. In the **KPI** ribbon, go to **Settings** > **Theme** and apply a theme.

[![Screenshot of built-in KPI themes.](media/intelligence-how-to-apply-themes/kpi-theme.png)](media/intelligence-how-to-apply-themes/kpi-theme.png#lightbox)

Theme colors determine the appearance of KPI metrics and charts.

[![Screenshot of  a high-contrast dark theme.](media/intelligence-how-to-apply-themes/change-kpi-theme.png)](media/intelligence-how-to-apply-themes/change-kpi-theme.png#lightbox)

## Create custom themes

Modify theme settings to align with your organization's branding and reporting needs. To customize theme colors, go to **Settings** > **Theme** > **Classic** > **Customize**. Assign colors for charts, measures, variances, and more.

- Expand the **Measure Colors** section and set the color for each measure.

  [![Screenshot of setting the measure colors in a theme.](media/intelligence-how-to-apply-themes/set-measure-colors-kpi.png)](media/intelligence-how-to-apply-themes/set-measure-colors-kpi.png#lightbox)
- Assign colors used to show positive and negative variances from the **Variance Colors** section.

  [![Screenshot of setting the variance colors in a theme.](media/intelligence-how-to-apply-themes/set-variance-colors-kpi.png)](media/intelligence-how-to-apply-themes/set-variance-colors-kpi.png#lightbox)
- Assign a custom background and font color from the **Canvas Colors** section.

  [![Screenshot of setting the background color in a theme.](media/intelligence-how-to-apply-themes/canvas-colors-kpi.png)](media/intelligence-how-to-apply-themes/canvas-colors-kpi.png#lightbox)

After designing a theme, you can export the JSON config and save it as a .json file. Import the config file into another intelligence sheet to reuse the same theme across all your charts.

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
