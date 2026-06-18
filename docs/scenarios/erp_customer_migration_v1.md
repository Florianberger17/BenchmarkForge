# ERP Customer Migration Scenario v1:

## 1. Szenario:
This scenario describes a typical ERP migration context in which customer master data is migrated from a legacy ERP system into a new target ERP system as part of a corporate integration process.

The focus is on data integration challenges such as schema differences, duplicate records, data quality issues, and business rule-based filtering.

---

## 2. Business Context

A company is being integrated into an existing corporate group. As part of this integration, the legacy ERP system will be replaced by a standardized target ERP system.

Customer master data must be migrated while ensuring:

- Data consistency
- Removal of duplicate records
- Compliance with business retention rules
- Correction of outdated or inconsistent data

---

## 3. Objective

The objective of this scenario is:

> To migrate valid customer master data from the legacy ERP system into the target ERP system according to defined business rules and data quality constraints.

---

## 4. Systems

### Source System (Legacy ERP)

Contains historical customer master data including:

- outdated records
- duplicate entries
- inconsistent address information

### Target System (New ERP)

Requires:

- standardized schema
- cleaned and validated customer data
- deduplicated records

---

## 5. Business Object

### Customer

Core entity of this scenario.

Typical attributes:

- CustomerID
- Name
- Street
- City
- Country
- LastBusinessActivityDate
- Status

---

## 6. Activities (High-Level Tasks)

This scenario consists of the following benchmark-relevant activities:

1. Schema Mapping
2. Duplicate Detection
3. Customer Filtering
4. Address Validation
5. Data Migration Output Generation

---

## 7. Business Rules

The following rules define valid migration behavior:

- Only customers with business activity within the last 3 years are migrated
- Duplicate customer records must be merged
- Address updates must be applied before migration

---

## 8. Inputs

- customer_master_source.csv
- customer_master_target_schema.csv
- address_updates.pdf

---

## 9. Outputs

- migrated_customer_master.csv
- migration_explanation.txt

---

## 10. Scope

### Included
- Customer master data migration
- Data cleaning and validation
- Schema mapping
- Business rule application

### Excluded
- ERP system configuration
- Infrastructure setup
- Performance optimization
- User training
