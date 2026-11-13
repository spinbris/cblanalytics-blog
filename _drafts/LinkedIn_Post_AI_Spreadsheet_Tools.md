# LinkedIn Post — Draft for Steve's review

---

**The Excel + Python + AI workflow nobody's talking about**

I've spent 20+ years building financial models in Excel and VBA. Recently I've been exploring how AI tools fit into that world — not as a replacement, but as a catalyst for a better architecture. What follows came out of a working conversation with Claude (Anthropic's AI), where we mapped the landscape and ended up designing something I think is genuinely useful.

**The problem we all know**

VBA has been the workhorse of Excel automation for decades. It works. But let's be honest: VBA-driven reporting is fragile, version control is painful, and debugging someone else's macro is nobody's idea of a good time. Meanwhile, every vendor is racing to put AI inside the spreadsheet — Copilot, Claude in Excel, Gemini in Sheets — but none of them can actually execute VBA, and most can't touch named ranges or data tables. We're in an awkward middle ground.

**What the AI tools can and can't do (Feb 2026)**

I asked Claude to help me map the actual capabilities across every tool I could find. The full comparison is in the document linked below, but the headline findings:

→ **Copilot Agent Mode** is the most Excel-native AI. It can generate named ranges, formulas, pivot tables, and charts — and you can now switch between GPT 5.2 and Claude Opus 4.5 as the underlying model. But it can't execute VBA, and it's not available in the EU/UK.

→ **Claude in Excel** reads your actual formulas and cell dependencies, can edit in-place, and has financial data connectors (S&P, FactSet, Pitchbook). But it's blind to VBA and named ranges.

→ **Python in Excel** (Microsoft's =PY() function) is excellent for in-grid analytics but has monthly compute quotas, can't access local files, and explicitly is not a VBA replacement.

→ **No AI tool can execute VBA.** All of them can write VBA code for you, but you're still the one pressing F5.

**The architecture that emerged**

The most interesting part of the conversation wasn't the tool comparison — it was what came after. We designed an architecture where:

1. The financial model is built simultaneously in **both Python and Excel**, with AI generating both versions from the same specification
2. The two models are **reconciled** automatically — essentially using Python as a second analyst, which gives you built-in model audit as a byproduct
3. **Excel becomes the sole source of truth for assumptions** — stakeholders maintain inputs in a familiar environment
4. **Python reads from Excel** (via xlwings) and handles everything Excel is bad at: Monte Carlo simulation, sensitivity analysis, advanced visualisation
5. **Quarto** pulls from both sources and renders parameterised, reproducible reports — replacing the worst part of VBA (reporting) with something maintainable

The key insight: this architecture exists *because* of the current limitations of AI tools. No AI can execute VBA? Fine — eliminate the need for VBA by separating the assumption layer (Excel) from the computation layer (Python). Python in Excel has compute quotas? Fine — run Python externally via xlwings. AI can't handle named ranges? Fine — xlwings can.

**The formula snapshot trick**

One problem we worked through: if someone edits a formula in the Excel model, the value-level reconciliation catches the discrepancy but can't explain *why*. The solution is a formula snapshot — when the model is first reconciled, export every formula string (not values) as a baseline. When reconciliation fails, diff the formulas against the baseline. You go from "NPV differs by £2.3m" to "cell G47 formula changed from straight-line to declining-balance depreciation." openpyxl can read formula strings without needing Excel installed.

That snapshot then feeds into a proper PR workflow. The formula diff shows up in a pull request as readable text — reviewers approve or reject the change, it gets a changelog entry, and the baseline updates only after approval. In a CI/CD setup, reconciliation runs automatically on every PR.

**Solving the "binary file in Git" problem**

The other thing we worked through: .xlsx files are binary, so Git can store them but can't diff them. The solution is to treat the Excel file as a *build artifact* rather than the source. The actual source — the thing you version-control and diff — is a set of YAML files: assumptions (keyed by parameter name), a formula map (every formula string keyed by cell reference), and a structure definition (sheet names, named ranges, cell mappings). These are text files, fully diffable, fully reviewable. The Excel workbook gets generated from them or validated against them. Stakeholders still work in Excel; governance happens in Git.

**For anyone thinking about this**

The migration doesn't need to be all-or-nothing. Start with Python in Excel for analytics you currently do with complex array formulas. Write your next automation task in xlwings instead of VBA. Move one painful report to Quarto. Build from there.

The full guide (17 pages, with comparison matrices and a step-by-step migration strategy) is linked below. It was genuinely co-produced — my domain knowledge, Claude's research and synthesis. I think this way of working with AI is more interesting than either "AI will replace us" or "AI is just autocomplete." It's a thinking partner, and the output is better than either of us would have produced alone.

---

*Written by Steve Parton in conversation with Claude (Anthropic) — February 2026*

#FinancialModelling #Excel #Python #AI #VBA #ProjectFinance #DCF #Quarto #xlwings #MonteCarlo #FinanceTransformation

---

**Notes for Steve:**
- LinkedIn's long-form limit is ~3,000 characters for regular posts. This draft is ~3,500 words which is well suited for a LinkedIn **article** (no character limit) rather than a standard post. If you want a shorter standard post, I can cut it down to the hook + key findings + link.
- You'll need to upload the document somewhere accessible (your own site, a public Google Drive link, or a LinkedIn article attachment) and add the link where it says "linked below."
- Feel free to edit the tone — I've tried to match a professional-but-accessible LinkedIn voice, but you know your audience better than I do.
