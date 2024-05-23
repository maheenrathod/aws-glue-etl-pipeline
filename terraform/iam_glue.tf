resource "aws_iam_role" "glue_role" {
  name = "AWSGlueRole"
  assume_role_policy = <<EOF
    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Action": "sts:AssumeRole",
        "Principal": {
            "Service": "glue.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
        }
    ]
    }
    EOF
}

resource "aws_iam_role_policy_attachment" "glue_role_policy" {
    role = aws_iam_role.glue_role.name
    policy_arn = "arn:aws:iam::aws:policy/PowerUserAccess"
}