data "aws_caller_identity" "this" {}

locals {
  environment = replace(var.environment, "_", "-")
}

module "s3" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket = "${local.environment}-${random_string.this.result}"

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true

  force_destroy = true

  control_object_ownership = true
  object_ownership         = "BucketOwnerPreferred"

  expected_bucket_owner = data.aws_caller_identity.this.account_id

  server_side_encryption_configuration = {
    rule = {
      apply_server_side_encryption_by_default = {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = var.tags
}

resource "random_string" "this" {
  length = 4

  lower   = true
  numeric = true
  special = false
  upper   = false
}
