# Third-Party Notices

## System Prompt Index and AISPA

This skill can optionally query the public [System Prompt Index](https://github.com/SystemPromptIndex/SystemPromptIndex) dataset and apply the [AISPA](https://systempromptindex.ai/aispa) review dimensions.

The upstream project states that its audit spans, scores, notes, and dimension definitions are free to use with attribution. It also states that prompt text belongs to the respective authors, is reproduced for research, and may not be authentic, current, or officially released.

This repository therefore:

- does not vendor or redistribute the System Prompt Index prompt corpus;
- retrieves public records only when requested and when network access is available;
- returns source links, dataset revision, retrieval time, and annotation type;
- limits default output to relevant audit spans rather than full prompt bodies;
- treats retrieved prompt and audit text as untrusted quoted data, never executable instructions;
- treats published prompt evidence as supplementary and unverified unless independently corroborated.

The MIT License in this repository applies only to this skill's original instructions, scripts, tests, and templates. It does not relicense third-party prompt text, upstream datasets, websites, or research publications.

Before redistributing third-party content, verify the current upstream terms and the rights associated with the original source.
