terraform {
  source = "../../modules"
}

remote_state {
  backend = "gcs"
  config = {
    bucket   = "ecoscope-tf-state"
    prefix   = "workflow-subject-tracking/dev-preview-##PREVIEW_NAME/terraform.tfstate"
    project  = "ecoscope-poc-421907"
    location = "us"
  }
}


inputs = {
  image = "" # Override at pipeline level

  project_id                         = "ecoscope-poc-421907"
  env                                = "dev-preview-##PREVIEW_NAME"
  network_name                       = "ecoscope-dev"
  service_url                        = "subject-tracking.dev-preview-##PREVIEW_NAME.ecoscope.io"
  workflows_services_custom_audience = "ecoscope-workflows-services-dev-preview-##PREVIEW_NAME"
  workflows_results_bucket           = "ecoscope-workflows-results-dev-preview-##PREVIEW_NAME"
}
