data "archive_file" "notifications_lambda" {
  type        = "zip"
  output_path = "${path.module}/notifications.zip"

  source_dir = "${path.module}/files/notifications/"
}

resource "random_id" "generator" {
  byte_length = 8
}

resource "aws_iam_role" "iam_for_lambda" {
  name = "notifications_lambda_${random_id.generator.id}"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_function" "notifications_lambda" {
  filename      = "${path.module}/notifications.zip"
  function_name = "notifications_${random_id.generator.id}"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "notifications.notifications"
  runtime       = "python3.6"

  environment {
    variables = {
      SLACK_WEBHOOK_URL = var.slack_webhook_url
      SLACK_CHANNEL     = var.slack_channel
      SLACK_USERNAME    = var.slack_username

      S3_BUCKET_NAME = var.s3_bucket_name

      CW_LOG_GROUPS  = jsonencode(var.cloudwatch_subscripted_log_group_names)
      SNS_TOPIC_ARNS = jsonencode(var.sns_subscripted_topics_arns)
    }
  }
}
