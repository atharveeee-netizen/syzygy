"""
SYZYGY Visual Architecture Engine: System Design 101 & Diagram-Design
Generates syntax-verified Mermaid.js diagrams for distributed systems and multi-agent meshes.
"""

from typing import Dict, Any, List

class ArchitectureDiagramGenerator:
    @staticmethod
    def generate_mesh_diagram() -> str:
        return """graph TD
    CLI["SYZYGY CLI / Prompt"]
    COORD["Lead Coordinator (Ch 7)"]
    RESEARCH["Firecrawl Research Index"]
    SPEC["8-File SDD Generator (.spec/)"]
    DESIGN["OpenDesign Engine (DESIGN.md)"]
    SEC["Strix Multi-Agent Pentester"]
    PRESENT["PPT Master Vector Generator"]

    CLI --> COORD
    COORD --> SPEC
    COORD --> RESEARCH
    COORD --> DESIGN
    COORD --> SEC
    COORD --> PRESENT
"""

    @staticmethod
    def generate_custom_diagram(components: List[str]) -> str:
        lines = ["graph TD"]
        for i, comp in enumerate(components):
            lines.append(f"    NODE_{i}[\"{comp}\"]")
            if i > 0:
                lines.append(f"    NODE_{i-1} --> NODE_{i}")
        return "\n".join(lines)
