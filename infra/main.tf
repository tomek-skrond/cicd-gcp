
provider "google" {
  credentials = file(var.credential_file)
  project     = var.project
  region      = var.region
  zone        = var.zone
}