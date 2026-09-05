class AIArchitectAgent:
    """
    Hardware-Aware AI Architect (ArchitectAgent).
    Evaluates deployment constraints (e.g., target hardware, memory limits) and dictates 
    the optimal model architecture, quantization, and software framework.
    """

    def __init__(self):
        # A matrix defining limits for different hardware targets
        self.hardware_matrix = {
            "esp32": {"max_ram_mb": 4, "recommended_framework": "TensorFlow Lite Micro", "quantization": "INT8"},
            "raspberry_pi_4": {"max_ram_mb": 8000, "recommended_framework": "llama.cpp", "quantization": "Q4_K_M"},
            "cloud_h100": {"max_ram_mb": 80000, "recommended_framework": "vLLM", "quantization": "BF16 or FP8"}
        }

    def judge_architecture(self, task_description):
        """Analyzes the task to prevent deploying massive models on edge devices."""
        print(f"\n--- AI ARCHITECT ENGINE INITIALIZED ---")
        print(f"Task: {task_description}")
        
        task_lower = task_description.lower()
        
        # Simple heuristic constraint solver (can be replaced with LLM logic)
        target_hardware = "unknown"
        if "esp32" in task_lower or "microcontroller" in task_lower:
            target_hardware = "esp32"
        elif "raspberry pi" in task_lower or "rpi" in task_lower:
            target_hardware = "raspberry_pi_4"
        elif "cloud" in task_lower or "server" in task_lower:
            target_hardware = "cloud_h100"
            
        if target_hardware in self.hardware_matrix:
            specs = self.hardware_matrix[target_hardware]
            decision = (
                f"HARDWARE TARGET: {target_hardware.upper()}\n"
                f"-> Max RAM: {specs['max_ram_mb']} MB\n"
                f"-> Framework: {specs['recommended_framework']}\n"
                f"-> Quantization: {specs['quantization']}\n"
                f"VERDICT: Do NOT deploy deep ML models here. Use the recommended framework."
            )
        else:
            decision = "Hardware target ambiguous. Defaulting to general lightweight model (Q4 quantization)."

        print(decision)
        print("--- AI ARCHITECT COMPLETE ---\n")
        
        return decision
