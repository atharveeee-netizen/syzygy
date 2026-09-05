import sys
import os

sys.path.insert(0, os.path.abspath("."))

from core import (
    OrchestratorEngine,
    OpenVikingClient,
    FirecrawlResearchIndex,
    PPTMasterDeckGenerator,
    ArchitectureDiagramGenerator,
    StrixPentestAgent,
    STE100Validator,
    AIMLEngineAgent,
    ReconEngineAgent,
    AIArchitectAgent,
    HackathonStrategistAgent,
    ScaffoldCryptoAgent,
    ScaffoldAuthAgent,
    ScaffoldTelemetryAgent,
    GitHubActionsAgent,
    ProjectSynthesizer
)

def test_all():
    print("1. Testing Memory persistence...")
    mem = OpenVikingClient()
    mem.put("viking://health_check", {"status": "ok", "db": "sqlite"})
    val = mem.get("viking://health_check")
    assert val and val.get("payload", {}).get("status") == "ok", f"Memory failed: {val}"
    print("   Memory OK:", val["payload"])

    print("2. Testing Pentest failure mode...")
    pt = StrixPentestAgent()
    res = pt.run({"target": "http://localhost:3000"})
    print("   Pentest result:", res)
    assert res.get("status") in ["FAILED", "SUCCESS"], f"Invalid status: {res}"

    print("3. Testing arXiv Research API...")
    res_agent = FirecrawlResearchIndex()
    papers = res_agent.search_and_extract("multi-agent consensus", max_papers=2)
    print(f"   arXiv query returned {len(papers)} papers.")
    if papers:
        print(f"   First paper: {papers[0].get('title')} ({papers[0].get('url')})")

    print("4. Testing ReconEngine (GitHub API)...")
    recon = ReconEngineAgent()
    gh_repos = recon.search_github("agentic design patterns", max_results=2)
    print(f"   GitHub query returned {len(gh_repos)} repos.")
    if gh_repos:
        print(f"   Top repo: {gh_repos[0].get('repo')} ({gh_repos[0].get('stars')} stars)")

    print("5. Testing Architect...")
    arch = AIArchitectAgent()
    decision = arch.judge_architecture("Build an autonomous agent for Jetson Nano edge robot")
    print(f"   Architect target: {decision.get('target_hardware')}, framework: {decision.get('recommended_framework')}")
    assert decision.get("target_hardware") == "JETSON_NANO"

    print("6. Testing Diagrammer...")
    diag = ArchitectureDiagramGenerator.generate_mesh_diagram()
    assert "graph TD" in diag and "subgraph Research" in diag
    print("   Diagram syntax verified!")

    print("7. Testing Master ProjectSynthesizer...")
    import shutil
    synth = ProjectSynthesizer()
    syn_res = synth.synthesize("Build real-time drone telemetry system on Jetson Nano", target_dir="./tmp_test_synth")
    assert syn_res["status"] == "SUCCESS", "Synthesis failed"
    assert len(syn_res["activated_agents"]) >= 7, f"Expected >= 7 agents, got {len(syn_res['activated_agents'])}"
    print(f"   Synthesizer OK! Activated {len(syn_res['activated_agents'])} agents dynamically.")
    shutil.rmtree("./tmp_test_synth", ignore_errors=True)

    print("\n>>> ALL VERIFICATION CHECKS PASSED SUCCESSFULLY! <<<")

if __name__ == "__main__":
    test_all()
