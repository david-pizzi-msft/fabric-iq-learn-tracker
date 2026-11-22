---
title: "Other operators"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/planning-reference-other-operators](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/planning-reference-other-operators) · Last updated on **2026-09-03**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Other operators

Summarize this article for me

Use arithmetic, comparison, and grouping operators in Plan formulas to calculate and compare values and control the order in which expressions are evaluated.

You can use these operators with **node references** and **measures**. The operators also support nodes and measures that contain calendar dates.

## Operator list reference

| Operator | Description |
| --- | --- |
| `+` | Adds two values or indicates a positive value. |
| `-` | Subtracts one value from another or indicates a negative value. |
| `*` | Multiplies two values. |
| `/` | Divides one value by another. |
| `>` | Checks whether one value is greater than another. |
| `>=` | Checks whether one value is greater than or equal to another. |
| `=` | Checks whether two values are equal. |
| `!=` | Checks whether two values are not equal. |
| `<` | Checks whether one value is less than another. |
| `<=` | Checks whether one value is less than or equal to another. |
| `()` | Groups expressions and controls the order of evaluation. |

## Arithmetic operators

Use `+`, `-`, `*`, and `/` to perform arithmetic calculations with node references and measures.

### Syntax

```
Value1 + Value2
Value1 - Value2
Value1 * Value2
Value1 / Value2
```

### Examples

```
Revenue + OtherIncome
Revenue - Cost
Units * Price
Revenue / Units
```

These expressions return the sum, difference, product, or quotient of the specified values.

## Comparison operators

Use comparison operators to compare values from node references and measures.

### Syntax

```
Value1 > Value2
Value1 >= Value2
Value1 = Value2
Value1 != Value2
Value1 < Value2
Value1 <= Value2
```

### Examples

```
Revenue > Budget
Revenue >= Budget
Revenue = Budget
Revenue != Budget
Revenue < Budget
Revenue <= Budget
```

Use comparison operators when you need to evaluate the relationship between planning values.

## Parentheses

Use parentheses `()` to group expressions and control the order in which operations are evaluated.

### Syntax

```
(Value1 + Value2) * Value3
```

### Example

```
(Revenue - Cost) / Revenue
```

In this example, Plan evaluates `Revenue - Cost` before dividing the result by `Revenue`.

Use parentheses when a formula contains multiple operations and the order of evaluation matters.

## Positive and negative values

Use the unary `+` and `-` operators to indicate a positive or negative value.

### Syntax

```
+Value
-Value
```

### Example

```
-1
```

Use the `-` operator to represent a negative value.

## Operators with calendar dates

You can use the supported arithmetic and comparison operators with nodes and measures that contain calendar dates.

## Combine operators in a formula

You can combine multiple operators in a single formula to perform more complex calculations.

For example:

```
(Revenue - Cost) / Revenue
```

This formula calculates the difference between `Revenue` and `Cost` and then divides the result by `Revenue`.

Use parentheses when combining multiple operators to make the intended order of evaluation explicit.

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
