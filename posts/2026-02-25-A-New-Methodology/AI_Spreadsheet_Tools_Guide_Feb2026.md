---
title: AI-Powered Financial Modelling — Tools, Architecture & What's Now Possible
subtitle: A Reference Guide for Finance Professionals
date: 2026-02-25
tags:
  - excel
  - python
  - ai-tools
  - financial-modelling
  - quarto
  - xlwings
  - monte-carlo
  - dual-model
---

# AI-Powered Financial Modelling

**Tools, Architecture & What's Now Possible — February 2026**

A guide for finance and analytics professionals exploring AI tools for Excel, advanced analytics, and modern modelling workflows.

---

## 1. Introduction

The landscape of AI-assisted financial modelling tools is evolving rapidly. For finance and analytics professionals, the building blocks now available — from Claude's financial plugins to Copilot Agent Mode to open source tools like xlwings and Quarto — open up workflow approaches that were not practical even six months ago. This document provides an objective guide to making best use of what now exists: the AI tools for spreadsheet work, the complementary Python/R toolset for advanced analytics and reporting, and a practical architecture that brings them together.

This guide covers three areas: the current AI tools that integrate with or generate spreadsheets, a workflow architecture that combines Excel (for stakeholder-facing models) with Python (for advanced analytics, simulation, and governance), and a practical getting-started path.

---

## What's New This Week (February 24-25, 2026)

As this guide was being finalised, Anthropic announced a significant set of updates at its Enterprise Agents event on February 24, 2026:

