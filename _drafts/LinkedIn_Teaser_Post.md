The hardest part of financial modelling with or without AI was always the build. That problem just got largely solved.

Anthropic released open source financial modelling plugins for Claude this week — DCF models, comp analysis, LBO, 3-statement financials, all as fully functional Excel workbooks with live formulas and industry-standard formatting. They're squarely aimed at corporate finance, and they're impressive. It will be interesting to see whether Anthropic extends into other domains, or whether practitioners build their own from the example provided.

Either way, for anyone doing serious work across multiple entities and over time, the build is the starting point, not the finish line. The model lives in Excel — stakeholders maintain assumptions there, and it remains a fully operational, auditable workbook and the key quantitative output. But Python sits alongside it, reading from and writing to the same workbook via xlwings, handling what spreadsheets aren't built for. Here's what I've been prototyping around that two-way connection:
 
→ Simulation and sensitivity analysis that Excel can't do at scale — Python runs Monte Carlo across thousands of iterations, reads assumptions from the workbook and writes results back (no AI tool currently handles data tables or in-workbook simulation)
→ Parameterised, reproducible reports that pull from both Excel and Python as required, report authoring and additional analytics/viz in quarto if required.
→ Assumptions and formulas exported to YAML in Git — the spreadsheet looks the same as it ever did, stakeholders still work in Excel, but the model's logic now lives in version-controlled text files that anyone can review
→ Python independently recalculates every output from the same assumptions and reconciles against Excel — every value, every cell. Differences are flagged automatically, formula strings are diffed against a validated baseline, and nothing changes without explanation. You go from "NPV is off by £2m" to "cell G47 changed from straight-line to declining-balance depreciation." The diff goes into a pull request, a reviewer approves or rejects, the changelog updates only after sign-off. Every change documented, every change deliberate. All automated, so largely transaparent to the user. 

The question now is how to make best use of all these building blocks together — the plugins, Claude in Excel, Claude Code, xlwings, Quarto — into a workflow that handles reuse, governance, advanced analytics, and reporting at scale.

Full writeup on the blog with a reference guide covering the architecture and toolset: https://blog.cblanalytics.com/posts/2026-02-25-A-New-Methodology/

Also, the Anthropic plugin skill files themselves are worth studying even without the enterprise data subscriptions — Anthropic's methodology for structuring DCF and comp analysis workflows is instructive. They're just markdown files in a public GitHub repo which we can all read and learn from.

#FinancialModelling #AI #Excel #Python #VibeAnalytics #Claude
