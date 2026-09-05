# CLAUDE.md: Instructions for Claude Code in Project SYZYGY

You are operating within **SYZYGY**, the master multi-agent autonomous engineering framework.

## Operating Principles
1. **Spec First:** Whenever asked to build or refactor a project, first run `python syzygy.py init "<Name>" --domain <type>` to create `.spec/` with all 8 SDD files.
2. **Zero Slop:** Enforce ASD-STE100 technical precision. Ban words like "delve", "testament", "revolutionize", and "cutting-edge".
3. **OpenDesign Adherence:** UI generation must reference `design-systems/DESIGN.md` for exact colors, font stacks, and motion springs.
4. **Vector Slides Only:** Slide generation must use `core/presenter.py` to produce native editable vector `.pptx` files.

## Fast Commands
- Scaffold new project: `python syzygy.py init "ProjectName" --domain web`
- Query research index: `python syzygy.py research "Topic"`
- Generate presentation: `python syzygy.py deck "Title"`
- Run security audit: `python syzygy.py audit`
- Audit text quality: `python syzygy.py validate "Text"`
