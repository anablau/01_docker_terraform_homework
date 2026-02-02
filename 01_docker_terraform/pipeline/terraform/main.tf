terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project     = var.project
  region      = "us-central1"
  credentials = file(var.credentials_file)
}

variable "project" {}

variable "credentials_file" {
  default = "/Users/i752501/Documents/GitHub/01_docker_terraform_homework/pipeline/terraform/service-key.json"
}

resource "random_id" "bucket_id" {
  byte_length = 4
}

resource "google_storage_bucket" "test_bucket" {
  name     = "tf-test-bucket-${random_id.bucket_id.hex}"
  location = "US"
}
