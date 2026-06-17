# BenchmarForge Metamodel v0.1

## Overview

BenchmarkForage defines a minimal metamodel for generating reproducible data integration benchmarks for ERP migration scenarios

The system follows a linear data transformation pipeline:

Scenario -> Schema -> Dataset -> Noise -> Task -> Ground Truth -> Evaluation

---

## Core Entities

### 1. Scenario
Defines the business context and migration setting (e.g., ERP customer migration).

### 2. Schema
Defines structure of source and target data model.

### 3. Dataset
Represents synthetically generated records following a schema.

### 4. NoiseProfile
Defines data corruption rules applied to datasets.

### 5. Task
Defines the transformation or analysis problem to be solved.

### 6. Ground Truth
Defines expected corrected output for a given task.

### 7. EvaluationResult
Stores computed performance metrics comparing predictions vs. ground truth

---

## Data Flow

Scenario
  ↓
Schema (Source + Target)
  ↓
Dataset Generation
  ↓
Noise Injection
  ↓
Task Generation
  ↓
Ground Truth Generation
  ↓
Evaluation

---

## Design Principles

- Minimal and extensible structure
- Clear separation of concerns
- Reproducibility of benchmark instances
- Deterministic generation where possible
