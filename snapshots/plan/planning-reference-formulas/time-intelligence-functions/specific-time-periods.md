---
title: "Calculate specific time periods"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/time-intelligence-functions/specific-time-periods](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/time-intelligence-functions/specific-time-periods) · Last updated on **2026-08-25**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Calculate specific time periods

Summarize this article for me

Planning supports specific time period functions that retrieve data for individual months, quarters, or years. These functions help you select data for a single time period or a range of time periods for analysis and reporting.

## MONTHPERIOD

The *MONTHPERIOD* function returns a range of dates for a specified month or range of months within a given year. Use this function with the `SELECT.BYDATE` function and an aggregate function, such as `SUM` or `AVERAGE`, to retrieve and aggregate data over the returned date range.

### Syntax

```
MONTHPERIOD(year, from_month, [to_month])
```

### Arguments

- `year`: The year for which data is returned.
- `from_month`: Specifies the month for which data is returned or the starting month of the range. Valid values are `1` through `12`.
- `to_month` (optional): Specifies the ending month of the range. Valid values are `1` through `12`.

### Return value

Returns a range of dates for the specified month or range of months.

### Examples

```
MONTHPERIOD(2025,1,7)
```

Returns the date range from **January** to **July** of **2025**.

[![Screenshot of a Planning sheet showing MONTHPERIOD function with from and to months.](../../media/planning-reference-formulas/time-intelligence-functions/specific-time-periods/monthperiod-to-month.png)](../../media/planning-reference-formulas/time-intelligence-functions/specific-time-periods/monthperiod-to-month.png#lightbox)

```
MONTHPERIOD(2025,4)
```

Returns the date range for **April 2025**.

[![Screenshot of a Planning sheet showing MONTHPERIOD function with from month.](../../media/planning-reference-formulas/time-intelligence-functions/specific-time-periods/monthperiod-from-month.png)](../../media/planning-reference-formulas/time-intelligence-functions/specific-time-periods/monthperiod-from-month.png#lightbox)

## QTRPERIOD

The *QTRPERIOD* function returns a range of dates for a specified quarter or range of quarters in a given year. Use this function with the `SELECT.BYDATE` function and an aggregate function, such as `SUM` or `AVERAGE`, to retrieve and aggregate data over the returned date range.

### Syntax

```
QTRPERIOD(year, from_quarter, [to_quarter])
```

### Arguments

- `year`: The year for which data is returned.
- `from_quarter`: The quarter to return, or the starting quarter when specifying a range. Valid values are `1` through `4`.
- `to_quarter` (optional): The ending quarter of the range. Valid values are `1` through `4`.

### Return value

Returns a range of dates for the specified quarter or range of quarters.

### Examples

```
QTRPERIOD(2025,1,3)
```

Returns the date range from the first quarter through the third quarter of **2025**.

[![Screenshot of a Planning sheet showing QTRPERIOD function with from and to quarters.](../../media/planning-reference-formulas/time-intelligence-functions/specific-time-periods/qtrperiod-to-quarter.png)](../../media/planning-reference-formulas/time-intelligence-functions/specific-time-periods/qtrperiod-to-quarter.png#lightbox)

```
QTRPERIOD(2025,4)
```

Returns the date range for the fourth quarter of **2025**.

[![Screenshot of a Planning sheet showing the QTRPERIOD function for a single quarter.](../../media/planning-reference-formulas/time-intelligence-functions/specific-time-periods/qtrperiod-from-quarter.png)](../../media/planning-reference-formulas/time-intelligence-functions/specific-time-periods/qtrperiod-from-quarter.png#lightbox)

## YEARPERIOD

The *YEARPERIOD* function returns a range of dates for a specified year or range of years. Use this function with the `SELECT.BYDATE` function and an aggregate function, such as `SUM` or `AVERAGE`, to retrieve and aggregate data over the returned date range.

### Syntax

```
YEARPERIOD(from_year, [to_year])
```

### Arguments

- `from_year`: The year to return, or the starting year when specifying a range.
- `to_year` (optional): The ending year of the range.

### Return value

Returns a range of dates for the specified year or range of years.

### Examples

```
YEARPERIOD(2024,2026)
```

Returns the date range from **2024** through **2026**.

[![Screenshot of a Planning sheet showing the YEARPERIOD function with from and to year.](../../media/planning-reference-formulas/time-intelligence-functions/specific-time-periods/yearperiod-to-year.png)](../../media/planning-reference-formulas/time-intelligence-functions/specific-time-periods/yearperiod-to-year.png#lightbox)

```
YEARPERIOD(2025)
```

Returns the date range for **2025**.

[![Screenshot of a Planning sheet with the Formula Measure pane showing a YearPeriod function with a single year.](../../media/planning-reference-formulas/time-intelligence-functions/specific-time-periods/yearperiod-from-year.png)](../../media/planning-reference-formulas/time-intelligence-functions/specific-time-periods/yearperiod-from-year.png#lightbox)

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
