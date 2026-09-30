variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "production-cicd-devops"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "production"
}