variable "aws_region" {
  description = "AWS region"
}

variable "slack_webhook_url" {
  description = "Slack incoming-webhook url"
}

variable "slack_channel" {
  description = "Slack channel to send notifications to"
}

variable "slack_username" {
  description = "Slack username that will publish notifications"
}

variable "s3_bucket_name" {
  description = "S3 bucket name"
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
