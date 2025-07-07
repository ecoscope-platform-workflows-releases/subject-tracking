data "google_pubsub_topic" "workflow_topic" {
  name    = startswith(var.env, "dev-preview") ? "workflow-requests-${var.env}" : "workflow-requests"
  project = var.project_id
}

data "google_pubsub_topic" "workflow_topic_dlq" {
  name    = startswith(var.env, "dev-preview") ? "workflow-requests-dead-letter-${var.env}" :  "workflow-requests-dead-letter"
  project = var.project_id
}

resource "google_pubsub_subscription" "run_from_pubsub" {
  name    = "${var.application_name}-sub-${var.env}"
  project = var.project_id
  topic   = data.google_pubsub_topic.workflow_topic.name

  filter = "hasPrefix(attributes.workflow_name, \"${replace(var.application_name, "workflow-", "")}\")"

  push_config {
    push_endpoint = "${google_cloud_run_v2_service.default.uri}/run-from-pubsub"

    oidc_token {
      service_account_email = google_service_account.default.email
    }
  }

  ack_deadline_seconds    = 600
  enable_message_ordering = false

  expiration_policy {
    ttl = ""
  }

  retry_policy {
    minimum_backoff = "10s"
    maximum_backoff = "600s"
  }

  dead_letter_policy {
    dead_letter_topic     = data.google_pubsub_topic.workflow_topic_dlq.id
    max_delivery_attempts = 5
  }
}