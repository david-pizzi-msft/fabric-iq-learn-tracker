---
title: "Period-to-date calculations"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations) · Last updated on **2026-08-25**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Period-to-date calculations

Summarize this article for me

Planning supports period-to-date functions that retrieve data from the beginning of the current month, quarter, or year up to the current period. These functions help you calculate cumulative values and analyze performance over a defined time period.

## MTD

The *MTD* function returns data for the current month. If an offset is specified, the function also returns data for the specified number of preceding months. Use this function with an aggregate function, such as `SUM` or `AVERAGE`, to calculate values over the returned date range.

### Syntax

```
MTD(measure, [offset])
```

### Arguments

- `measure`: The measure for which data is returned.
- `offset` (optional): The number of preceding months to include along with the current month.

### Return value

Returns the specified measure for the current month or for the current month and the specified number of preceding months.

### Examples

```
MTD([Sales])
```

Returns the *Sales* data for the current month.

[![Screenshot of a Planning sheet with MTD function.](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/mtd.png)](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/mtd.png#lightbox)

```
MTD([Sales],2)
```

Returns the *Sales* data for the current month and the preceding two months.

[![Screenshot of a Planning sheet with the Formula Measure pane showing the MTD function with an offset of 2.](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/mtd-offset.png)](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/mtd-offset.png#lightbox)

## QTD

The *QTD* function returns data for the current quarter. If an offset is specified, the function also returns data for the specified number of preceding quarters. Use this function with an aggregate function, such as `SUM` or `AVERAGE`, to calculate values over the returned date range.

### Syntax

```
QTD(measure, [offset])
```

### Arguments

- `measure`: The measure for which data is returned.
- `offset` (optional): The number of preceding quarters to include along with the current quarter.

### Return value

Returns the specified measure for the current quarter or for the current quarter and the specified number of preceding quarters.

### Examples

```
QTD([Sales])
```

Returns the *Sales* data for the current quarter.

[![Screenshot of a Planning sheet with QTD function.](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/qtd.png)](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/qtd.png#lightbox)

```
QTD([Sales],3)
```

Returns the *Sales* data for the current quarter and the preceding three quarters.

[![Screenshot of a Planning sheet with the Formula Measure pane showing the QTD formula with a quarter offset.](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/qtd-offset.png)](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/qtd-offset.png#lightbox)

## YTD

The *YTD* function returns data for the current year. If an offset is specified, the function also returns data for the specified number of preceding years. Use this function with an aggregate function, such as `SUM` or `AVERAGE`, to calculate values over the returned date range.

### Syntax

```
YTD(measure, [offset])
```

### Arguments

- `measure`: The measure for which data is returned.
- `offset` (optional): The number of preceding years to include along with the current year.

### Return value

Returns the specified measure for the current year or for the current year and the specified number of preceding years.

### Examples

```
YTD([Sales])
```

Returns the *Sales* data for the current year.

[![Screenshot of a Planning sheet with YTD function.](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/ytd.png)](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/ytd.png#lightbox)

```
YTD([Sales],2)
```

Returns the *Sales* data for the current year and the preceding two years.

[![Screenshot of a Planning sheet with the YTD function using an offset of 2 in the Formula Measure panel.](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/ytd-offset.png)](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/ytd-offset.png#lightbox)

## TOTALMTD

The *TOTALMTD* function returns the month-to-date value of a measure in the current context. Use this function with an aggregate function, such as `SUM` or `AVERAGE`, to calculate cumulative values for the current month.

### Syntax

```
TOTALMTD(measure)
```

### Arguments

- `measure`: The measure for which the month-to-date value is returned.

### Return value

Returns the month-to-date values for the specified measure. When used with an aggregate function, it returns a cumulative value from the beginning of the current month up to the current period.

### Example

The following formula returns the cumulative *Sales* value for each day in the current month.

```
SUM(TOTALMTD([Sales]))
```

For example, on **January 4**, the result is the sum of the *Sales* values from **January 1** through **January 4**.

[![Screenshot of a Planning sheet with TOTALMTD function.](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/totalmtd.png)](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/totalmtd.png#lightbox)

## TOTALQTD

The **TOTALQTD** function evaluates the quarter-to-date value of a measure in the current context. It is typically used with an aggregate function such as `SUM` or `AVERAGE` to calculate cumulative values from the beginning of the current quarter up to the current period.

### Syntax

```
TOTALQTD(measure)
```

### Arguments

The **TOTALQTD** function syntax has the following arguments:

- `measure`: The measure for which the quarter-to-date value is calculated.

### Return value

Returns the quarter-to-date range for the specified measure. When used with an aggregate function, it returns the cumulative value from the beginning of the current quarter up to the current period.

### Example

```
SUM(TOTALQTD([Sales]))
```

Returns the cumulative sales value for each period within the current quarter.

In the following example, the **QTD** column displays the cumulative sales from the beginning of the current quarter up to each month. For example, the value for **February** is the sum of **January** and **February** sales, and the value for **March** is the sum of **January**, **February**, and **March** sales. When a new quarter begins, the cumulative total resets and starts again from the first month of that quarter.

[![Screenshot of a Planning sheet with TOTALQTD function.](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/totalqtd.png)](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/totalqtd.png#lightbox)

## TOTALYTD

The *TOTALYTD* function evaluates the year-to-date value of a measure in the current context. It is typically used with an aggregate function such as `SUM` or `AVERAGE` to calculate cumulative values from the beginning of the current year up to the current period.

### Syntax

```
TOTALYTD([measure])
```

### Arguments

- `measure`: The measure for which the year-to-date value is calculated.

### Return value

Returns a range of values. When used with an aggregate function, it returns a scalar value representing the cumulative value from the beginning of the current year to the current period.

### Example

```
SUM(TOTALYTD([Sales]))
```

Returns the year-to-date sales by cumulatively summing the *Sales* measure for each year.

In the following example, the *YTD* measure shows the cumulative sales from the beginning of each year up to the current period. The cumulative value resets at the start of a new year.

[![Screenshot of a Planning sheet with TOTALYTD function.](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/totalytd.png)](../../media/planning-reference-formulas/time-intelligence-functions/period-to-date-calculations/totalytd.png#lightbox)

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