- **Financial services plugins** — five new open source plugins (financial analysis, investment banking, equity research, private equity, wealth management) released on [GitHub](https://github.com/anthropics/financial-services-plugins) under Apache 2.0. The core financial analysis plugin builds DCF models, comparable company analyses, LBO models, and 3-statement financials as fully functional Excel workbooks with live formulas, sensitivity tables, and industry-standard formatting. 41 skills, 38 commands, 11 MCP integrations.
- **Partner plugins** — LSEG (fixed income, FX, equities, macro analysis with live data) and S&P Global (Capital IQ tearsheets, earnings previews, funding digests).
- **Cross-application workflows** — Claude can now carry context between Excel and PowerPoint in a single session, available as a research preview for all paid plans.
- **New MCP connectors** — FactSet and MSCI join the existing connector ecosystem (S&P Global, LSEG, Daloopa, Morningstar, Moody's, PitchBook, Aiera, Chronograph, Egnyte).
- **Cowork enterprise features** — private plugin marketplaces, per-user provisioning, and auto-install capabilities for organisations.

These plugins are squarely aimed at **corporate finance** — valuations of listed companies, deal workflows, equity research, and portfolio management using public market data. They do not address project finance, infrastructure feasibility, or other specialist modelling domains (see Section 7 for how custom Claude skills fill that gap). For corporate finance workflows, however, they significantly strengthen the "build" side of the process. The architecture in Sections 4–6 is designed to complement these tools — adding the governance, simulation, and reporting layers that wrap around the AI-generated outputs.

---

## 2. AI Tools for Spreadsheet Work

The following section compares five distinct Claude surfaces and two major competitors, focusing on the capabilities most relevant to finance professionals: formula handling, VBA support, named ranges, data connectors, and automation depth.

### 2.1 Claude Surfaces

#### 2.1.1 Claude Chat (claude.ai / Desktop App)

The standard web and desktop chat interface. It includes a built-in code execution environment (Python) that can create .xlsx files from scratch with formulas, formatting, charts, and multiple tabs. Users upload data or describe requirements; Claude generates a downloadable file.

**Strengths:** Good for generating new workbooks from natural language descriptions. Can write VBA code, Power Query M code, and Office Scripts as text for the user to implement. Supports file uploads up to 30MB. Strong reasoning for complex analytical questions.

**Limitations:** When analysing uploaded workbooks, reads cell values only and does not reconstruct formula logic or cell dependencies. Cannot embed VBA into .xlsm files. No live editing of existing workbooks. Generated files use Python libraries (openpyxl) so some Excel-native features like named ranges require explicit prompting.

#### 2.1.2 Claude Cowork (Desktop Agent)

Runs in a sandboxed Linux VM with full Python access and curated skills for .xlsx creation. Operates via the Claude desktop application and is designed for multi-step, iterative workflows.

**Strengths:** Can read uploaded files, analyse data, build multi-tab models with working formulas, and iterate across multiple steps. Supports todo tracking, verification steps, and can produce Word, PowerPoint, and PDF outputs alongside spreadsheets. More persistent and capable than Chat for complex multi-file projects.

**Limitations:** Same underlying openpyxl engine as Chat, so the same constraints on VBA embedding apply. Named ranges and conditional formatting are technically possible but not always leveraged by default. Runs on Linux, so no COM-based Excel automation.

#### 2.1.3 Claude Code (CLI Tool)

A terminal-based agentic coding tool aimed at software developers. Operates directly in the user's local file system with full access to their development environment.

**Strengths:** The most powerful option for Excel manipulation. If the user has xlwings, win32com, or other COM-based libraries installed locally, Claude Code can write Python that directly automates Excel via COM, including VBA injection, named range creation, and full workbook object model access. Can also generate Power Query M code and Office Scripts.

**Limitations:** Requires comfort with a terminal and a local Python environment. Aimed at developers rather than finance professionals. No graphical interface.

#### 2.1.4 Claude in Excel (Add-in)

A sidebar add-in that runs inside Microsoft Excel itself. Currently in beta, available to Pro, Max, Team, and Enterprise plan subscribers.

**Strengths:** Reads the actual workbook including formulas, cell dependencies, and multi-tab structures. Can edit cells, build pivot tables, create charts, apply conditional formatting, sort/filter data, and set data validation. Preserves formula dependencies when updating assumptions. Provides cell-level citations. Supports MCP connectors for external financial data (S&P Global, FactSet, Pitchbook, LSEG, Daloopa, Moody's). Users can switch between Sonnet and Opus models.

**Limitations:** Cannot read, write, execute, or modify VBA macros. Cannot create or interact with named ranges. Does not support data tables (what-if analysis). Chat history is not saved between sessions. The .xlsm format is supported but the VBA layer is completely invisible to the add-in.

**Recent update (February 24, 2026):** Claude can now work across Excel and PowerPoint in a single session, carrying context between the two applications. Available as a research preview for all paid plans on Mac and Windows. Anthropic also announced 5 new financial plugins (financial analysis, investment banking, equity research, private equity, wealth management) and new MCP connectors for FactSet and MSCI.

#### 2.1.5 Claude Surface Comparison Matrix

| Capability | Chat | Cowork | Code (CLI) | In Excel |
|---|---|---|---|---|
| Create new .xlsx files | Yes (Python) | Yes (Python) | Yes (any lib) | Yes (in-place) |
| Read existing formulas | Values only | Values only | Full (COM) | Full |
| Edit workbooks in-place | No (download) | No (download) | Yes (COM) | Yes |
| VBA: generate code as text | Yes | Yes | Yes | No |
| VBA: embed/execute in workbook | No | No | Yes (with COM) | No |
| Named ranges | Via openpyxl | Via openpyxl | Full (COM) | No |
| Conditional formatting | Via openpyxl | Via openpyxl | Full (COM) | Yes |
| Pivot tables | Limited | Limited | Full (COM) | Yes |
| Charts | Yes (basic) | Yes (basic) | Full (COM) | Yes |
| Financial data connectors | No | No | No | Yes (MCP) |
| Multi-step workflows | Limited | Strong | Strong | Moderate |
| Power Query M code | Text only | Text only | Text only | No |
| Data validation | Via openpyxl | Via openpyxl | Full (COM) | Yes |

### 2.2 Microsoft Copilot (Agent Mode in Excel)

Agent Mode reached general availability in January 2026 on Windows and Mac. It is the most Excel-native AI assistant currently available, built on the Excel calculation engine rather than external libraries.

**Key capabilities:** Generates formulas (including complex nested logic and dynamic arrays), creates pivot tables, generates named ranges, builds charts and dashboards, adds sheets, and iterates through multi-step workbook builds with built-in validation checks. Users can switch between GPT 5.2 (OpenAI) and Claude Opus 4.5 (Anthropic) as the underlying model.

**VBA support:** Can generate VBA code from natural language prompts but cannot execute VBA automatically within the workbook. VBA execution is described as something that may come in future desktop builds.

**Licensing:** Requires Microsoft 365 Personal/Family with AI credits, Microsoft 365 Premium, or a commercial Copilot subscription.

**Regional availability:** Personal and Family subscriptions are not currently available in the EU or UK. Commercial Copilot licences are available globally.

**Limitations:** App Skills are being retired in late February 2026, consolidating everything into Agent Mode. Some desktop macro functionality and offline workflows may not be fully supported until later builds ship. Agent Mode only works with the currently open workbook and cannot access other files or enterprise data.

### 2.3 Google Gemini (in Google Sheets)

Gemini is tightly integrated into Google Sheets for formula suggestions, data profiling, charting, and data cleaning. It works natively within the spreadsheet grid, enabling real-time formula creation, live data profiling, and automated cleaning.

**Key limitation for Excel users:** Google Sheets does not support VBA at all. It uses Apps Script (JavaScript-based) for automation. If existing models are VBA-heavy, Gemini is not a viable option without significant rewriting. Gemini also struggles with multi-sheet relationships and advanced Excel-specific logic when .xlsx files are uploaded. Charts embedded in Excel files are generally ignored, and advanced formatting is not preserved.

**Best suited for:** Teams already in the Google Workspace ecosystem doing lightweight collaborative analysis. Not a replacement for serious Excel-based financial modelling.

### 2.4 Head-to-Head: AI Excel Tools

| Capability | Copilot Agent Mode | Claude in Excel | Gemini in Sheets |
|---|---|---|---|
| Named ranges | Yes (generates) | No | N/A (Sheets) |
| VBA execution | No (generates text) | No | N/A (no VBA) |
| Formula depth | Strong (native engine) | Strong (reads formulas) | Moderate |
| Pivot tables | Yes | Yes | Sheets-native only |
| Charts | Yes | Yes | Yes |
| Conditional formatting | Yes | Yes | Sheets-native only |
| Data connectors | M365 ecosystem | MCP (S&P, FactSet...) | Workspace connectors |
| Cross-platform | Web + Windows + Mac | Windows + Mac | Web + mobile |
| Model switching | GPT 5.2 / Opus 4.5 | Sonnet / Opus | Gemini models only |
| Regional restrictions | Not in EU/UK | None known | None known |
| Licensing cost | M365 Copilot add-on | Claude Pro/Team/Ent | Workspace subscription |

---

## 3. Python in Excel (Microsoft Built-in)

Microsoft's built-in Python integration (the `=PY()` function) is now generally available for Business and Enterprise M365 subscribers on Windows, Mac, and Excel for the web.

### 3.1 What It Does

Users type Python code directly into cells using the `=PY()` function. Code executes in a sandboxed Azure container with pre-installed libraries including pandas, NumPy, matplotlib, scikit-learn, and NLTK. Results display in the worksheet grid. A dedicated Python Editor provides syntax highlighting, code completion, and data referencing via the `xl()` function.

### 3.2 What It Does Not Do

Python in Excel is explicitly positioned by Microsoft as an alternative to the formula language, not to VBA. It has significant constraints:

- Cannot access local files, devices, or the user's computer
- Cannot call web APIs or install custom packages
- Cannot interact with VBA macros or modify workbook properties (charts, pivot tables, formatting)
- Cannot accept user inputs or trigger events
- Requires an internet connection (cloud execution only)
- Subject to monthly compute quotas; exceeding the limit produces a `#BLOCKED` error
- Execution runs left-to-right, top-to-bottom; no parallel execution

In essence, Python in Excel is a two-dimensional Jupyter notebook embedded in the grid. It is excellent for analytics and visualisation within the workbook but cannot automate workbook operations.

### 3.3 Office Scripts (TypeScript-based Automation)

Office Scripts is Microsoft's cloud-first automation language for Excel, using TypeScript (a superset of JavaScript). It runs on any platform that supports Excel for the web, including Windows, macOS, iOS, and Linux.

**Key advantage:** Deep integration with Power Automate, allowing workbooks to be updated through scheduled or event-driven flows without opening Excel. This makes Office Scripts the preferred choice for cloud-based, cross-platform automation.

**Current limitations vs VBA:** Office Scripts do not support Excel-level events (worksheet changes, workbook open, etc.), cannot interact with other programs or multiple workbooks simultaneously, cannot create new workbooks, and have no Foreign Function Interface for calling COM or Win32 APIs. Feature coverage is growing but does not yet match VBA's desktop capabilities.

**Strategic outlook:** Microsoft has stated VBA will not be enhanced beyond occasional Object Model extensions. All major development investment is going into Office Scripts and the Power Platform. The practical recommendation is to retain VBA for legacy compatibility while adopting Office Scripts for new cloud-based workflows.

---

## 4. Modern Workflow Architectures

The AI tools described above address specific tasks within the spreadsheet. For finance and analytics teams seeking to modernise end-to-end workflows, including data acquisition, transformation, analysis, simulation, and reporting, a broader toolkit is needed. The following sections describe proven approaches that complement rather than replace Excel.

### 4.1 xlwings: Replacing VBA with Python

xlwings is an open-source Python library (BSD licence) that provides full programmatic control over Microsoft Excel via the COM interface on Windows and the application scripting bridge on Mac. It uses a syntax deliberately close to VBA, making it the lowest-friction migration path for VBA-experienced professionals.

**Core Capabilities:**

- **Scripting:** Automate and interact with Excel from Python using a syntax close to VBA (e.g., `wb.sheets['Sheet1'].range('A1').value`)
- **Macros:** Replace VBA macros with Python code, triggered from buttons or ribbon commands within Excel
- **User Defined Functions (UDFs):** Write custom Excel functions in Python (Windows only), with full support for NumPy arrays and pandas DataFrames
- **Named ranges:** Full read/write access to named ranges, a critical gap in most AI tools
- **Full object model:** Charts, pivot tables, conditional formatting, shapes, pictures, and workbook events

**Deployment Options:**

A common concern is distribution: colleagues need Python installed to run xlwings scripts. Two modern solutions address this:

- **xlwings Server:** Host the Python runtime centrally and expose endpoints. Users interact with Excel as normal; Python runs on a server. More technical to set up but centralises all dependencies.
- **xlwings Lite:** An Excel add-in that runs Python in the browser using Pyodide (WebAssembly). Runs locally in a sandboxed environment without sending data to the cloud. No installation required for end users.

The latest release (v0.33.20, January 2026) confirms active development, with multiple releases throughout 2025 and into 2026.

### 4.2 Monte Carlo Simulation

Monte Carlo simulation is a cornerstone technique in project evaluation, risk modelling, and financial forecasting. It quantifies uncertainty by running thousands of iterations with randomly sampled input variables, producing probability distributions of outcomes rather than single-point estimates.

**The Excel-Python Hybrid Approach:**

The most practical approach for finance teams is to keep the financial model in Excel (where stakeholders can review assumptions) and use Python for the simulation engine. xlwings provides the bridge:

1. Build the financial model in Excel (e.g., DCF, project NPV, EBITDA forecast) with clearly identified input assumptions
2. Use xlwings to connect Python to the workbook, reading assumption cells and writing results
3. Run the Monte Carlo simulation in Python using NumPy for random sampling across defined distributions (normal, triangular, uniform, log-normal, etc.)
4. For each iteration, write sampled inputs to Excel, trigger recalculation, and capture outputs
5. Analyse results in Python: histograms, percentile tables, tornado charts for sensitivity analysis, and probability of meeting threshold targets
6. Write summary results and charts back to a dedicated Excel output sheet, or render via Quarto

This approach has been documented by multiple finance education platforms and is used in practice for equity valuation, project finance feasibility, and portfolio risk modelling.

**R as an Alternative:**

R has excellent Monte Carlo capabilities, particularly through packages like mc2d (two-dimensional Monte Carlo for risk assessment), MCMCpack (Markov Chain Monte Carlo), and the base `sample()` and `replicate()` functions. R's strength lies in its statistical rigour and the depth of its distribution-fitting tools. For teams already using R, it is a strong choice. The results can be fed into Quarto reports alongside Python outputs.

### 4.3 Quarto: Automated, Reproducible Reporting

Quarto is an open-source publishing system from Posit (formerly RStudio). It takes documents containing a mix of markdown text and executable Python or R code, and renders them into polished PDFs, Word documents, HTML pages, presentations, dashboards, and books. All outputs are reproducible: re-running the document with updated data produces updated reports automatically.

**Why Quarto Replaces VBA-based Reporting:**

VBA-driven report generation is functional but fragile, difficult to maintain, and produces outputs that are hard to version-control. Quarto addresses every major pain point:

- **Parameterisation:** Define parameters (fiscal year, entity, scenario) in the document header. Render the same template multiple times with different values to produce customised reports for each business unit, period, or scenario.
- **Data integration:** Read directly from Excel files (via pandas/openpyxl or readxl in R), SQL databases, APIs, or CSV files. No manual copy-paste or VBA data-shuttling.
- **Professional formatting:** Templates control fonts, colours, headers, footers, and page layout. Outputs are publication-quality without manual formatting.
- **Version control:** Quarto documents are plain text (.qmd files), so they work with Git. Track changes to report logic over time, collaborate via pull requests, and maintain an audit trail.
- **Mixed language support:** Use Python and R in the same document. Run statistical analysis in R, data wrangling in Python, and combine into a single output.
- **Batch rendering:** A single command can render reports for all entities, all months, or all scenarios. One user replaced a 20-hour monthly VBA reporting process with a 10-minute Quarto pipeline.

**Practical Workflow Example:**

A typical monthly reporting workflow using Quarto might look like this:

1. xlwings script refreshes the Excel model with latest data from SQL/ERP
2. Quarto document reads the updated Excel file and any supplementary data sources
3. Python/R code blocks perform variance analysis, trend calculations, and chart generation
4. Quarto renders to PDF or Word, applying corporate templates
5. Parameterised rendering produces one report per business unit automatically
6. Outputs are saved to a shared drive or emailed automatically via a scheduling tool

---

## 5. Dual-Model Reconciliation: Excel as Source of Truth

The tools and workflows described in Sections 2–4 each address specific aspects of spreadsheet work. However, a more powerful architecture emerges when the financial model is built simultaneously in both Python and Excel, reconciled, and then used as the foundation for all downstream analytics and reporting. This section describes that approach, explains why it is particularly well-suited to the current toolset landscape, and outlines the practical workflow.

### 5.1 The Concept

In traditional project finance and DCF modelling, model audit is performed by having a second analyst rebuild the model independently. The dual-model approach applies the same principle using Python as the second analyst. The financial model is built in both Python (using pandas and NumPy) and Excel (using standard formulas and structure) from the same process, typically with AI assistance from Claude or similar tools. The two outputs are then reconciled cell-by-cell or section-by-section to verify logical consistency.

Once reconciliation is achieved, the two versions serve different purposes:

- **Excel becomes the sole source of truth for assumptions.** Stakeholders maintain, review, and challenge assumptions in a familiar spreadsheet environment. This is the auditable, version-controlled input layer.
- **Python becomes the analytical engine.** It reads assumption values from Excel (via xlwings or openpyxl) and performs all downstream computation: model recalculation, Monte Carlo simulation, sensitivity analysis, advanced visualisation, and statistical modelling.
- **Quarto produces the reports.** It pulls from both Excel (for assumption tables and summary outputs as stakeholders entered them) and Python (for analytical depth, simulation distributions, and charts), rendering everything into polished, parameterised documents.

### 5.2 Why This Architecture Works Now

This approach is not merely a theoretical ideal; it is a pragmatic response to the specific capabilities and limitations of the current toolset:

#### 5.2.1 AI Makes Dual-Model Construction Feasible

Building the same model in two languages was historically too time-consuming to be practical. AI assistants (Claude Chat, Claude Cowork, Claude Code) can now generate both the Excel formulas and the equivalent Python logic from a single set of requirements, dramatically reducing the effort. The AI can also assist with the reconciliation step itself, writing comparison scripts that flag discrepancies between the two outputs.

#### 5.2.2 Current AI Tools Cannot Replace VBA for Automation

As documented in Section 2, no AI tool can execute VBA, and most cannot interact with named ranges, data tables, or workbook events. By separating the model into an Excel assumption layer and a Python computation layer, the need for VBA-based automation is eliminated entirely. Python handles what VBA used to do (and more), without the limitations of the in-Excel AI tools.

#### 5.2.3 Python in Excel Is Not Enough on Its Own

Microsoft's Python in Excel (`=PY()`) is excellent for in-grid analytics but cannot access local files, call APIs, install custom packages, or interact with VBA. It also has monthly compute quotas that make large-scale Monte Carlo simulation impractical. By running Python externally (via xlwings or standalone scripts), these limitations are removed while Excel remains the user-facing interface.

#### 5.2.4 Reconciliation Provides Built-in Model Audit

The dual-model approach produces a verified model as a byproduct of the build process. In regulated environments or for investment-grade analysis, this is a significant advantage. The reconciliation script (a natural output of the build process) serves as a regression test that can be re-run whenever assumptions change, catching errors that would otherwise require manual review.

#### 5.2.5 Quarto Unifies Reporting from Multiple Sources

Previous approaches to automated reporting (typically VBA-driven) were fragile, difficult to maintain, and produced low-quality outputs. Quarto's ability to read from both Excel and Python in the same document means the report can show assumptions exactly as stakeholders entered them alongside analytical depth that Excel alone cannot produce. Parameterisation allows the same template to serve multiple projects, scenarios, or reporting periods.

### 5.3 Practical Workflow

The end-to-end workflow operates as follows:

- **Model construction:** Using AI assistance, build the financial model in both Python and Excel. The AI generates Excel formulas and equivalent Python (pandas/NumPy) logic from the same specification. This can be done iteratively, section by section (e.g., revenue build, operating costs, capital structure, cash flows, returns).
- **Reconciliation:** Run an automated reconciliation script that reads outputs from both the Excel and Python models, compares them within a defined tolerance (e.g., ±0.01), and flags discrepancies. Fix any differences until the two models agree. This script becomes a persistent regression test.
- **Assumption maintenance:** Stakeholders update assumptions in the Excel workbook. This is the only place assumptions are stored. Python reads them via xlwings or openpyxl at runtime. No hardcoded assumptions in Python.
- **Advanced analytics:** Python reads the current assumptions from Excel and runs Monte Carlo simulation (NumPy for random sampling across defined distributions), sensitivity analysis (tornado charts, spider plots), scenario comparison, and any statistical modelling required. Results are stored as pandas DataFrames and matplotlib/plotly figures.
- **Reporting:** Quarto reads from both sources. Assumption tables come from Excel (so stakeholders see their own inputs). Analytical outputs (probability distributions, sensitivity rankings, scenario comparisons, charts) come from Python. The Quarto template is parameterised by project, scenario, or period, allowing batch rendering.
- **Iteration:** When assumptions change, re-run the Python pipeline and Quarto render. The reconciliation test confirms the models still agree. New reports are produced automatically.

#### 5.3.1 Formula Change Detection

Value-level reconciliation can tell you that outputs differ and where they differ, but not necessarily why. If a stakeholder updates an assumption value in Excel, the reconciliation script will detect that both models now produce different outputs from the previous run, but they should still agree with each other once re-run with the updated values. The more difficult case is when someone edits a formula in Excel. The Python model retains the original logic, so it will produce the "correct" answer while the Excel model diverges. The reconciliation script flags the discrepancy but can only report "row 47, NPV differs by £2.3m" — it cannot explain that the depreciation formula was changed from straight-line to declining balance.

This is a genuine limitation of the architecture, but it can be addressed with a formula snapshot approach:

- **Baseline capture:** When the model is first built and reconciled, the Python script uses openpyxl (or xlwings) to export every formula string in the workbook — not the calculated values but the formula text itself (e.g., `=SUM(D10:D22)`, `=C15*Assumptions!B7`). This is stored as a baseline, typically a JSON file or pandas DataFrame, keyed by sheet name and cell reference.
- **Formula diff on failure:** When a value-level reconciliation fails, the script re-reads all formula strings from the current workbook, compares them to the stored baseline, and reports exactly which cells have changed formulas. This narrows the diagnosis from "something is different" to "cell G47 formula changed from `=D47/useful_life` to `=D47*(2/useful_life)`".
- **Implementation:** openpyxl can read formula strings from .xlsx files without needing Excel installed or COM access. For any cell, if the value attribute starts with `=`, it is a formula. Iterating through the used range and capturing these strings is straightforward. xlwings can also do this and additionally handles volatile functions and array formulas more reliably.
- **Ongoing use:** The formula snapshot should be updated each time a deliberate formula change is made and reconciled. It then serves as a formula-level regression test alongside the value-level reconciliation, catching both intentional and accidental formula edits.

This two-layer approach — value reconciliation plus formula snapshot — provides comprehensive change detection. Value differences are caught immediately; formula changes are identified and attributed to specific cells. Together, they approximate the rigour of a formal model audit process, automated and re-runnable on every iteration.

#### 5.3.2 PR Workflow and Changelog

The formula snapshot integrates naturally into a Git-based pull request workflow. When the reconciliation detects a formula change, the updated snapshot file (YAML or JSON) is committed. Because the snapshot is a text file, the resulting pull request shows a readable diff: "cell G47 changed from `=D47/useful_life` to `=D47*(2/useful_life)`". A reviewer can see exactly what moved, approve or reject the change, and the merge creates a changelog entry automatically. The reconciliation baseline is updated only after approval.

The practical flow is: a stakeholder edits the Excel model → the reconciliation script flags the discrepancy → the formula snapshot is re-exported → a PR is raised showing the formula diff → the change is reviewed and approved → the Python model is updated to match (or the Excel change is rejected) → the baseline is updated. In a CI/CD environment, the reconciliation can run automatically on every PR, ensuring that no formula change reaches the approved baseline without passing both value-level and formula-level checks.

#### 5.3.3 Version Control: Excel as Artifact, YAML as Source

A fundamental challenge with spreadsheet-based models is that .xlsx files are binary. Git can store them (providing rollback capability) but cannot meaningfully diff them. Two versions of the same workbook look identical in a Git log unless you open both and compare manually.

The architecture addresses this by treating the Excel file as a **build artifact** rather than a source file. The version-controlled "source" consists of text files that represent the model's specification:

- **Assumptions file (YAML):** All input assumptions, keyed by section and parameter name, with their cell locations in the workbook. When assumptions change, this file changes and the diff is human-readable. For example:

```yaml
revenue:
  capacity_mw: 150
  capacity_factor: 0.35
  ppa_price_mwh: 85.00
  escalation_pct: 0.025
```

- **Formula map (YAML or JSON):** Every formula string in the workbook, keyed by sheet name and cell reference. This is the formula snapshot described above, serving double duty as both a reconciliation baseline and a version-controlled specification.
- **Structure definition (YAML):** Sheet names, named ranges, cell mappings, and output locations. This defines the workbook's architecture independently of any particular set of values.
- **Python model code:** The equivalent computational logic, fully diffable and reviewable in any code review tool.

The Excel workbook can also be committed to Git (so a copy exists at every version), but the meaningful diffs happen on the text representations. A build script can generate a fresh Excel workbook from the YAML and Python sources, or validate that an existing workbook matches them. This gives you two paths: "generate Excel from spec" for new models, and "validate Excel against spec" for ongoing maintenance.

The result is that the model's logic, assumptions, and structure are all under proper version control with full diff and review capability, while stakeholders continue to interact with a standard Excel workbook. The governance happens in Git; the user experience stays in Excel.

### 5.4 Role of AI Throughout the Workflow

AI tools assist at multiple stages, but the architecture does not depend on any single AI product:

- **Model construction:** Claude Chat, Cowork, or Code can generate both Excel formulas and Python equivalents from natural language specifications. This is where AI delivers the largest time saving.
- **Reconciliation scripting:** AI can write the comparison/validation scripts that check Excel vs Python outputs.
- **Ongoing analysis:** Claude in Excel or Copilot Agent Mode can be used interactively for ad-hoc exploration of the Excel model. Python-side analysis can be assisted by AI for writing simulation code, chart formatting, or statistical tests.
- **Report authoring:** AI can help draft Quarto template narrative sections, interpret simulation results, and generate variance commentary.

Critically, the architecture remains fully functional without AI. The Excel model, Python scripts, reconciliation tests, and Quarto templates are all standard, auditable, version-controllable artefacts. AI accelerates the build and assists with analysis, but the outputs stand on their own.

---

## 6. Reference Architecture

The following architecture separates concerns so that each tool does what it is best at. Excel remains the front end for assumptions and stakeholder interaction; Python handles automation, simulation, and data transformation; Quarto handles reporting; and AI tools assist at every stage.

### 6.1 The Stack

| Layer | Tool | Role |
|---|---|---|
| Front end | Microsoft Excel | Assumption input, stakeholder review, ad-hoc analysis |
| Automation bridge | xlwings | Replace VBA: read/write Excel, trigger recalculations, named ranges |
| Analytics engine | Python (pandas, NumPy, scipy) and/or R | Monte Carlo simulation, statistical analysis, data transformation |
| In-grid analytics | Python in Excel (`=PY()`) | Embedded analytics and visualisation within the workbook |
| Cloud automation | Office Scripts + Power Automate | Scheduled, event-driven, cross-platform automation |
| AI assistance | Claude in Excel / Copilot Agent Mode | Formula generation, data exploration, model review |
| Reporting | Quarto | Parameterised, reproducible PDF/Word/HTML reports |
| Version control | Git | Track changes to Python scripts, Quarto templates, and configuration |

### 6.2 Getting Started

The architecture does not need to be adopted all at once. Each layer can be introduced independently:

- **Start with AI in-Excel:** Use Claude in Excel or Copilot Agent Mode for formula generation, model exploration, and ad-hoc analysis. No changes to existing workflows required.
- **Add Python alongside Excel:** Use xlwings to read from and write to existing workbooks. Start with a single model as a proof of concept.
- **Build the dual-model approach:** For a new model, generate both Excel and Python versions from the same specification using AI. Run reconciliation.
- **Introduce Quarto reporting:** Move one reporting process to Quarto as a proof of concept. Pick a report that would benefit from parameterisation and reproducibility.
- **Add Monte Carlo and advanced analytics:** Implement simulation and statistical modelling in Python or R, connected to the Excel model via xlwings.

### 6.3 Key Gaps to Watch

As of February 2026, several important gaps remain across all tools:

- **VBA execution:** No AI tool can execute VBA automatically within a workbook. All can generate VBA code as text, but the user must paste and run it manually.
- **Named ranges in AI tools:** Copilot Agent Mode can generate named ranges. Claude (all surfaces except Code with COM) and Gemini cannot. This is a significant gap for finance models.
- **Data tables (what-if analysis):** Not supported by any AI tool for in-place manipulation.
- **Copilot regional availability:** Agent Mode is not available in the EU or UK, which limits its usefulness for many organisations.
- **Python in Excel compute limits:** Monthly quotas can disrupt workflows, particularly for Monte Carlo simulations or large data processing tasks.
- **Office Scripts maturity:** Feature coverage does not yet match VBA, particularly around events, multi-workbook operations, and COM interop.

---

## 7. Skill Libraries: From Existing Models to Reusable AI Workflows

The financial plugins described in Section 2 are excellent at corporate finance — a `/dcf Apple` command builds a standard DCF from public market data in minutes. But finance covers a much broader territory than corporate valuations.

Consider a renewables project finance model. It requires a generation engine (installed capacity × full load hours × monthly production profile × availability step functions × cumulative degradation), a PPA waterfall allocating contracted and merchant generation across multiple offtake agreements, real-to-nominal price escalation, FAST-compliant corkscrew balances for debt, depreciation, tax losses, and retained earnings, and sector-specific integrity checks such as "does the generation profile sum to 100%" and "is the capacity factor within the expected range for this technology type." None of this exists in any plugin — it is a fundamentally different modelling discipline from corporate DCF.

This is where custom Claude skills fill the gap. A skill is a structured markdown document that encodes the assumptions framework, calculation methodology, compliance rules, and domain-specific checks for a particular model type. We have been building skill libraries organised by project type — one skill per domain (renewables, toll road, mining feasibility, etc.). The renewables skill, for example, runs to several hundred lines of detailed reference material covering generation engines, PPA revenue waterfalls, availability/degradation mechanics, and FAST standard rules with common pitfalls.

### 7.1 Building Skills from Existing Excel Models

The most promising approach for creating these skills is to start from the Excel models that every experienced modeller already has. The process:

1. **Feed the existing model to Claude Code** — Claude Code (the CLI tool) can read formulas, sheet structure, assumption layout, and calculation logic via COM-based libraries like xlwings or openpyxl. Other Claude surfaces (Chat, Cowork) read cell values only and cannot reconstruct formula logic — so this step specifically requires Claude Code or a Python script that exports the formula strings first.
2. **Claude generates the skill** — a SKILL.md capturing the methodology, assumptions framework, build sequence, compliance rules, and verification checks. The domain knowledge that was implicit in the spreadsheet becomes explicit and reusable.
3. **Pre-populate the formula YAML** — the formula map described in Section 5 can be extracted directly from the existing model, giving the skill concrete implementation patterns from day one.
4. **Add sector reference documents** — domain-specific assumptions, typical cost ranges, default profiles, and reasonableness checks that an experienced modeller carries in their head but rarely documents.

The old model becomes the training data; the skill becomes the reusable institutional knowledge. Each subsequent model built from that skill benefits from the accumulated methodology.

### 7.2 Where Plugins and Custom Skills Fit Together

| Domain | Plugin available? | Custom skill needed? |
|---|---|---|
| Corporate DCF (listed companies) | Yes — `/dcf [company]` | No (plugin sufficient for standard analysis) |
| Comparable company analysis | Yes — `/comps [company]` | No |
| LBO / leveraged buyout | Yes | No |
| 3-statement models from SEC filings | Yes | No |
| Renewables project finance (wind, solar, battery) | No | Yes — generation engine, PPA waterfall, FAST compliance |
| Toll road / transport concession | No | Yes — traffic modelling, concession structure |
| Mining / resources feasibility | No | Yes — reserve depletion, commodity pricing, processing |
| Real estate development | No | Yes — staging, absorption, lease-up |
| Data centre / infrastructure | No | Yes — power capacity, redundancy, tenant structure |

For corporate finance, start with the plugins. For specialist domains, build custom skills — ideally from your existing model library. The SEC DCF is a useful first step to prove the architecture; the real value emerges in specialist domains where no plugin exists and the modelling methodology lives in your team's institutional knowledge.

### 7.3 Studying the Plugin Skill Files

The plugin skill files themselves are worth studying regardless of whether you use the enterprise features. They are markdown files in a public GitHub repository ([anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins)), licensed under Apache 2.0. Reading how Anthropic has structured their DCF, comp analysis, and deal workflow skills provides a practical template for structuring your own domain-specific skills.

---

## 8. Conclusion

The AI tools have largely solved the model build problem. Claude's financial plugins, Copilot Agent Mode, and Claude in Excel make it remarkably fast to go from a specification to a finished, formatted workbook. That's a genuine step change.

The question for finance professionals is how to make best use of all these new building blocks together. The architecture described in this guide — Excel as the stakeholder-facing model, Python for advanced analytics and simulation, xlwings as the bridge, Quarto for reproducible reporting, and Git for governance — is designed to wrap around the AI-generated outputs and deliver the reuse, auditability, and analytical depth that serious modelling work requires.

Each layer can be adopted independently, and the benefits compound as more of the stack comes together. The building blocks are already in place.

---

## Sources & Further Reading

- [Microsoft: Python in Excel Availability](https://support.microsoft.com/en-us/office/python-in-excel-availability-781383e6-86b9-4156-84fb-93e786f7cab0)
- [Microsoft: Agent Mode in Excel](https://support.microsoft.com/en-us/office/agent-mode-in-excel-a2fd6fe4-97ac-416b-b89a-22f4d1357c7a)
- [Microsoft: Differences between Office Scripts and VBA](https://learn.microsoft.com/en-us/office/dev/scripts/resources/vba-differences)
- [Anthropic: Use Claude in Excel](https://support.claude.com/en/articles/12650343-use-claude-in-excel)
- [xlwings Documentation](https://docs.xlwings.org)
- [xlwings: My Thoughts on Python in Excel](https://www.xlwings.org/blog/my-thoughts-on-python-in-excel)
- [Quarto: Parameterized Reports with Python](https://quarto.org/docs/blog/posts/2025-07-24-parameterized-reports-python)
- [Posit: Building a Reporting Infrastructure with Quarto](https://posit.co/blog/building-a-reporting-infrastructure-with-quarto)
- [Analytics Vidhya: Monte Carlo Simulation in Excel with Python](https://www.analyticsvidhya.com/blog/2025/09/python-monte-carlo-simulation-in-excel)
- [PyXLL: Monte Carlo Simulations in Excel with Python](https://www.pyxll.com/blog/monte-carlo-simulations-in-excel-with-python)
- [FM Magazine: Introduction to Python in Excel](https://www.fm-magazine.com/issues/2026/jan/an-introduction-to-python-in-excel-part-1)
