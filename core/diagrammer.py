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
    
    subgraph Research
        RESEARCH["Firecrawl Research Index"]
    end
    
    subgraph Design & Verification
        SPEC["8-File SDD Generator (.spec/)"]
        DESIGN["OpenDesign Engine (DESIGN.md)"]
        SEC["Strix Multi-Agent Pentester"]
        PRESENT["PPT Master Vector Generator"]
    end

    CLI --> COORD
    COORD --> SPEC
    COORD --> RESEARCH
    COORD --> DESIGN
    COORD --> SEC
    COORD --> PRESENT
"""

    @staticmethod
    def generate_custom_diagram(graph_type: str = "TD", 
                                nodes: List[Dict[str, str]] = None, 
                                edges: List[Dict[str, str]] = None,
                                subgraphs: Dict[str, List[str]] = None) -> str:
        """
        Generates a flexible Mermaid diagram supporting subgraphs, bidirectional edges, and labels.
        nodes: [{"id": "A", "label": "Node A"}, ...]
        edges: [{"from": "A", "to": "B", "label": "Optional Label", "type": "-->"}, ...]
        subgraphs: {"Subgraph Name": ["A", "B"]}
        """
        nodes = nodes or []
        edges = edges or []
        subgraphs = subgraphs or {}
        
        lines = [f"graph {graph_type}"]
        
        # Track which nodes are in subgraphs
        in_subgraph = set()
        
        for sg_name, sg_nodes in subgraphs.items():
            lines.append(f"    subgraph {sg_name.replace(' ', '_')} [\"{sg_name}\"]")
            for node_id in sg_nodes:
                in_subgraph.add(node_id)
                # Find label
                label = next((n['label'] for n in nodes if n['id'] == node_id), node_id)
                lines.append(f"        {node_id}[\"{label}\"]")
            lines.append("    end")
            
        # Add remaining nodes not in subgraphs
        for node in nodes:
            if node['id'] not in in_subgraph:
                lines.append(f"    {node['id']}[\"{node['label']}\"]")
                
        # Add edges
        for edge in edges:
            edge_type = edge.get("type", "-->")
            label = edge.get("label", "")
            if label:
                lines.append(f"    {edge['from']} {edge_type}|\"{label}\"| {edge['to']}")
            else:
                lines.append(f"    {edge['from']} {edge_type} {edge['to']}")
                
        return "\n".join(lines)


class CanonicalImageHarness:
    """
    SYZYGY Canonical Technical Image Generation Engine.
    Enforces pure white (#ffffff) canvas, physical BOM silicon anchoring,
    zero-paragraph/zero-bullet constraints, and reference style conditioning.
    """
    CANONICAL_PALETTE = {
        "bg": "#ffffff",
        "lines": "#0f172a",
        "primary": "#0284c7",
        "success": "#16a34a",
        "warning": "#d97706",
        "alert": "#e11d48",
        "box_fill": "#f8fafc",
        "box_border": "#cbd5e1"
    }

    @staticmethod
    def build_canonical_prompt(title: str,
                               system_name: str,
                               diagram_type: str,
                               sections: List[Dict[str, Any]],
                               scorecard: List[str] = None) -> str:
        """
        Builds a verified, zero-AI-slop technical prompt for DeepMind Imagen 3.
        Mandates pure white canvas, explicit silicon part numbers, and no text walls.
        """
        prompt_lines = [
            f"High-resolution technical engineering {diagram_type} for {system_name}: '{title}' on pure white background (#ffffff).",
            "Modern clean IEEE engineering publication style with crisp black linework, pastel engineering fills, component illustrations, circuit chips, waveforms, and directional data arrows.",
            "Strictly pictorial schematic and flowchart format. Absolutely NO paragraphs and NO bullet point lists."
        ]

        for sec in sections:
            prompt_lines.append(f"\n{sec.get('heading', 'Subsystem Layer')}:")
            for item in sec.get('items', []):
                prompt_lines.append(f"- {item}")

        if scorecard:
            prompt_lines.append("\nVisual Scorecard Strip:")
            for sc in scorecard:
                prompt_lines.append(f"- {sc}")

        prompt_lines.append(
            "\nStyle: Clean technical IEEE whitepaper graphic, pure white canvas (#ffffff), dark technical lines, sharp vector iconography, zero decorative AI slop, zero text paragraphs, zero bullet lists."
        )

        return "\n".join(prompt_lines)

