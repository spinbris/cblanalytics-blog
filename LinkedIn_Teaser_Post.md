Anthropic released open source financial modelling plugins for Claude this week. The DCF plugin builds a fully functional Excel workbook — live formulas, sensitivity tables, industry-standard formatting — from a single command. It's impressive.

But for anyone doing serious work across multiple entities and over time, the build is the starting point, not the finish line.

What wraps around it?

→ Python via xlwings for Monte Carlo simulation, sensitivity analysis, and analytics Excel can't do (no AI tool currently handles data tables or in-workbook simulation at scale)
→ Quarto for parameterised, reproducible reports that pull from both Excel and Python — one template, multiple entities
→ A formula snapshot that diffs every formula string against a baseline, so when something changes you know exactly which cell and how
→ YAML-as-source for assumptions and formulas in Git — stakeholders work in Excel, governance happens in text

The plugins have largely solved the build problem. The question now is how to make best use of all these new building blocks together — the plugins, Claude in Excel, Claude Code, xlwings, Quarto — into a workflow that handles reuse, governance, advanced analytics, and reporting at scale.

That's what I've been prototyping. Full writeup on the blog with a reference guide covering the architecture and toolset: [LINK]

The plugin skill files themselves are worth studying even without the enterprise data subscriptions — Anthropic's methodology for structuring DCF and comp analysis workflows is instructive. They're just markdown files in a public GitHub repo.

#FinancialModelling #AI #Excel #Python #VibeAnalytics #Claude
