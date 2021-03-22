resource "aws_s3_bucket" "s3_bucket" {
  count = var.create_bucket ? 1 : 0

  bucket        = var.s3_bucket_name
  acl           = "private"
  force_destroy = "true"

  versioning {
    enabled = false
  }

  policy = <<POLICY
{
  "Id": "Policy",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:PutObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::${var.s3_bucket_name}/*",
      "Principal": {
        "AWS": [
          "arn:aws:iam::${data.aws_caller_identity.current.account_id}:role/${aws_iam_role.iam_for_lambda.name}"
        ]
      }
    }
  ]
}
POLICY


  # make it encrypted
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}
