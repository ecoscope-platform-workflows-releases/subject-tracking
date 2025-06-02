resource "google_cloud_run_v2_service" "default" {
  name     = "${var.application}-${var.env}"
  project  = var.project_id
  location = var.location
  ingress  = var.ingress

  custom_audiences = [
    var.workflows_services_custom_audience
  ]

  template {
    service_account                  = google_service_account.default.email
    max_instance_request_concurrency = var.max_instance_request_concurrency
    timeout = "${var.timeout}s"

    scaling {
      min_instance_count = var.min_instance_count
      max_instance_count = var.max_instance_count
    }

    vpc_access {
      egress = "ALL_TRAFFIC"
      network_interfaces {
        network    = var.network_name
        subnetwork = var.subnet
      }
    }

    containers {
      image = var.image

      resources {
        limits            = var.limits
        cpu_idle          = true
        startup_cpu_boost = true
      }

      env {
        name  = "WORKFLOW_RESULTS_ROOT_PATH"
        value = var.workflows_results_bucket
      }
      
      env {
        name = "UVICORN_TIMEOUT"
        value = var.timeout
      }
    }
  }
  depends_on = [
    google_service_account_iam_member.gha-sa-user,
    google_project_iam_member.serviceAgent
  ]
}

data "google_dns_managed_zone" "ecoscope" {
  name = var.dns_config_name
}

resource "google_dns_record_set" "cname" {
  count        = startswith(var.env, "dev-preview") ? 1 : 0
  name         = var.service_url
  managed_zone = data.google_dns_managed_zone.ecoscope.name
  type         = "CNAME"
  ttl          = 300
  rrdatas      = ["ghs.googlehosted.com."]
}

resource "google_cloud_run_domain_mapping" "default" {
  location = var.location
  name     = var.service_url
  project  = var.project_id

  metadata {
    namespace = var.project_id
  }

  spec {
    route_name = google_cloud_run_v2_service.default.name
  }

  depends_on = [ google_dns_record_set.cname ]
}
