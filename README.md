# terraform-aws-notifications

[![Terraform CI](https://github.com/mvg-org/terraform-aws-notifications/actions/workflows/workflow.yaml/badge.svg)](https://github.com/mvg-org/terraform-aws-notifications/actions/workflows/workflow.yaml)


## Example Usage

```
module "notifications" {
  source = "github.com/mvg-org/terraform-aws-notifications"

  aws_region = var.aws_region

  slack_webhook_url = "https://hooks.slack.com/services/XPTOXPTO/XPTOXPTOXPTOXPTOXPTOXPTOXPTOXPTO"
  slack_channel     = "#sns-notifications"
  slack_username    = "sns-notifcations"

  s3_bucket_name = "notification-logs"
  create_bucket  = true

  sns_subscripted_topics_arns = {
    (aws_sns_topic.tst_notifications["ses_tst_bounces"].arn) = {
      targets = ["SLACK", "S3"]
    },
    (aws_sns_topic.tst_notifications["ses_tst_complaints"].arn) = {
      targets = ["SLACK", "S3"]
    },
    (aws_sns_topic.tst_notifications["ses_tst_deliveries"].arn) = {
      targets = ["S3"]
    }
  }

  cloudwatch_subscripted_log_group_names = {
    "sns/eu-west-1/12345678954328/DirectPublishToPhoneNumber" = {
      targets = ["SLACK"]
    }
  }
}
```

## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 0.12.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 3.19 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_archive"></a> [archive](#provider\_archive) | n/a |
| <a name="provider_aws"></a> [aws](#provider\_aws) | >= 3.19 |
| <a name="provider_random"></a> [random](#provider\_random) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_iam_role.iam_for_lambda](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_lambda_function.notifications_lambda](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) | resource |
| [aws_s3_bucket.s3_bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket) | resource |
| [random_id.generator](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/id) | resource |
| [archive_file.notifications_lambda](https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file) | data source |
| [aws_caller_identity.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/caller_identity) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_aws_region"></a> [aws\_region](#input\_aws\_region) | AWS region | `any` | n/a | yes |
| <a name="input_cloudwatch_subscripted_log_group_names"></a> [cloudwatch\_subscripted\_log\_group\_names](#input\_cloudwatch\_subscripted\_log\_group\_names) | Cloudwatch log groups subscribed to lambda | `map` | `{}` | no |
| <a name="input_create_bucket"></a> [create\_bucket](#input\_create\_bucket) | Should create bucket? | `bool` | `true` | no |
| <a name="input_s3_bucket_name"></a> [s3\_bucket\_name](#input\_s3\_bucket\_name) | S3 bucket name | `any` | n/a | yes |
| <a name="input_slack_channel"></a> [slack\_channel](#input\_slack\_channel) | Slack channel to send notifications to | `any` | n/a | yes |
| <a name="input_slack_username"></a> [slack\_username](#input\_slack\_username) | Slack username that will publish notifications | `any` | n/a | yes |
| <a name="input_slack_webhook_url"></a> [slack\_webhook\_url](#input\_slack\_webhook\_url) | Slack incoming-webhook url | `any` | n/a | yes |
| <a name="input_sns_subscripted_topics_arns"></a> [sns\_subscripted\_topics\_arns](#input\_sns\_subscripted\_topics\_arns) | SNS topic arns subscribed to lambda | `map` | `{}` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_arn"></a> [arn](#output\_arn) | The ARN of the Lambda function |
| <a name="output_function_name"></a> [function\_name](#output\_function\_name) | The name of the Lambda function name |
| <a name="output_role_name"></a> [role\_name](#output\_role\_name) | The name of the IAM role attached to the Lambda Function |
