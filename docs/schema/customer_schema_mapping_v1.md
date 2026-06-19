# Customer Schema Mapping Specification v1

## Overview

This document defines the transformation rules between the legacy ERP source schema and the target ERP schema.

It specifies how source attributes are mapped, transformed, and used to derive target attributes.

---

## Purpose

The mapping specification is used for:

- Deterministic transformation from Source → Target schema
- Synthetic dataset transformation (clean data)
- Ground truth generation
- Evaluation of migration correctness

---

## Field Mappings

### Direct Mappings

| Source Field   | Target Field |
|----------------|-------------|
| CustNo         | CustomerID |
| CompanyName    | Name |
| ZipCode        | PostalCode |
| Town           | City |
| CountryCode    | Country |
| LastOrderDate  | LastBusinessActivityDate |

---

## Composed Fields

### Street Construction

The target field `Street` is derived from:

- StreetAddress
- HouseNo (optional)

**Rule:**

- If HouseNo exists:
  - Street = StreetAddress + " " + HouseNo
- Else:
  - Street = StreetAddress

---

## Derived Fields

### Status (Target Field)

Status is derived from LastBusinessActivityDate:

- If date is within last 3 years → `active`
- If older than 3 years → `inactive`
- If NULL → `inactive`

---

## Field Constraints Alignment

### Country Normalization Requirement

The target schema requires:

- ISO-3166 alpha-3 format

Therefore:

- CountryCode → Country requires normalization step

Example mapping:

- DE → DEU
- GER → DEU
- Germany → DEU

---

### Required Field Handling

Target requires:

- LastBusinessActivityDate (required)
- Country (required)

If missing in source:

- LastOrderDate missing → must be handled via rule (e.g. NULL → inactive + flagged in evaluation context)

---

## Ignored Fields

- CustomerType (not used in target system)

---

## Notes

- This mapping is deterministic for clean datasets
- It is independent of noise injection
- It serves as the canonical transformation logic for Ground Truth generation
