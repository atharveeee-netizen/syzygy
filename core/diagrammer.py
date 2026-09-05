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
