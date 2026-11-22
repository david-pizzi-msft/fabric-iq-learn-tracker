---
title: "What is a cube?"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-concept-cube](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-concept-cube) · Last updated on **2026-08-17**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# What is a cube?

Summarize this article for me

In many business scenarios, you create plans separately for each dimension - such as regions, product lines, departments, or time periods - which results in duplicated effort and fragmented planning. By using multidimensional cube planning, you can create and allocate plans across multiple dimensions with different granularities in a single step. Cubes enable plans to stay synchronized across different levels of detail.

## Plan across unrelated dimensions

In real-world planning, different functions often use different dimensions to represent their planning requirements. For example, the Sales function might plan revenue by *Product*, *City*, *Time*, and *Channel*, while Finance plans revenue by *GL Account*, *Region/Country*, and *Time*.

These dimensions don't have a direct one-to-one relationship. You can't directly map a sales plan to a finance plan. However, both functions might need to plan, reconcile, and report on the same revenue.

[![Screenshot of unrelated dimensions used for planning in sales and finance functions.](media/planning-concept-cube/unrelated-sales-finance-dimensions.png)](media/planning-concept-cube/unrelated-sales-finance-dimensions.png#lightbox)

A cube can bridge these different planning structures by creating a multidimensional view of the data and allocating values across the required dimensions.

Note

Cubes don't require every planning function to use the same dimensions. Each function can continue planning at the grain appropriate to its business process while the cube provides the multidimensional layer needed to distribute and consolidate values.

[![Screenshot of a conceptual multidimensional cube.](media/planning-concept-cube/multidimensional-cube.png)](media/planning-concept-cube/multidimensional-cube.png#lightbox)

For example:

- Finance sets a revenue budget by *GL Account*, *Region/Country*, and *Time*.
- Sales needs to distribute that budget across *Product*, *City*, *Channel*, and *Time*\*.
- The cube uses the available relationships and allocation drivers to distribute the finance-level value across the sales dimensions.
- Sales can then refine the forecast at its planning grain, while the values aggregate back to the finance dimensions for consolidated reporting.

The cube allocates Finance revenue budget across Sales dimensions using allocation drivers.

![Screenshot of multidimensinal alocation across sales and finance dimensions.](media/planning-concept-cube/multidimensional-allocation-example.png)

Sales refines the plan at its grain, while the cube ensures that values roll up to Finance dimensions for consolidated reporting.

[![Screenshot of aggregating plans at the grain of sales dimensions to finance level dimensions.](media/planning-concept-cube/multidimensional-allocation-aggregation.png)](media/planning-concept-cube/multidimensional-allocation-aggregation.png#lightbox)

## Driver-based allocation model

Each cube is configured around a [data input measure](planning-how-to-input-data) or [forecast](planning-forecasting/planning-how-to-build-forecasts) measure. The cube uses an allocation driver (also called a reference measure or allocation key) to perform allocation within the cube.

The allocation driver is typically a DAX (Data Analysis Expressions) measure from the semantic model, such as prior year actuals, current year revenue, units sold, headcount, or production volume.

The allocation driver is usually a DAX (Data Analysis Expressions) measure from the semantic model, such as prior year actuals, current year revenue, units sold, headcount, or production volume. This driver measure provides the weights and ratios for proportional distribution.

## How allocation works

1. Enter a value at a summarized level, such as 500 for a product without selecting lower-level dimensions (for example, region or province).
2. The selected allocation driver measure determines how the cube distributes values.
3. The cube allocates the value proportionally across all valid dimension intersections, based on the driver measureâs relative weights.

[![Screenshot of distributing values across products based on the weights of units sold.](media/planning-concept-cube/weighted-allocation-example.png)](media/planning-concept-cube/weighted-allocation-example.png#lightbox)

## Allocation formula (conceptual)

The allocated value is calculated by multiplying the entered value by the relative weight of the allocation driver at each valid intersection. The following formula shows how allocation works:

```
Allocated Value =
Entered Value Ã
(Driver Value at the intersection Ã· Sum of Driver Values within the hierarchy scope)
```

In the formula:

- *Entered Value* is the total value entered at a higher level of aggregation.
- *Driver Value at the intersection* is the allocation driver's value for a combination of row and column dimensions.
- The *hierarchy scope* includes all valid lowerâlevel intersections over which the cube distributes the entered value.

## What allocation means in practice

Allocation happens only for dimension intersections where the driver has a non-null value.

The cube distributes values based on the relative contribution of each driver value within the hierarchy scope.

Allocation respects the dimensional granularity and breakdowns configured in the cube, ensuring consistency with the data model.

[![Screenshot of allocating values.](media/planning-concept-cube/allocation.png)](media/planning-concept-cube/allocation.png#lightbox)

## Multidimensional allocation

Cubes support distributing plans across:

- Dimensions present in the planning sheet
- Dimensions not currently visible in the sheet, but configured in the cube breakdown
- Multiple granularities, simultaneously

Complex enterprise allocations - such as Region > Product Line > Department - can occur in a single action, while maintaining data integrity across the cube.

You don't need to add the allocation driver measure to the planning sheet. It can exist solely in the semantic model and be used internally as the weighting mechanism.

## Use case: Enterprise-level budget allocation

Consider an organization allocating an annual budget across regions, product lines, and departments.

The organization can follow these steps to use a cube:

1. Enter the total budget at a higher level.
2. Select a driver measure (for example, prior year actuals) as the allocation driver.
3. The cube proportionally distributes the budget across all valid intersections.
4. Allocations remain synchronized across all dimensionsâeven the dimensions not visible in the current sheet.

This approach avoids manual breakdowns, duplicate models, and reconciliation errors.

## Use case: Multi-granular assumptions with hierarchical allocation

Consider an organization planning across two core hierarchies:

- Geography Hierarchy: Region > City
- Product Hierarchy: Brand > Category > Product

These hierarchies define the full analytical space (Region Ã City Ã Brand Ã Category Ã Product Ã Time).

The organization can follow these steps to apply a cube-driven planning model:

1. Capture assumptions at their natural grain.

   Enter each assumption at the level most relevant to the business:

   - Revenue plan > Product Ã City
   - Cost plan > Region Ã Brand
   - Marketing plan > Brand

   Each input reflects how the business actually plans, not an artificial lowest level.
2. Use a common driver for alignment.

   A consistent driver measure (for example, Revenue Actuals) is used to determine distribution weights across the entire hierarchy.
3. Allocate across hierarchies.

   The cube automatically spreads each assumption across missing dimensions:

   - Brand-level > down to Category > Product
   - Region-level > down to City
   - Combined > expanded to Product Ã City

   All allocations follow the driver distribution.
4. Converge to a common grain.

   Align all assumptions to a unified level: Product Ã City Ã Time.
5. Enable unified reporting.

   Once aligned, you can combine assumptions seamlessly, enabling metrics like: Profit = Revenue â (Cost + Marketing) at the Product Ã City level.

   Planners can work at different levels while ensuring all data converges into a single, consistent analytical model.

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
