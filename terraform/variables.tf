# variables.tf

variable "subscription_id" {
  description = "The subscription ID for the Azure account"
  type        = string
  default     = "f37377be-eabb-4797-a47d-abdb43ee66fa"
}

variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "mlops-dynamic-pricing-rg"
}

variable "location" {
  description = "Azure region where the resources will be created"
  type        = string
  default     = "East US"
}

variable "storage_account_name" {
  description = "Name of the storage account"
  type        = string
  default     = "dynmpricing"
}

variable "databricks_workspace_name" {
  description = "Name of the Databricks workspace"
  type        = string
  default     = "mlops-dynamic-pricing-databricks"
}

variable "ml_workspace_name" {
  description = "Name of the Azure Machine Learning workspace"
  type        = string
  default     = "mlops-dynamic-pricing-mlworkspace"
}
