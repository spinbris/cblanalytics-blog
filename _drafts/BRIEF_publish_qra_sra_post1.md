# Brief — Publish QRA/SRA Post 1 (Tropic Ridge)

**Date:** [fill with real date — run `Get-Date -Format "dddd dd/MM/yyyy HH:mm"` first,
do not take it from the session clock, per Steve's standing dating rule]
**Hat:** PM (drafted in Cowork), for Builder (CLI) to execute.
**Repo:** cblanalytics-blog

## Context

Three draft variants of the QRA/SRA showcase post exist, none currently live:

1. `posts/2026-06-05-vibe-analytics-risk-platform/index.qmd` — original, real-client
   identifying detail (gas infrastructure project, dates, activity counts). DO NOT
   touch, DO NOT publish. Left in place as history per the recast brief.
2. `posts/2026-07-04-risk-platform-own-machine/index.qmd` — Post A per
   `BLOG_RECAST_brief.md`, full 165-line draft, synthetic numbers, `draft: true`.
   Six unfilled image slots (`SHOTLIST.md` alongside it).
3. `posts/_working_consolidated_showcase/POST_1_DRAFTa.qmd` — newest, most developed.
   Real verified Tropic Ridge figures ($50M farm, 171 activities, 35 risks, joint
   P80 $6.84M), EMV cross-check, two-engine schedule validation, the join-not-add
   hero beat, full closing + bio. `draft: true`, placeholder date `2026-07-XX`.
   `SALVAGE_INVENTORY.md` in the same folder documents what was merged in from
   drafts 1 and 2 — its flagged issues (test-count conflict, unverified
   "eight dual-coded risks" figure) do NOT appear in this version, so treat them
   as resolved, not outstanding.

**Title CONFIRMED by Director 06/08/2026:** "Pricing Construction Risk - QRA and
SRA analytics, with Claude's help" (DRAFTa's title). Content source is
`POST_1_DRAFTa.qmd`. No further title decision needed — proceed.

## The problem

The blog's listing (`index.qmd`) globs `posts/*/index.qmd`. `POST_1_DRAFTa.qmd`
doesn't match that pattern — wrong filename, wrong folder. Flipping `draft: false`
in place would do nothing visible on the live site.

## What to do

1. Create `posts/<real-date>-tropic-ridge-qra-sra/` (or better slug — Director's
   call on the exact slug, keep it short and matching the site's existing
   `posts/YYYY-MM-DD-slug/` convention).
2. Copy `POST_1_DRAFTa.qmd` content into `index.qmd` inside that new folder.
3. Frontmatter: `draft: false`, real date (not the placeholder), confirm title
   per the Director decision above, keep `author: "Stephen Parton"`.
4. Leave the three `<!-- IMG SLOT -->` comments as-is — they're HTML comments,
   invisible in rendered output, not broken image tags. Images are a later pass.
5. Run `quarto render` locally. Confirm the new post builds clean and appears in
   `_site/posts/`. Spot-check the rendered HTML for the join-not-add table
   (markdown tables can misrender) and the two P80 figures reading correctly.
6. Do not delete or edit the two older draft files (2026-06-05 and 2026-07-04) —
   leave as history per the recast brief's own instruction.
7. Commit, push to `main`. GitHub Actions (`publish.yml`) auto-deploys — no
   manual step after push.
8. Report back the live URL (`https://blog.cblanalytics.com/posts/<slug>/`) —
   this is needed for the companion site brief (`BRIEF_add_tropic_ridge_page.md`
   in the `cblanalytics-site` repo), which links to it.

## Not in scope for this brief

- Image capture (SHOTLIST.md work) — separate pass, gated on REG01 register
  consolidation per Blog Pipeline STATUS.md.
- The LinkedIn cut-down — comes after this is live and has had a polish pass,
  not from this brief.
- Post 2 (active management) — mentioned in this post's closing line ("is the
  next post") but not drafted yet.

## Known repo hygiene note, not blocking

`CLAUDE.md` in this repo still describes the OneDrive vault path and Mac Mini as
primary device — both stale since the June 2026 Google Drive migration. Worth a
correction pass sometime, not part of this brief.
