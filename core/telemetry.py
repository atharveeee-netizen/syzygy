"""
ScaffoldTelemetryAgent
Domain: Observability & Distributed Tracing Boilerplate
Note: This is a SCAFFOLDING tool. It generates boilerplate for OpenTelemetry.
"""
import logging
import os

logger = logging.getLogger("SYZYGY.ScaffoldTelemetryAgent")

class ScaffoldTelemetryAgent:
    def __init__(self):
        logger.info("Initializing ScaffoldTelemetryAgent for Tracing & Metrics boilerplate.")

    def run(self, task):
        project_dir = task.get("project_dir", ".")
        language = task.get("language", "typescript").lower()
        logger.info(f"Scaffolding OpenTelemetry instrumentation for {language} in {project_dir}")
        
        if language == "python":
             telemetry_path = os.path.join(project_dir, "telemetry.py")
             telemetry_content = """# SYZYGY OpenTelemetry Boilerplate (Python)
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

def setup_telemetry(service_name: str = "syzygy-app"):
    provider = TracerProvider()
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
    return trace.get_tracer(service_name)
"""
        else: # Default typescript
             telemetry_path = os.path.join(project_dir, "instrumentation.ts")
             telemetry_content = """// SYZYGY OpenTelemetry Boilerplate (Node.js/Next.js)
import { registerOTel } from '@vercel/otel';

export function register() {
  registerOTel({
    serviceName: process.env.OTEL_SERVICE_NAME || 'syzygy-app',
    attributes: {
      'deployment.environment': process.env.NODE_ENV || 'development',
    },
  });
}
"""
        with open(telemetry_path, "w", encoding="utf-8") as f:
            f.write(telemetry_content)
            
        logger.info(f"Generated OpenTelemetry boilerplate at {telemetry_path}")
        return {"status": "SUCCESS", "module": "telemetry", "files": [telemetry_path]}
