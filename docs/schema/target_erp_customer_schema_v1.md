# Target ERP Customer Schema v1

## 1. Overview

This schema defines the target structure for customer master data in the ERP system.

It represents the canonical data model used for migration output and benchmark evaluation.

---

## 2. Purpose

The schema defines:

- required attributes
- data types
- validation constraints
- structural expectations for migrated data

---

## 3. Entity: Customer

The Customer entity represents a standardized customer record in the target ERP system.

---

## 4. Attributes

- CustomerID (string, required, unique)
- Name (string, required)
- Street (string, optional)
- City (string, optional)
- PostalCode (string, optional)
- Country (string, ISO format, required)
- Email (string, optional)
- LastBusinessActivityDate (date, required)
- Status (active/inactive, required)

---

## 5. Constraints

- CustomerID must be unique
- Name must not be empty
- Country must follow ISO 3166 alpha-3 format
- Status must be either active or inactive
- Active customers must have LastBusinessActivityDate

---

## 6. Usage in Benchmark

This schema is used for:

- Schema Mapping (Activity ACT-001)
- Data Validation (ACT-005)
- Ground Truth generation
- Evaluation of migration outputs
