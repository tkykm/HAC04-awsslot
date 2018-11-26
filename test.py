import image_processing as ip

services = [
[{"name": "apigateway"}, {"name": "aws"}, {"name": "ec2"}],
[{"name": "apigateway"}, {"name": "iam"}, {"name": "iam"}],
[{"name": "apigateway"}, {"name": "apigateway"}, {"name": "route53"} ]
]

image = ip.create_image(services)
image_path = ip.draw_line(image, 2, (255,0,0))
upload_s3(image_path)
