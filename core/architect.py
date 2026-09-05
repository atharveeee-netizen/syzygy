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
            "jetson_nano": {"max_ram_mb": 4000, "recommended_framework": "TensorRT-LLM", "quantization": "FP16"},
            "apple_m2": {"max_ram_mb": 24000, "recommended_framework": "MLX", "quantization": "4-bit"},
            "generic_x86": {"max_ram_mb": 16000, "recommended_framework": "Ollama / llama.cpp", "quantization": "Q4_K_M"},
            "cloud_h100": {"max_ram_mb": 80000, "recommended_framework": "vLLM", "quantization": "BF16 or FP8"}
        }

    def judge_architecture(self, task_description: str) -> dict:
        """Analyzes the task to prevent deploying massive models on edge devices."""
        print(f"\n--- AI ARCHITECT ENGINE INITIALIZED ---")
        print(f"Task: {task_description}")
        
        task_lower = task_description.lower()
        
        # Heuristic constraint solver
        target_hardware = "generic_x86" # Default
        if any(kw in task_lower for kw in ["esp32", "microcontroller", "arduino"]):
            target_hardware = "esp32"
        elif any(kw in task_lower for kw in ["raspberry pi", "rpi"]):
            target_hardware = "raspberry_pi_4"
        elif any(kw in task_lower for kw in ["jetson", "nvidia tegra"]):
            target_hardware = "jetson_nano"
        elif any(kw in task_lower for kw in ["macbook", "m1", "m2", "m3", "apple silicon"]):
            target_hardware = "apple_m2"
        elif any(kw in task_lower for kw in ["cloud", "server", "h100", "a100", "gpu cluster"]):
            target_hardware = "cloud_h100"
            
        specs = self.hardware_matrix[target_hardware]
        
        # Determine verdict based on constraints
        if specs["max_ram_mb"] < 1000:
            verdict = "CRITICAL LIMIT: Do NOT deploy deep ML models here. Use the recommended micro-framework."
        elif specs["max_ram_mb"] < 10000:
            verdict = "EDGE LIMIT: Use highly quantized models (e.g. 4-bit) that fit in RAM."
        else:
            verdict = "CAPABLE: Hardware can support larger, unquantized or lightly quantized models."

        decision = {
            "target_hardware": target_hardware.upper(),
            "max_ram_mb": specs['max_ram_mb'],
            "recommended_framework": specs['recommended_framework'],
            "quantization": specs['quantization'],
            "verdict": verdict
        }

        import json
        print(json.dumps(decision, indent=2))
        print("--- AI ARCHITECT COMPLETE ---\n")
        
        return decision
