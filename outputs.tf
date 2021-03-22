output "arn" {
  description = "The ARN of the Lambda function"
  value       = aws_lambda_function.notifications_lambda.arn
}

output "role_name" {
  description = "The name of the IAM role attached to the Lambda Function"
  value       = aws_iam_role.iam_for_lambda.name
}

output "function_name" {
  description = "The name of the Lambda function name"
  value       = aws_lambda_function.notifications_lambda.function_name
}
