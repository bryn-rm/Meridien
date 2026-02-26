resource "google_cloud_run_v2_service" "orchestrator" {
  name     = "orchestrator-agent"
  location = var.region

  template {
    containers {
      image = "us-central1-docker.pkg.dev/${var.project_id}/meridian/orchestrator:latest"
      ports { container_port = 8000 }
    }
  }
}
