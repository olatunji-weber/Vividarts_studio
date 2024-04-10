provider "aws" {
  region = "us-west-1"
}
variable "vivids3bukets" {
  default = ["s3bucket1", "s3bucket2"]
}
module "s3-bucket" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "3.15.1"

  count = length(var.vivids3bukets)

  bucket = "${var.vivids3bukets[count.index]}-oo-bucket"

  # Disable public access block
  block_public_acls   = false
  block_public_policy = false
  ignore_public_acls  = false
}
output "bucket_names" {
  value = module.s3-bucket[*]
}
