variable "vpc_cidr" {
  description = "CIDR block for the VPC"
}

variable "subnet_cidr" {
  description = "CIDR block for the subnet"
}

variable "availability_zone" {
  description = "The availability zone for the subnet"
}

variable "ami_id" {
  description = "The AMI ID for the EC2 instance"
}

variable "instance_type" {
  description = "The instance type for the EC2 instance"
}

variable "volume_size" {
  description = "The size of the root EBS volume in GB"
}
