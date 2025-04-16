variable "name" {
  description = "Name of the module"
  type        = string
}

output "name" {
  value = var.name
}
