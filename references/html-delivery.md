# HTML Delivery and Verification

Use when the user requests an HTML journey, contract report, prompt specification, or architecture report.

## Artifact requirements

- Produce one standalone HTML file unless the user requests a site bundle.
- Use semantic headings, a visible evidence legend, a sticky or compact section navigator, responsive cards and tables, and printable colors.
- Keep long evidence text readable with wrapping; make wide tables horizontally scrollable.
- Use local clickable links for screenshots and prior artifacts when available.
- Put the evidence class and IDs adjacent to claims. Do not rely on color alone.
- Include an explicit scope/gaps section and a final unknowns section.
- Do not embed credentials, private identifiers, raw browser state, or hidden metadata.

## Diagram requirements

- Mermaid is suitable for journeys, state machines, ER diagrams, sequences, data flows, and layered architecture.
- Give every decision branch an explicit condition.
- Label edges with semantic actions rather than unlabeled arrows.
- Add evidence IDs inside important nodes or in an adjacent trace table.
- Provide a legend for confirmed, inferred, recommended, risk, and unknown styles.
- Keep source text copyable when useful.

If the report must work fully offline, bundle Mermaid locally or render diagrams to SVG during generation. If a CDN script is used, disclose that diagrams require network access while the tables and text remain available.

## Local verification

After writing the file:

1. Serve it from a local HTTP server when browser security or module loading makes `file://` unreliable.
2. Load it in a browser and wait for diagram rendering.
3. Verify title, section count, navigation, table overflow, and all Mermaid SVGs.
4. Check browser console errors.
5. Inspect at least one desktop viewport and one narrow viewport for overflow.
6. Click only local report controls; do not use verification as authorization to mutate the product under study.
7. Fix errors and repeat until the artifact is stable.

## Template use

[report-template.html](../assets/report-template.html) is a lightweight shell. Copy and adapt it; replace all bracketed placeholders, delete unused sections, and preserve the evidence legend and verification note. It is not evidence and should never be cited as product behavior.
