# Source Customer Schema v1

## Overview

This schema defines the structure of customer master data stored in the legacy ERP system.

It describes only the structural contract of the data, without any assumptions about data quality, inconsistencies, or real-world noise.

---

## Purpose

The source schema is used to:

- Define the structure of synthetic legacy ERP datasets
- Serve as input for schema mapping tasks
- Enable deterministic dataset generation
- Provide a structural basis for benchmark scenarios

---

## Entity: Customer

The Customer entity represents a business customer record in the legacy ERP system.

---

## Attributes

| Attribute      | Type   | Required | Description |
|----------------|--------|----------|-------------|
| CustNo         | string | Yes      | Unique customer identifier |
| CompanyName    | string | Yes      | Name of the customer organization |
| StreetAddress  | string | No       | Street and house number |
| ZipCode        | string | No       | Postal code |
| Town           | string | No       | City or municipality |
| CountryCode    | string | No       | Country identifier |
| LastOrderDate  | date   | No       | Date of last recorded business transaction |
| CustomerType   | string | No       | Type of customer entity |

---

## Constraints

### CON-SRC-001
CustNo must be unique within the dataset.

### CON-SRC-002
CompanyName must be provided for each customer record.

---

## Notes

This schema is intentionally minimal and does not encode any assumptions about:

- data quality
- missing values
- inconsistencies
- real-world variations

Such characteristics are introduced later via the Noise Injection Engine.
