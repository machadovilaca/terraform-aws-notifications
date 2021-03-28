variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "slack_webhook_url" {
  description = "Slack incoming-webhook url"
  type        = string
}

variable "slack_channel" {
  description = "Slack channel to send notifications to"
  type        = string
}

variable "slack_username" {
  description = "Slack username that will publish notifications"
  type        = string
}

variable "s3_bucket_name" {
  description = "S3 bucket name"
  type        = string
}

variable "create_bucket" {
  description = "Should create bucket?"
  default     = true
}

variable "cloudwatch_subscripted_log_group_names" {
  description = "Cloudwatch log groups subscribed to lambda"
  default     = {}
}

variable "sns_subscripted_topics_arns" {
  description = "SNS topic arns subscribed to lambda"
  default     = {}
}
