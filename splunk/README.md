# 🔍 Splunk - AI + SOAR Implementation

## Overview
This module demonstrates AI-based threat detection and automated response using Splunk.

---

## AI-Based Detection

We implemented the following detection techniques:

### 1. Multiple User Login Detection
Identifies systems attempting multiple usernames (credential stuffing).

### 2. Brute Force Detection
Detects repeated failed login attempts on a single account.

### 3. Failure Rate Analysis
Calculates percentage of failed logins to detect anomalies.

---

## SOAR Implementation

Splunk alerts are configured to trigger automated actions:

- Execute Python script to block malicious IP
- Generate alert notifications

---

## Workflow

Logs → Splunk Queries → Detection → Alert Trigger → Script Execution → Action

---

## Outcome

- Real-time detection of attacks
- Automated response system
- Simulation of AI-driven SOC + SOAR pipeline
