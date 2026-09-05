"""
OpenTelemetryAgent
Domain: Observability & Distributed Tracing
Stack: OpenTelemetry + Prometheus / Grafana
"""
import logging
import os

logger = logging.getLogger("SYZYGY.OpenTelemetryAgent")

class OpenTelemetryAgent:
    def __init__(self):
        logger.info("Initializing OpenTelemetryAgent for Tracing & Metrics.")

    def run(self, task):
        project_dir = task.get("project_dir", ".")
        logger.info(f"Scaffolding OpenTelemetry instrumentation in {project_dir}")
        
        telemetry_path = os.path.join(project_dir, "instrumentation.ts")
        telemetry_content = """// OpenTelemetry Distributed Tracing Instrumentation
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
            
        logger.info(f"Generated OpenTelemetry instrumentation at {telemetry_path}")
        return {"status": "SUCCESS", "module": "telemetry", "files": [telemetry_path]}
