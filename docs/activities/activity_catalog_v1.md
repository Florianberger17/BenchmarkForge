# Activity Catalog v1

## 1. Overview

The Activity Catalog defines a reusable set of domain-agnostic data integration operations.

These activities represent atomic building blocks for:
- ERP migration pipelines
- synthetic benchmark generation
- data quality processing
- future LangGraph node mapping

They are independent of any specific scenario and can be composed into tasks.

---

## 2. Design Principles

- Activities are reusable across scenarios
- Each activity has clear inputs and outputs
- Activities are atomic (no orchestration logic)
- Activities are domain-agnostic where possible
- Activities will later map to executable pipeline nodes

---

## 3. Activity Definitions

---

### ACT-001: Schema Mapping

**Purpose:**  
Map source schema fields to target schema fields.

**Inputs:**
- source_schema
- target_schema
- dataset

**Outputs:**
- mapped_dataset

**Description:**  
Transforms data from a source structure into a target structure.

---

### ACT-002: Record Filtering

**Purpose:**  
Filter dataset records based on business rules.

**Inputs:**
- dataset
- business_rules

**Outputs:**
- filtered_dataset

**Description:**  
Removes records that do not satisfy defined business conditions.

---

### ACT-003: Duplicate Detection

**Purpose:**  
Identify duplicate records in a dataset.

**Inputs:**
- dataset

**Outputs:**
- duplicate_report

**Description:**  
Detects duplicates based on matching heuristics or keys.

---

### ACT-004: Data Enrichment

**Purpose:**  
Enrich dataset using external or auxiliary information.

**Inputs:**
- dataset
- external_sources

**Outputs:**
- enriched_dataset

**Description:**  
Adds missing or updated information to existing records.

---

### ACT-005: Data Validation

**Purpose:**  
Validate dataset consistency and rule compliance.

**Inputs:**
- dataset
- validation_rules

**Outputs:**
- validation_report

**Description:**  
Checks data integrity and business rule adherence.

---

### ACT-006: Output Generation

**Purpose:**  
Generate final benchmark output artifacts.

**Inputs:**
- dataset

**Outputs:**
- final_dataset
- execution_report

**Description:**  
Produces final outputs for benchmarking and evaluation.

---

## 4. Summary

The Activity Catalog forms the operational core of BenchmarkForge,
bridging abstract scenario definitions and executable data processing pipelines.
